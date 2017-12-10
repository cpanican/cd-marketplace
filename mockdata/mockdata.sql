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
INSERT INTO `bids` VALUES (1,2,100,'2017-12-10 19:52:52'),(2,4,160,'2017-12-10 20:00:59'),(2,5,170,'2017-12-10 20:02:37'),(6,7,250,'2017-12-10 20:09:53'),(2,7,180,'2017-12-10 20:10:14'),(3,7,220,'2017-12-10 20:10:32'),(5,2,140,'2017-12-10 20:13:06'),(4,2,50,'2017-12-10 20:13:15'),(11,2,200,'2017-12-10 20:45:01'),(12,2,150,'2017-12-10 20:45:12'),(7,2,100,'2017-12-10 20:45:17'),(9,2,50,'2017-12-10 20:45:29'),(10,7,150,'2017-12-10 20:51:29'),(8,7,100,'2017-12-10 20:51:39'),(20,2,150,'2017-12-10 21:11:17'),(16,2,50,'2017-12-10 21:11:25'),(21,4,100,'2017-12-10 21:12:18'),(13,4,180,'2017-12-10 21:12:26'),(16,5,45,'2017-12-10 21:12:40'),(14,5,50,'2017-12-10 21:12:47'),(13,5,170,'2017-12-10 21:12:52'),(15,5,100,'2017-12-10 21:12:57'),(17,14,200,'2017-12-10 21:14:04'),(13,14,165,'2017-12-10 21:14:11'),(14,14,45,'2017-12-10 21:14:17'),(16,14,30,'2017-12-10 21:14:31'),(19,4,100,'2017-12-10 21:18:04'),(24,15,100,'2017-12-10 21:24:25'),(23,4,100,'2017-12-10 21:28:31');
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
INSERT INTO `blacklist` VALUES (10,'This site will not be used for mining bitcoins.','2017-12-10 14:55:00');
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
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `post`
--

