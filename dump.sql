-- MySQL dump 10.13  Distrib 5.5.34, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: gorod_in
-- ------------------------------------------------------
-- Server version	5.5.34-0ubuntu0.13.04.1

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
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add city',7,'add_city'),(20,'Can change city',7,'change_city'),(21,'Can delete city',7,'delete_city'),(22,'Can add article',8,'add_article'),(23,'Can change article',8,'change_article'),(24,'Can delete article',8,'delete_article'),(28,'Can add article rubric',10,'add_articlerubric'),(29,'Can change article rubric',10,'change_articlerubric'),(30,'Can delete article rubric',10,'delete_articlerubric'),(31,'Can add migration history',11,'add_migrationhistory'),(32,'Can change migration history',11,'change_migrationhistory'),(33,'Can delete migration history',11,'delete_migrationhistory'),(34,'Can add organization',12,'add_organization'),(35,'Can change organization',12,'change_organization'),(36,'Can delete organization',12,'delete_organization'),(37,'Can add city info',13,'add_cityinfo'),(38,'Can change city info',13,'change_cityinfo'),(39,'Can delete city info',13,'delete_cityinfo'),(40,'Can add organization category',14,'add_organizationcategory'),(41,'Can change organization category',14,'change_organizationcategory'),(42,'Can delete organization category',14,'delete_organizationcategory'),(43,'Can add organization phone',15,'add_organizationphone'),(44,'Can change organization phone',15,'change_organizationphone'),(45,'Can delete organization phone',15,'delete_organizationphone'),(46,'Can add organization address',16,'add_organizationaddress'),(47,'Can change organization address',16,'change_organizationaddress'),(48,'Can delete organization address',16,'delete_organizationaddress'),(49,'Can add organization schedule',17,'add_organizationschedule'),(50,'Can change organization schedule',17,'change_organizationschedule'),(51,'Can delete organization schedule',17,'delete_organizationschedule'),(52,'Can add user social auth',18,'add_usersocialauth'),(53,'Can change user social auth',18,'change_usersocialauth'),(54,'Can delete user social auth',18,'delete_usersocialauth'),(55,'Can add nonce',19,'add_nonce'),(56,'Can change nonce',19,'change_nonce'),(57,'Can delete nonce',19,'delete_nonce'),(58,'Can add association',20,'add_association'),(59,'Can change association',20,'change_association'),(60,'Can delete association',20,'delete_association'),(61,'Can add code',21,'add_code'),(62,'Can change code',21,'change_code'),(63,'Can delete code',21,'delete_code'),(64,'Can add user',22,'add_user'),(65,'Can change user',22,'change_user'),(66,'Can delete user',22,'delete_user'),(67,'Can add captcha store',23,'add_captchastore'),(68,'Can change captcha store',23,'change_captchastore'),(69,'Can delete captcha store',23,'delete_captchastore'),(70,'Can add source',24,'add_source'),(71,'Can change source',24,'change_source'),(72,'Can delete source',24,'delete_source'),(73,'Can add thumbnail',25,'add_thumbnail'),(74,'Can change thumbnail',25,'change_thumbnail'),(75,'Can delete thumbnail',25,'delete_thumbnail'),(76,'Can add thumbnail dimensions',26,'add_thumbnaildimensions'),(77,'Can change thumbnail dimensions',26,'change_thumbnaildimensions'),(78,'Can delete thumbnail dimensions',26,'delete_thumbnaildimensions'),(79,'Can add site',27,'add_site'),(80,'Can change site',27,'change_site'),(81,'Can delete site',27,'delete_site'),(82,'Can add city welcome',28,'add_citywelcome'),(83,'Can change city welcome',28,'change_citywelcome'),(84,'Can delete city welcome',28,'delete_citywelcome'),(85,'Can create article without admin checking',8,'article_create_wo_check'),(86,'Can sen not approved articles',8,'article_see_not_checked'),(87,'Can add city info question',29,'add_cityinfoquestion'),(88,'Can change city info question',29,'change_cityinfoquestion'),(89,'Can delete city info question',29,'delete_cityinfoquestion'),(90,'Can add complaint',30,'add_complaint'),(91,'Can change complaint',30,'change_complaint'),(92,'Can delete complaint',30,'delete_complaint'),(93,'Can add city hub',31,'add_hubquestion'),(94,'Can change city hub',31,'change_hubquestion'),(95,'Can delete city hub',31,'delete_hubquestion'),(96,'Can add hub answer',32,'add_hubanswer'),(97,'Can change hub answer',32,'change_hubanswer'),(98,'Can delete hub answer',32,'delete_hubanswer'),(99,'Can add user stat',33,'add_userstat'),(100,'Can change user stat',33,'change_userstat'),(101,'Can delete user stat',33,'delete_userstat');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$12000$PZQIr1qrJX5g$t6+CfTymbeIWbVajgqMKsHCFR6ioMjebY17tLOJA8jw=','2014-06-07 22:37:50',1,'igor','Игорь','Карбачинский','igorkarbachinsky@mail.ru',1,1,'2014-03-03 13:00:01'),(2,'pbkdf2_sha256$12000$UrxoYQxPndv7$sFQt3Em7oePkWspc1BKM00W830sF+ahwCMTj9hblpZY=','2014-03-08 18:44:43',1,'laima','Барабулька','','knagisl@gmail.com',1,1,'2014-03-04 09:59:16'),(3,'pbkdf2_sha256$12000$2u9BRzNIGDqu$CNNtUDSJUpZNEdfkUAyWhknC/igNxO0V4s1saVKF/k8=','2014-03-12 09:44:09',1,'e.godov','Евгений','Годов','',1,1,'2014-03-04 10:01:05');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `captcha_captchastore`
--

