-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema dojosandninjas
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `dojosandninjas` ;

-- -----------------------------------------------------
-- Schema dojosandninjas
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `dojosandninjas` DEFAULT CHARACTER SET utf8 ;
USE `dojosandninjas` ;

-- -----------------------------------------------------
-- Table `dojosandninjas`.`Dojos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dojosandninjas`.`Dojos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dojosandninjas`.`Ninjas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dojosandninjas`.`Ninjas` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `age` INT NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `Dojos_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_Ninjas_Dojos_idx` (`Dojos_id` ASC) VISIBLE,
  CONSTRAINT `fk_Ninjas_Dojos`
    FOREIGN KEY (`Dojos_id`)
    REFERENCES `dojosandninjas`.`Dojos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
