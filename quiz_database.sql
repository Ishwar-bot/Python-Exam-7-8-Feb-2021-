-- MySQL dump 10.13  Distrib 8.0.21, for Win64 (x86_64)
--
-- Host: localhost    Database: quiz_database
-- ------------------------------------------------------
-- Server version	8.0.21

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
-- Table structure for table `question`
--

DROP TABLE IF EXISTS `question`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `question` (
  `quiz_id` int NOT NULL,
  `question_id` int NOT NULL,
  `question` varchar(200) DEFAULT NULL,
  `option_1` varchar(100) DEFAULT NULL,
  `option_2` varchar(100) DEFAULT NULL,
  `option_3` varchar(100) DEFAULT NULL,
  `option_4` varchar(100) DEFAULT NULL,
  `correct_option` tinyint DEFAULT NULL,
  PRIMARY KEY (`quiz_id`,`question_id`),
  CONSTRAINT `question_ibfk_1` FOREIGN KEY (`quiz_id`) REFERENCES `quiz` (`quiz_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `question`
--

LOCK TABLES `question` WRITE;
/*!40000 ALTER TABLE `question` DISABLE KEYS */;
INSERT INTO `question` VALUES (1,1,'In which language is Python written?','English','PHP','C','All of the Above',3),(1,2,'Which one of the following is the correct extension of the Python file?','.py','.python','.p','None of the Above',1),(1,3,'What do we use to define a block of code in Python language?','Key','Brackets','Indentations','None of the Above',3),(1,4,'Which character is used in Python to make a single line comment?','/','//','#','!',3),(1,5,'What is the method inside the class in python language?','Object','Function','Attribute','Argument',2),(1,6,'Which of the following declarations is incorrect?','_x = 2','__x = 3','__xyz__ = 5','None of these',4),(1,7,'Why does the name of local variables start with an underscore discouraged?','To identify the variable','It confuses the interpreter','private variable of a class','None of these',3),(1,8,'Which of the following is not a keyword in Python language?','val','raise','try','with',1),(2,1,'Which of the following words cannot be a variable in python language?','_val','val','try','_try_',3),(2,2,'Which of the following operators is the correct option for power(ab)','a ^ b','a**b','a ^ ^ b','a ^ * b',2),(2,3,'Which one of the following has the highest precedence in the expression?','Division','Subtraction','Power','Parenthesis',4),(2,4,'Which of the following functions is a built-in function in python language?','val()','print()','modify()','None of these',2),(2,5,'Which of the following statements is correct for variable names in Python language?','All variable names must begin with an underscore','Unlimited length','The variable name length is a maximum of 2.','All of the above',2),(2,6,' In which year was the Python language developed?','1995','1972','1981','1989',4),(2,7,'What is the maximum possible length of an identifier?','16','32','64','None of the above',4),(2,8,' Who developed the Python language?','Zim Den','Guido van Rossum','Niene Stom','Wick van Rossum',2);
/*!40000 ALTER TABLE `question` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `quiz`
--

DROP TABLE IF EXISTS `quiz`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `quiz` (
  `quiz_id` int NOT NULL,
  `quiz_name` varchar(50) DEFAULT NULL,
  `topic` varchar(50) DEFAULT NULL,
  `difficulty` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`quiz_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `quiz`
--

LOCK TABLES `quiz` WRITE;
/*!40000 ALTER TABLE `quiz` DISABLE KEYS */;
INSERT INTO `quiz` VALUES (1,'Python Assignment-1','Python','Easy'),(2,'Python Assignment-2','Python','Medium');
/*!40000 ALTER TABLE `quiz` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `result`
--

DROP TABLE IF EXISTS `result`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `result` (
  `email_id` varchar(40) NOT NULL,
  `quiz_id` int NOT NULL,
  `question_id` int NOT NULL,
  `user_response` tinyint DEFAULT NULL,
  `correct_response` tinyint DEFAULT NULL,
  PRIMARY KEY (`email_id`,`quiz_id`,`question_id`),
  KEY `quiz_id` (`quiz_id`,`question_id`),
  CONSTRAINT `result_ibfk_1` FOREIGN KEY (`email_id`) REFERENCES `user` (`email_id`),
  CONSTRAINT `result_ibfk_2` FOREIGN KEY (`quiz_id`, `question_id`) REFERENCES `question` (`quiz_id`, `question_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `result`
--

LOCK TABLES `result` WRITE;
/*!40000 ALTER TABLE `result` DISABLE KEYS */;
/*!40000 ALTER TABLE `result` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `email_id` varchar(40) NOT NULL,
  `password` varchar(30) DEFAULT NULL,
  `super_user` tinyint(1) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `phone_no` varchar(13) DEFAULT NULL,
  PRIMARY KEY (`email_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES ('aditi11997@gmail.com','aditi101',0,'Aditi Deshpande','Pune','+919592378273'),('harishd2002@gmail.com','harish',0,'Harish Deshmukh','Jalgaon','+919075596630'),('ishudeshmukh2013@gmail.com','botbotbot',1,'Ishwarchandra Deshmukh','Pune','+917558723219');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-02-08  8:13:42
