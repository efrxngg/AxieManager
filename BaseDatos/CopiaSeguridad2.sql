-- MariaDB dump 10.19  Distrib 10.7.3-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: dataxie
-- ------------------------------------------------------
-- Server version	10.7.3-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `becado`
--

DROP TABLE IF EXISTS `becado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `becado` (
  `id_beca` int(11) NOT NULL,
  `id_persona` varchar(10) COLLATE utf8mb4_spanish_ci NOT NULL,
  `total_slp` int(11) DEFAULT 0,
  `copas` int(11) DEFAULT 1200,
  `top` int(11) DEFAULT 0,
  KEY `fk_idBeca` (`id_beca`),
  KEY `fk_cedula` (`id_persona`),
  CONSTRAINT `fk_cedula` FOREIGN KEY (`id_persona`) REFERENCES `persona` (`cedula`),
  CONSTRAINT `fk_idBeca` FOREIGN KEY (`id_beca`) REFERENCES `ronin` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `becado`
--

LOCK TABLES `becado` WRITE;
/*!40000 ALTER TABLE `becado` DISABLE KEYS */;
INSERT INTO `becado` VALUES
(1,'0954943114',0,1200,0);
/*!40000 ALTER TABLE `becado` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `persona`
--

DROP TABLE IF EXISTS `persona`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `persona` (
  `cedula` varchar(10) COLLATE utf8mb4_spanish_ci NOT NULL,
  `nombre` varchar(125) COLLATE utf8mb4_spanish_ci NOT NULL,
  `apellido` varchar(125) COLLATE utf8mb4_spanish_ci NOT NULL,
  `edad` int(2) NOT NULL,
  `nacionalidad` varchar(50) COLLATE utf8mb4_spanish_ci NOT NULL,
  `contacto` varchar(30) COLLATE utf8mb4_spanish_ci NOT NULL,
  `depo_ronin` varchar(50) COLLATE utf8mb4_spanish_ci NOT NULL,
  `fecha_ingreso` date DEFAULT current_timestamp(),
  `fecha_salida` date DEFAULT NULL,
  `estado` char(1) COLLATE utf8mb4_spanish_ci DEFAULT 'A',
  PRIMARY KEY (`cedula`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `persona`
--

LOCK TABLES `persona` WRITE;
/*!40000 ALTER TABLE `persona` DISABLE KEYS */;
INSERT INTO `persona` VALUES
('0000000001','ADAN','GOD',99,'OLIMPICA','@ADAN','ronin:77e44a4d265c51751b2db841ea665c6e9bb4ec0a','2022-03-25',NULL,'A'),
('0000000002','EVA','GOD',99,'OLIMPICA','@EVA','ronin:470513a86b7f4079802523790d9f28428ff','2022-03-25','2022-03-29','A'),
('0000000006','Jose','Delgado',99,'Ecuatoriana','Noc','ronin','2022-03-26','2022-03-28','I'),
('0000000007','Ruben','Eguiguren',40,'Ecuatoriana','@ruben','ronin:nonenonfe','2022-04-07','2022-04-07','I'),
('0100000000','TEST','TEST',2,'Ecuatoriana','NONE','NONE','2022-03-26','2022-03-28','I'),
('0944444444','JUAN ','GABRIEL',19,'Ecuatoriana','NONE','NONE','2022-03-25','2022-03-29','I'),
('0952335811','Daniel','Galarza',18,'Ecuatoriana','@daniel','ronin:_ksdfkalsjflaskjf','2022-03-30',NULL,'A'),
('0954444443','Marjorie','Galarza',22,'Ecuatoriana','NONE','NAN','2022-03-25','2022-03-29','I'),
('0954444444','MIGUEL','ALVAREZ',19,'Ecuatoriana','NONE','NON','2022-03-25','2022-03-29','I'),
('0954941111','Gisell ','Castro',18,'Ecuatoriana','@c_gisell','ronin:470513a86b7f4079802523790d9f28428950e67f','2022-03-25',NULL,'A'),
('0954943112','Efren','Galarza',16,'Ecuatoriana','0997188086','ronin:77e44a4d265c51751b2db841ea665c6e9bb4ec0b','2022-03-20','2022-03-29','I'),
('0954943114','Efren','Galarza',19,'Ecuatoriana','0997188086','ronin:77e44a4d265c51751b2db841ea665c6e9bb4ec0a','2022-03-20',NULL,'A'),
('0954943116','Julio','Pico',19,'Ecuatoriana','@BokuNoPico','ronin:470513a86b7f4079802523790d9f28428950efef','2022-03-25',NULL,'A'),
('0954943333','DOMENICA','OÑA',19,'EC','NONE','NONE','2022-03-25','2022-03-28','I'),
('0954966666','Jimena','Sanches',19,'Ecuatoriana','@jime','ronin:470513a86b7f4079802523790d9f28428950eggg','2022-03-26',NULL,'A'),
('0955555555','Carlos','Vera',23,'Ecuatoriana','onen','ronin:470513a86b7f4079802523790d9f28428950e666','2022-03-26',NULL,'A'),
('0957777777','Jesus','Campoverde',18,'Ecuatoriana','@flash','ronin:none','2022-03-30',NULL,'A'),
('0959999999','Mono','Loco',19,'Ninguna','@monoloco','ronin:monoloco','2022-03-30','2022-03-30','I'),
('0966666666','Jorge','Vera',25,'Ecuatoriana','none','ronin:470513a86b7f4079802523790d9f28428950e67g','2022-03-26',NULL,'A'),
('0985444444','Erick','Fernandez',18,'EstadoUnidense','@erick_gg','ronin:ronin','2022-03-30',NULL,'A'),
('0988888888','Sebastian','Sopapo',20,'Colombiana','@seba_ff','ronin:roninkdslafaklhdfak','2022-04-05',NULL,'A'),
('1234567891','Steven','Patiño',18,'Ecuatoriana','@steven_Ec','ronin_nonenoe','2022-03-30',NULL,'A'),
('2423333333','Gargola','NOce',24,'dfsfsfsdfsdfdf','@g4rgola','ronin:fsldafkjsadfijiosa','2022-03-26','2022-03-28','I'),
('8888888888','Juanito','Alimaña',29,'None','fsds','dfsd','2022-03-26','2022-03-28','I'),
('9999999999','Don','NASARENO',40,'Ecuatoriano','noche','ronin:none','2022-03-26','2022-03-29','I');
/*!40000 ALTER TABLE `persona` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ronin`
--

