// DNS.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
//#include <regex>
#include <pcap.h>
#include <string>
#pragma comment(lib,"ws2_32.lib")
#pragma warning(disable:4996)

using namespace std;

typedef struct ip_address{
	u_char byte1;
	u_char byte2;
	u_char byte3;
	u_char byte4;
}ip_address;

/* IPv4 首部 */
typedef struct ip_header{
	u_char  ver_ihl;        // 版本 (4 bits) + 首部长度 (4 bits)
	u_char  tos;            // 服务类型(Type of service) 
	u_short tlen;           // 总长(Total length) 
	u_short identification; // 标识(Identification)
	u_short flags_fo;       // 标志位(Flags) (3 bits) + 段偏移量(Fragment offset) (13 bits)
	u_char  ttl;            // 存活时间(Time to live)
	u_char  proto;          // 协议(Protocol)
	u_short crc;            // 首部校验和(Header checksum)
	ip_address  saddr;      // 源地址(Source address)
	ip_address  daddr;      // 目的地址(Destination address)
	u_int   op_pad;         // 选项与填充(Option + Padding)
}ip_header;

typedef struct dns_header{
	u_short id;
	u_short flags;
	u_short num_q;
	u_short num_answ_rr;
	u_short num_auth_rr;
	u_short num_addi_rr;
	u_char dnsname;
}dns_header;

/* UDP 首部*/
typedef struct udp_header{
	u_short sport;          // 源端口(Source port)
	u_short dport;          // 目的端口(Destination port)
	u_short len;            // UDP数据包长度(Datagram length)
	u_short crc;            // 校验和(Checksum)
}udp_header;

int k = 0;
/* 回调函数原型 */
void packet_handler(u_char *param, const struct pcap_pkthdr *header, const u_char *pkt_data);



