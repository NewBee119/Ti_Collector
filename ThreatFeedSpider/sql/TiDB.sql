SET character_set_client = utf8;
SET character_set_results = utf8;
SET character_set_connection = utf8;
SET character_set_server = utf8;

CREATE DATABASE IF NOT EXISTS TiDB default character set utf8;
USE TiDB;

DROP TABLE IF EXISTS url_table;
CREATE TABLE `url_table` (
  `url_index` VARCHAR(300) NOT NULL,
  `stamp` VARCHAR(100) NOT NULL,
  `update_time` VARCHAR(50) NOT NULL,
  `source` VARCHAR(1000) NOT NULL,
  `url` VARCHAR(15000) NOT NULL, 
  PRIMARY KEY (`url_index`)
) AUTO_INCREMENT=1;

DROP TABLE IF EXISTS domain_table;
CREATE TABLE `domain_table` (
  `domain` VARCHAR(300) NOT NULL,
  `update_time` VARCHAR(50) NOT NULL,
  `source` VARCHAR(1000) NOT NULL,
  `stamp` VARCHAR(500) NOT NULL, 
  PRIMARY KEY (`domain`)
)AUTO_INCREMENT=1;

DROP TABLE IF EXISTS ip_table;
CREATE TABLE `ip_table` (
  `ip` VARCHAR(200) NOT NULL,
  `update_time` VARCHAR(50) NOT NULL,
  `source` VARCHAR(1000) NOT NULL,
  `stamp` VARCHAR(500) NOT NULL, 
  PRIMARY KEY (`ip`)
)AUTO_INCREMENT=1;