LOCK TABLES `captcha_captchastore` WRITE;
/*!40000 ALTER TABLE `captcha_captchastore` DISABLE KEYS */;
INSERT INTO `captcha_captchastore` VALUES (9,'NMWK','nmwk','8a9c3e45231a9418e1a596047d55b1d43b9d750b','2014-06-21 23:28:37'),(11,'VAKG','vakg','62ff1a4d8332e5cc6948542a4b52d26734faa38c','2014-06-22 12:35:01');
/*!40000 ALTER TABLE `captcha_captchastore` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2014-06-17 16:39:30',4,22,'3','karbachinsky',2,'Изменен city.'),(2,'2014-06-17 16:42:40',4,22,'3','karbachinsky',2,'Изменен city.'),(3,'2014-06-17 17:04:08',4,22,'3','karbachinsky',2,'Изменен city.'),(4,'2014-06-17 17:04:38',4,22,'3','karbachinsky',2,'Изменен city.'),(5,'2014-06-17 17:08:45',4,22,'3','karbachinsky',2,'Ни одно поле не изменено.'),(6,'2014-06-17 17:09:08',4,22,'3','karbachinsky',2,'Изменен city.'),(7,'2014-06-17 17:11:55',4,22,'3','karbachinsky',2,'Изменен city.'),(8,'2014-06-21 21:26:17',4,8,'59','34234234',2,'Изменен picture и text.'),(9,'2014-07-08 09:07:43',4,8,'57','igor admin',2,'Изменен picture и text.'),(10,'2014-07-11 16:20:35',4,8,'58','karbachinsy article',2,'Изменен rubric и text.'),(11,'2014-07-11 16:20:54',4,8,'58','karbachinsy article',2,'Изменен rubric.'),(12,'2014-07-11 16:21:13',4,8,'52','sdfgsf',2,'Изменен rubric.'),(13,'2014-07-11 16:41:24',4,12,'2','dfbdf',2,'Изменен city.'),(14,'2014-07-17 21:34:05',4,28,'1','CityWelcome object',1,''),(15,'2014-07-17 21:36:38',4,28,'1','CityWelcome object',2,'Ни одно поле не изменено.'),(16,'2014-07-18 13:05:57',4,28,'1','CityWelcome object',1,''),(17,'2014-07-22 09:33:36',4,8,'57','igor admin',2,'Изменен text.'),(18,'2014-07-22 09:34:12',4,8,'57','igor admin',2,'Изменен text.'),(19,'2014-07-22 10:29:48',4,8,'57','igor admin',2,'Изменен text.'),(20,'2014-07-22 10:31:11',4,8,'57','igor admin',2,'Ни одно поле не изменено.'),(21,'2014-07-22 11:09:20',4,10,'1','event',2,'Изменен title_plural.'),(22,'2014-07-22 16:52:48',4,7,'2','PK',2,'Изменен short_title.'),(23,'2014-07-24 07:11:36',4,13,'1','CityInfo object',2,'Добавлен city info question \"CityInfoQuestion object\". Добавлен city info question \"CityInfoQuestion object\".'),(24,'2014-07-25 07:20:13',4,8,'57','igor admin',2,'Ни одно поле не изменено.'),(25,'2014-08-07 17:04:33',4,7,'2','pk',2,'Изменен name.'),(26,'2014-08-10 14:47:31',4,31,'1','HubQuestion object',1,''),(27,'2014-08-10 15:18:06',4,31,'1','HubQuestion object',2,'Изменены text для hub answer \"HubAnswer object\". Изменены text для hub answer \"HubAnswer object\".'),(28,'2014-08-12 17:44:38',4,12,'2','dfbdf',2,'Добавлен organization phone \"123123123123123\".');
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'log entry','admin','logentry'),(2,'permission','auth','permission'),(3,'group','auth','group'),(5,'content type','contenttypes','contenttype'),(6,'session','sessions','session'),(7,'city','gorod','city'),(8,'article','gorod','article'),(10,'article rubric','gorod','articlerubric'),(11,'migration history','south','migrationhistory'),(12,'organization','gorod','organization'),(13,'city info','gorod','cityinfo'),(14,'organization category','gorod','organizationcategory'),(15,'organization phone','gorod','organizationphone'),(16,'organization address','gorod','organizationaddress'),(17,'organization schedule','gorod','organizationschedule'),(18,'user social auth','default','usersocialauth'),(19,'nonce','default','nonce'),(20,'association','default','association'),(21,'code','default','code'),(22,'user','gorod','user'),(23,'captcha store','captcha','captchastore'),(24,'source','easy_thumbnails','source'),(25,'thumbnail','easy_thumbnails','thumbnail'),(26,'thumbnail dimensions','easy_thumbnails','thumbnaildimensions'),(27,'site','sites','site'),(28,'city welcome','gorod','citywelcome'),(29,'city info question','gorod','cityinfoquestion'),(30,'complaint','gorod','complaint'),(31,'city hub','gorod','hubquestion'),(32,'hub answer','gorod','hubanswer'),(33,'user stat','gorod','userstat');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('1pjl47gm1goecq0ba5l7isbwaxuw3961','NjI2OTZlYTIwNGRhYTJhYjAxOTA0OWNlZWI0OTgyYTIzMjBlZmFmODp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MX0=','2014-03-17 13:48:36'),('223mlqewpv4rwgsibvsevugczts3ev5k','Y2EyYjI5ZTc4Njg1ZjIxYmY1ZGRlZjhmZDc3ZDZiMmZjN2ViOGRhNzp7InZrLW9hdXRoMl9zdGF0ZSI6Iml5SWJpajZjTms5Q3VveDExSTVPZTJlcDB0aDJNenhnIiwiX2F1dGhfdXNlcl9pZCI6Mywic29jaWFsX2F1dGhfbGFzdF9sb2dpbl9iYWNrZW5kIjoidmstb2F1dGgyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoic29jaWFsLmJhY2tlbmRzLnZrLlZLT0F1dGgyIiwibmV4dCI6Ii90b3duL1BLLyIsIl9zZXNzaW9uX2V4cGlyeSI6ODYzOTR9','2014-06-12 17:16:25'),('32kmb2ibvs3hnvmi4fhx7srhu6cdunm8','NjI2OTZlYTIwNGRhYTJhYjAxOTA0OWNlZWI0OTgyYTIzMjBlZmFmODp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MX0=','2014-03-26 10:53:59'),('3x6xdnrmz9ldiu0x5crom43rj6ihs312','MDJkODk5Y2EyMmNkNTQ0NTZjMjk1NmEzMjViNzBjN2JiMjRhYTM1Yzp7fQ==','2014-06-25 17:15:32'),('4nmu8vt7hurbqhg9ox3q0iqsfhuunuex','MDJkODk5Y2EyMmNkNTQ0NTZjMjk1NmEzMjViNzBjN2JiMjRhYTM1Yzp7fQ==','2014-06-25 17:15:32'),('4wx3bpago7npop8zwmjccws4ebn1aqia','MGMyZTViY2MwYWYxZTEzZjlmNjczOGU0YzUyZDhhYWZmNzQ1ZWFhOTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6NH0=','2014-07-25 16:19:47'),('5kd7yj1prwyb9p8r2n8ov5nb7ji1hekw','YWE4OTNiNWUyMGYwYmIzZWUzNmQxNDM0YWU3MTk2ZTIwNzZmNTRkNzp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6M30=','2014-03-18 10:49:10'),('7ac9l5jau2lu6b1piqn7mwitnvskzkd2','YWE4OTNiNWUyMGYwYmIzZWUzNmQxNDM0YWU3MTk2ZTIwNzZmNTRkNzp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6M30=','2014-03-25 07:21:00'),('8k3eiz9zmky0qjxni7ek0xl5hglrc8n0','NjI2OTZlYTIwNGRhYTJhYjAxOTA0OWNlZWI0OTgyYTIzMjBlZmFmODp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MX0=','2014-04-23 16:44:33'),('8n9s9hrhxqb5ntuay0eizhxu4kc0u970','NjI2OTZlYTIwNGRhYTJhYjAxOTA0OWNlZWI0OTgyYTIzMjBlZmFmODp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MX0=','2014-03-30 19:01:39'),('8piu2wctyqb5n9vsr1sui5hm7dvj3eto','MDJkODk5Y2EyMmNkNTQ0NTZjMjk1NmEzMjViNzBjN2JiMjRhYTM1Yzp7fQ==','2014-06-21 22:32:35'),('ah6jzbr9jbmdj6jerjq0h1rqwqpnm0yg','MGMyZTViY2MwYWYxZTEzZjlmNjczOGU0YzUyZDhhYWZmNzQ1ZWFhOTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6NH0=','2014-07-05 19:30:52'),('bff6mzmrimx86yyn3jv37m3kapcftpb4','YTk2MDg0MDAxOTMzZjg4MWQ1YjA1ZWQ4MTFjMDYzM2NkODQ0NDdjMjp7InZrLW9hdXRoMl9zdGF0ZSI6InVXemhwb2QzNlRvTGFqOUdtaG9sTXA4Vzg3V1c0WWZjIiwiX2F1dGhfdXNlcl9pZCI6Mywic29jaWFsX2F1dGhfbGFzdF9sb2dpbl9iYWNrZW5kIjoidmstb2F1dGgyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoic29jaWFsLmJhY2tlbmRzLnZrLlZLT0F1dGgyIiwibmV4dCI6Ii9way8iLCJfc2Vzc2lvbl9leHBpcnkiOjg2Mzk1fQ==','2014-08-12 09:21:13'),('e4pesdh9086v89ro86bnudfbmzhehr9f','YWE4OTNiNWUyMGYwYmIzZWUzNmQxNDM0YWU3MTk2ZTIwNzZmNTRkNzp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6M30=','2014-03-24 05:12:50'),('efesvjc31cj3ljxh86r89vmd23a6gxsu','MDJkODk5Y2EyMmNkNTQ0NTZjMjk1NmEzMjViNzBjN2JiMjRhYTM1Yzp7fQ==','2014-06-25 17:15:32'),('ehgjxgjtasic10gsdr4yerd9xyenwakq','NjI2OTZlYTIwNGRhYTJhYjAxOTA0OWNlZWI0OTgyYTIzMjBlZmFmODp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MX0=','2014-03-23 19:13:56'),('fpklcon989ticbmdbnul3fgiacwlayt1','NjI2OTZlYTIwNGRhYTJhYjAxOTA0OWNlZWI0OTgyYTIzMjBlZmFmODp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MX0=','2014-03-26 19:28:29'),('ger7fpoe1nv9ya6xaohjs50lncibkq26','NDkxMTA2YzFhMzVmMTlkZGQ3NGMwYTI0ZGUwODU1MWNhOGQ0ZDRkYzp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6Mn0=','2014-03-22 18:44:43'),('hjbgxd941sadha0em4uiz21i31r0gvod','NzQ4ODY2MWIyNTYyNWQwY2YyY2E1MmU0ZWY0ZDQxODFmODU1OWM3Njp7InZrLW9hdXRoMl9zdGF0ZSI6Im5YT1NqcE1IcHBrWFFzTWR6MThud2dmakxPVGhXSnRDIn0=','2014-06-21 21:28:06'),('jllptwm6ltl9zwrnlufstsf6owmtftx0','ZDgwNDkwYjhlMDBkZTQ0ZmY1YWNiN2QzOTk1YTFhNjQwNDc0ODE1Njp7InZrLW9hdXRoMl9zdGF0ZSI6ImE0Y1R1ckxORHM1UnVya2VhVWE5NHRTTVlOd1k2NlVsIiwiX2F1dGhfdXNlcl9pZCI6MSwic29jaWFsX2F1dGhfbGFzdF9sb2dpbl9iYWNrZW5kIjoidmstb2F1dGgyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoic29jaWFsLmJhY2tlbmRzLnZrLlZLT0F1dGgyIiwibmV4dCI6Ii90b3duL2JlbGV2LyIsIl9zZXNzaW9uX2V4cGlyeSI6ODYzOTV9','2014-06-09 22:23:00'),('kmk1ebfxuul150qcwe1mwy4dl83iz8f3','MGZmMzU1N2VhNTU3MDQ2NDBiN2Q4YWM5MWU3MTYyYTk1MjY2ZjYxZDp7ImZhY2Vib29rX3N0YXRlIjoidWdWMDVKQldGMEdJSlBrUFhWM0x6cDBnSXRHYXlSTHYiLCJ2ay1vYXV0aDJfc3RhdGUiOiJ0a2cxTlg0ZHlTd2ZlT0tuNHRlREFoNjVmanJtdE5xdSIsImdvb2dsZS1vYXV0aDJfc3RhdGUiOiJNTld2QlNlbzRlMkh5SjVPeWFweHRWMVozSm1ZYUt3NSIsIl9hdXRoX3VzZXJfaWQiOjEsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2014-06-06 17:04:50'),('lqy6qn69z3e37lo3ybv4b5m6vr1c5iwc','NDkxMTA2YzFhMzVmMTlkZGQ3NGMwYTI0ZGUwODU1MWNhOGQ0ZDRkYzp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6Mn0=','2014-03-18 10:00:25'),('mpuhax94lo043f9pwdbh327qktkf57kk','NDkxMTA2YzFhMzVmMTlkZGQ3NGMwYTI0ZGUwODU1MWNhOGQ0ZDRkYzp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6Mn0=','2014-03-18 10:02:08'),('nvp9ei79bilu1av7377xefxqk5r607pt','MDJkODk5Y2EyMmNkNTQ0NTZjMjk1NmEzMjViNzBjN2JiMjRhYTM1Yzp7fQ==','2014-06-22 22:22:53'),('ppj785556ygkwz4s57tqq29w4dri0www','MWIzZjBmNTE5ZGE0YmYyMzUwZDIwZDIwYWJiZDM1N2EyZDBhZjlhZjp7InZrLW9hdXRoMl9zdGF0ZSI6Imw3d2ltMkZDaDNHc0g0cXFlakk0SG52WlR5UUQwSnpuIiwiX2F1dGhfdXNlcl9pZCI6Mywic29jaWFsX2F1dGhfbGFzdF9sb2dpbl9iYWNrZW5kIjoidmstb2F1dGgyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoic29jaWFsLmJhY2tlbmRzLnZrLlZLT0F1dGgyIiwibmV4dCI6Ii90b3duL2JlbGV2LyIsIl9zZXNzaW9uX2V4cGlyeSI6ODYzOTV9','2014-06-18 16:26:04'),('q8bpt0c8vf5nt1c3ubkl766rmfpe9p3v','MGMyZTViY2MwYWYxZTEzZjlmNjczOGU0YzUyZDhhYWZmNzQ1ZWFhOTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6NH0=','2014-08-26 17:44:16'),('qbavlzrfm5qaur3ygnx7jhg3pggmdci5','MDJkODk5Y2EyMmNkNTQ0NTZjMjk1NmEzMjViNzBjN2JiMjRhYTM1Yzp7fQ==','2014-06-25 17:15:32'),('r88npvhhvlmos1bjsoajlmzi9d6bn9mh','NjI2OTZlYTIwNGRhYTJhYjAxOTA0OWNlZWI0OTgyYTIzMjBlZmFmODp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MX0=','2014-05-10 08:18:17'),('scvo34qt7hoqw2j63ay9m63zki7oofm4','MzRlOWYyN2RkN2U1YTMyNDhjOWY4NjVjYWNmNjAzM2MzOGY2OGIzMjp7InZrLW9hdXRoMl9zdGF0ZSI6IlFYY25xNzRBc2pCaDZJTWl0Z3lHOVcweVpRaTI1RGZpIiwiX2F1dGhfdXNlcl9pZCI6Mywic29jaWFsX2F1dGhfbGFzdF9sb2dpbl9iYWNrZW5kIjoidmstb2F1dGgyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoic29jaWFsLmJhY2tlbmRzLnZrLlZLT0F1dGgyIiwibmV4dCI6Ii90b3duL1BLLyIsIl9zZXNzaW9uX2V4cGlyeSI6ODYzOTR9','2014-06-20 21:29:47'),('t4j9npnl5gcu6dijw6nbkk0indynotth','YWE4OTNiNWUyMGYwYmIzZWUzNmQxNDM0YWU3MTk2ZTIwNzZmNTRkNzp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6M30=','2014-03-26 09:44:09'),('tig27oqc664cjtivirub9pc2y6tej840','NjI2OTZlYTIwNGRhYTJhYjAxOTA0OWNlZWI0OTgyYTIzMjBlZmFmODp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MX0=','2014-03-26 08:12:08'),('tjviybh75e84dpvg0ig8y07sthdiq7t6','MGMyZTViY2MwYWYxZTEzZjlmNjczOGU0YzUyZDhhYWZmNzQ1ZWFhOTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6NH0=','2014-08-10 19:28:33'),('ubex0ek8hwq6ol76bz4sc29id46j8xrt','MDJkODk5Y2EyMmNkNTQ0NTZjMjk1NmEzMjViNzBjN2JiMjRhYTM1Yzp7fQ==','2014-06-21 22:36:16'),('w7wdsp75a3nav0omntyid47nksz0863e','MDY0YTY5YzBlMTFiMjk0NDdjZWMzNDU4MGU0MWU5NGJhZDQ5MjU5ZTp7InZrLW9hdXRoMl9zdGF0ZSI6ImlzaEV3N0ZzV2FWd2c3cDgwSGdneHhXVUFoc0JNSXdZIiwiX2F1dGhfdXNlcl9pZCI6MSwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQifQ==','2014-06-16 17:26:00');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `django_site`
--

LOCK TABLES `django_site` WRITE;
/*!40000 ALTER TABLE `django_site` DISABLE KEYS */;
INSERT INTO `django_site` VALUES (1,'example.com','example.com');
/*!40000 ALTER TABLE `django_site` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `easy_thumbnails_source`
--

LOCK TABLES `easy_thumbnails_source` WRITE;
/*!40000 ALTER TABLE `easy_thumbnails_source` DISABLE KEYS */;
/*!40000 ALTER TABLE `easy_thumbnails_source` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `easy_thumbnails_thumbnail`
--

LOCK TABLES `easy_thumbnails_thumbnail` WRITE;
/*!40000 ALTER TABLE `easy_thumbnails_thumbnail` DISABLE KEYS */;
/*!40000 ALTER TABLE `easy_thumbnails_thumbnail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `easy_thumbnails_thumbnaildimensions`
--

LOCK TABLES `easy_thumbnails_thumbnaildimensions` WRITE;
/*!40000 ALTER TABLE `easy_thumbnails_thumbnaildimensions` DISABLE KEYS */;
/*!40000 ALTER TABLE `easy_thumbnails_thumbnaildimensions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `gorod_article`
--

LOCK TABLES `gorod_article` WRITE;
/*!40000 ALTER TABLE `gorod_article` DISABLE KEYS */;
INSERT INTO `gorod_article` VALUES (52,'sdfgsf','2014-04-26 08:33:03',2,3,'<p>Сургут</p>\r\n',3,'',1,1),(54,'Кукурурза','2014-05-04 20:22:52',3,3,'<p>Сурогатака</p>\r\n',1,'pictures/belev1.jpg',1,1),(55,'вава','2014-06-21 14:20:38',2,3,'',1,'',1,0),(56,'xcv','2014-06-21 14:32:51',2,3,'',1,'',1,1),(57,'igor admin','2014-06-21 14:34:57',2,4,'<p>Ляляляляывв &nbsp;ывап вапр вы пфывар ыы фуап рыцук е23ке 34е у&nbsp;</p>\r\n\r\n<p>ап ывап выа апв</p>\r\n\r\n<p>&nbsp;ы пвп р</p>\r\n\r\n<p>ыврвкпр ва&nbsp;пр вапр цук 3х9 хцщк ыапвппппппппппппппппппппппппппппппппп ывап ывап паввыыыыыыыыыыыыыыы ывап вывап &nbsp; &nbsp;ывапааааааааааааааааааааааааааааааааа ывап ывапВыапывап</p>\r\n\r\n<p>выапывап выапаывппппппппппппппппппы вап ывр выфцвппвр фцапваые пупва</p>\r\n',1,'pictures/2014/07/IMG_7038.JPG',1,1),(58,'karbachinsy article','2014-06-21 14:36:26',2,3,'<p>OLOLOl</p>\r\n',2,'',1,0),(59,'34234234','2014-06-21 15:07:55',1,4,'<p>dgsdfgsdgsfdgdsgf</p>\r\n',3,'pictures/2014/06/download_copy.png',1,1),(60,'sdfasdfas','2014-06-21 17:47:04',3,4,'sdfvsdfvsdfgsdvsd',4,'',1,1),(61,'svxcv','2014-06-21 21:32:28',1,4,'sfvdfvsdfvdsfv',2,'',1,1),(62,'Белев','2014-06-21 21:33:09',1,4,'',1,'',1,1),(63,'123123123','2014-06-21 21:49:37',1,4,'1232r234',4,'',1,1),(64,'srfgsdfg','2014-06-21 21:56:49',1,4,'',1,'pictures/2014/06/belev1.jpg',1,1),(65,'dfgdfg','2014-06-21 22:14:04',1,4,'',1,'',1,1),(66,'sdvzxcv','2014-06-21 23:25:00',1,4,'',1,'pictures/2014/06/belev1_1.jpg',1,1),(68,'dgsdfg','2014-08-14 11:02:43',2,4,'',1,'',1,1);
/*!40000 ALTER TABLE `gorod_article` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `gorod_articlerubric`
--

LOCK TABLES `gorod_articlerubric` WRITE;
/*!40000 ALTER TABLE `gorod_articlerubric` DISABLE KEYS */;
INSERT INTO `gorod_articlerubric` VALUES (1,'event','Событие','События'),(2,'afisha','Афиша',NULL),(3,'photo','Фото',NULL),(4,'ad','Реклама',NULL);
/*!40000 ALTER TABLE `gorod_articlerubric` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `gorod_city`
--

LOCK TABLES `gorod_city` WRITE;
/*!40000 ALTER TABLE `gorod_city` DISABLE KEYS */;
INSERT INTO `gorod_city` VALUES (1,'kashin','Кашин','2014-03-03 13:49:09','',NULL),(2,'pk','Петропавловск-Камчатский','2014-03-06 07:53:12','','П-Камчатский'),(3,'belev','Белёв','2014-03-11 07:29:46','fgdfgdfg',NULL);
/*!40000 ALTER TABLE `gorod_city` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `gorod_cityinfo`
--

LOCK TABLES `gorod_cityinfo` WRITE;
/*!40000 ALTER TABLE `gorod_cityinfo` DISABLE KEYS */;
INSERT INTO `gorod_cityinfo` VALUES (1,1);
/*!40000 ALTER TABLE `gorod_cityinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `gorod_cityinfoquestion`
--

LOCK TABLES `gorod_cityinfoquestion` WRITE;
/*!40000 ALTER TABLE `gorod_cityinfoquestion` DISABLE KEYS */;
INSERT INTO `gorod_cityinfoquestion` VALUES (1,1,'Quest','<p>sdf</p>\r\n\r\n<p>sdf s</p>\r\n\r\n<p>g dh dgh fdh dfg&nbsp;</p>\r\n','2014-07-24 07:11:36'),(2,1,'quest 2','<p>sdfs</p>\r\n\r\n<p>dg sdfg</p>\r\n\r\n<p>&nbsp;dgh fhj g f</p>\r\n','2014-07-24 07:11:36');
/*!40000 ALTER TABLE `gorod_cityinfoquestion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `gorod_citywelcome`
--

LOCK TABLES `gorod_citywelcome` WRITE;
/*!40000 ALTER TABLE `gorod_citywelcome` DISABLE KEYS */;
INSERT INTO `gorod_citywelcome` VALUES (1,1,'<p>safs</p>\r\n\r\n<p>dfas</p>\r\n\r\n<p>fsa</p>\r\n\r\n<p>fafas</p>\r\n\r\n<p>df</p>\r\n','2014-07-18 13:05:57');
/*!40000 ALTER TABLE `gorod_citywelcome` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `gorod_complaint`
--

LOCK TABLES `gorod_complaint` WRITE;
/*!40000 ALTER TABLE `gorod_complaint` DISABLE KEYS */;
INSERT INTO `gorod_complaint` VALUES (1,'igorkarbachinsky2@mail.ru','igorkarbachinsky@mail.ru\r\nigorkarbachinsky@mail.ru\r\nПривет',2,'/aa/fvv',0,'2014-08-03 16:21:22'),(2,'igorkarbachinsky2@mail.ru','igorkarbachinsky@mail.ru\r\nigorkarbachinsky@mail.ru\r\nПривет',2,'/aa/fvv',0,'2014-08-03 16:23:14'),(3,'igorkarbachinsky2@mail.ru','igorkarbachinsky@mail.ru\r\nigorkarbachinsky@mail.ru\r\nПривет',2,'/aa/fvv',0,'2014-08-03 16:23:50'),(4,'igorkarbachinsky2@mail.ru','igorkarbachinsky@mail.ru\r\nigorkarbachinsky@mail.ru\r\nПривет',2,'/aa/fvv',0,'2014-08-03 16:24:16'),(5,'igogog@mail.ru','ОЛООЛ!!',2,'/a/b',0,'2014-08-03 16:25:28'),(6,'mad@masdas.ru','Привет!',2,'/',0,'2014-08-03 16:30:08'),(7,'mad@masdas.ru','Привет!',2,'/',0,'2014-08-03 16:30:22'),(8,'mad@masdas.ru','Привет!',2,'/',0,'2014-08-03 16:36:02'),(9,'mad@masdas.ru','Привет!',2,'/',0,'2014-08-03 16:44:14'),(10,'mad@masdas.ru','Привет!',2,'/',0,'2014-08-03 16:45:46'),(11,'mad@masdas.ru','Привет!',2,'/',0,'2014-08-03 16:46:40'),(12,'mad@masdas.ru','Привет!',2,'/',0,'2014-08-03 16:46:56'),(13,'mad@masdas.ru','Привет!',2,'/',0,'2014-08-03 16:47:11'),(14,'mad@masdas.ru','Привет!',2,'/',0,'2014-08-03 16:48:38'),(15,'mad@masdas.ru','Привет!',2,'/',0,'2014-08-03 16:49:19');
/*!40000 ALTER TABLE `gorod_complaint` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `gorod_hubanswer`
--

LOCK TABLES `gorod_hubanswer` WRITE;
/*!40000 ALTER TABLE `gorod_hubanswer` DISABLE KEYS */;
INSERT INTO `gorod_hubanswer` VALUES (1,1,5,'2014-08-10 14:47:31','<p>Ну так себе!</p>\r\n',1),(2,1,3,'2014-08-10 14:47:31','<p>ахуенно!</p>\r\n\r\n<p>А что?</p>\r\n',1);
/*!40000 ALTER TABLE `gorod_hubanswer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `gorod_hubquestion`
--

LOCK TABLES `gorod_hubquestion` WRITE;
/*!40000 ALTER TABLE `gorod_hubquestion` DISABLE KEYS */;
INSERT INTO `gorod_hubquestion` VALUES (1,1,'Как дела?',4,'2014-08-10 14:47:31',1);
/*!40000 ALTER TABLE `gorod_hubquestion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `gorod_organization`
--

LOCK TABLES `gorod_organization` WRITE;
/*!40000 ALTER TABLE `gorod_organization` DISABLE KEYS */;
INSERT INTO `gorod_organization` VALUES (1,'2014-04-22 15:37:03','Пхпхпх',3,'',3,'','',56,''),(2,'2014-04-26 08:20:31','dfbdf',2,'',3,'','',7,'');
/*!40000 ALTER TABLE `gorod_organization` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `gorod_organizationaddress`
--

LOCK TABLES `gorod_organizationaddress` WRITE;
/*!40000 ALTER TABLE `gorod_organizationaddress` DISABLE KEYS */;
INSERT INTO `gorod_organizationaddress` VALUES (3,'eeee',1),(4,'erfefgsdfg',1),(5,'dfgdf',1),(6,'г. Кашин, ул. Ленинаа, д.2',2),(7,'svfdsfg',1);
/*!40000 ALTER TABLE `gorod_organizationaddress` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `gorod_organizationcategory`
--

LOCK TABLES `gorod_organizationcategory` WRITE;
/*!40000 ALTER TABLE `gorod_organizationcategory` DISABLE KEYS */;
INSERT INTO `gorod_organizationcategory` VALUES (1,'Связь','Связь',NULL,1,12,1,0),(2,'Салоны связи','Салоны связи',1,2,3,1,1),(3,'Почта, отделения связи','Почта, отделения связи',1,4,5,1,1),(4,'Почтовые услуги','Почтовые услуги',1,6,7,1,1),(5,'Провайдеры','Провайдеры',1,8,9,1,1),(6,'Операторы сотовой связи','Операторы сотовой связи',1,10,11,1,1),(7,'Средства массовой информации','Средства массовой информации',NULL,1,10,2,0),(8,'Издательства, издательские услуги','Издательства, издательские услуги',7,2,3,2,1),(9,'Радио, радиокомпании','Радио, радиокомпании',7,4,5,2,1),(10,'Редакции газет и журналов','Редакции газет и журналов',7,6,7,2,1),(11,'Телекомпании, телестудии','Телекомпании, телестудии',7,8,9,2,1),(12,'Туризм','Туризм',NULL,1,24,3,0),(13,'Гостиницы','Гостиницы',12,2,3,3,1),(14,'Детские лагеря отдыха','Детские лагеря отдыха',12,4,5,3,1),(15,'Кемпинги','Кемпинги',12,6,7,3,1),(16,'Оформление виз и загранпаспортов','Оформление виз и загранпаспортов',12,8,9,3,1),(17,'Посольства и консульства','Посольства и консульства',12,10,11,3,1),(18,'Турбазы','Турбазы',12,12,13,3,1),(19,'Туроператоры','Туроператоры',12,14,15,3,1),(20,'Турфирмы','Турфирмы',12,16,17,3,1),(21,'Хостелы','Хостелы',12,18,19,3,1),(22,'Дома отдыха','Дома отдыха',12,20,21,3,1),(23,'Санатории, пансионаты','Санатории, пансионаты',12,22,23,3,1),(24,'Красота','Красота',NULL,1,26,4,0),(25,'Косметология, косметические кабинеты','Косметология, косметические кабинеты',24,2,3,4,1),(26,'Ногтевые студии','Ногтевые студии',24,4,5,4,1),(27,'Парикмахерские','Парикмахерские',24,6,7,4,1),(28,'Пластическая хирургия','Пластическая хирургия',24,8,9,4,1),(29,'Салоны красоты','Салоны красоты',24,10,11,4,1),(30,'Солярии','Солярии',24,12,13,4,1),(31,'Парфюмерные компании','Парфюмерные компании',24,14,15,4,1),(32,'СПА-салоны','СПА-салоны',24,16,17,4,1),(33,'Косметические компании','Косметические компании',24,18,19,4,1),(34,'Массажные салоны','Массажные салоны',24,20,21,4,1),(35,'Тату салоны','Тату салоны',24,22,23,4,1),(36,'Магазины парфюмерии и косметики','Магазины парфюмерии и косметики',24,24,25,4,1),(37,'Медицина','Медицина',NULL,1,50,5,0),(38,'Аптеки','Аптеки',37,2,3,5,1),(39,'Справочная аптек','Справочная аптек',37,4,5,5,1),(40,'Фармацевтические компании','Фармацевтические компании',37,6,7,5,1),(41,'Больницы','Больницы',37,8,9,5,1),(42,'Медвытрезвители','Медвытрезвители',37,10,11,5,1),(43,'Амбулатории, здравпункты, медпункты','Амбулатории, здравпункты, медпункты',37,12,13,5,1),(44,'Поликлиники','Поликлиники',37,14,15,5,1),(45,'Медицинские центры','Медицинские центры',37,16,17,5,1),(46,'Детские поликлиники','Детские поликлиники',37,18,19,5,1),(47,'Диспансеры','Диспансеры',37,20,21,5,1),(48,'Женские консультации','Женские консультации',37,22,23,5,1),(49,'Медсанчасти','Медсанчасти',37,24,25,5,1),(50,'Психоневрологические интернаты','Психоневрологические интернаты',37,26,27,5,1),(51,'Родильные дома','Родильные дома',37,28,29,5,1),(52,'Психологические службы','Психологические службы',37,30,31,5,1),(53,'Судебно-медицинская экспертиза','Судебно-медицинская экспертиза',37,32,33,5,1),(54,'Станции переливания крови','Станции переливания крови',37,34,35,5,1),(55,'Травмпункты','Травмпункты',37,36,37,5,1),(56,'Медицинские центры и клиники','Медицинские центры и клиники',37,38,39,5,1),(57,'Скорая помощь','Скорая помощь',37,40,41,5,1),(58,'Стоматология','Стоматология',37,42,43,5,1),(59,'Хосписы','Хосписы',37,44,45,5,1),(60,'Частно практикующие врачи','Частно практикующие врачи',37,46,47,5,1),(61,'Салоны оптики','Салоны оптики',37,48,49,5,1),(62,'Магазины','Магазины',NULL,1,86,6,0),(63,'Магазины CD и DVD дисков','Магазины CD и DVD дисков',62,2,3,6,1),(64,'Магазины электроники','Магазины электроники',62,4,5,6,1),(65,'Фотомагазины','Фотомагазины',62,6,7,6,1),(66,'Букинистические магазины','Букинистические магазины',62,8,9,6,1),(67,'Музыкальные магазины','Музыкальные магазины',62,10,11,6,1),(68,'Ювелирные магазины','Ювелирные магазины',62,12,13,6,1),(69,'Магазины канцтоваров','Магазины канцтоваров',62,14,15,6,1),(70,'Книжные магазины','Книжные магазины',62,16,17,6,1),(71,'Магазины бытовой техники','Магазины бытовой техники',62,18,19,6,1),(72,'Магазины мебели','Магазины мебели',62,20,21,6,1),(73,'Компьютерные магазины','Компьютерные магазины',62,22,23,6,1),(74,'Магазины алкогольных напитков','Магазины алкогольных напитков',62,24,25,6,1),(75,'Магазины цветов','Магазины цветов',62,26,27,6,1),(76,'Магазины для садоводов','Магазины для садоводов',62,28,29,6,1),(77,'Оптовые базы','Оптовые базы',62,30,31,6,1),(78,'Рынки','Рынки',62,32,33,6,1),(79,'Гипермаркеты','Гипермаркеты',62,34,35,6,1),(80,'Супермаркеты','Супермаркеты',62,36,37,6,1),(81,'Торговые центры','Торговые центры',62,38,39,6,1),(82,'Универмаги','Универмаги',62,40,41,6,1),(83,'Магазины хозтоваров','Магазины хозтоваров',62,42,43,6,1),(84,'Магазины ткани','Магазины ткани',62,44,45,6,1),(85,'Магазины табака и курительных принадлежностей','Магазины табака и курительных принадлежностей',62,46,47,6,1),(86,'Магазины одежды и обуви','Магазины одежды и обуви',62,48,49,6,1),(87,'Магазины галантереи','Магазины галантереи',62,50,51,6,1),(88,'Магазины головных уборов','Магазины головных уборов',62,52,53,6,1),(89,'Магазины кожи и меха','Магазины кожи и меха',62,54,55,6,1),(90,'Магазины часов','Магазины часов',62,56,57,6,1),(91,'Елочные базары','Елочные базары',62,58,59,6,1),(92,'Магаины для творчества и рукоделия','Магаины для творчества и рукоделия',62,60,61,6,1),(93,'Магазины подарков','Магазины подарков',62,62,63,6,1),(94,'Спортивные магазины','Спортивные магазины',62,64,65,6,1),(95,'Антикварные магазины','Антикварные магазины',62,66,67,6,1),(96,'Магазины посуды','Магазины посуды',62,68,69,6,1),(97,'Магазины электротоваров','Магазины электротоваров',62,70,71,6,1),(98,'Магазины продуктов питания','Магазины продуктов питания',62,72,73,6,1),(99,'Магазины обоев','Магазины обоев',62,74,75,6,1),(100,'Магазины нумизмат','Магазины нумизмат',62,76,77,6,1),(101,'Радиомагазины','Радиомагазины',62,78,79,6,1),(102,'Секс-шопы','Секс-шопы',62,80,81,6,1),(103,'Магазины медтехники','Магазины медтехники',62,82,83,6,1),(104,'Магазины сантехники','Магазины сантехники',62,84,85,6,1),(105,'Домашние животные','Домашние животные',NULL,1,24,7,0),(106,'Ветпомощь на дому','Ветпомощь на дому',105,2,3,7,1),(107,'Ветеринарные аптеки','Ветеринарные аптеки',105,4,5,7,1),(108,'Ветеринарные клиники','Ветеринарные клиники',105,6,7,7,1),(109,'Гостиницы для животных','Гостиницы для животных',105,8,9,7,1),(110,'Зоомагазины','Зоомагазины',105,10,11,7,1),(111,'Зоосалоны, зоопарикмахерские','Зоосалоны, зоопарикмахерские',105,12,13,7,1),(112,'Кинологические клубы','Кинологические клубы',105,14,15,7,1),(113,'Клубы любителей животных','Клубы любителей животных',105,16,17,7,1),(114,'Питомники животных','Питомники животных',105,18,19,7,1),(115,'Приюты для животных','Приюты для животных',105,20,21,7,1),(116,'Ритуальные услуги для животных','Ритуальные услуги для животных',105,22,23,7,1),(117,'Спорт и фитнес','Спорт и фитнес',NULL,1,34,8,0),(118,'Бассейны','Бассейны',117,2,3,8,1),(119,'Яхт-клубы','Яхт-клубы',117,4,5,8,1),(120,'Ипподромы','Ипподромы',117,6,7,8,1),(121,'Спортивные клубы и базы','Спортивные клубы и базы',117,8,9,8,1),(122,'Спортивные комплексы','Спортивные комплексы',117,10,11,8,1),(123,'Стадионы','Стадионы',117,12,13,8,1),(124,'Йога','Йога',117,14,15,8,1),(125,'Фитнес-клубы','Фитнес-клубы',117,16,17,8,1),(126,'Гольф-клубы','Гольф-клубы',117,18,19,8,1),(127,'Катки','Катки',117,20,21,8,1),(128,'Аэроклубы','Аэроклубы',117,22,23,8,1),(129,'Лазертаг','Лазертаг',117,24,25,8,1),(130,'Пейнтбол','Пейнтбол',117,26,27,8,1),(131,'Страйкбол','Страйкбол',117,28,29,8,1),(132,'Школы танцев','Школы танцев',117,30,31,8,1),(133,'Спортивные школы','Спортивные школы',117,32,33,8,1),(134,'Транспорт и перевозки','Транспорт и перевозки',NULL,1,30,9,0),(135,'Авиакомпании','Авиакомпании',134,2,3,9,1),(136,'Аэропорты','Аэропорты',134,4,5,9,1),(137,'Автобусные парки','Автобусные парки',134,6,7,9,1),(138,'Автовокзалы и автостанции','Автовокзалы и автостанции',134,8,9,9,1),(139,'Водные базы, лодочные станции','Водные базы, лодочные станции',134,10,11,9,1),(140,'Морские и речные вокзалы','Морские и речные вокзалы',134,12,13,9,1),(141,'Пароходства и порты','Пароходства и порты',134,14,15,9,1),(142,'Железнодорожные вокзалы и станции','Железнодорожные вокзалы и станции',134,16,17,9,1),(143,'Трамвайные депо','Трамвайные депо',134,18,19,9,1),(144,'Трамвайные станции','Трамвайные станции',134,20,21,9,1),(145,'Троллейбусные парки','Троллейбусные парки',134,22,23,9,1),(146,'Троллейбусные станции','Троллейбусные станции',134,24,25,9,1),(147,'Такси','Такси',134,26,27,9,1),(148,'Перевозка грузов','Перевозка грузов',134,28,29,9,1),(149,'Государство и общество','Государство и общество',NULL,1,80,10,0),(150,'Благотворительные фонды','Благотворительные фонды',149,2,3,10,1),(151,'ЗАГСы','ЗАГСы',149,4,5,10,1),(152,'Детские дома','Детские дома',149,6,7,10,1),(153,'Профсоюзы','Профсоюзы',149,8,9,10,1),(154,'Детские приюты','Детские приюты',149,10,11,10,1),(155,'Религия','Религия',149,12,13,10,1),(156,'Политические партии','Политические партии',149,14,15,10,1),(157,'Дома инвалидов и престарелых','Дома инвалидов и престарелых',149,16,17,10,1),(158,'Дома ребенка','Дома ребенка',149,18,19,10,1),(159,'Миграционные услуги','Миграционные услуги',149,20,21,10,1),(160,'Ночлежные дома','Ночлежные дома',149,22,23,10,1),(161,'Общежития','Общежития',149,24,25,10,1),(162,'Организации инвалидов','Организации инвалидов',149,26,27,10,1),(163,'Пенсионные фонды','Пенсионные фонды',149,28,29,10,1),(164,'Банки','Банки',149,30,31,10,1),(165,'Кадровые агентства','Кадровые агентства',149,32,33,10,1),(166,'Центры занятости','Центры занятости',149,34,35,10,1),(167,'Банкоматы','Банкоматы',149,36,37,10,1),(168,'Депозитарии и регистраторы','Депозитарии и регистраторы',149,38,39,10,1),(169,'Обмен валют','Обмен валют',149,40,41,10,1),(170,'Социальная помощь','Социальная помощь',149,42,43,10,1),(171,'Вневедомственная охрана','Вневедомственная охрана',149,44,45,10,1),(172,'Военкоматы и комиссариаты','Военкоматы и комиссариаты',149,46,47,10,1),(173,'Налоговые инспекции, службы','Налоговые инспекции, службы',149,48,49,10,1),(174,'Отделения полиции и милиции','Отделения полиции и милиции',149,50,51,10,1),(175,'Отделы по делам несовершеннолетних','Отделы по делам несовершеннолетних',149,52,53,10,1),(176,'Паспортные и миграционные службы','Паспортные и миграционные службы',149,54,55,10,1),(177,'Прокуратуры','Прокуратуры',149,56,57,10,1),(178,'Судебные приставы','Судебные приставы',149,58,59,10,1),(179,'Суды','Суды',149,60,61,10,1),(180,'Таможни','Таможни',149,62,63,10,1),(181,'Тюрьмы, колонии, СИЗО','Тюрьмы, колонии, СИЗО',149,64,65,10,1),(182,'Администрации городские','Администрации городские',149,66,67,10,1),(183,'Администрации областные','Администрации областные',149,68,69,10,1),(184,'Администрация Президента','Администрация Президента',149,70,71,10,1),(185,'Казначейства','Казначейства',149,72,73,10,1),(186,'Инспекции','Инспекции',149,74,75,10,1),(187,'Адвокаты','Адвокаты',149,76,77,10,1),(188,'Санэпиднадзор','Санэпиднадзор',149,78,79,10,1),(189,'Отдых и развлечения','Отдых и развлечения',NULL,1,88,11,0),(190,'Игровые клубы','Игровые клубы',189,2,3,11,1),(191,'Дельфинарии, океанариумы','Дельфинарии, океанариумы',189,4,5,11,1),(192,'Зоны отдыха','Зоны отдыха',189,6,7,11,1),(193,'Зоопарки','Зоопарки',189,8,9,11,1),(194,'Художественные салоны','Художественные салоны',189,10,11,11,1),(195,'Казино','Казино',189,12,13,11,1),(196,'Лесопарки и заповедники','Лесопарки и заповедники',189,14,15,11,1),(197,'Парки культуры и отдыха','Парки культуры и отдыха',189,16,17,11,1),(198,'Аквапарки','Аквапарки',189,18,19,11,1),(199,'Видеопрокат','Видеопрокат',189,20,21,11,1),(200,'Филармонии','Филармонии',189,22,23,11,1),(201,'Культурные центры','Культурные центры',189,24,25,11,1),(202,'Консерватории','Консерватории',189,26,27,11,1),(203,'Концертные залы','Концертные залы',189,28,29,11,1),(204,'Выставочные комплексы, галереи, залы','Выставочные комплексы, галереи, залы',189,30,31,11,1),(205,'Музеи','Музеи',189,32,33,11,1),(206,'Антикафе','Антикафе',189,34,35,11,1),(207,'Дворцы и дома культуры','Дворцы и дома культуры',189,36,37,11,1),(208,'Кинотеатры','Кинотеатры',189,38,39,11,1),(209,'Театры','Театры',189,40,41,11,1),(210,'Бани, сауны','Бани, сауны',189,42,43,11,1),(211,'Бильярдные клубы','Бильярдные клубы',189,44,45,11,1),(212,'Боулинг-клубы','Боулинг-клубы',189,46,47,11,1),(213,'Караоке-клубы','Караоке-клубы',189,48,49,11,1),(214,'Клубы досуга','Клубы досуга',189,50,51,11,1),(215,'Музыкальные клубы','Музыкальные клубы',189,52,53,11,1),(216,'Ночные клубы','Ночные клубы',189,54,55,11,1),(217,'Парки аттракционов','Парки аттракционов',189,56,57,11,1),(218,'Планетарии','Планетарии',189,58,59,11,1),(219,'Развлекательные центры','Развлекательные центры',189,60,61,11,1),(220,'Цирки','Цирки',189,62,63,11,1),(221,'Службы знакомств','Службы знакомств',189,64,65,11,1),(222,'Бары, пабы','Бары, пабы',189,66,67,11,1),(223,'Быстрое питание','Быстрое питание',189,68,69,11,1),(224,'Кальян-бары','Кальян-бары',189,70,71,11,1),(225,'Кафе','Кафе',189,72,73,11,1),(226,'Кофейни','Кофейни',189,74,75,11,1),(227,'Пиццерии','Пиццерии',189,76,77,11,1),(228,'Рестораны','Рестораны',189,78,79,11,1),(229,'Спорт-бары','Спорт-бары',189,80,81,11,1),(230,'Интернет-кафе','Интернет-кафе',189,82,83,11,1),(231,'Столовые','Столовые',189,84,85,11,1),(232,'Суши-бары','Суши-бары',189,86,87,11,1),(233,'Строительство и недвижимость','Строительство и недвижимость',NULL,1,24,12,0),(234,'Агентства недвижимости','Агентства недвижимости',233,2,3,12,1),(235,'Бизнес-центры','Бизнес-центры',233,4,5,12,1),(236,'БТИ','БТИ',233,6,7,12,1),(237,'Строительные кооперативы','Строительные кооперативы',233,8,9,12,1),(238,'ДСК','ДСК',233,10,11,12,1),(239,'ЖСК','ЖСК',233,12,13,12,1),(240,'Строительные компании','Строительные компании',233,14,15,12,1),(241,'Аренда квартир и офисов','Аренда квартир и офисов',233,16,17,12,1),(242,'Двери, дверные блоки','Двери, дверные блоки',233,18,19,12,1),(243,'Окна','Окна',233,20,21,12,1),(244,'Строительные магазины','Строительные магазины',233,22,23,12,1),(245,'Авто','Авто',NULL,1,34,13,0),(246,'Автоателье','Автоателье',245,2,3,13,1),(247,'Автомойки','Автомойки',245,4,5,13,1),(248,'Автосервисы','Автосервисы',245,6,7,13,1),(249,'Автотехпомощь','Автотехпомощь',245,8,9,13,1),(250,'Пункты техосмотра','Пункты техосмотра',245,10,11,13,1),(251,'Шиномонтаж','Шиномонтаж',245,12,13,13,1),(252,'Автошколы','Автошколы',245,14,15,13,1),(253,'АЗС','АЗС',245,16,17,13,1),(254,'Автостоянки, паркинг','Автостоянки, паркинг',245,18,19,13,1),(255,'ГАИ, ГИБДД','ГАИ, ГИБДД',245,20,21,13,1),(256,'МРЭО','МРЭО',245,22,23,13,1),(257,'Автозапчасти','Автозапчасти',245,24,25,13,1),(258,'Автоломбарды','Автоломбарды',245,26,27,13,1),(259,'Автомагазины','Автомагазины',245,28,29,13,1),(260,'Авторынки','Авторынки',245,30,31,13,1),(261,'Автосалоны','Автосалоны',245,32,33,13,1),(262,'Услуги','Услуги',NULL,1,82,14,0),(263,'Бытовые услуги','Бытовые услуги',262,2,3,14,1),(264,'Вывоз и переработка мусора','Вывоз и переработка мусора',262,4,5,14,1),(265,'Дезинфекция, дезинсекция, дератизация','Дезинфекция, дезинсекция, дератизация',262,6,7,14,1),(266,'Металлоремонт','Металлоремонт',262,8,9,14,1),(267,'Прачечные','Прачечные',262,10,11,14,1),(268,'Пункты проката','Пункты проката',262,12,13,14,1),(269,'Санэпидемстанции','Санэпидемстанции',262,14,15,14,1),(270,'Трубочисты','Трубочисты',262,16,17,14,1),(271,'Химчистки','Химчистки',262,18,19,14,1),(272,'Видеоуслуги','Видеоуслуги',262,20,21,14,1),(273,'Фотоуслуги','Фотоуслуги',262,22,23,14,1),(274,'Доставка еды и напитков','Доставка еды и напитков',262,24,25,14,1),(275,'Заказ и доставка билетов','Заказ и доставка билетов',262,26,27,14,1),(276,'Аварийные службы','Аварийные службы',262,28,29,14,1),(277,'Компьютерный ремонт и услуги','Компьютерный ремонт и услуги',262,30,31,14,1),(278,'Коммунальные службы','Коммунальные службы',262,32,33,14,1),(279,'Котельные','Котельные',262,34,35,14,1),(280,'Нотариальные услуги','Нотариальные услуги',262,36,37,14,1),(281,'Бюро переводов','Бюро переводов',262,38,39,14,1),(282,'Курьерские услуги','Курьерские услуги',262,40,41,14,1),(283,'ТСЖ','ТСЖ',262,42,43,14,1),(284,'Энергосбыт','Энергосбыт',262,44,45,14,1),(285,'Доставка цветов и букетов','Доставка цветов и букетов',262,46,47,14,1),(286,'Организация торжеств и праздников','Организация торжеств и праздников',262,48,49,14,1),(287,'Свадебные агентства','Свадебные агентства',262,50,51,14,1),(288,'Свадебные салоны','Свадебные салоны',262,52,53,14,1),(289,'Общественные туалеты','Общественные туалеты',262,54,55,14,1),(290,'Кладбища','Кладбища',262,56,57,14,1),(291,'Ремонт сотовых телефонов','Ремонт сотовых телефонов',262,58,59,14,1),(292,'Крематории','Крематории',262,60,61,14,1),(293,'Морги','Морги',262,62,63,14,1),(294,'Ремонт оргтехники','Ремонт оргтехники',262,64,65,14,1),(295,'Полиграфия','Полиграфия',262,66,67,14,1),(296,'Страхование','Страхование',262,68,69,14,1),(297,'Ломбарды','Ломбарды',262,70,71,14,1),(298,'Детективные агентства','Детективные агентства',262,72,73,14,1),(299,'Реклама','Реклама',262,74,75,14,1),(300,'Ритуальные услуги','Ритуальные услуги',262,76,77,14,1),(301,'Ателье по пошиву одежды','Ателье по пошиву одежды',262,78,79,14,1),(302,'Прочее','Прочее',262,80,81,14,1),(303,'Производство','Производство',NULL,1,52,15,0),(304,'Агрофирмы, колхозы, совхозы','Агрофирмы, колхозы, совхозы',303,2,3,15,1),(305,'Животноводческие хозяйства','Животноводческие хозяйства',303,4,5,15,1),(306,'Зверофермы','Зверофермы',303,6,7,15,1),(307,'Птицефабрики','Птицефабрики',303,8,9,15,1),(308,'Овощные базы','Овощные базы',303,10,11,15,1),(309,'Металлообработка','Металлообработка',303,12,13,15,1),(310,'Газовые компании','Газовые компании',303,14,15,15,1),(311,'Нефтяные компании','Нефтяные компании',303,16,17,15,1),(312,'Приемные пункты макулатуры и вторсырья','Приемные пункты макулатуры и вторсырья',303,18,19,15,1),(313,'Приемные пункты стеклотары','Приемные пункты стеклотары',303,20,21,15,1),(314,'Пивоваренные заводы','Пивоваренные заводы',303,22,23,15,1),(315,'Производство продуктов питания','Производство продуктов питания',303,24,25,15,1),(316,'Хлебозаводы','Хлебозаводы',303,26,27,15,1),(317,'Электростанции','Электростанции',303,28,29,15,1),(318,'Энергетические организации','Энергетические организации',303,30,31,15,1),(319,'Сырьевые базы','Сырьевые базы',303,32,33,15,1),(320,'Топливные компании','Топливные компании',303,34,35,15,1),(321,'Приборостроение','Приборостроение',303,36,37,15,1),(322,'Газоперерабатывающие заводы','Газоперерабатывающие заводы',303,38,39,15,1),(323,'Хладокомбинаты','Хладокомбинаты',303,40,41,15,1),(324,'Производство и продажа одежды','Производство и продажа одежды',303,42,43,15,1),(325,'Лесничества, лесхозы','Лесничества, лесхозы',303,44,45,15,1),(326,'Автомобильные заводы','Автомобильные заводы',303,46,47,15,1),(327,'Вагоностроительные и  вагоноремонтные заводы','Вагоностроительные и  вагоноремонтные заводы',303,48,49,15,1),(328,'Мебельные фабрики','Мебельные фабрики',303,50,51,15,1),(329,'Образование','Образование',NULL,1,38,16,0),(330,'Академии','Академии',329,2,3,16,1),(331,'Вузы','Вузы',329,4,5,16,1),(332,'Дополнительное образование','Дополнительное образование',329,6,7,16,1),(333,'Учебные центры','Учебные центры',329,8,9,16,1),(334,'Фотошколы','Фотошколы',329,10,11,16,1),(335,'Воскресные школы','Воскресные школы',329,12,13,16,1),(336,'Гимназии','Гимназии',329,14,15,16,1),(337,'Колледжи','Колледжи',329,16,17,16,1),(338,'Лицеи','Лицеи',329,18,19,16,1),(339,'Общеобразовательные школы','Общеобразовательные школы',329,20,21,16,1),(340,'Техникумы, политехникумы','Техникумы, политехникумы',329,22,23,16,1),(341,'Школы-интернаты','Школы-интернаты',329,24,25,16,1),(342,'Репетиторы','Репетиторы',329,26,27,16,1),(343,'Художественные школы','Художественные школы',329,28,29,16,1),(344,'Музыкальные школы и училища','Музыкальные школы и училища',329,30,31,16,1),(345,'Детские сады','Детские сады',329,32,33,16,1),(346,'Архивы','Архивы',329,34,35,16,1),(347,'Библиотеки','Библиотеки',329,36,37,16,1);
/*!40000 ALTER TABLE `gorod_organizationcategory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `gorod_organizationphone`
--

LOCK TABLES `gorod_organizationphone` WRITE;
/*!40000 ALTER TABLE `gorod_organizationphone` DISABLE KEYS */;
INSERT INTO `gorod_organizationphone` VALUES (3,'23213 123 123 123 123 12 23',1),(4,'123123123123123',2);
/*!40000 ALTER TABLE `gorod_organizationphone` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `gorod_organizationschedule`
--

LOCK TABLES `gorod_organizationschedule` WRITE;
/*!40000 ALTER TABLE `gorod_organizationschedule` DISABLE KEYS */;
INSERT INTO `gorod_organizationschedule` VALUES (9,'15:00','16:00','tuesday',1),(11,'9:00','10:00','wednesday',1);
/*!40000 ALTER TABLE `gorod_organizationschedule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `gorod_user`
--

LOCK TABLES `gorod_user` WRITE;
/*!40000 ALTER TABLE `gorod_user` DISABLE KEYS */;
INSERT INTO `gorod_user` VALUES (3,'!vNxqfLWaMNtj2A6fWI6nEDaeUJTMo8iTZ17D36XC','2014-08-11 09:21:18',0,'karbachinsky','Игорь','Карбачинский','igorkarbachinsky@mail.ru',0,1,'2014-06-11 13:54:00',2,'http://cs9322.vk.me/u2959747/e_6f9ea567.jpg'),(4,'pbkdf2_sha256$12000$YFEdb6tnfBEG$sJWIpAgTxe1EupnM9MzjMOMtNy2uLb2hMEmOIrN+Q54=','2014-08-12 17:44:16',1,'igor','','','',1,1,'2014-06-11 14:07:09',1,''),(5,'pbkdf2_sha256$12000$LH2H3aGFt85D$Ip+cXyFqV/I8v/em7LAWg87XO1nO6Q/WBah2ejkK2Hg=','2014-06-22 12:43:57',1,'kalech','','','',1,1,'2014-06-22 12:43:57',NULL,NULL);
/*!40000 ALTER TABLE `gorod_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `gorod_user_groups`
--

LOCK TABLES `gorod_user_groups` WRITE;
/*!40000 ALTER TABLE `gorod_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `gorod_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `gorod_user_user_permissions`
--

LOCK TABLES `gorod_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `gorod_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `gorod_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `gorod_userstat`
--

LOCK TABLES `gorod_userstat` WRITE;
/*!40000 ALTER TABLE `gorod_userstat` DISABLE KEYS */;
/*!40000 ALTER TABLE `gorod_userstat` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `social_auth_association`
--

LOCK TABLES `social_auth_association` WRITE;
/*!40000 ALTER TABLE `social_auth_association` DISABLE KEYS */;
/*!40000 ALTER TABLE `social_auth_association` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `social_auth_code`
--

LOCK TABLES `social_auth_code` WRITE;
/*!40000 ALTER TABLE `social_auth_code` DISABLE KEYS */;
/*!40000 ALTER TABLE `social_auth_code` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `social_auth_nonce`
--

LOCK TABLES `social_auth_nonce` WRITE;
/*!40000 ALTER TABLE `social_auth_nonce` DISABLE KEYS */;
/*!40000 ALTER TABLE `social_auth_nonce` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `social_auth_usersocialauth`
--

LOCK TABLES `social_auth_usersocialauth` WRITE;
/*!40000 ALTER TABLE `social_auth_usersocialauth` DISABLE KEYS */;
INSERT INTO `social_auth_usersocialauth` VALUES (2,3,'vk-oauth2','2959747','{\"access_token\": \"18f98807308ada460f8e05eb9684b7d67ad0b057637270d428fd143c3aceaaa23b84d62f55c30da20a595\", \"expires\": 86395, \"id\": null}');
/*!40000 ALTER TABLE `social_auth_usersocialauth` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `south_migrationhistory`
--

LOCK TABLES `south_migrationhistory` WRITE;
/*!40000 ALTER TABLE `south_migrationhistory` DISABLE KEYS */;
INSERT INTO `south_migrationhistory` VALUES (1,'gorod','0001_initial','2014-03-12 09:43:16'),(71,'gorod','0051_auto__add_userstat','2014-08-14 11:32:50');
/*!40000 ALTER TABLE `south_migrationhistory` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2014-08-14 15:40:36