DROP TABLE IF EXISTS `ronin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ronin` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ronin` varchar(50) COLLATE utf8mb4_spanish_ci NOT NULL,
  `becado` varchar(10) COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `total_slp` int(11) DEFAULT 0,
  `porcentaje_becado` int(11) DEFAULT 0,
  `fecha_ingreso` date DEFAULT current_timestamp(),
  PRIMARY KEY (`id`),
  UNIQUE KEY `ronin` (`ronin`),
  KEY `fk_becados` (`becado`),
  CONSTRAINT `fk_becados` FOREIGN KEY (`becado`) REFERENCES `persona` (`cedula`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ronin`
--

LOCK TABLES `ronin` WRITE;
/*!40000 ALTER TABLE `ronin` DISABLE KEYS */;
INSERT INTO `ronin` VALUES
(1,'ronin:470513a86b7f4079802523790d9f28428950e67f','0000000001',1008,40,'2022-03-20'),
(15,'ronin:3b8387c83132b80478ae51b5a864545e8cb35b95','0954941111',681,50,'2022-04-05'),
(16,'0xa9c205b1584e42d6158620f582dc1da3f60629a1','0000000002',9895,50,'2022-04-06'),
(18,'ronin:63943b48cafce1029b147d85c9a4e3c9907316ab',NULL,18241,0,'2022-04-06'),
(19,'ronin:7616bc6b4c0860d7aabe0364a93d9b96dbb596a9',NULL,10861,0,'2022-04-06');
/*!40000 ALTER TABLE `ronin` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-07 23:19:18
