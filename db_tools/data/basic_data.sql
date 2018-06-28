-- MySQL dump 10.13  Distrib 5.6.40, for Linux (x86_64)
--
-- Host: localhost    Database: gistandard
-- ------------------------------------------------------
-- Server version	5.6.40

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
-- Table structure for table `rbac_menu`
--

DROP TABLE IF EXISTS `rbac_menu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rbac_menu` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(32) NOT NULL,
  `is_top` tinyint(1) NOT NULL,
  `icon` varchar(50) DEFAULT NULL,
  `code` varchar(50) DEFAULT NULL,
  `url` varchar(128) DEFAULT NULL,
  `parent_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `title` (`title`),
  UNIQUE KEY `url` (`url`),
  KEY `rbac_menu_parent_id_60a5b178_fk_rbac_menu_id` (`parent_id`),
  CONSTRAINT `rbac_menu_parent_id_60a5b178_fk_rbac_menu_id` FOREIGN KEY (`parent_id`) REFERENCES `rbac_menu` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=90 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rbac_menu`
--

LOCK TABLES `rbac_menu` WRITE;
/*!40000 ALTER TABLE `rbac_menu` DISABLE KEYS */;
INSERT INTO `rbac_menu` VALUES (1,'系统',1,NULL,'SYSTEM','/system/',NULL),(2,'行政',1,NULL,'ADM','/adm/',NULL),(3,'人事',0,NULL,'PERSONNEL','/personnel/',NULL),(4,'流程',1,NULL,'FLOW','/flow/',NULL),(5,'我的工作台',0,NULL,'PERSONAL','/personal/',NULL),(6,'基础设置',0,'fa fa-gg','SYSTEM-BASIC',NULL,1),(7,'权限管理',0,'fa fa-user-plus','SYSTEM-RBAC',NULL,1),(8,'系统工具',0,'fa fa-wrench','SYSTEM-TOOLS',NULL,1),(9,'组织架构',0,NULL,'SYSTEM-BASIC-STRUCTURE','/system/basic/structure/',6),(10,'用户管理',0,NULL,'SYSTEM-BASIC-USER','/system/basic/user/',6),(11,'菜单管理',0,NULL,'SYSTEM-RBAC-MENU','/system/rbac/menu/',7),(12,'角色管理',0,NULL,'SYSTEM-RBAC-ROLE','/system/rbac/role/',7),(15,'组织架构：列表',0,NULL,'SYSTEM-BASIC-STRUCTURE-LIST','/system/basic/structure/list',9),(16,'组织架构：详情',0,NULL,'SYSTEM-BASIC-STRUCTURE-DETAIL','/system/basic/structure/detail',9),(17,'组织架构：删除',0,NULL,'SYSTEM-BASIC-STRUCTURE-DELETE','/system/basic/structure/delete',9),(18,'组织架构：关联用户',0,NULL,'SYSTEM-BASIC-STRUCTURE-ADD_USER','/system/basic/structure/add_user',9),(19,'用户管理：列表',0,NULL,'SYSTEM-BASIC-USER-LIST','/system/basic/user/list',10),(20,'用户管理：详情',0,NULL,'SYSTEM-BASIC-USER','/system/basic/user/detail',10),(21,'用户管理：修改',0,NULL,'SYSTEM-BASIC-USER-UPDATE','/system/basic/user/update',10),(22,'用户管理：创建',0,NULL,'SYSTEM-BASIC-USER-CREATE','/system/basic/user/create',10),(23,'用户管理：删除',0,NULL,'SYSTEM-BASIC-USER-DELETE','/system/basic/user/delete',10),(24,'用户管理：启用',0,NULL,'SYSTEM-BASIC-USER-ENABLE','/system/basic/user/enable',10),(25,'用户管理：禁用',0,NULL,'SYSTEM-BASIC-USER-DISABLE','/system/basic/user/disable',10),(26,'用户管理：修改用户密码',0,NULL,'SYSTEM-BASIC-USER-AdminPasswdChange','/system/basic/user/adminpasswdchange',10),(27,'角色管理：列表',0,NULL,'SYSTEM-RBAC-ROLE-LIST','/system/rbac/role/list',12),(28,'角色管理：详情-编辑',0,NULL,'SYSTEM-RBAC-ROLE-DETAIL','/system/rbac/role/detail',12),(29,'角色管理：删除',0,NULL,'SYSTEM-RBAC-ROLE-DELETE','/system/rbac/role/delete',12),(30,'角色管理：关联菜单',0,NULL,'SYSTEM-RBAC-ROLE-ROLE_MENU','/system/rbac/role/role_menu',12),(31,'角色管理：菜单列表',0,NULL,'SYSTEM-RBAC-ROLE-ROLE_MENU_LIST','/system/rbac/role/role_menu_list',12),(32,'角色管理：关联用户',0,NULL,'SYSTEM-RBAC-ROLE-ROLE_LIST','/system/rbac/role/role_user',12),(33,'菜单管理：列表',0,NULL,'SYSTEM-RBAC-MENU-LIST','/system/rbac/menu/list',11),(34,'系统设置',0,NULL,'SYSTEM-TOOLS-SYSTEM_SETUP','/system/tools/system_setup/',8),(35,'发件邮箱设置',0,NULL,'SYSTEM-TOOLS-EMAIL_SETUP','/system/tools/email_setup/',8),(36,'基础管理',0,'fa fa-gg','ADM-BSM',NULL,2),(37,'分销商管理',0,NULL,'ADM-BSM-SUPPLIER','/adm/bsm/supplier/',36),(38,'供应商管理：列表',0,NULL,'ADM-BSM-SUPPLIER-LIST','/adm/bsm/supplier/list',37),(39,'基础管理：详情-修改',0,NULL,'ADM-BSM-SUPPLIER-DETAIL','/adm/bsm/supplier/detail',37),(40,'供应商管理：删除',0,NULL,'ADM-BSM-SUPPLIER-DELETE','/adm/bsm/supplier/delete',37),(41,'资产类型',0,NULL,'ADM-BSM-ASSETTYPE','/adm/bsm/assettype/',36),(42,'资产类型：列表',0,NULL,'ADM-BSM-ASSETTYPE-LIST','/adm/bsm/assettype/list',41),(43,'资产类型：编辑-详情',0,NULL,'ADM-BSM-ASSETYPE-DETAIL','/adm/bsm/assettype/detail',41),(44,'资产类型：删除',0,NULL,'ADM-BSM-ASSETTYPE-DELETE','/adm/bsm/assettype/delete',41),(45,'客户信息',0,NULL,'ADM-BSM-CUSTOMER','/adm/bsm/customer/',36),(46,'客户信息：列表',0,NULL,'ADM-BSM-CUSTOMER-LIST','/adm/bsm/customer/list',45),(47,'客户信息：编辑-详情',0,NULL,'ADM-BSM-CUSTOMER-DETAIL','/adm/bsm/customer/detail',45),(48,'客户信息：删除',0,NULL,'ADM-BSM-CUSTOMER-DELETE','/adm/bsm/customer/delete',45),(49,'设备类型',0,NULL,'ADM-BSM-EQUIPMENTTYPE','/adm/bsm/equipmenttype/',36),(50,'资产管理',1,'fa fa-desktop','ADM-ASSET','/adm/asset/',2),(51,'设备管理',0,'fa fa-keyboard-o','ADM-EQUIPMENT','/adm/equipment/',2),(52,'用户管理：修改个人密码',0,NULL,'SYSTEM-BASIC-USER-PASSWDCHANGE','/system/basic/user/passwdchange',10),(53,'设备类型：列表',0,NULL,'ADM-BSM-EQUIPMENTTYPE-LIST','/adm/bsm/equipmenttype/list',49),(54,'设备类型：编辑-详情',0,NULL,'ADM-BSM-EQUIPMENTTYPE-DETAIL','/adm/bsm/equipmenttype/detail',49),(55,'设备类型：删除',0,NULL,'ADM-BSM-EQUIPMENTTYPE-DELETE','/adm/bsm/equipmenttype/delete',49),(56,'设备管理：列表',0,NULL,'ADM-EQUIPMENT-LIST','/adm/equipment/list',51),(57,'设备管理：新建-修改',0,NULL,'ADM-EQUIPMENT-CREATE','/adm/equipment/create',51),(58,'设备管理：删除',0,NULL,'ADM-EQUIPMENT-DELETE','/adm/equipment/delete',51),(59,'设备管理：详情',0,NULL,'ADM-EQUIPMENT-DETAIL','/adm/equipment/detail',51),(60,'设备管理：维保更新',0,NULL,'ADM-EQUIPMENT-SERVICEINFO','/adm/equipment/serviceinfoupdate',51),(61,'个人中心',0,'fa fa-user-plus','PERSONAL-USERINFO','/personal/userinfo',5),(62,'上传头像',0,NULL,'PERSONAL-USERINFO-UPLOADIMAGE','/personal/uploadimage',61),(63,'修改密码',0,NULL,'PERSONAL-USERINFO-PASSWORDCHANGE','/personal/passwordchange',61),(64,'内部通信',0,'fa fa-book','PERSONAL-PHONEBOOK','/personal/phonebook',5),(65,'菜单管理：详情-修改',0,NULL,'SYSTEM-RBAC-MENU-DETAIL','/system/rbac/menu/detail',11),(66,'工单管理',1,'fa fa-list-alt','PERSONAL-WORKORDER',NULL,5),(67,'我创建的工单',1,'fa fa-caret-right','PERSONAL-WORKORDER_ICRT','/personal/workorder_Icrt/',66),(68,'我创建的工单：创建',1,NULL,'PERSONAL-WORKORDER_ICRT-CREATE','/personal/workorder_Icrt/create',67),(69,'我创建的工单：列表',1,NULL,'PERSONAL-WORKORDER_ICRT-LIST','/personal/workorder_Icrt/list',67),(70,'我创建的工单：详情',1,NULL,'PERSONAL-WORKORDER-DETAIL','/personal/workorder_Icrt/detail',67),(71,'我创建的工单：删除',1,NULL,'PERSONAL-WORKORDER_ICRT-DELETE','/personal/workorder_Icrt/delete',67),(72,'我创建的工单：修改',1,NULL,'PERSONAL-WORKORDER-UPDATE','/personal/workorder_Icrt/update',67),(73,'我审批的工单',1,'fa fa-caret-right','PERSONAL-WORKORDER_APP','/personal/workorder_app/',66),(74,'我收到的工单',1,'fa fa-caret-right','PERSONAL-WORKORDER_REC','/personal/workorder_rec/',66),(75,'我审批的工单：派发',1,NULL,'PERSONAL-WORKORDER_APP-SEND','/personal/workorder_app/send',73),(76,'我收到的工单：执行',1,NULL,'PERSONAL-WORKORDER-EXECUTE','/personal/workorder_rec/execute',74),(77,'我收到的工单：确认',1,NULL,'PERSONAL-WORKORDER_REC-FINISH','/personal/workorder_rec/finish',74),(78,'资产管理：列表',1,NULL,'ADM-ASSET-LIST','/adm/asset/list',50),(79,'资产管理：创建',1,NULL,'ADM-ASSET-CREATE','/adm/asset/create',50),(80,'资产管理：修改',1,NULL,'ADM-ASSET-UPDATE','/adm/asset/update',50),(81,'资产管理：详情',1,NULL,'ADM-ASSET-DETAIL','/adm/asset/detail',50),(82,'资产管理：删除',1,NULL,'ADM-ASSET-DELETE','/adm/asset/delete',50),(83,'我创建的工单：上传项目资料',1,NULL,'PERSONAL-WORKORDER-PROJECT_UPLOAD','/personal/workorder_Icrt/upload',67),(84,'我收到的工单：上传配置资料',1,NULL,'PERSONAL-WORKORDER-UPLOAD','/personal/workorder_rec/upload',74),(85,'工单统计',1,NULL,'PERSONAL-WORKORDER-ALL','/personal/workorder_all/',66),(86,'资产管理：上传',1,NULL,'ADM-ASSET-UPLOAD','/adm/asset/upload',50),(87,'我收到的工单：退回',1,NULL,'PERSONAL-WORKORDER-RETURN','/personal/workorder_rec/return',74),(88,'工单文档',1,'fa  fa-folder','PERSONAL-DOCUMENT','/personal/document/',5),(89,'工单文档：列表',1,NULL,'PERSONAL-DOCUMENT-LIST','/personal/document/list',88);
/*!40000 ALTER TABLE `rbac_menu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rbac_role`
--

DROP TABLE IF EXISTS `rbac_role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rbac_role` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(32) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rbac_role`
--

LOCK TABLES `rbac_role` WRITE;
/*!40000 ALTER TABLE `rbac_role` DISABLE KEYS */;
INSERT INTO `rbac_role` VALUES (1,'系统'),(6,'行政'),(7,'人力'),(8,'技术'),(9,'销售'),(10,'管理'),(11,'核算'),(12,'审批');
/*!40000 ALTER TABLE `rbac_role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rbac_role_permissions`
--

DROP TABLE IF EXISTS `rbac_role_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rbac_role_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `role_id` int(11) NOT NULL,
  `menu_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `rbac_role_permissions_role_id_menu_id_8ba9f835_uniq` (`role_id`,`menu_id`),
  KEY `rbac_role_permissions_menu_id_bb73fb9a_fk_rbac_menu_id` (`menu_id`),
  CONSTRAINT `rbac_role_permissions_menu_id_bb73fb9a_fk_rbac_menu_id` FOREIGN KEY (`menu_id`) REFERENCES `rbac_menu` (`id`),
  CONSTRAINT `rbac_role_permissions_role_id_d10416cb_fk_rbac_role_id` FOREIGN KEY (`role_id`) REFERENCES `rbac_role` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2874 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rbac_role_permissions`
--

LOCK TABLES `rbac_role_permissions` WRITE;
/*!40000 ALTER TABLE `rbac_role_permissions` DISABLE KEYS */;
INSERT INTO `rbac_role_permissions` VALUES (1,1,1),(2,1,2),(3,1,3),(4,1,4),(5,1,5),(6,1,6),(7,1,7),(8,1,8),(9,1,9),(10,1,10),(11,1,11),(12,1,12),(59,1,15),(54,1,16),(55,1,17),(56,1,18),(57,1,19),(58,1,20),(60,1,21),(61,1,22),(62,1,23),(63,1,24),(64,1,25),(65,1,26),(68,1,27),(69,1,28),(70,1,29),(71,1,30),(72,1,31),(66,1,32),(67,1,33),(78,1,34),(79,1,35),(80,1,36),(81,1,37),(82,1,38),(83,1,39),(84,1,40),(85,1,41),(86,1,42),(87,1,43),(88,1,44),(276,1,45),(277,1,46),(278,1,47),(279,1,48),(371,1,52),(2305,6,2),(2325,6,5),(2306,6,36),(2307,6,37),(2308,6,38),(2309,6,41),(2310,6,42),(2311,6,43),(2312,6,45),(2313,6,46),(2314,6,49),(2316,6,50),(2322,6,51),(2315,6,53),(2323,6,56),(2324,6,59),(2326,6,61),(2327,6,62),(2328,6,63),(2329,6,64),(2330,6,66),(2331,6,67),(2332,6,68),(2333,6,69),(2334,6,70),(2335,6,71),(2336,6,72),(2338,6,74),(2339,6,76),(2340,6,77),(2317,6,78),(2318,6,79),(2319,6,80),(2320,6,81),(2337,6,83),(2341,6,84),(2321,6,86),(1505,7,2),(1525,7,5),(1506,7,36),(1507,7,37),(1508,7,38),(1509,7,39),(1510,7,41),(1511,7,42),(1512,7,43),(1513,7,45),(1514,7,46),(1515,7,47),(1516,7,49),(1519,7,50),(1520,7,51),(1517,7,53),(1518,7,54),(1521,7,56),(1522,7,57),(1523,7,59),(1524,7,60),(1526,7,61),(1527,7,62),(1528,7,63),(1529,7,64),(1530,7,66),(1531,7,67),(1532,7,68),(1533,7,69),(1534,7,70),(1535,7,71),(1536,7,72),(1537,7,74),(1538,7,76),(1539,7,77),(2790,8,2),(2812,8,5),(2791,8,36),(2792,8,37),(2793,8,38),(2794,8,39),(2795,8,41),(2796,8,42),(2797,8,43),(2798,8,45),(2799,8,46),(2800,8,47),(2801,8,49),(2804,8,50),(2807,8,51),(2802,8,53),(2803,8,54),(2808,8,56),(2809,8,57),(2810,8,59),(2811,8,60),(2813,8,61),(2814,8,62),(2815,8,63),(2816,8,64),(2817,8,66),(2818,8,67),(2819,8,68),(2820,8,69),(2821,8,70),(2822,8,71),(2823,8,72),(2825,8,74),(2826,8,76),(2827,8,77),(2805,8,78),(2806,8,81),(2824,8,83),(2828,8,84),(2829,8,87),(2830,8,88),(2831,8,89),(2832,9,2),(2854,9,5),(2833,9,36),(2834,9,37),(2835,9,38),(2836,9,39),(2837,9,41),(2838,9,42),(2839,9,43),(2840,9,45),(2841,9,46),(2842,9,47),(2843,9,49),(2846,9,50),(2849,9,51),(2844,9,53),(2845,9,54),(2850,9,56),(2851,9,57),(2852,9,59),(2853,9,60),(2855,9,61),(2856,9,62),(2857,9,63),(2858,9,64),(2859,9,66),(2860,9,67),(2861,9,68),(2862,9,69),(2863,9,70),(2864,9,71),(2865,9,72),(2867,9,74),(2868,9,76),(2869,9,77),(2847,9,78),(2848,9,81),(2866,9,83),(2870,9,84),(2871,9,87),(2872,9,88),(2873,9,89),(2705,10,1),(2736,10,2),(2767,10,5),(2706,10,6),(2722,10,7),(2733,10,8),(2707,10,9),(2712,10,10),(2723,10,11),(2726,10,12),(2708,10,15),(2709,10,16),(2710,10,17),(2711,10,18),(2713,10,19),(2714,10,20),(2715,10,21),(2716,10,22),(2717,10,23),(2718,10,24),(2719,10,25),(2720,10,26),(2727,10,27),(2728,10,28),(2729,10,29),(2730,10,30),(2731,10,31),(2732,10,32),(2724,10,33),(2734,10,34),(2735,10,35),(2737,10,36),(2738,10,37),(2739,10,38),(2740,10,39),(2741,10,40),(2742,10,41),(2743,10,42),(2744,10,43),(2745,10,44),(2746,10,45),(2747,10,46),(2748,10,47),(2749,10,48),(2750,10,49),(2754,10,50),(2761,10,51),(2721,10,52),(2751,10,53),(2752,10,54),(2753,10,55),(2762,10,56),(2763,10,57),(2764,10,58),(2765,10,59),(2766,10,60),(2768,10,61),(2769,10,62),(2770,10,63),(2771,10,64),(2725,10,65),(2772,10,66),(2773,10,67),(2774,10,68),(2775,10,69),(2776,10,70),(2777,10,71),(2778,10,72),(2780,10,73),(2782,10,74),(2781,10,75),(2783,10,76),(2784,10,77),(2755,10,78),(2756,10,79),(2757,10,80),(2758,10,81),(2759,10,82),(2779,10,83),(2785,10,84),(2787,10,85),(2760,10,86),(2786,10,87),(2788,10,88),(2789,10,89),(1945,12,5),(1946,12,66),(1947,12,73),(1948,12,75);
/*!40000 ALTER TABLE `rbac_role_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `system_systemsetup`
--

DROP TABLE IF EXISTS `system_systemsetup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `system_systemsetup` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `loginTitle` varchar(20) DEFAULT NULL,
  `mainTitle` varchar(20) DEFAULT NULL,
  `headTitle` varchar(20) DEFAULT NULL,
  `copyright` varchar(100) DEFAULT NULL,
  `url` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `system_systemsetup`
--

LOCK TABLES `system_systemsetup` WRITE;
/*!40000 ALTER TABLE `system_systemsetup` DISABLE KEYS */;
INSERT INTO `system_systemsetup` VALUES (1,NULL,NULL,NULL,NULL,NULL),(2,'江苏沙河','SandBox','SandBox','江苏沙盒',NULL),(3,'江苏沙盒科技','SandBox','SandBox','江苏沙盒科技',NULL),(4,'江苏沙盒科技','SandBox','SandBox','Copyright © 2016-2017 江苏沙盒科技.Version1.0.1',NULL),(5,'江苏沙盒科技','SandBox','SandBox','Copyright © 2016-2017 江苏沙盒科技.Version1.0.1',NULL),(6,'江苏沙盒协同办公平台','SandBox','SandBox','Copyright © 2016-2017 江苏沙盒科技.Version1.0.1',NULL),(7,'江苏沙盒协同办公平台','SandBox','SandBox','Copyright © 2016-2017 江苏沙盒科技.Version2.0.2',NULL),(8,'沙盒协同办公平台','SandBox','SandBox','Copyright © 2016-2017 江苏沙盒科技.Version2.0.2',NULL),(9,'沙盒协同办公平台','SandBox','SandBox','Copyright © 2016-2017 江苏沙盒科技.Version2.0.3',NULL),(10,'沙盒协同办公平台','SandBox','SandBox','Copyright © 2016-2017 江苏沙盒科技.Version2.0.6',NULL),(11,'沙盒协同办公平台','SandBox','SandBox','Copyright © 2017-2018 江苏沙盒科技.Version2.0.6',NULL);
/*!40000 ALTER TABLE `system_systemsetup` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_structure`
--

DROP TABLE IF EXISTS `users_structure`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users_structure` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(60) NOT NULL,
  `type` varchar(20) NOT NULL,
  `parent_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `users_structure_parent_id_e73fd647_fk_users_structure_id` (`parent_id`),
  CONSTRAINT `users_structure_parent_id_e73fd647_fk_users_structure_id` FOREIGN KEY (`parent_id`) REFERENCES `users_structure` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_structure`
--

LOCK TABLES `users_structure` WRITE;
/*!40000 ALTER TABLE `users_structure` DISABLE KEYS */;
INSERT INTO `users_structure` VALUES (5,'江苏沙盒科技','firm',NULL),(9,'销售部','department',5),(10,'技术部','department',5),(11,'商务中心','department',5),(12,'行政中心','department',5),(13,'财务','department',9),(14,'车队','department',9),(15,'销售部-内','department',5);
/*!40000 ALTER TABLE `users_structure` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_userprofile`
--

DROP TABLE IF EXISTS `users_userprofile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users_userprofile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `name` varchar(20) NOT NULL,
  `birthday` date DEFAULT NULL,
  `gender` varchar(10) NOT NULL,
  `mobile` varchar(11) NOT NULL,
  `email` varchar(100) NOT NULL,
  `image` varchar(100) DEFAULT NULL,
  `post` varchar(50) DEFAULT NULL,
  `joined_date` date DEFAULT NULL,
  `department_id` int(11) DEFAULT NULL,
  `superior_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  KEY `users_userprofile_department_id_b060d851_fk_users_structure_id` (`department_id`),
  KEY `users_userprofile_superior_id_3869391f_fk_users_userprofile_id` (`superior_id`),
  CONSTRAINT `users_userprofile_department_id_b060d851_fk_users_structure_id` FOREIGN KEY (`department_id`) REFERENCES `users_structure` (`id`),
  CONSTRAINT `users_userprofile_superior_id_3869391f_fk_users_userprofile_id` FOREIGN KEY (`superior_id`) REFERENCES `users_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_userprofile`
--

LOCK TABLES `users_userprofile` WRITE;
/*!40000 ALTER TABLE `users_userprofile` DISABLE KEYS */;
INSERT INTO `users_userprofile` VALUES (11,'pbkdf2_sha256$36000$m93UiveYcXJi$OF2RSJvsBRXi/OQFMziNwIlDRhVMAa0WIWNqWdwIfnQ=','2018-06-21 11:05:59.107485',1,'admin','','',1,1,'2017-12-12 16:51:00.000000','管理员',NULL,'male','13813836955','admin@sandbox.com','image/default.jpg',NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `users_userprofile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_userprofile_groups`
--

DROP TABLE IF EXISTS `users_userprofile_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users_userprofile_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userprofile_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_userprofile_groups_userprofile_id_group_id_823cf2fc_uniq` (`userprofile_id`,`group_id`),
  KEY `users_userprofile_groups_group_id_3de53dbf_fk_auth_group_id` (`group_id`),
  CONSTRAINT `users_userprofile_gr_userprofile_id_a4496a80_fk_users_use` FOREIGN KEY (`userprofile_id`) REFERENCES `users_userprofile` (`id`),
  CONSTRAINT `users_userprofile_groups_group_id_3de53dbf_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_userprofile_groups`
--

LOCK TABLES `users_userprofile_groups` WRITE;
/*!40000 ALTER TABLE `users_userprofile_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `users_userprofile_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_userprofile_roles`
--

DROP TABLE IF EXISTS `users_userprofile_roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users_userprofile_roles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userprofile_id` int(11) NOT NULL,
  `role_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_userprofile_roles_userprofile_id_role_id_81c255df_uniq` (`userprofile_id`,`role_id`),
  KEY `users_userprofile_roles_role_id_740e5521_fk_rbac_role_id` (`role_id`),
  CONSTRAINT `users_userprofile_ro_userprofile_id_ae49de2a_fk_users_use` FOREIGN KEY (`userprofile_id`) REFERENCES `users_userprofile` (`id`),
  CONSTRAINT `users_userprofile_roles_role_id_740e5521_fk_rbac_role_id` FOREIGN KEY (`role_id`) REFERENCES `rbac_role` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=85 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_userprofile_roles`
--

LOCK TABLES `users_userprofile_roles` WRITE;
/*!40000 ALTER TABLE `users_userprofile_roles` DISABLE KEYS */;
INSERT INTO `users_userprofile_roles` VALUES (84,11,10);
/*!40000 ALTER TABLE `users_userprofile_roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_userprofile_user_permissions`
--

DROP TABLE IF EXISTS `users_userprofile_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users_userprofile_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userprofile_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_userprofile_user_p_userprofile_id_permissio_d0215190_uniq` (`userprofile_id`,`permission_id`),
  KEY `users_userprofile_us_permission_id_393136b6_fk_auth_perm` (`permission_id`),
  CONSTRAINT `users_userprofile_us_permission_id_393136b6_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `users_userprofile_us_userprofile_id_34544737_fk_users_use` FOREIGN KEY (`userprofile_id`) REFERENCES `users_userprofile` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_userprofile_user_permissions`
--

LOCK TABLES `users_userprofile_user_permissions` WRITE;
/*!40000 ALTER TABLE `users_userprofile_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `users_userprofile_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-06-21 11:22:31
