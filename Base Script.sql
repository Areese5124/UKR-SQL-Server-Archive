-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema UKPP_Database
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema UKPP_Database
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `UKPP_Database` DEFAULT CHARACTER SET utf8 ;
USE `UKPP_Database` ;

-- -----------------------------------------------------
-- Table `UKPP_Database`.`Poster`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `UKPP_Database`.`Poster` ;

CREATE TABLE IF NOT EXISTS `UKPP_Database`.`Poster` (
  `idPoster` INT NOT NULL AUTO_INCREMENT,
  `Poster_Name` VARCHAR(50) NULL,
  PRIMARY KEY (`idPoster`),
  UNIQUE INDEX `Authorcol_UNIQUE` (`Poster_Name` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `UKPP_Database`.`Author`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `UKPP_Database`.`Author` ;

CREATE TABLE IF NOT EXISTS `UKPP_Database`.`Author` (
  `idAuthor` INT NOT NULL AUTO_INCREMENT,
  `Author_Name` VARCHAR(50) NULL,
  PRIMARY KEY (`idAuthor`),
  UNIQUE INDEX `Authorcol_UNIQUE` (`Author_Name` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `UKPP_Database`.`Archivist`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `UKPP_Database`.`Archivist` ;

CREATE TABLE IF NOT EXISTS `UKPP_Database`.`Archivist` (
  `idArchivist` INT NOT NULL AUTO_INCREMENT,
  `Archivist_Name` VARCHAR(50) NULL,
  PRIMARY KEY (`idArchivist`),
  UNIQUE INDEX `Authorcol_UNIQUE` (`Archivist_Name` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `UKPP_Database`.`Translator`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `UKPP_Database`.`Translator` ;

CREATE TABLE IF NOT EXISTS `UKPP_Database`.`Translator` (
  `idTranslator` INT NOT NULL,
  `Translator_Name` VARCHAR(45) NULL,
  PRIMARY KEY (`idTranslator`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `UKPP_Database`.`Language`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `UKPP_Database`.`Language` ;

CREATE TABLE IF NOT EXISTS `UKPP_Database`.`Language` (
  `idLanguage` INT NOT NULL,
  `Languag_Name` VARCHAR(45) NULL,
  PRIMARY KEY (`idLanguage`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `UKPP_Database`.`UKR-Posted`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `UKPP_Database`.`UKR-Posted` ;

CREATE TABLE IF NOT EXISTS `UKPP_Database`.`UKR-Posted` (
  `idUKR` INT NOT NULL AUTO_INCREMENT,
  `Archivist_Name` INT NULL,
  `Author_Name` INT NULL,
  `Post_Url` VARCHAR(500) NULL,
  `Poster_Name` INT NULL,
  `Poem_Text` INT NULL,
  `Posted_Language` INT NULL,
  `Translated_Post` TINYINT NULL,
  `Translator` INT NULL,
  `Original_Language` INT NULL,
  `Themes` INT NOT NULL,
  `Date_Posted` DATE NULL,
  `Poems_In_Comments` TINYINT NULL,
  `Suggestions_Or_Corrections` TINYINT NULL,
  `Comments` VARCHAR(500) NULL,
  `Number_Of_Likes` INT NULL,
  `Number_Of_Comments` INT NULL,
  `Number_Of_Shares` INT NULL,
  PRIMARY KEY (`idUKR`),
  INDEX `Original_Language_idx` (`Original_Language` ASC) VISIBLE,
  INDEX `Posted_Language_idx` (`Posted_Language` ASC) VISIBLE,
  INDEX `Archivist_Name_idx` (`Archivist_Name` ASC) VISIBLE,
  INDEX `Translator_idx` (`Translator` ASC) VISIBLE,
  INDEX `Poster_Name_idx` (`Poster_Name` ASC) VISIBLE,
  INDEX `Author_Name_idx` (`Author_Name` ASC) VISIBLE,
  CONSTRAINT `Original_Language`
    FOREIGN KEY (`Original_Language`)
    REFERENCES `UKPP_Database`.`Language` (`idLanguage`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `Posted_Language`
    FOREIGN KEY (`Posted_Language`)
    REFERENCES `UKPP_Database`.`Language` (`idLanguage`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `Archivist_Name`
    FOREIGN KEY (`Archivist_Name`)
    REFERENCES `UKPP_Database`.`Archivist` (`idArchivist`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `Translator`
    FOREIGN KEY (`Translator`)
    REFERENCES `UKPP_Database`.`Translator` (`idTranslator`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `Poster_Name`
    FOREIGN KEY (`Poster_Name`)
    REFERENCES `UKPP_Database`.`Poster` (`idPoster`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `Authort_Name`
    FOREIGN KEY (`Author_Name`)
    REFERENCES `UKPP_Database`.`Author` (`idAuthor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `UKPP_Database`.`timestamps`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `UKPP_Database`.`timestamps` ;

CREATE TABLE IF NOT EXISTS `UKPP_Database`.`timestamps` (
  `create_time` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` TIMESTAMP NULL,
  `delete_time` TIMESTAMP NULL);

USE `UKPP_Database`;

DELIMITER $$

USE `UKPP_Database`$$
DROP TRIGGER IF EXISTS `UKPP_Database`.`UKR-Posted_BEFORE_INSERT_1` $$
USE `UKPP_Database`$$
CREATE DEFINER = CURRENT_USER TRIGGER `UKPP_Database`.`UKR-Posted_BEFORE_INSERT_1` BEFORE INSERT ON `UKR-Posted` FOR EACH ROW
BEGIN
INSERT INTO timestamps (create_time) VALUES (CURRENT_TIME());
END$$


USE `UKPP_Database`$$
DROP TRIGGER IF EXISTS `UKPP_Database`.`UKR-Posted_BEFORE_UPDATE` $$
USE `UKPP_Database`$$
CREATE DEFINER = CURRENT_USER TRIGGER `UKPP_Database`.`UKR-Posted_BEFORE_UPDATE` BEFORE UPDATE ON `UKR-Posted` FOR EACH ROW
BEGIN
INSERT INTO timestamps (update_time) VALUES (CURRENT_TIME());
END$$


USE `UKPP_Database`$$
DROP TRIGGER IF EXISTS `UKPP_Database`.`UKR-Posted_BEFORE_DELETE` $$
USE `UKPP_Database`$$
CREATE DEFINER = CURRENT_USER TRIGGER `UKPP_Database`.`UKR-Posted_BEFORE_DELETE` BEFORE DELETE ON `UKR-Posted` FOR EACH ROW
BEGIN
INSERT INTO timestamps (delete_time) VALUES (CURRENT_TIME());
END$$


DELIMITER ;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