int _tmain(int argc, _TCHAR* argv[])
{

	u_int netmask;
	pcap_if_t * allAdapters;//适配器列表
	pcap_if_t * adapter;
	pcap_t           * adapterHandle;//适配器句柄
	//struct pcap_pkthdr * packetHeader;
	//const u_char       * packetData;
	char errorBuffer[PCAP_ERRBUF_SIZE];//错误信息缓冲区
	char packet_filter[] = "udp port 53";
	struct bpf_program fcode;
	if (pcap_findalldevs_ex(PCAP_SRC_IF_STRING, NULL,
		&allAdapters, errorBuffer) == -1)
	{//检索机器连接的所有网络适配器
		fprintf(stderr, "Error in pcap_findalldevs_ex function: %s\n", errorBuffer);
		system("pause");
		return -1;
	}
	if (allAdapters == NULL)
	{//不存在任何适配器
		printf("\nNo adapters found! Make sure WinPcap is installed.\n");
		system("pause");
		return 0;
	}
	int crtAdapter = 0;
	for (adapter = allAdapters; adapter != NULL; adapter = adapter->next)
	{//遍历输入适配器信息(名称和描述信息)
		printf("\n%d.%s ", ++crtAdapter, adapter->name);
		printf("-- %s\n", adapter->description);
	}
	printf("\n");
	//选择要捕获数据包的适配器
	int adapterNumber;
	printf("Enter the adapter number between 1 and %d:", crtAdapter);
	scanf_s("%d", &adapterNumber);
	if (adapterNumber < 1 || adapterNumber > crtAdapter)
	{
		printf("\nAdapter number out of range.\n");
		// 释放适配器列表
		pcap_freealldevs(allAdapters);
		system("pause");
		return -1;
	}
	adapter = allAdapters;
	for (crtAdapter = 0; crtAdapter < adapterNumber - 1; crtAdapter++)
		adapter = adapter->next;
	// 打开指定适配器
	adapterHandle = pcap_open(adapter->name, // name of the adapter
		65536,         // portion of the packet to capture
		// 65536 guarantees that the whole 
		// packet will be captured
		PCAP_OPENFLAG_PROMISCUOUS, // promiscuous mode
		1000,             // read timeout - 1 millisecond
		NULL,          // authentication on the remote machine
		errorBuffer    // error buffer
		);
	if (adapterHandle == NULL)
	{//指定适配器打开失败
		fprintf(stderr, "\nUnable to open the adapter\n", adapter->name);
		// 释放适配器列表
		pcap_freealldevs(allAdapters);
		system("pause");
		return -1;
	}

	/* 检查数据链路层，为了简单，我们只考虑以太网 */
	if (pcap_datalink(adapterHandle) != DLT_EN10MB)
	{
		fprintf(stderr, "\nThis program works only on Ethernet networks.\n");
		/* 释放设备列表 */
		pcap_freealldevs(allAdapters);
		system("pause");
		return -1;
	}

	if (adapter->addresses != NULL)
		/* 获得接口第一个地址的掩码 */
		netmask = ((struct sockaddr_in *)(adapter->addresses->netmask))->sin_addr.S_un.S_addr;
	else
		/* 如果接口没有地址，那么我们假设一个C类的掩码 */
		netmask = 0xffffff;


	//编译过滤器
	if (pcap_compile(adapterHandle, &fcode, packet_filter, 1, netmask) <0)
	{
		fprintf(stderr, "\nUnable to compile the packet filter. Check the syntax.\n");
		/* 释放设备列表 */
		pcap_freealldevs(allAdapters);
		system("pause");
		return -1;
	}

	//设置过滤器
	if (pcap_setfilter(adapterHandle, &fcode)<0)
	{
		fprintf(stderr, "\nError setting the filter.\n");
		/* 释放设备列表 */
		pcap_freealldevs(allAdapters);
		system("pause");
		return -1;
	}

	printf("\nlistening on %s...\n", adapter->description);

	/* 释放设备列表 */
	pcap_freealldevs(allAdapters);

	/* 开始捕捉 */
	pcap_loop(adapterHandle, 0, packet_handler, NULL);

	return 0;
}
void packet_handler(u_char *param, const struct pcap_pkthdr *header, const u_char *pkt_data)
{
	//regex pattern("[a-zA-Z0-9][-a-zA-Z0-9]{0,62}(\.[a-zA-Z0-9][-a-zA-Z0-9]{0,62})+\.?", regex_constants::extended);
	//match_results<string::const_iterator> result;


	struct tm *ltime;
	struct dns_header *dns_protocol;
	char timestr[16];
	ip_header *ih;
	udp_header *uh;
	u_int ip_len;
	u_short sport, dport;
	time_t local_tv_sec;
	int u, v, w, y;

	/* 将时间戳转换成可识别的格式 */
	local_tv_sec = header->ts.tv_sec;
	ltime = localtime(&local_tv_sec);
	strftime(timestr, sizeof timestr, "%H:%M:%S", ltime);
	//printf("%s.%.6d len:%d ", timestr, header->ts.tv_usec, header->len);

	/* 获得IP数据包头部的位置 */
	ih = (ip_header *)(pkt_data +
		14); //以太网头部长度

	/* 获得UDP首部的位置 */
	ip_len = (ih->ver_ihl & 0xf) * 4;
	uh = (udp_header *)((u_char*)ih + ip_len);

	/* 指向dns问题字段 */
	dns_protocol = (struct dns_header*)(pkt_data + 34 + 8);

	/* 将网络字节序列转换成主机字节序列 */
	sport = ntohs(uh->sport);
	dport = ntohs(uh->dport);

	//FILE *fp;
	//fp = fopen(".\\Dns.txt", "a");
	freopen(".\\Dns.txt", "a+", stdout);

	if (k == 0)
	{
		printf(" \n  IP Source          Dns Server             Time            DNS  \n  ");
	}
	k = 1;

	u = ntohs(dns_protocol->num_addi_rr);
	v = ntohs(dns_protocol->num_answ_rr);
	w = ntohs(dns_protocol->num_auth_rr);

	y = (!u) && (!v) && (!w);
	if ((!(ntohs(dns_protocol->flags) >> 15)) && y)//过滤DNS请求包
		/* 打印IP地址和UDP端口 */
	{

		printf("\n%d.%d.%d.%d.%d \t %d.%d.%d.%d.%d",

			ih->saddr.byte1,
			ih->saddr.byte2,
			ih->saddr.byte3,
			ih->saddr.byte4,
			sport,
			ih->daddr.byte1,
			ih->daddr.byte2,
			ih->daddr.byte3,
			ih->daddr.byte4,
			dport);

		u_char *query = &(dns_protocol->dnsname);
		u_char  domainname[5120] = { 0 };

		u_int k = 0;
		query++;

		while (*query)
		{
			if (*query < 0x10)//48以后出现数字和英文字母  
			{

				domainname[k] = '.';
			}
			else
			{
				domainname[k] = *query;
			}

			query++;
			k++;

		}
		/* 打印数据包的时间戳和长度 */

		printf("\t\t%s.%.6d  ", timestr, header->ts.tv_usec);
		//string buf;
		//buf = (char*)domainname;
		//bool valid = regex_match(buf, result, pattern);
		//if (!valid)
		//	fprintf(fp, "\tUknown");
		//else
		printf("\t%s", domainname);

		fflush(stdout);


		//fclose(fp);
	}
}

