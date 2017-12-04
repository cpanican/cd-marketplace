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
  `price` int(11) DEFAULT NULL,
  `date` timestamp NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bids`
--

LOCK TABLES `bids` WRITE;
/*!40000 ALTER TABLE `bids` DISABLE KEYS */;
INSERT INTO `bids` VALUES (2,1,40,'2017-12-03 21:06:25'),(2,3,231,'2017-12-03 21:13:15'),(1,1,123,'2017-12-03 22:29:27');
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
INSERT INTO `blacklist` VALUES (6,'posted a meme submission','2017-12-03 19:46:33');
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
  `start_price` int(11) DEFAULT NULL,
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
INSERT INTO `post` VALUES (1,'Hello Developers! Please help me with the design of my startup company\'s database! Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec in lacinia eros. Vestibulum efficitur ipsum massa. Fusce ultricies urna sit amet velit bibendum mollis.',40,'2017-12-24 05:01:17','2017-12-03 05:01:17',NULL,2,'Help with database design of startup company',39,'',1,5,3),(2,'Hi! My new startup company needs a landing page! Please help me design it. Aliquam condimentum a quam sed tincidunt. Nunc pharetra, neque varius vulputate semper, odio lectus sagittis risus, eu cursus elit urna ut est. ',30,'2017-12-17 05:05:24','2017-12-03 05:05:24',NULL,2,'Startup Company New Landing Page',36,'shiba.txt',1,15,2),(3,'Hello! I am a bitcoin enthusiast and I would like someone to make me a program to mine bitcoins! Paying a LOT of cash!',100,'2017-12-10 05:07:34','2017-12-03 05:07:34',NULL,5,'Mining bitcoin software',59,'shiba.txt',1,30,0);
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
  `client_rating` int(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `project`
--

LOCK TABLES `project` WRITE;
/*!40000 ALTER TABLE `project` DISABLE KEYS */;
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
  `balance` int(11) DEFAULT '0',
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'chrispanican@gmail.com','webapp123','2017-12-03 04:08:33','chris1800','d','Chris','Panican',0,0,'Hi I am a developer with tons of experience!',1,0,'Web Development','Chris-Panican-Resume.pdf',NULL,'chrispanican.com',NULL,0),(2,'haroldfalk@aol.com','webapp123','2017-12-03 04:08:47','haroldfalk','c','Harold','Falk',0,0,NULL,1,0,NULL,NULL,NULL,NULL,NULL,0),(3,'peterparker123@email.com','webapp123','2017-12-03 04:09:12','peterparker','d','Peter','Parker',0,0,NULL,0,0,NULL,NULL,NULL,NULL,NULL,0),(4,'stevejobs@apple.com','webapp123','2017-12-03 04:09:33','stevejobs','d','Steve','Jobs',0,0,NULL,0,0,NULL,NULL,NULL,NULL,NULL,0),(5,'bitcoin@email.com','webapp123','2017-12-03 04:10:32','bitcoin','c','Bitcoin','MineGuy',0,0,NULL,0,0,NULL,NULL,NULL,NULL,NULL,0),(6,'ayylmao@meme.com','webapp123','2017-12-03 04:10:45','ayylmao','c','Ayy','Lmao',0,0,NULL,0,0,NULL,NULL,NULL,NULL,NULL,0),(7,'luigimario','webapp123','2017-12-03 04:11:25','luigimario','c','Luigi','Mario',0,0,NULL,1,0,NULL,NULL,NULL,NULL,NULL,0),(8,'chrispanican','webapp123','2017-12-03 04:25:21','chris','a','Chris','Panican',0,0,NULL,0,0,NULL,NULL,NULL,NULL,NULL,0);
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

-- Dump completed on 2017-12-03 22:33:45