LOCK TABLES `post` WRITE;
/*!40000 ALTER TABLE `post` DISABLE KEYS */;
INSERT INTO `post` VALUES (1,'Hi developers, I need a new landing site for my startup company.',100,'2018-06-03 18:52:21','2017-12-10 19:52:21',2,3,'Landing Site',3,'description.txt',1,5,1),(2,'Hello! I am a business man and I would like someone to make me a program to track the stock market! Paying a LOT of cash!',150,'2018-05-27 18:59:48','2017-12-10 19:59:48',7,6,'Finance Tracker',18,'',1,15,3),(3,'Hello Developers! I have a request for you to build me a bitcoin software. It should be pretty simple. All I want is to have way to track the market.',200,'2018-05-20 19:04:13','2017-12-10 20:04:13',7,3,'Bitcoin Software',5,'description.txt',1,15,1),(4,'Please Help me finish my HW. I will attach the homework assignment.',50,'2018-05-13 19:05:37','2017-12-10 20:05:37',2,8,'Data Structures HW',6,'',1,5,1),(5,'I want a software to buy shoes for me. Especially those designer shoes',130,'2018-05-06 19:07:02','2017-12-10 20:07:02',2,9,'Shoe Buyer',6,'',1,15,1),(6,'Please make me a personal site to feature my  art.',250,'2018-04-29 19:08:57','2017-12-10 20:08:57',7,12,'Develop a Site',10,'',1,15,1),(7,'Please help me with Cuny Tech Prep project',100,'2018-04-22 19:18:08','2017-12-10 20:18:08',2,3,'CTP Project',8,'',1,15,1),(8,'Please help my team design a database system for my startup',100,'2018-04-15 19:34:37','2017-12-10 20:34:37',7,3,'Startup Database',10,'',1,3,1),(9,'Please help me build a heap sorting algorithm',50,'2018-04-08 19:36:21','2017-12-10 20:36:21',2,8,'Algorithms HW',5,'',1,15,1),(10,'Please make an application to track best prices of shoes',150,'2018-04-01 19:37:44','2017-12-10 20:37:44',7,9,'Tracking of Shoes',5,'',1,3,1),(11,'Please make a simple android app for me',200,'2018-03-25 19:38:50','2017-12-10 20:38:50',2,12,'App Development',8,'',1,5,1),(12,'Please make an application to alert me every time stock goes low.',150,'2018-03-18 19:39:38','2017-12-10 20:39:38',2,6,'Stock Alerts',6,'',1,3,1),(13,'Our current log-in system is not secure. Help us improve the security.',200,'2018-03-11 20:03:14','2017-12-10 21:03:14',4,3,'New Log-In System',7,'',1,15,3),(14,'I just purchased a raspberry pi and i dont know how to install an OS. Help me.',50,'2018-03-04 21:04:15','2017-12-10 21:04:15',5,6,'Raspberry Pi',6,'',1,3,2),(15,'I want to have an automated calling system to users who have warnings',100,'2018-02-25 21:04:55','2017-12-10 21:04:55',5,3,'Automated Calling',5,'',1,15,1),(16,'I need help with my database HW.',50,'2018-02-18 21:05:32','2017-12-10 21:05:32',NULL,8,'Database HW',6,'',1,5,3),(17,'Please make me a tool to customize my shoes',200.6,'2018-02-11 21:06:32','2017-12-10 21:06:32',NULL,9,'Shoe Customizer',2,'',1,15,1),(18,'I want a tool to lookup shoes better than google',100,'2018-02-04 21:07:20','2017-12-10 21:07:20',NULL,9,'Shoe Finder',0,'',1,3,0),(19,'I need an online art gallery. Pictures will be high resolution',100,'2018-01-28 21:08:11','2017-12-10 21:08:11',4,12,'Art Gallery',5,'',1,3,1),(20,'I need a search capability for my site',140,'2018-01-21 21:08:59','2017-12-10 21:08:59',NULL,3,'Search Capability',3,'',1,5,1),(21,'I want a business alert for a specific stock.',100,'2018-01-14 21:10:10','2017-12-10 21:10:10',NULL,6,'Business Alerts',3,'',1,15,1),(22,'I want to revamp the design of my site and make it mobile responsive',140,'2018-01-07 21:16:46','2017-12-10 21:16:46',NULL,3,'Revamp Site',0,'',1,3,0),(23,'I need a new Logo',100,'2017-12-31 21:21:31','2017-12-10 21:21:31',4,3,'New Logo',3,'',1,15,1),(24,'Make my site mobile responsive',100,'2017-12-24 21:22:16','2017-12-10 21:22:16',15,12,'Mobile Responsive',3,'',1,3,1),(25,'make an app for shoes maybe for andorid',200,'2017-12-17 21:22:55','2017-12-10 21:22:55',NULL,9,'App for Shoes',0,'',1,30,0);
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
  `client_rating` int(1) DEFAULT '0',
  `submit_text` varchar(255) DEFAULT NULL,
  `submit_file` blob,
  `dev_rating` int(1) DEFAULT '0',
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
INSERT INTO `project` VALUES (1,'Completed',100,2,3,'Good job. Looks really nice.',4,'Here is my submission. Please review the parts','.gitignore',5,'Great client. Provided a great summary of project.',0,0,'2017-12-10 14:53:02','2017-12-15 14:53:02'),(3,'Completed',220,7,3,'Not bad',5,'Here is my submission','.gitignore',4,'Good client',0,0,'2017-12-10 15:14:14','2017-12-25 15:14:14'),(5,'Completed',140,2,9,'Thanks',4,'Heres the project','.gitignore',4,'Great client. Provided a great summary of project.',0,0,'2017-12-10 15:35:44','2017-12-25 15:35:44'),(4,'Completed',50,2,8,'Thank you',5,'Here you go','',5,'Very Clear',0,0,'2017-12-10 15:35:56','2017-12-15 15:35:56'),(12,'Completed',150,2,6,'Thank',5,'Here is my submission. Please review the parts','.gitignore',5,'Great client. Provided a great summary of project.',0,0,'2017-12-10 15:45:42','2017-12-13 15:45:42'),(7,'Completed',100,2,3,'Great',5,'Attached is my submission','.gitignore',5,'Great client. Provided a great summary of project.',0,0,'2017-12-10 15:45:53','2017-12-25 15:45:53'),(9,'Completed',50,2,8,'Nice',5,'Attached is my submission','.gitignore',5,'Great client. Provided a great summary of project.',0,0,'2017-12-10 15:48:16','2017-12-25 15:48:16'),(11,'Completed',200,2,12,'Nice',4,'Here is my submission. Please review the parts','.gitignore',5,'Great client. Provided a great summary of project.',0,0,'2017-12-10 15:48:28','2017-12-15 15:48:28'),(10,'Completed',150,7,9,'Very Bad',4,'Here','',2,'Thanks',0,0,'2017-12-10 15:51:59','2017-12-13 15:51:59'),(8,'Completed',100,7,3,'Really bad',4,'Here you go','.gitignore',1,'Nice',0,0,'2017-12-10 15:52:18','2017-12-13 15:52:18'),(2,'Completed',180,7,6,'Really bad',4,'Here is my submission. Please review the parts','.gitignore',1,'Great client. Provided a great summary of project.',0,0,'2017-12-10 15:52:30','2017-12-25 15:52:30'),(6,'Completed',250,7,12,'bad',4,'Here is my submission. Please review the parts','.gitignore',3,'hes okay',0,0,'2017-12-10 15:52:45','2017-12-25 15:52:45'),(13,'Ongoing',180,4,3,NULL,0,NULL,NULL,0,NULL,0,0,'2017-12-10 16:15:48','2017-12-25 16:15:48'),(15,'Ongoing',100,5,3,NULL,0,NULL,NULL,0,NULL,0,0,'2017-12-10 16:16:04','2017-12-25 16:16:04'),(14,'Completed',50,5,6,'Nice',5,'Here you go','.gitignore',5,'Easy',0,0,'2017-12-10 16:17:25','2017-12-13 16:17:25'),(19,'Completed',100,4,12,'Nice',5,'Here is my submission. Please review the parts','.gitignore',5,'Nice',0,0,'2017-12-10 16:18:27','2017-12-13 16:18:27'),(24,'Admin Review',100,15,12,'Really bad',5,'Here','.gitignore',1,'TY',0,0,'2017-12-10 16:24:34','2017-12-13 16:24:34'),(23,'Pending',100,4,3,NULL,5,'Here','uTorrent.exe',0,'Thanks',0,0,'2017-12-10 16:28:44','2017-12-25 16:28:44');
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
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'admin@email.com','webapp123','2017-12-10 19:30:58','admin','a','Admin','Account',0,0,'Hello! I am the admin of Developer\'s Marketplace.',1,0,'Dev Market',NULL,NULL,'https://cd-marketplace.herokuapp.com/','Owner',344),(2,'chrispanican@gmail.com','webapp123','2017-12-10 19:35:48','chris1800','d','Chris','Panican',34,0,'Hi I am a developer with tons of experience',1,7,'Web Development','Chris-Panican-Resume.pdf',NULL,'https://chrispanican.com','Student',750.5),(3,'haroldpain@aol.com','webapp123','2017-12-10 19:36:02','haroldpain','c','Harold','Pain',23,0,'I am an owner of a new startup and would will have several projects in this site.',1,5,'Startup',NULL,NULL,NULL,'CEO',423.75),(4,'bill@microsoft.com','webapp123','2017-12-10 19:36:22','billgates','d','Bill','Gates',5,0,'Co-founder of the Microsoft Corporation along with Paul Allen.',1,1,'Philanthropy',NULL,NULL,'microsoft','Retired',228),(5,'stevejobs@apple.com','webapp123','2017-12-10 19:36:33','stevejobs','d','Steve','Jobs',5,0,'I am the one who established Apple Company. I don\'t think I need to say more.',1,1,'Apple',NULL,NULL,'apple.com',NULL,95),(6,'tom@company.com','webapp123','2017-12-10 19:37:04','hiimtom','c','Tom','Nguyen',14,0,'I am an entrepreneur and passionate about technology.',1,3,'Money',NULL,NULL,NULL,NULL,398.4),(7,'elon@tesla.com','webapp123','2017-12-10 19:37:38','elonmusk','d','Elon','Musk',11,0,'Hat Salesman',1,5,'Technology',NULL,NULL,'Tesla and SpaceX',NULL,667.85),(8,'rongfeng@gmail.com','webapp123','2017-12-10 19:38:01','rongfeng','c','Rongfeng','Lin',10,0,'Student who might need some help with CS projects',1,2,'Computer Science',NULL,NULL,NULL,NULL,200),(9,'andyyang@gmail.com','webapp123','2017-12-10 19:38:14','andyyang','c','Andy','Yang',8,0,'I am a shoes enthusiast. I like collecting shoes',1,2,'Shoes',NULL,NULL,NULL,NULL,446.245),(10,'bitcoin@email.com','webapp123','2017-12-10 19:38:34','bitcoin','c','Bitcoin','Miner',0,0,NULL,0,0,NULL,NULL,NULL,NULL,NULL,0),(11,'spam@lmao.com','webapp123','2017-12-10 19:38:54','spam','c','Spam','Account',0,0,NULL,0,0,NULL,NULL,NULL,NULL,NULL,0),(12,'johndoe@email.com','webapp123','2017-12-10 19:39:15','johndoe','c','John','Doe',18,0,'I am an artist who would like to express myself through online medium',1,4,'Art',NULL,NULL,NULL,NULL,159.375),(13,'nivek@gmail.com','webapp123','2017-12-10 19:40:29','nivek','c','Kevin','Baguyo',0,0,NULL,0,0,NULL,NULL,NULL,NULL,NULL,0),(14,'tchou@gmail.com','webapp123','2017-12-10 21:13:18','triketora','d','Tracy','Chou',0,0,'I am an entrepreneur, software engineer, and diversity advocate.',1,0,'Computer Science',NULL,NULL,NULL,NULL,0),(15,'vtoad@gmail.com','webapp123','2017-12-10 21:24:01','vince','d','Vince','Toad',1,0,NULL,1,1,NULL,NULL,NULL,NULL,NULL,47.5);
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

-- Dump completed on 2017-12-10 16:29:22
