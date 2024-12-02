SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema UKR_Database
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `UKR_Database`;
USE `UKR_Database` ;

-- -----------------------------------------------------
-- Table `UKR_Database`.`Archivist`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `UKR_Database`.`Archivist` (
  `idArchivist` INT NOT NULL AUTO_INCREMENT,
  `Archivist_Name` VARCHAR(50) NULL DEFAULT NULL,
  PRIMARY KEY (`idArchivist`))
ENGINE = InnoDB;

CREATE UNIQUE INDEX `Authorcol_UNIQUE` ON `UKR_Database`.`Archivist` (`Archivist_Name` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `UKR_Database`.`Author`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `UKR_Database`.`Author` (
  `idAuthor` INT NOT NULL AUTO_INCREMENT,
  `Author_Name` VARCHAR(50) NULL DEFAULT NULL,
  PRIMARY KEY (`idAuthor`))
ENGINE = InnoDB;

CREATE UNIQUE INDEX `Authorcol_UNIQUE` ON `UKR_Database`.`Author` (`Author_Name` ASC) VISIBLE;

-- -----------------------------------------------------
-- Table `UKR_Database`.`Original_Language`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `UKR_Database`.`Original_Language` (
  `idOriginal_Language` INT NOT NULL AUTO_INCREMENT,
  `Original_Language` VARCHAR(30) NULL DEFAULT NULL,
  PRIMARY KEY (`idOriginal_Language`))
ENGINE = InnoDB;

CREATE UNIQUE INDEX `idPoem_UNIQUE` ON `UKR_Database`.`Original_Language` (`idOriginal_Language` ASC) VISIBLE;

CREATE INDEX `Poem_Text_idx` ON `UKR_Database`.`Original_Language` (`idOriginal_Language` ASC) VISIBLE;

-- -----------------------------------------------------
-- Table `UKR_Database`.`Poem`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `UKR_Database`.`Poem` (
  `idPoems` INT NOT NULL AUTO_INCREMENT,
  `Poem_Full_Text` MEDIUMTEXT NULL DEFAULT NULL,
  `Poem_Original_Language` INT NULL DEFAULT NULL,
  PRIMARY KEY (`idPoems`),
  CONSTRAINT `Poem_Original_Lang`
    FOREIGN KEY (`Poem_Original_Language`)
    REFERENCES `UKR_Database`.`Original_Language` (`idOriginal_Language`))
ENGINE = InnoDB;

CREATE INDEX `Poem_Original_Lang_idx` ON `UKR_Database`.`Poem` (`Poem_Original_Language` ASC) VISIBLE;

-- -----------------------------------------------------
-- Table `UKR_Database`.`Poster`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `UKR_Database`.`Poster` (
  `idPoster` INT NOT NULL AUTO_INCREMENT,
  `Poster_Name` VARCHAR(50) NULL DEFAULT NULL,
  PRIMARY KEY (`idPoster`))
ENGINE = InnoDB;

CREATE UNIQUE INDEX `Authorcol_UNIQUE` ON `UKR_Database`.`Poster` (`Poster_Name` ASC) VISIBLE;

-- -----------------------------------------------------
-- Table `UKR_Database`.`Themes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `UKR_Database`.`Themes` (
  `idTheme_Poem` INT NULL DEFAULT NULL,
  CONSTRAINT `Theme_ Poem_ id`
    FOREIGN KEY (`idTheme_Poem`)
    REFERENCES `UKR_Database`.`Poem` (`idPoems`))
ENGINE = InnoDB;

CREATE UNIQUE INDEX `idThemes_UNIQUE` ON `UKR_Database`.`Themes` (`idTheme_Poem` ASC);


-- -----------------------------------------------------
-- Table `UKR_Database`.`Translation_Languages`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `UKR_Database`.`Translation_Languages` (
  `idTranslation_Languages` INT NOT NULL AUTO_INCREMENT,
  `Languages` VARCHAR(20) NULL DEFAULT NULL,
  PRIMARY KEY (`idTranslation_Languages`))
ENGINE = InnoDB;

CREATE UNIQUE INDEX `idTranslation_Languages_UNIQUE` ON `UKR_Database`.`Translation_Languages` (`idTranslation_Languages` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `UKR_Database`.`Translator`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `UKR_Database`.`Translator` (
  `idTranslator` INT NOT NULL AUTO_INCREMENT,
  `Translator_Name` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`idTranslator`))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `UKR_Database`.`UKR_Poem_Details`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `UKR_Database`.`UKR_Poem_Details` (
  `Poem` INT NULL DEFAULT NULL,
  `Author_Name` INT NULL DEFAULT NULL,
  `Archivist_Name` INT NULL DEFAULT NULL,
  `Post_Url` VARCHAR(500) NULL DEFAULT NULL,
  `Poster_Name` INT NULL DEFAULT NULL,
  `Translated_Post` TINYINT NULL DEFAULT NULL,
  `Translator` INT NULL DEFAULT NULL,
  `Translation_Language` INT NULL DEFAULT NULL,
  `Date_Posted` DATE NULL DEFAULT NULL,
  `Poems_In_Comments` TINYINT NULL DEFAULT NULL,
  `Suggestions_Or_Corrections` TINYINT NULL DEFAULT NULL,
  `Comments` VARCHAR(500) NULL DEFAULT NULL,
  `Number_Of_Likes` INT NULL DEFAULT NULL,
  `Number_Of_Comments` INT NULL DEFAULT NULL,
  `Number_Of_Shares` INT NULL DEFAULT NULL,
  CONSTRAINT `Archivist_Name`
    FOREIGN KEY (`Archivist_Name`)
    REFERENCES `UKR_Database`.`Archivist` (`idArchivist`),
  CONSTRAINT `Authort_Name`
    FOREIGN KEY (`Author_Name`)
    REFERENCES `UKR_Database`.`Author` (`idAuthor`),
  CONSTRAINT `Poem_Full_Text`
    FOREIGN KEY (`Poem`)
    REFERENCES `UKR_Database`.`Poem` (`idPoems`),
  CONSTRAINT `Poster_Name`
    FOREIGN KEY (`Poster_Name`)
    REFERENCES `UKR_Database`.`Poster` (`idPoster`),
  CONSTRAINT `Translation_Language`
    FOREIGN KEY (`Translation_Language`)
    REFERENCES `UKR_Database`.`Translation_Languages` (`idTranslation_Languages`),
  CONSTRAINT `Translator_Name`
    FOREIGN KEY (`Translator`)
    REFERENCES `UKR_Database`.`Translator` (`idTranslator`))
ENGINE = InnoDB;

CREATE INDEX `Archivist_Name_idx` ON `UKR_Database`.`UKR_Poem_Details` (`Archivist_Name` ASC) VISIBLE;

CREATE INDEX `Translator_idx` ON `UKR_Database`.`UKR_Poem_Details` (`Translator` ASC) VISIBLE;

CREATE INDEX `Poster_Name_idx` ON `UKR_Database`.`UKR_Poem_Details` (`Poster_Name` ASC) VISIBLE;

CREATE INDEX `Author_Name_idx` ON `UKR_Database`.`UKR_Poem_Details` (`Author_Name` ASC) VISIBLE;

CREATE INDEX `Poem_Full_Text_idx` ON `UKR_Database`.`UKR_Poem_Details` (`Poem` ASC) VISIBLE;

CREATE INDEX `Translation_Language_idx` ON `UKR_Database`.`UKR_Poem_Details` (`Translation_Language` ASC) VISIBLE;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
