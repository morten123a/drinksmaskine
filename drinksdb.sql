-- --------------------------------------------------------
-- Vært:                         172.21.114.12
-- Server-version:               8.0.39 - MySQL Community Server - GPL
-- ServerOS:                     Win64
-- HeidiSQL Version:             12.3.0.6589
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- Dumping structure for tabel drinksdb.ingredients
CREATE TABLE IF NOT EXISTS `ingredients` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table drinksdb.ingredients: ~24 rows (tilnærmelsesvis)
INSERT INTO `ingredients` (`id`, `name`) VALUES
	(1, 'rom'),
	(2, 'gin'),
	(3, 'vodka'),
	(4, 'tequila'),
	(5, 'whisky'),
	(6, 'malibu'),
	(7, 'fanta'),
	(8, 'cola'),
	(9, 'schweppers'),
	(10, 'bailey'),
	(11, 'faxe kondi'),
	(12, 'booster'),
	(13, 'appelsinjuice'),
	(14, 'jeagermeister'),
	(15, 'baileys'),
	(16, 'mango sirup'),
	(17, 'rød sodavand'),
	(18, 'likør43'),
	(19, 'blue curacao'),
	(20, 'passionfruit sirup'),
	(21, 'redbull'),
	(22, 'æblejuice'),
	(23, 'cuba caramel'),
	(24, 'grenadine');

-- Dumping structure for tabel drinksdb.recipes
CREATE TABLE IF NOT EXISTS `recipes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table drinksdb.recipes: ~12 rows (tilnærmelsesvis)
INSERT INTO `recipes` (`id`, `name`) VALUES
	(1, 'bmw'),
	(2, 'vodka juice'),
	(3, 'vodka booster'),
	(4, 'gin hass'),
	(5, 'brandbil'),
	(6, 'jeagerbomb'),
	(7, 'æblekage shot'),
	(8, 'rom & cola'),
	(9, 'champagnebrus'),
	(10, 'filur'),
	(11, 'isbjørn'),
	(12, 'astronaut');

-- Dumping structure for tabel drinksdb.recipes_ingredients
CREATE TABLE IF NOT EXISTS `recipes_ingredients` (
  `id` int NOT NULL AUTO_INCREMENT,
  `recipes_id` int DEFAULT NULL,
  `ingredients_id` int DEFAULT NULL,
  `amount` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_recipes_ingridients_recipes` (`recipes_id`),
  KEY `FK_recipes_ingredients_ingredients` (`ingredients_id`),
  CONSTRAINT `FK_recipes_ingredients_ingredients` FOREIGN KEY (`ingredients_id`) REFERENCES `ingredients` (`id`),
  CONSTRAINT `FK_recipes_ingridients_recipes` FOREIGN KEY (`recipes_id`) REFERENCES `recipes` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table drinksdb.recipes_ingredients: ~29 rows (tilnærmelsesvis)
INSERT INTO `recipes_ingredients` (`id`, `recipes_id`, `ingredients_id`, `amount`) VALUES
	(1, 1, 5, 2),
	(2, 1, 6, 2),
	(3, 1, 15, 2),
	(4, 2, 3, 4),
	(5, 2, 13, 14),
	(6, 3, 3, 2),
	(7, 3, 12, 15),
	(8, 4, 2, 4),
	(9, 4, 16, 2),
	(10, 4, 9, 10),
	(11, 5, 14, 3),
	(12, 5, 17, 12),
	(13, 6, 14, 2),
	(14, 6, 21, 4),
	(15, 7, 22, 12),
	(16, 7, 18, 4),
	(17, 8, 1, 4),
	(18, 8, 8, 10),
	(19, 9, 11, 10),
	(20, 9, 23, 2),
	(21, 10, 3, 4),
	(22, 10, 13, 6),
	(23, 10, 17, 4),
	(24, 11, 3, 4),
	(25, 11, 19, 2),
	(26, 11, 11, 12),
	(27, 12, 2, 4),
	(28, 12, 24, 3),
	(29, 12, 11, 10);

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
