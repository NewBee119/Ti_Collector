  ThreatArticleSpider.py用来爬取https://badcyber.com这个网站上的链接，从这些链接中拓宽威胁情报的来源。其爬取的结果是ret.json然后再通过人工的方式进一步判断这些链接是否有价值。

  badcyber.com 是国外的一个安全类资讯网站，会不定期的发布与信息安全相关的一些信息。对于这类网站，主要进行两种处理。
  一、爬取其他网站的链接如ThreatArticleSpider.py中所作。
  二、寻找文章中提及的IoC信息，其结果在Result文件夹中有所体现。