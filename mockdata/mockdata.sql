-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: cd-marketplace
-- ------------------------------------------------------
-- Server version	5.7.19-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `bids`
--

DROP TABLE IF EXISTS `bids`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bids` (
  `job_id` int(11) DEFAULT NULL,
  `dev_id` int(11) DEFAULT NULL,
  `price` double DEFAULT NULL,
  `date` timestamp NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bids`
--

LOCK TABLES `bids` WRITE;
/*!40000 ALTER TABLE `bids` DISABLE KEYS */;
INSERT INTO `bids` VALUES (3,3,225,'2017-12-09 01:53:51'),(2,3,70,'2017-12-09 03:28:03'),(3,6,230,'2017-12-09 23:25:41'),(3,8,200,'2017-12-09 23:36:01');
/*!40000 ALTER TABLE `bids` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blacklist`
--

DROP TABLE IF EXISTS `blacklist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blacklist` (
  `user_id` int(11) NOT NULL,
  `reason` varchar(255) DEFAULT NULL,
  `date` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blacklist`
--

LOCK TABLES `blacklist` WRITE;
/*!40000 ALTER TABLE `blacklist` DISABLE KEYS */;
INSERT INTO `blacklist` VALUES (7,'Name seems to be fake.','2017-12-08 18:53:46'),(10,'Seems like a spam account.','2017-12-08 18:54:12');
/*!40000 ALTER TABLE `blacklist` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `post`
--

DROP TABLE IF EXISTS `post`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `post` (
  `job_id` int(11) NOT NULL AUTO_INCREMENT,
  `proj_description` varchar(255) DEFAULT NULL,
  `start_price` double DEFAULT NULL,
  `deadline` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `post_date` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `dev_id` int(11) DEFAULT NULL,
  `client_id` int(11) DEFAULT NULL,
  `title` varchar(45) DEFAULT NULL,
  `clicks` int(11) DEFAULT '0',
  `file` longblob,
  `visibility` int(1) DEFAULT '1',
  `project_days` int(2) DEFAULT '3',
  `bids` int(11) DEFAULT '0',
  PRIMARY KEY (`job_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `post`
--

LOCK TABLES `post` WRITE;
/*!40000 ALTER TABLE `post` DISABLE KEYS */;
INSERT INTO `post` VALUES (1,'Hello Developers! I have a request for you to build me a bitcoin software. It should be pretty simple. All I want is to have way to track the market. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec in lacinia eros. Vestibulum efficitur ip.',100,'2017-12-30 00:22:57','2017-12-09 00:22:57',NULL,2,'Bitcoin Software',9,'',1,15,0),(2,'Hello. Please help me with my data structures homework project. I\'m only a student so please don\'t bid a very high amount.',75,'2017-12-23 00:25:17','2017-12-09 00:25:17',3,5,'Data Structures HW',24,'',1,5,2),(3,'Please make a website landing page for my site. It should look very modern and functional. I also want it to be mobile responsive.',200,'2017-12-16 00:30:55','2017-12-09 00:30:55',8,13,'Website Landing Page',46,'',1,15,4);
/*!40000 ALTER TABLE `post` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `project`
--

DROP TABLE IF EXISTS `project`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `project` (
  `job_id` int(11) DEFAULT NULL,
  `status` varchar(45) DEFAULT NULL,
  `final_price` int(11) DEFAULT NULL,
  `dev_id` int(11) DEFAULT NULL,
  `client_id` int(11) DEFAULT NULL,
  `dev_rating_desc` varchar(255) DEFAULT NULL,
  `client_rating` int(1) DEFAULT NULL,
  `submit_text` varchar(255) DEFAULT NULL,
  `submit_file` blob,
  `dev_rating` int(1) DEFAULT NULL,
  `client_rating_desc` varchar(255) DEFAULT NULL,
  `client_complaint` int(1) DEFAULT '0',
  `dev_complaint` int(1) DEFAULT '0',
  `create_time` datetime DEFAULT CURRENT_TIMESTAMP,
  `due_date` datetime DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `project`
--

LOCK TABLES `project` WRITE;
/*!40000 ALTER TABLE `project` DISABLE KEYS */;
INSERT INTO `project` VALUES (2,'Completed',70,3,5,'Well done',4,'Here is my submission. Please review the parts','.gitignore',5,'Good client',0,0,'2017-12-09 14:17:52','2017-12-23 14:17:52'),(3,'Admin Review',200,8,13,'Very bad. Only met 1 out of 7 requirements.',3,'Here you go','hey bich.html',1,'Instructions were not clear enough',0,0,'2017-12-09 18:37:37','2017-12-24 18:37:37');
/*!40000 ALTER TABLE `project` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(255) NOT NULL,
  `password` varchar(32) NOT NULL,
  `create_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `username` varchar(45) NOT NULL,
  `role` char(1) NOT NULL,
  `first_name` varchar(45) NOT NULL,
  `last_name` varchar(45) NOT NULL,
  `rating` double NOT NULL DEFAULT '0',
  `warning` int(11) NOT NULL DEFAULT '0',
  `description` varchar(255) DEFAULT NULL,
  `confirmed` tinyint(1) DEFAULT '0',
  `finished_projects` int(11) NOT NULL DEFAULT '0',
  `interest` varchar(45) DEFAULT NULL,
  `resume` blob,
  `image` blob,
  `sample_work` varchar(255) DEFAULT NULL,
  `business_credential` varchar(255) DEFAULT NULL,
  `balance` double DEFAULT '0',
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'admin@email.com','webapp123','2017-12-08 23:44:12','admin','a','Admin','Account',0,0,'Hello clients and developers. I am the admin of this site.',1,0,'Management',NULL,NULL,'Dev Market',NULL,0),(2,'stevejobs@apple.com','webapp123','2017-12-08 23:45:40','stevejobs','c','Steve','Jobs',0,0,'I am the one who established Apple Company. I don\'t think I need to say more.',1,0,'Apple',NULL,NULL,'apple.com','CEO',150),(3,'chrispanican@gmail.com','webapp123','2017-12-08 23:45:52','chris1800','d','Chris','Panican',5,0,'I\'m an aspiring developer. I need extra income right now so please give me some projects!',1,1,'Web Development',NULL,NULL,'https://chrispanican.com','Bachelor\'s Degree',0),(4,'bill@microsoft.com','webapp123','2017-12-08 23:46:16','billgates','d','Bill','Gates',0,0,'I\'m the one of the first people who made Microsoft. I\'m retired and have a lot of free time.',1,0,'Programming',NULL,NULL,'microsoft','Retired',0),(5,'haroldpain@aol.com','webapp123','2017-12-08 23:46:43','haroldpain','c','Harold','Pain',4,0,'I am just a student who is failing classes. Please go easy on me.',1,1,'School',NULL,NULL,'None','None',200),(6,'tchou@gmail.com','webapp123','2017-12-08 23:48:25','triketora','d','Tracy','Chou',0,0,'I am an entrepreneur, software engineer, and diversity advocate.',1,0,'Computer Science',NULL,NULL,'Project Include','Founder',0),(7,'bitcoin@email.com','webapp123','2017-12-08 23:50:21','bitcoin','c','Bitcoin','Mining',0,0,NULL,0,0,NULL,NULL,NULL,NULL,NULL,0),(8,'andyyang@gmail.com','webapp123','2017-12-08 23:50:54','andyyang','d','Andy','Yang',1,0,NULL,1,1,NULL,NULL,NULL,NULL,NULL,0),(9,'kb12@gmail.com','webapp123','2017-12-08 23:51:24','kevinb','d','Kevin','Baguyo',0,0,NULL,1,0,NULL,NULL,NULL,NULL,NULL,0),(10,'ayylmao@meme.com','webapp123','2017-12-08 23:51:39','ayylmao','c','Ayy','Lmao',0,0,NULL,0,0,NULL,NULL,NULL,NULL,NULL,0),(11,'rongfeng@gmail.com','webapp123','2017-12-08 23:52:48','rongfeng','d','Rongfeng','Lin',0,0,NULL,0,0,NULL,NULL,NULL,NULL,NULL,0),(12,'hello@gmail.com','webapp123','2017-12-08 23:53:08','helloworld','d','Hello','World',0,0,NULL,0,0,NULL,NULL,NULL,NULL,NULL,0),(13,'tom@company.com','webapp123','2017-12-09 00:08:33','hiimtom','c','Tom','Nguyen',3,0,'Hi! My name is Tom. I am a very experience business man and I have many ideas.',1,1,'Technology',NULL,NULL,'tomnguyen.com','CEO and Owner',450);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-12-09 19:10:11
