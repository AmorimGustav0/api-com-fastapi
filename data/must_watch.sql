CREATE DATABASE  IF NOT EXISTS `must_watch` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `must_watch`;
-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: must_watch
-- ------------------------------------------------------
-- Server version	8.0.35

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `ator`
--

DROP TABLE IF EXISTS `ator`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ator` (
  `id_autor` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) NOT NULL,
  `ano_nasc` int NOT NULL,
  PRIMARY KEY (`id_autor`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ator`
--

LOCK TABLES `ator` WRITE;
/*!40000 ALTER TABLE `ator` DISABLE KEYS */;
INSERT INTO `ator` VALUES (1,'tom holland',1997),(2,'tom hanks',1990),(4,'vin disel',1990),(5,'paul walker',1982),(6,'The Rock',1972),(7,'miller',1972),(8,'ursula',1989),(9,'alvaro morte',1975),(10,'Zendaya',1997);
/*!40000 ALTER TABLE `ator` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ator_serie`
--

DROP TABLE IF EXISTS `ator_serie`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ator_serie` (
  `id_ator` int NOT NULL,
  `id_serie` int NOT NULL,
  `personagem` varchar(100) NOT NULL,
  PRIMARY KEY (`id_ator`,`id_serie`),
  KEY `id_serie_idx` (`id_serie`),
  CONSTRAINT `id_autor` FOREIGN KEY (`id_ator`) REFERENCES `ator` (`id_autor`),
  CONSTRAINT `id_serie` FOREIGN KEY (`id_serie`) REFERENCES `serie` (`id_serie`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ator_serie`
--

LOCK TABLES `ator_serie` WRITE;
/*!40000 ALTER TABLE `ator_serie` DISABLE KEYS */;
INSERT INTO `ator_serie` VALUES (4,14,'Dominic Toreto'),(5,9,'denver'),(5,14,'Bryan'),(6,14,'Agente Hobbys'),(7,4,'Michael Scoffield'),(8,9,'Tokio'),(10,1,'mj'),(10,4,'mj');
/*!40000 ALTER TABLE `ator_serie` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `ator_series`
--

DROP TABLE IF EXISTS `ator_series`;
/*!50001 DROP VIEW IF EXISTS `ator_series`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `ator_series` AS SELECT 
 1 AS `nome_ator`,
 1 AS `personagem`,
 1 AS `nome_serie`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `avaliacao_serie`
--

DROP TABLE IF EXISTS `avaliacao_serie`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `avaliacao_serie` (
  `id_avaliacao` int NOT NULL AUTO_INCREMENT,
  `id_serie` int NOT NULL,
  `nota` int NOT NULL,
  `comentario` text NOT NULL,
  `data_avaliacao` datetime NOT NULL,
  PRIMARY KEY (`id_avaliacao`),
  KEY `id_serie_idx` (`id_serie`),
  CONSTRAINT `fk_serie_avaliacao` FOREIGN KEY (`id_serie`) REFERENCES `serie` (`id_serie`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `avaliacao_serie`
--

LOCK TABLES `avaliacao_serie` WRITE;
/*!40000 ALTER TABLE `avaliacao_serie` DISABLE KEYS */;
INSERT INTO `avaliacao_serie` VALUES (1,1,9,'muito bom','2025-05-20 00:00:00'),(2,9,9,'boa trama','2022-05-21 00:00:00'),(3,13,6,'serie muito sem pe e sem cabeça','2022-12-12 00:00:00'),(4,16,9,'muito bom a batalha','2025-05-20 09:24:43');
/*!40000 ALTER TABLE `avaliacao_serie` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `categoria`
--

DROP TABLE IF EXISTS `categoria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `categoria` (
  `id_categoria` int NOT NULL AUTO_INCREMENT,
  `nome_categoria` varchar(50) NOT NULL,
  PRIMARY KEY (`id_categoria`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categoria`
--

LOCK TABLES `categoria` WRITE;
/*!40000 ALTER TABLE `categoria` DISABLE KEYS */;
INSERT INTO `categoria` VALUES (1,'ação'),(2,'comédia'),(3,'drama'),(4,'terror'),(5,'suspense'),(6,'anime'),(7,'ficcao');
/*!40000 ALTER TABLE `categoria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `motivo_assistir`
--

DROP TABLE IF EXISTS `motivo_assistir`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `motivo_assistir` (
  `id_motivo_assistir` int NOT NULL AUTO_INCREMENT,
  `id_serie` int NOT NULL,
  `motivo` text NOT NULL,
  PRIMARY KEY (`id_motivo_assistir`),
  KEY `id_serie_idx` (`id_serie`),
  CONSTRAINT `fk_serie_motivo` FOREIGN KEY (`id_serie`) REFERENCES `serie` (`id_serie`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `motivo_assistir`
--

LOCK TABLES `motivo_assistir` WRITE;
/*!40000 ALTER TABLE `motivo_assistir` DISABLE KEYS */;
INSERT INTO `motivo_assistir` VALUES (1,1,'uma boa serie sobre...'),(2,4,'o cara tem o mapa da prisao tatuado no corpo'),(3,9,'roubar um banco central? essa historia e familiar'),(4,16,'uma boa serie sobre aranhas...');
/*!40000 ALTER TABLE `motivo_assistir` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `serie`
--

DROP TABLE IF EXISTS `serie`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `serie` (
  `id_serie` int NOT NULL AUTO_INCREMENT,
  `id_categoria` int NOT NULL,
  `titulo` varchar(60) NOT NULL,
  `descricao` varchar(200) NOT NULL,
  `ano_lancamento` int NOT NULL,
  PRIMARY KEY (`id_serie`),
  KEY `id_categoria_idx` (`id_categoria`),
  CONSTRAINT `id_categoria` FOREIGN KEY (`id_categoria`) REFERENCES `categoria` (`id_categoria`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `serie`
--

LOCK TABLES `serie` WRITE;
/*!40000 ALTER TABLE `serie` DISABLE KEYS */;
INSERT INTO `serie` VALUES (1,1,'homem aranha ','aaaaaa',2023),(4,1,'prison break','aaaaaa',2000),(9,1,'La casa de papel','bbbbbbr',2018),(11,1,'homem aranha','aaaaaa',2023),(13,1,'Wanda vision','dfanhgr',2021),(14,1,'Velozes e furiosos','aaaa',2001),(16,1,'amazing spider man','aaaaaa',2023);
/*!40000 ALTER TABLE `serie` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Final view structure for view `ator_series`
--

/*!50001 DROP VIEW IF EXISTS `ator_series`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `ator_series` AS select `ator`.`nome` AS `nome_ator`,`ator_serie`.`personagem` AS `personagem`,`serie`.`titulo` AS `nome_serie` from ((`ator_serie` join `ator` on((`ator_serie`.`id_ator` = `ator`.`id_autor`))) join `serie` on((`ator_serie`.`id_serie` = `serie`.`id_serie`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-05-20 16:28:29
