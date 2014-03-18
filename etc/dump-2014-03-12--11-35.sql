-- MySQL dump 10.14  Distrib 5.5.35-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: gorodin
-- ------------------------------------------------------
-- Server version	5.5.35-MariaDB

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_5f412f9a` (`group_id`),
  KEY `auth_group_permissions_83d7f98b` (`permission_id`),
  CONSTRAINT `group_id_refs_id_f4b32aac` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `permission_id_refs_id_6ba0f519` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_37ef4eb4` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_d043b34a` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add city',7,'add_city'),(20,'Can change city',7,'change_city'),(21,'Can delete city',7,'delete_city'),(22,'Can add article',8,'add_article'),(23,'Can change article',8,'change_article'),(24,'Can delete article',8,'delete_article'),(25,'Can add article rubric',9,'add_articlerubric'),(26,'Can change article rubric',9,'change_articlerubric'),(27,'Can delete article rubric',9,'delete_articlerubric');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$12000$PZQIr1qrJX5g$t6+CfTymbeIWbVajgqMKsHCFR6ioMjebY17tLOJA8jw=','2014-03-09 19:13:56',1,'igor','','','igorkarbachinsky@mail.ru',1,1,'2014-03-03 13:00:01'),(2,'pbkdf2_sha256$12000$UrxoYQxPndv7$sFQt3Em7oePkWspc1BKM00W830sF+ahwCMTj9hblpZY=','2014-03-08 18:44:43',1,'laima','Барабулька','','knagisl@gmail.com',1,1,'2014-03-04 09:59:16'),(3,'pbkdf2_sha256$12000$2u9BRzNIGDqu$CNNtUDSJUpZNEdfkUAyWhknC/igNxO0V4s1saVKF/k8=','2014-03-11 07:21:00',1,'e.godov','Евгений','Годов','',1,1,'2014-03-04 10:01:05');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_6340c63c` (`user_id`),
  KEY `auth_user_groups_5f412f9a` (`group_id`),
  CONSTRAINT `group_id_refs_id_274b862c` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `user_id_refs_id_40c41112` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_6340c63c` (`user_id`),
  KEY `auth_user_user_permissions_83d7f98b` (`permission_id`),
  CONSTRAINT `permission_id_refs_id_35d9ac25` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `user_id_refs_id_4dc23c39` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_6340c63c` (`user_id`),
  KEY `django_admin_log_37ef4eb4` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_93d2d1f8` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `user_id_refs_id_c0d12874` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2014-03-03 13:49:10',1,7,'1','kashin',1,''),(2,'2014-03-03 13:49:26',1,8,'1','Российский рынок акций пикирует вниз ',1,''),(3,'2014-03-03 14:31:57',1,8,'1','Российский рынок акций пикирует вниз ',2,'Изменен text.'),(4,'2014-03-03 15:37:26',1,8,'1','Российский рынок акций пикирует вниз ',2,'Изменен text.'),(5,'2014-03-04 09:59:16',1,4,'2','laima',1,''),(6,'2014-03-04 09:59:37',1,4,'2','laima',2,'Изменен first_name,last_name и is_superuser.'),(7,'2014-03-04 10:00:16',1,4,'2','laima',2,'Изменен is_staff.'),(8,'2014-03-04 10:01:05',2,4,'3','e.godov',1,''),(9,'2014-03-04 10:01:21',2,4,'3','e.godov',2,'Изменен first_name,last_name,is_staff и is_superuser.'),(10,'2014-03-06 07:45:11',2,8,'2','Масленица по-кашински',1,''),(11,'2014-03-06 07:46:59',2,8,'3','Кашинские театралы в Твери',1,''),(12,'2014-03-06 07:47:22',2,8,'3','Кашинские театралы в Твери',2,'Ни одно поле не изменено.'),(13,'2014-03-06 07:48:12',2,8,'4','Весь этот джаз',1,''),(14,'2014-03-06 07:48:22',2,8,'1','Российский рынок акций пикирует вниз ',3,''),(15,'2014-03-06 07:50:28',2,8,'5','Региональные соревнования',1,''),(16,'2014-03-06 07:51:57',2,8,'6','Отчет отдела вневедомственной охраны',1,''),(17,'2014-03-06 07:53:08',2,7,'2','PK',1,''),(18,'2014-03-06 07:55:13',2,8,'7','Авачинский залив',1,''),(19,'2014-03-06 07:56:41',2,8,'8','Cостоялся митинг в поддержку украинского народа',1,''),(20,'2014-03-06 07:58:08',2,8,'9','Три пассажира пострадали в ДТП по вине пьяного водителя',1,''),(21,'2014-03-06 07:58:20',2,8,'9','Три пассажира пострадали в ДТП по вине пьяного водителя',2,'Ни одно поле не изменено.'),(22,'2014-03-06 07:58:40',2,8,'10','Мощный циклон со снегопадами и ураганным ветром обрушится на Камчатку уже завтра.',1,''),(23,'2014-03-06 08:00:21',2,4,'2','laima',2,'Изменен first_name и last_name.'),(24,'2014-03-06 09:46:05',2,8,'4','Весь этот джаз',2,'Изменен text.'),(25,'2014-03-06 09:46:40',2,8,'4','Весь этот джаз',2,'Изменен text.'),(26,'2014-03-06 09:47:03',2,8,'4','Весь этот джаз',2,'Изменен text.'),(27,'2014-03-06 09:47:58',2,8,'4','Весь этот джаз',2,'Изменен text.'),(28,'2014-03-08 18:50:16',2,8,'10','Мощный циклон со снегопадами и ураганным ветром обрушится на Камчатку уже завтра.',3,''),(29,'2014-03-08 18:50:16',2,8,'9','Три пассажира пострадали в ДТП по вине пьяного водителя',3,''),(30,'2014-03-08 18:50:16',2,8,'8','Cостоялся митинг в поддержку украинского народа',3,''),(31,'2014-03-08 18:50:16',2,8,'7','Авачинский залив',3,''),(32,'2014-03-08 18:51:14',2,8,'11','Закрыт проезд вдоль трассы газопровода Соболево-Петропавловск-Камчатский',1,''),(33,'2014-03-08 18:52:46',2,8,'11','Закрыт проезд вдоль трассы газопровода Соболево-Петропавловск-Камчатский',2,'Изменен text.'),(34,'2014-03-08 18:53:23',2,8,'11','Закрыт проезд вдоль трассы газопровода Соболево-Петропавловск-Камчатский',2,'Ни одно поле не изменено.'),(35,'2014-03-08 18:54:55',2,8,'12','дорожники уже приступили к ликвидации последствий циклона',1,''),(36,'2014-03-08 18:55:30',2,8,'12','Дорожники уже приступили к ликвидации последствий циклона',2,'Изменен title.'),(37,'2014-03-08 18:56:42',2,8,'13','Развлекательный комплекс «Атмосфера» обновят',1,''),(38,'2014-03-08 19:00:10',2,8,'14','На БАМе открылся новый магазин «Шамсы» ',1,''),(39,'2014-03-08 19:01:17',2,8,'14','На БАМе открылся новый магазин «Шамсы» ',2,'Ни одно поле не изменено.'),(40,'2014-03-08 19:01:19',2,8,'14','На БАМе открылся новый магазин «Шамсы» ',2,'Ни одно поле не изменено.'),(41,'2014-03-08 19:02:49',2,8,'15','Митинг в поддержку украинского народа',1,''),(42,'2014-03-08 19:04:38',2,8,'16','С улиц уберут 39 гаражей и 1 контейнер',1,''),(43,'2014-03-08 19:05:40',2,4,'2','laima',2,'Изменен email.'),(44,'2014-03-08 19:08:19',2,8,'17','Бьянка в «Шамсе»',1,''),(45,'2014-03-08 19:14:00',2,8,'18','3 марта - самое время поиграть в снежки!',1,''),(46,'2014-03-08 19:15:45',2,8,'19','Самые опасные дороги в городе',1,''),(47,'2014-03-08 19:17:50',2,8,'20','Камчатский вуз попал в «чёрный» список',1,''),(48,'2014-03-08 19:19:26',2,8,'21','Первенство Камчатского края по судомодельному спорту',1,''),(49,'2014-03-08 19:21:00',2,8,'22','Помогите найти человека!',1,''),(50,'2014-03-08 19:22:37',2,8,'23','Подростки обокрали школьную столовую',1,''),(51,'2014-03-08 19:25:04',2,8,'24','Приложения панорам Камчатки',1,''),(52,'2014-03-08 19:26:30',2,8,'25','Францева завоевала бронзовую медаль',1,''),(53,'2014-03-08 19:28:33',2,8,'26','Музыкальный конкурс «Вдохновение»',1,''),(54,'2014-03-08 19:30:30',2,8,'27','Отменены занятия в школах',1,''),(55,'2014-03-11 07:29:36',3,7,'3','belev',1,''),(56,'2014-03-11 07:42:05',3,8,'28','«Щелкунчик и мышиный король» в Театре юного зрителя',1,'');
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'log entry','admin','logentry'),(2,'permission','auth','permission'),(3,'group','auth','group'),(4,'user','auth','user'),(5,'content type','contenttypes','contenttype'),(6,'session','sessions','session'),(7,'city','gorod','city'),(8,'article','gorod','article'),(9,'article rubric','gorod','articlerubric');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_b7b81f0c` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('1pjl47gm1goecq0ba5l7isbwaxuw3961','NjI2OTZlYTIwNGRhYTJhYjAxOTA0OWNlZWI0OTgyYTIzMjBlZmFmODp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MX0=','2014-03-17 13:48:36'),('5kd7yj1prwyb9p8r2n8ov5nb7ji1hekw','YWE4OTNiNWUyMGYwYmIzZWUzNmQxNDM0YWU3MTk2ZTIwNzZmNTRkNzp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6M30=','2014-03-18 10:49:10'),('7ac9l5jau2lu6b1piqn7mwitnvskzkd2','YWE4OTNiNWUyMGYwYmIzZWUzNmQxNDM0YWU3MTk2ZTIwNzZmNTRkNzp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6M30=','2014-03-25 07:21:00'),('e4pesdh9086v89ro86bnudfbmzhehr9f','YWE4OTNiNWUyMGYwYmIzZWUzNmQxNDM0YWU3MTk2ZTIwNzZmNTRkNzp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6M30=','2014-03-24 05:12:50'),('ehgjxgjtasic10gsdr4yerd9xyenwakq','NjI2OTZlYTIwNGRhYTJhYjAxOTA0OWNlZWI0OTgyYTIzMjBlZmFmODp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MX0=','2014-03-23 19:13:56'),('ger7fpoe1nv9ya6xaohjs50lncibkq26','NDkxMTA2YzFhMzVmMTlkZGQ3NGMwYTI0ZGUwODU1MWNhOGQ0ZDRkYzp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6Mn0=','2014-03-22 18:44:43'),('lqy6qn69z3e37lo3ybv4b5m6vr1c5iwc','NDkxMTA2YzFhMzVmMTlkZGQ3NGMwYTI0ZGUwODU1MWNhOGQ0ZDRkYzp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6Mn0=','2014-03-18 10:00:25'),('mpuhax94lo043f9pwdbh327qktkf57kk','NDkxMTA2YzFhMzVmMTlkZGQ3NGMwYTI0ZGUwODU1MWNhOGQ0ZDRkYzp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6Mn0=','2014-03-18 10:02:08');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gorod_article`
--

DROP TABLE IF EXISTS `gorod_article`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gorod_article` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `add_date` datetime NOT NULL,
  `city_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `text` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `gorod_article_b376980e` (`city_id`),
  KEY `gorod_article_6340c63c` (`user_id`),
  CONSTRAINT `city_id_refs_id_a4dec0c6` FOREIGN KEY (`city_id`) REFERENCES `gorod_city` (`id`),
  CONSTRAINT `user_id_refs_id_0728b7ba` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gorod_article`
