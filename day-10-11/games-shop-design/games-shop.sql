-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: games_shop
-- ------------------------------------------------------
-- Server version	8.0.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `customers`
--

DROP TABLE IF EXISTS `customers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customers` (
  `customer_ID` int NOT NULL AUTO_INCREMENT,
  `email` varchar(50) NOT NULL,
  `phone_number` varchar(50) DEFAULT NULL,
  `pwd` binary(20) NOT NULL,
  `salt` binary(20) NOT NULL,
  PRIMARY KEY (`customer_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customers`
--

LOCK TABLES `customers` WRITE;
/*!40000 ALTER TABLE `customers` DISABLE KEYS */;
INSERT INTO `customers` VALUES (1,'customer1@gmail.com',NULL,_binary 'hashed_pwd\0\0\0\0\0\0\0\0\0\0',_binary 'salt_placeholder\0\0\0\0'),(2,'customer2@gmail.com',NULL,_binary 'hashed_pwd\0\0\0\0\0\0\0\0\0\0',_binary 'salt_placeholder\0\0\0\0'),(3,'customer3@gmail.com',NULL,_binary 'hashed_pwd\0\0\0\0\0\0\0\0\0\0',_binary 'salt_placeholder\0\0\0\0'),(4,'customer4@gmail.com',NULL,_binary 'hashed_pwd\0\0\0\0\0\0\0\0\0\0',_binary 'salt_placeholder\0\0\0\0'),(5,'customer5@gmail.com',NULL,_binary 'hashed_pwd\0\0\0\0\0\0\0\0\0\0',_binary 'salt_placeholder\0\0\0\0');
/*!40000 ALTER TABLE `customers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `genres`
--

DROP TABLE IF EXISTS `genres`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `genres` (
  `genre_id` int NOT NULL AUTO_INCREMENT,
  `genre_name` varchar(50) NOT NULL,
  PRIMARY KEY (`genre_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `genres`
--

LOCK TABLES `genres` WRITE;
/*!40000 ALTER TABLE `genres` DISABLE KEYS */;
INSERT INTO `genres` VALUES (1,'Horror'),(2,'Fantasy'),(3,'FPS'),(4,'MMORPG'),(5,'Moba');
/*!40000 ALTER TABLE `genres` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders` (
  `order_ID` int NOT NULL AUTO_INCREMENT,
  `FK_customer_ID` int NOT NULL,
  `FK_product_ID` int NOT NULL,
  `quantity` int DEFAULT '1',
  `transaction_amount` float NOT NULL,
  `transaction_date` date NOT NULL,
  PRIMARY KEY (`order_ID`),
  KEY `FK_customer_ID` (`FK_customer_ID`),
  KEY `FK_product_ID` (`FK_product_ID`),
  CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`FK_customer_ID`) REFERENCES `customers` (`customer_ID`),
  CONSTRAINT `orders_ibfk_2` FOREIGN KEY (`FK_product_ID`) REFERENCES `products` (`product_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES (1,1,1,1,14.99,'2023-02-06'),(2,2,2,1,13.77,'2023-03-22'),(3,1,3,1,19.99,'2022-02-24'),(4,4,4,1,24.99,'2023-04-17'),(5,3,5,1,54.99,'2023-06-03');
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products` (
  `product_ID` int NOT NULL AUTO_INCREMENT,
  `product_name` varchar(50) NOT NULL,
  `FK_genre_ID` int NOT NULL,
  `rating` int DEFAULT '0',
  `price` float NOT NULL,
  `FK_supplier_ID` int NOT NULL,
  `inventory` int DEFAULT '0',
  PRIMARY KEY (`product_ID`),
  KEY `FK_genre_ID` (`FK_genre_ID`),
  KEY `FK_supplier_ID` (`FK_supplier_ID`),
  CONSTRAINT `products_ibfk_1` FOREIGN KEY (`FK_genre_ID`) REFERENCES `genres` (`genre_id`),
  CONSTRAINT `products_ibfk_2` FOREIGN KEY (`FK_supplier_ID`) REFERENCES `suppliers` (`supplier_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES (1,'Game 1',1,0,9.99,1,5),(2,'Game 2',5,0,8.77,3,8),(3,'Game 3',2,0,14.99,4,3),(4,'Game 4',4,0,19.99,5,1),(5,'Game 5',3,0,49.99,2,0);
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `suppliers`
--

DROP TABLE IF EXISTS `suppliers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `suppliers` (
  `supplier_ID` int NOT NULL AUTO_INCREMENT,
  `supplier_name` varchar(50) NOT NULL,
  `supplier_location` varchar(50) NOT NULL,
  PRIMARY KEY (`supplier_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `suppliers`
--

LOCK TABLES `suppliers` WRITE;
/*!40000 ALTER TABLE `suppliers` DISABLE KEYS */;
INSERT INTO `suppliers` VALUES (1,'Xbox','USA'),(2,'Nintendo','JP'),(3,'Tencent','CH'),(4,'Ubisoft','USA'),(5,'Sony','JP');
/*!40000 ALTER TABLE `suppliers` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-17 11:57:34