--

LOCK TABLES `gorod_article` WRITE;
/*!40000 ALTER TABLE `gorod_article` DISABLE KEYS */;
INSERT INTO `gorod_article` VALUES (2,'Масленица по-кашински','2014-03-06 07:43:11',1,2,'<p style=\"line-height: 16px; margin: 0px 0px 5px; text-align: justify; font-family: \'Open Sans\', Arial, Helvetica, sans-serif;\">На минувшей масленичной неделе в Кашине прошли народные гулянья, посвященные проводам зимы.</p>\r\n\r\n<p style=\"line-height: 16px; margin: 0px 0px 5px; text-align: justify; font-family: \'Open Sans\', Arial, Helvetica, sans-serif;\">В воскресенье 2 марта кашинцы по традиции отметили широкую Масленицу всем городом на Пролетарской площади. На празднике, организованном силами работников районного Дома культуры, прошли конкурсы креативных валенок и частушек, со сцены народ развлекали скоморохи, не обошлось без угощения блинчиками и сжигания чучела зимы. Самые смелые молодые люди приняли участие в аттракционе &laquo;Покорение столба&raquo;, пытаясь достать заветный приз.</p>\r\n\r\n<p style=\"line-height: 16px; margin: 0px 0px 5px; text-align: justify; font-family: \'Open Sans\', Arial, Helvetica, sans-serif;\">В четверг в детской библиотеке состоялись фольклорные праздники для учащихся 2 и 7 классов школы № 5. Сотрудники библиотеки и Кашинского краеведческого музея познакомили ребят с традициями этого праздника на Руси в целом и в Кашине в частности. Дети почитали заклички, попели песни и поиграли, познакомились с музейными экспонатами, а напоследок, как и полагается, отведали блинов, сообщила старший научный сотрудник музея Анна Петровна Малова.</p>\r\n\r\n<p style=\"line-height: 16px; margin: 0px 0px 5px; text-align: justify; font-family: \'Open Sans\', Arial, Helvetica, sans-serif;\">А в субботу на территории санатория &laquo;Кашин&raquo; на праздник, организованный туристической компанией &laquo;Кашин Град&raquo;, собрались более 250 человек: туристы из Москвы, отдыхающие на курорте и жители близлежащих домов. Участвуя в увлекательных народных играх, вместе с Микулой-богатырем и мудрым Колываном они помогли красавице Весне победить Зиму-Маревну, снегов королевну. Все желающие приобрели сувениры на ярмарке, научились лепить свечи из вощины на мастер-классе. ООО &laquo;Кашин Град&raquo; благодарит ООО &laquo;Санаторий Кашин&raquo; и его генерального директора Андрея Валерьевича Корешкова, районный Дом культуры и его директора Надежду Георгиевну Зимникову и директора ООО &laquo;Мебель&raquo; Наталию Ивановну Ковшун.</p>\r\n\r\n<p style=\"line-height: 16px; margin: 0px 0px 5px; text-align: justify; font-family: \'Open Sans\', Arial, Helvetica, sans-serif;\">&nbsp;</p>\r\n\r\n<p style=\"line-height: 16px; margin: 0px 0px 5px; text-align: justify; font-family: \'Open Sans\', Arial, Helvetica, sans-serif;\"><img alt=\"\" src=\"/media/uploads/2014/03/06/285_184_IMG_0193.JPG\" style=\"width: 285px; height: 184px;\" />&nbsp;<img alt=\"\" src=\"/media/uploads/2014/03/06/285_184_IMG_4833.JPG\" style=\"width: 285px; height: 184px;\" />&nbsp;</p>\r\n'),(3,'Кашинские театралы в Твери','2014-03-06 07:46:05',1,2,'<p style=\"line-height: 16px; margin: 0px 0px 5px; text-align: justify; font-family: \'Open Sans\', Arial, Helvetica, sans-serif;\"><img alt=\"\" src=\"/media/uploads/2014/03/06/328_246_IMG_0646.jpg\" style=\"width: 328px; height: 246px; float: left;\" /></p>\r\n\r\n<p style=\"line-height: 16px; margin: 0px 0px 5px; text-align: justify; font-family: \'Open Sans\', Arial, Helvetica, sans-serif;\">&laquo;Дети Мельпомены&raquo; &ndash; так назывался прошедший в феврале в Твери третий областной фестиваль-конкурс детского театрального творчества учащихся детских школ искусств Тверской области. Театральный коллектив &laquo;Зеркало&raquo; Кашинской ДШИ впервые выступал на областной сцене. К конкурсу была подготовлена музыкально-литературная композиция о Кашине, о людях, живших здесь в XVIII&ndash;XIX веках. Автором текста является руководитель коллектива Мария Николаевна Соткина.</p>\r\n\r\n<p style=\"line-height: 16px; margin: 0px 0px 5px; text-align: justify; font-family: \'Open Sans\', Arial, Helvetica, sans-serif;\">Оценивало выступление юных артистов профессиональное жюри: председатель Елена Аллеевна Салейкова, художественный руководитель и режиссер Московского детского театра &laquo;Клякса&raquo;, заслуженный работник культуры Анна Васильевна Козова, председатель ПЦК &laquo;Театральное творчество&raquo; Тверского колледжа культуры имени Н.А. Львова, заслуженный артист РФ, актер Тверского театра юного зрителя Александр Борисович Романов. Очень приятно, что дебют наших артистов на конкурсе такого уровня оказался успешным: театральный коллектив &laquo;Зеркало&raquo; Кашинской ДШИ награжден дипломом &laquo;За создание музыкально-драматической композиции о родном крае&raquo;. Поздравляем Дениса Соколова, Викторию Дубову, Алексея Тяпкина, Павла Жданова, а также участниц вокального ансамбля &laquo;Шармэль&raquo; Веронику Кушталь, Ксению Приходько, Алину Стрелкову, Кристину Никишаеву, благодаря которым спектакль получился более ярким, выразительным. Поздравляем Марию Николаевну Соткину с успехом. Благодарим Елену Валерьевну Стионову за инициативу и желаем не останавливаться на достигнутом и развивать творческое сотрудничество.</p>\r\n'),(4,'Весь этот джаз','2014-03-06 07:47:45',1,2,'<p><img alt=\"\" src=\"/media/uploads/2014/03/06/328_246_DSCN3469.JPG\" style=\"width: 327px; height: 246px; float: left;\" />12 февраля в Кашинской детской школе искусств состоялся отборочный тур второго межмуниципального фестиваля-конкурса эстрадно-джазового исполнительства &laquo;Дебют&raquo;.<br />\r\nДжаз достаточно сложен для исполнения и, наверное, поэтому не очень популярен. Но юные музыканты нашей школы вместе со своими педагогами показали неплохие результаты в этом новом для них жанре. Оценивало выступление конкурсантов жюри в составе заведующего отделом по делам культуры и туризма администрации Кашинского района Е.К. Корзиновой, директора районного Дома культуры Н.Г. Зимниковой, заведующего фортепианным отделением ДШИ, педагога высшей категории Т.И. Багровой, директора ДШИ, педагога высшей категории О.П. Стионовой. В отборочном туре приняли участие солисты вокального ансамбля &laquo;Шармэль&raquo; в возрасте от 7 до 13 лет, средняя и старшая группы ансамбля, а также учащиеся класса гитары Екатерина Козлова и Дмитрий Катуар, ВИА &laquo;ДеСанТа&raquo; в составе Татьяны Беляковой, Алины Стрелковой, Вероники Кушталь, Дениса Данишевского, Александра Гаврилова.<br />\r\nПо результатам конкурса дипломы первой степени получили средняя группа ансамбля &laquo;Шармэль&raquo;, солисты Александра Куликова (11 лет), Гришина Полина (10 лет), Офелия Кашинцева (7 лет). По условиям отборочного тура обладатели дипломов первой степени будут представлять нашу школу в финале конкурса в Торжке. Дипломами второй степени отмечены старшая группа ансамбля &laquo;Шармэль&raquo; и солистка ансамбля Анна Спирина (10 лет). Дипломантами третьей степени стали ВИА &laquo;ДеСанТа&raquo;, дуэт гитаристов и солисты ансамбля &laquo;Шармэль&raquo; Анастасия Коробка (12 лет) и Вероника Чудакова (13 лет). Ну а подготовили детей к конкурсу преподаватель класса гитары Ю.В. Сиднин и руководитель ансамбля &laquo;Шармэль&raquo; Е.В. Стионова.</p>\r\n'),(5,'Региональные соревнования','2014-03-06 07:50:33',1,2,'<p><span style=\"color: rgb(84, 84, 84); font-family: verdana, sans-serif; line-height: 16px; text-align: justify;\">На трассе ЛК &laquo;Б. Гришкино&raquo; прошли очередные региональные соревнования &ndash; 2 тур Чемпионата области и первенство среди спортивных школ и клубов. Соревнования проходили в очень сложных погодных условиях.&nbsp;</span><br style=\"margin: 0px; padding: 0px; color: rgb(84, 84, 84); font-family: verdana, sans-serif; line-height: 16px; text-align: justify;\" />\r\n<span style=\"color: rgb(84, 84, 84); font-family: verdana, sans-serif; line-height: 16px; text-align: justify;\">По итогам двух дней соревнований в сумме рейтинговых очков команда СК &laquo;Кашин&raquo; - на втором месте из пятнадцати спортивных школ и клубов области.</span><br style=\"margin: 0px; padding: 0px; color: rgb(84, 84, 84); font-family: verdana, sans-serif; line-height: 16px; text-align: justify;\" />\r\n<span style=\"color: rgb(84, 84, 84); font-family: verdana, sans-serif; line-height: 16px; text-align: justify;\">Две наши Виктории &ndash; Парфёнова и Солодовникова &ndash; завоевали для своей команды два золота и два серебра региональной пробы, Арина Богачёва &ndash; два четвёртых места. Команда в составе этих девушек показала самый высокий спортивный результат, они набрали наибольшее количество очков для своей сборной.&nbsp;</span><br style=\"margin: 0px; padding: 0px; color: rgb(84, 84, 84); font-family: verdana, sans-serif; line-height: 16px; text-align: justify;\" />\r\n<span style=\"color: rgb(84, 84, 84); font-family: verdana, sans-serif; line-height: 16px; text-align: justify;\">В состав нашей команды вошли: Юлия Лаврентьева, Екатерина Шишкина, Илья Белоусов, Максим Смирнов, Аташ Курбангельдиев, Артём и Александр Гейнц.</span><br style=\"margin: 0px; padding: 0px; color: rgb(84, 84, 84); font-family: verdana, sans-serif; line-height: 16px; text-align: justify;\" />\r\n<span style=\"color: rgb(84, 84, 84); font-family: verdana, sans-serif; line-height: 16px; text-align: justify;\">Следующие областные соревнования запланированы на 9 марта, но состоятся эти старты или нет, во многом будет зависеть от погоды.</span></p>\r\n'),(6,'Отчет отдела вневедомственной охраны','2014-03-06 07:52:01',1,2,'<p><span style=\"color: rgb(84, 84, 84); font-family: verdana, sans-serif; line-height: 16px; text-align: justify;\">Статистика показывает, что квартирные кражи на сегодняшний день остаются одним из самых распространённых видов преступлений. Воры не гнушаются ничем - похищают всё, что можно унести. Так что квартирная кража - это действительно беда и предупредить её можно только совместными усилиями правоохранительных органов и самих владельцев жилья. С целью профилактики квартирных краж и разъяснения населению элементарных мер по безопасности жилья на территории города Кашина проводится операция &quot;Безопасный дом, безопасный подъезд, безопасная квартира&quot; в проведении данной операции задействованы все службы МО &laquo;Кашинский&raquo;.</span></p>\r\n'),(11,'Закрыт проезд вдоль трассы газопровода Соболево-Петропавловск-Камчатский','2014-03-07 08:00:00',2,2,'<p>По данным дежурного ОАО &laquo;Газпром&raquo;, закрыт технологический проезд вдоль трассы газопровода Соболево-Петропавловск-Камчатский. Закрытие проезда связано с ухудшением видимости и метелью.<img alt=\"\" src=\"/media/uploads/2014/03/08/392643-4992x3328.jpg\" style=\"width: 600px; height: 400px;\" /></p>\r\n'),(12,'Дорожники уже приступили к ликвидации последствий циклона','2014-03-07 07:12:29',2,2,'<p>Для обработки подъемов и спусков противогололедным материалом на дороги краевого центра уже вышли пескоразбрасыватели. На тротуарах работает малая механизированная техника &ndash; с ее помощью дорожники счищают оттаявший снег с пешеходных дорожек, сообщает мэрия.</p>\r\n\r\n<p>По прогнозам синоптиков, во второй половине дня в Петропавловске ожидается метель. Как сообщили в МУП &laquo;Спецдорремстрой&raquo; как только осадки начнут усиливаться на трассы выйдет дополнительная спецтехника. В частности уже прошли профилактическое обслуживание и готовы к выходу 18 комбинированных дорожных машин, 16 грейдеров, а также шнекороторы, погрузчики и т.д.</p>\r\n\r\n<p>В первую очередь внимание дорожных служб будет уделено расчистке социальных объектов &ndash; детских садов, школ, больниц. До тех пор, пока погода не наладится, коммунальные службы будут работать в усиленном режиме.</p>\r\n\r\n<p><img alt=\"\" src=\"/media/uploads/2014/03/08/maxresdefault.jpg\" style=\"width: 500px; height: 281px;\" /></p>\r\n'),(13,'Развлекательный комплекс «Атмосфера» обновят','2014-03-07 05:56:32',2,2,'<p>В спортивно-развлекательном комплексе &laquo;Атмосфера&raquo; в Петропавловске-Камчатском будут возведены дополнительные трибуны для зрителей, расширены раздевалки, а также установлено новое звуковое оборудование. Об этом рассказали в министерстве спорта и молодежной политики Камчатского края.</p>\r\n\r\n<p>В планах также оборудование дополнительной автостоянки, ремонт машин для подготовки льда, замена освещения и бортов хоккейной коробки, установка современного ограждения для безопасности зрителей. Все это, по мнению специалистов, позволит улучшить условия для посетителей и увеличить пропускную способность спортивного сооружения, тем самым увеличив количество занимающихся физической культурой и спортом в Камчатском крае.</p>\r\n\r\n<p>Напомним, после того, как СРК &laquo;Атмосфера&raquo; в конце 2013 года по решению губернатора Камчатского края Владимира Илюхина был приобретен в собственность края и передан в КГАУ &laquo;Стадион &laquo;Спартак&raquo;, физкультурно-оздоровительная и спортивная деятельность значительно изменилась, став более доступной для населения.</p>\r\n\r\n<p>В сезоне 2013-2014 на базе СРК &laquo;Атмосфера&raquo; прошли городские соревнования на призы клуба &laquo;Золотая шайба&raquo; среди детей и подростков, открытый чемпионат города Петропавловска-Камчатского среди хоккейных команд взрослых с общим количеством участников более 300 человек. За дни новогодних каникул каток посетили более 5 тысяч. Ежедневно в &laquo;Атмосфере&raquo; проходят тренировки детских дворовых команд - &laquo;Звезда&raquo;, &laquo;Барс&raquo;, &laquo;Сероглазка&raquo;, учащихся детско-юношеской спортивной школы и взрослых команд по хоккею с шайбой, фигуристов.</p>\r\n'),(14,'На БАМе открылся новый магазин «Шамсы» ','2014-03-06 08:00:00',2,2,'<p>Весна в &laquo;Шамсе&raquo; началась с открытия нового супермаркета в районе БАМ (он расположен по адресу: Кирдищева, 6). Руководителем нового магазина назначена опытный сотрудник розничной сети ГК &laquo;Шамса&raquo; - Валикова Оксана Александровна. 5 марта 2014 года на торжественное открытие магазина пришли многие жители микрорайона. Одними из первых посетили магазин депутат Законодательного Собрания Камчатского края Александр Нуриев и представители проекта &laquo;Народный контроль&raquo;. Праздничное настроение воцарилось с первых минут его работы, а красочное оформление супермаркета порадовало всех без исключения.</p>\r\n\r\n<p>Посетителей встречали ростовые куклы и мимы . Сотрудники &laquo;Шамсы&raquo; приготовили в этот день для своих любимых покупателей приятные сюрпризы, скидки и подарки. Покупателей порадовали неизменное качество обслуживания. Они были приятно удивлены ассортиментом представленных товаров и вполне демократичными ценами. Состав солнечной Группы Компаний пополнился ещё одним прекрасным супермаркетом.</p>\r\n\r\n<p>&laquo;Развитие розничной сети - одна из приоритетных стратегических задач ГК &laquo;Шамса&raquo;, - рассказывает генеральный директор ООО &laquo;Шамса-Холдинг&raquo; Рашид Шамоян. - Мы стараемся обеспечить население Камчатки высоким уровнем обслуживания, разнообразным ассортиментом товаров, и создать комфортные условия для совершения покупок всем жителям краевого центра и других населенных пунктов. Мы очень рады тому, что во многих районах наши магазины становятся своеобразным центром притяжения для многих людей, местом для проведения интересных встреч, общественно значимых и социальных акций, благотворительных мероприятий. Мы всегда рады видеть Вас!&raquo;</p>\r\n\r\n<p><img alt=\"\" src=\"/media/uploads/2014/03/08/1 (1).jpg\" style=\"width: 500px; height: 375px;\" /></p>\r\n'),(15,'Митинг в поддержку украинского народа','2014-03-05 10:01:35',2,2,'<p>Митинг в поддержку братского украинского народа состоялся в Петропавловске-Камчатском. В нем приняли участие более 4,5 тысяч жителей Камчатки: представители различных национальных диаспор, родовых общин коренных малочисленных народов Севера, ветераны Великой Отечественной войны, члены камчатского казачьего войска, члены трудовых коллективов, политических партий и профсоюзных организаций.</p>\r\n\r\n<p>&laquo;Я еду в Украину и говорю, что еду домой. Еду из Украины в Россию &ndash; тоже домой, &ndash; говорит руководитель национально-культурной автономии украинцев Камчатки Виктор Манжос. &ndash; Сегодня в наш общий дом пришла беда. И мы должны все вместе встать на его защиту&raquo;.</p>\r\n\r\n<p>О поддержке народа Украины, о солидарности с позицией Президента России Путина говорили и руководители региональных отделений политических партий.</p>\r\n\r\n<p>&laquo;Мы полностью поддерживаем позицию правительства Российской Федерации и президента России Владимира Путина. Сегодня мы видим, что при вмешательстве сторонних сил происходит насильственное смещение власти, принижение роли украинского народа в самоопределении&raquo;, - сказал руководитель камчатского регионального отделения КПРФ Михаил Смагин.</p>\r\n\r\n<p>&laquo;Все россияне, вся наша страна готовы выступить в защиту тех, чьи гражданские и конституционные права нарушены. Сегодня мы объединяемся в единое движение в поддержку братского народа!&raquo;, - резюмировал председатель регионального отделения общероссийской организации &laquo;Содружество&raquo; Виталий Кибалов.</p>\r\n\r\n<p>Напомним, с инициативой о проведении митинга в краевой столице выступило региональное отделение общероссийской организации &laquo;Содружество&raquo;.</p>\r\n\r\n<p><img alt=\"\" src=\"/media/uploads/2014/03/08/large_e3ab491604.JPG\" style=\"width: 500px; height: 333px;\" /></p>\r\n'),(16,'С улиц уберут 39 гаражей и 1 контейнер','2014-03-05 19:03:41',2,2,'<p>Управлением по взаимодействию с субъектами малого и среднего предпринимательства Петропавловска составлен очередной список объектов, подлежащих демонтажу. В скором времени с улиц краевого центра на площадку временного хранения вывезут ещё 39 гаражей и 1 контейнер, владельцы которых не имеют разрешительных документов на их размещение.</p>\r\n\r\n<p>Как пояснили в Управлении, данные объекты расположены по ул. Ларина 10/6 и ул. Войцешека 3А. Ознакомиться с полным перечнем и описанием конструкций, подлежащих вывозу можно на официальном сайте администрации: http://pkgo.ru в разделе &laquo;Объявления&raquo;.</p>\r\n\r\n<p>В Управлении сообщили, что собственникам строений было дано время на то, чтобы самостоятельно вывезти своё имущество. Освободить земельные участки они должны в срок до 6 марта. В противном случае гаражи будут вывезены на площадку временного хранения в принудительном порядке. При этом расходы по транспортировке впоследствии взыщут с собственников.</p>\r\n\r\n<p><img alt=\"\" src=\"/media/uploads/2014/03/08/20130217440.jpg\" style=\"width: 500px; height: 375px;\" /></p>\r\n'),(17,'Бьянка в «Шамсе»','2014-03-03 23:00:00',2,2,'<p>Весна в &laquo;Шамсе&raquo; начнётся с приезда популярной артистки, исполнительницы хитов поп-музыки Бьянки, 5 марта в 19.00 всех почитателей творчества молодой певицы будут ждать в новом корпусе т\\ц &laquo;Шамса&raquo;.</p>\r\n\r\n<p><img alt=\"\" src=\"/media/uploads/2014/03/08/13081676.jpg\" style=\"width: 500px; height: 281px;\" /></p>\r\n'),(18,'3 марта - самое время поиграть в снежки!','2014-03-03 08:00:00',2,2,'<p><img alt=\"\" src=\"/media/uploads/2014/03/08/0oYxjbTTTwQ.jpg\" style=\"width: 500px; height: 380px;\" /></p>\r\n'),(19,'Самые опасные дороги в городе','2014-03-02 14:43:00',2,2,'<p>По топографическому анализу происшествий за 2013 год самым опасным участком признан проспект Победы: там произошло 24 ДТП, два человека погибли.</p>\r\n\r\n<p>Также в списке самых аварийных: пр. 50 лет Октября (10 ДТП, ранены 11 человек), Циолковского (11 ДТП, ранены 14 человек), ул. Тушканова (9 ДТП, 12 ранены), ул. Ленинградская (10 ДТП, 12 пострадавших), Набережная (8 ДТП, 15 пострадавших), Зеркальная, Пограничная, Ленинская, Океанская и проспект Рыбаков.</p>\r\n\r\n<p>&nbsp;</p>\r\n'),(20,'Камчатский вуз попал в «чёрный» список','2014-02-28 09:00:00',2,2,'<p><span style=\"color: rgb(0, 0, 0); font-family: \'PT Serif\', Georgia, serif; font-size: 14px; line-height: 17.279998779296875px;\">Филиал Современной гуманитарной академии в Петропавловске лишён лицензии на образовательную деятельность.</span></p>\r\n\r\n<p><span style=\"color: rgb(0, 0, 0); font-family: \'PT Serif\', Georgia, serif; font-size: 14px; line-height: 17.279998779296875px;\">&laquo;В период подготовки к&nbsp;приемной кампании, чтобы помочь абитуриентами и&nbsp;выпускниками текущего года в&nbsp;предстоящем выборе вуза для&nbsp;продолжения образования, Рособрнадзор публикует перечень образовательных организаций и&nbsp;филиалов, чьи лицензии на&nbsp;образовательную деятельность исключены из&nbsp;реестра лицензий с&nbsp;1 сентября 2013 по&nbsp;27 февраля 2014 годов&raquo;, &mdash; говорится в сообщении ведомства.</span></p>\r\n'),(21,'Первенство Камчатского края по судомодельному спорту','2014-03-08 19:19:19',2,2,'<p>В воскресение, 16 февраля, пройдет первенство Камчатского края по судомодельному спорту. Посмотреть на это увлекательное действие приглашаются все желающие. Место проведения соревнований - бассейн на 9-м километре. Начало мероприятия в 10-00. Приходите сами, приводите детей.</p>\r\n'),(22,'Помогите найти человека!','2014-03-07 21:20:47',2,2,'<p>Помогите пожалуйста найти человека!</p>\r\n\r\n<p>Мой сосед сверху: его адрес 50 лет октября, д9/3, кв. 23 - ищем всем подьездом - затопил меня кипятком! (Сауну устроил). телефона никто не знает. перекрыли стояк - теперь во всем подъезде нет не горячей воды, не отопления. Все комунальщики и другие структуры разводят руками, ПРАЗДНИКИ... Зовут его вроде Васильев Виктор, только и слышу - он редко дома бывает...</p>\r\n'),(23,'Подростки обокрали школьную столовую','2014-03-07 08:50:00',2,2,'<p>Двое подростков обокрали школьную столовую в Петропавловске. Оттуда они вынесли кондитерские изделия, сообщает пресс-служба городского УМВД.</p>\r\n\r\n<p>Там рассказали, в фойе школы вошел подросток и попросил у женщины-сторожа, разрешения забрать из раздевалки забытую сменную обувь. Женщина впустила мальчика, следом за ним в здание учебного заведения вошли еще двое несовершеннолетних. Один из подростков, явно самый старший, находился в состоянии алкогольного опьянения, женщина пригрозила вызвать полицию. Выпившего несовершеннолетнего сторож закрыла в подсобном помещении, а двое других в это время стали бегать от нее по школе и прятаться. Пытаясь догнать детей, женщина не увидела, как один из подростков взял на вахте ключ с надписью &laquo;столовая&raquo;.</p>\r\n\r\n<p>&laquo;Украв в столовой сладости, подростки сбежали через окно, расположенное на первом этаже. Подъехавшим по сигналу тревожной кнопки полицейским пенсионерка рассказала о случившемся, и показала, где закрыла одного из подростков&raquo;, - рассказали в МВД.<br />\r\nУстановлено, что кражу совершили двое несовершеннолетних жителей Петропавловска. 13-летний мальчик возраста, с которого наступает уголовная ответственность, не достиг, поэтому к административной ответственности привлечены его родители. А вот 16-летнему придется отвечать по всей строгости закона. В отношении него возбуждено уголовное дело по ст. 158 УК РФ &laquo;Кража&raquo;, с него взята подписка о невыезде.</p>\r\n\r\n<p>Третий шутник, которому 17-лет, привлечен к административной ответственности по ст. 20.21 КРФоАП &laquo;Появление в общественных местах в состоянии опьянения&raquo;.</p>\r\n'),(24,'Приложения панорам Камчатки','2014-03-05 20:30:04',2,2,'<p>Инициаторами проекта стали специалисты компании AirPano из Москвы, рассказали в пресс-службе Кроноцкого заповедника. Для работы были использованы беспилотные летательные аппараты. Они помогли запечатлеть извержение вулкана Плоский Толбачик, нерест лососей и рыбалку медведей на Курильском озере, извержение источников и кипящих котлов в Долине гейзеров. Из полученного материала были созданы сферические панорамы 360&ordm;. Теперь они оформлены в виде бесплатных приложений. Их, владельцам продукции компании Apple, можно скачать в интернет-магазине App Store.Подключение к интернету требуется только для первичной установки. После этого приложения работают в автономном режиме.</p>\r\n\r\n<p>Найти и скачать приложения AirPano для iPad можно по следующим ссылкам:</p>\r\n\r\n<p>https://itunes.apple.com/us/app/volcano-360/id651461233?mt=8</p>\r\n\r\n<p>https://itunes.apple.com/us/app/geyser-360/id813811579?mt=8</p>\r\n\r\n<p>https://itunes.apple.com/us/app/bears-360/id817468889?mt=8</p>\r\n\r\n<p><img alt=\"\" src=\"/media/uploads/2014/03/08/b4oJAuQBuZc.jpg\" style=\"width: 500px; height: 363px;\" /></p>\r\n'),(25,'Францева завоевала бронзовую медаль','2014-03-08 19:25:56',2,2,'<p>Камчатская горнолыжница Александра Францева завоевала бронзовую медаль в скоростном спуске среди спортсменок с нарушением зрения на Паралимпийских играх в Сочи.</p>\r\n\r\n<p><img alt=\"\" src=\"/media/uploads/2014/03/08/xdbPVsbzaFs.jpg\" style=\"width: 421px; height: 264px;\" /></p>\r\n'),(26,'Музыкальный конкурс «Вдохновение»','2014-03-08 19:28:29',2,2,'<p>II городской смотр-конкурс юных исполнителей на народных и оркестровых инструментах &laquo;Вдохновение&raquo; пройдет в Петропавловске с 13 по 15 марта. Прослушивания состоятся в концертном зале Детской музыкальной школы № 5 по адресу: пр. Циолковского, 25. В конкурсе примут участие 102 солиста из 6 детских музыкальных школ городского округа.</p>\r\n'),(27,'Отменены занятия в школах','2014-03-07 07:30:20',2,2,'<p>В связи с неблагоприятными погодными условиями занятия с 1 по 4 классы всех школ города в первую смену отменены. Во второй половине дня погода ухудшиться, поэтому занятия второй смены во всех городских школах также отменены.</p>\r\n'),(28,'«Щелкунчик и мышиный король» в Театре юного зрителя','2014-03-11 07:42:02',3,2,'<p>18 марта 2014 года в Театре юного зрителя (г.Тула) состоится показ спектакля по сказке Э.Т.А. Гофмана &laquo;Щелкунчик и мышиный король&raquo;. Приглашаем всех жителей <strong>г.Белёва</strong> порадовать своих деток прекрасным представлением. Тем более, есть надежда, что юному зрителю представят классическую постановку, а не осовремененный &laquo;креатив&raquo;. Там же, но уже 23 марта можно будет посмотреть спектакль &laquo;Вождь краснокожих&raquo; и &laquo;Бременские музыканты&raquo; (25 марта).</p>\r\n');
/*!40000 ALTER TABLE `gorod_article` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gorod_articlerubric`
--

DROP TABLE IF EXISTS `gorod_articlerubric`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gorod_articlerubric` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gorod_articlerubric`
--

LOCK TABLES `gorod_articlerubric` WRITE;
/*!40000 ALTER TABLE `gorod_articlerubric` DISABLE KEYS */;
/*!40000 ALTER TABLE `gorod_articlerubric` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gorod_city`
--

DROP TABLE IF EXISTS `gorod_city`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gorod_city` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `title` varchar(255) NOT NULL,
  `add_date` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gorod_city`
--

LOCK TABLES `gorod_city` WRITE;
/*!40000 ALTER TABLE `gorod_city` DISABLE KEYS */;
INSERT INTO `gorod_city` VALUES (1,'kashin','Кашин','2014-03-03 13:49:09'),(2,'PK','Петропавловск-Камчатский','2014-03-06 07:53:12'),(3,'belev','Белёв','2014-03-11 07:29:46');
/*!40000 ALTER TABLE `gorod_city` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2014-03-12 11:35:24
