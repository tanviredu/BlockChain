-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `GlobalSuperStore` DEFAULT CHARACTER SET utf8 ;
USE `GlobalSuperStore` ;

-- -----------------------------------------------------
-- Table `mydb`.`Address`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `GlobalSuperStore`.`Address` (
  `AddressID` INT NOT NULL AUTO_INCREMENT,
  `City` VARCHAR(45) NULL,
  `State` VARCHAR(45) NULL,
  `Country` VARCHAR(45) NULL,
  `PostalCode` INT NULL,
  PRIMARY KEY (`AddressID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Customer`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `GlobalSuperStore`.`Customer` (
  `CustomerID` INT NOT NULL AUTO_INCREMENT,
  `CustomerName` VARCHAR(45) NULL,
  `ContactDetails` VARCHAR(45) NULL,
  PRIMARY KEY (`CustomerID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `GlobalSuperStore`.`Subcategory`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `GlobalSuperStore`.`Subcategory` (
  `SubcategoryID` INT NOT NULL AUTO_INCREMENT,
  `Name` VARCHAR(45) NULL,
  PRIMARY KEY (`SubcategoryID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `GlobalSuperStore`.`Category`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `GlobalSuperStore`.`Category` (
  `CategoryID` INT NOT NULL AUTO_INCREMENT,
  `Name` VARCHAR(45) NULL,
  `SubcategoryID` INT NULL,
  PRIMARY KEY (`CategoryID`),
  INDEX `fk_Category_subcategory_idx` (`SubcategoryID` ASC) VISIBLE,
  CONSTRAINT `fk_Category_subcategory`
    FOREIGN KEY (`SubcategoryID`)
    REFERENCES `GlobalSuperStore`.`Subcategory` (`SubcategoryID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `GlobalSuperStore`.`Product`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `GlobalSuperStore`.`Product` (
  `ProductID` INT NOT NULL AUTO_INCREMENT,
  `Name` VARCHAR(45) NULL,
  `Price` DECIMAL NULL,
  `CategoryID` INT NULL,
  PRIMARY KEY (`ProductID`),
  INDEX `fk_product_category_idx` (`CategoryID` ASC) VISIBLE,
  CONSTRAINT `fk_product_category`
    FOREIGN KEY (`CategoryID`)
    REFERENCES `GlobalSuperStore`.`Category` (`CategoryID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `GlobalSuperStore`.`Shipment`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `GlobalSuperStore`.`Shipment` (
  `ShipmentID` INT NOT NULL AUTO_INCREMENT,
  `ShipmentMode` VARCHAR(45) NULL,
  `ShipmentCost` DECIMAL(2,1) NULL,
  `ShipmentDate` DATE NULL,
  `AddressID` INT NULL,
  PRIMARY KEY (`ShipmentID`),
  INDEX `fk_shipment_address_idx` (`AddressID` ASC) VISIBLE,
  CONSTRAINT `fk_shipment_address`
    FOREIGN KEY (`AddressID`)
    REFERENCES `GlobalSuperStore`.`Address` (`AddressID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `GlobalSuperStore`.`Order`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `GlobalSuperStore`.`Order` (
  `OrderID` INT NOT NULL AUTO_INCREMENT,
  `OrderDate` DATETIME NULL,
  `Quantity` INT NULL,
  `TotalCost` DECIMAL(2,1) NULL,
  `Discount` DECIMAL(2,1) NULL,
  `OrderPriority` INT NULL,
  `CustomerID` INT NULL,
  `ProductID` INT NULL,
  `ShippingID` INT NULL,
  PRIMARY KEY (`OrderID`),
  INDEX `fk_order_customer_idx` (`CustomerID` ASC) VISIBLE,
  INDEX `fk_Order_product_idx` (`ProductID` ASC) VISIBLE,
  INDEX `fk_Order_shipping_idx` (`ShippingID` ASC) VISIBLE,
  CONSTRAINT `fk_order_customer`
    FOREIGN KEY (`CustomerID`)
    REFERENCES `GlobalSuperStore`.`Customer` (`CustomerID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_Order_product`
    FOREIGN KEY (`ProductID`)
    REFERENCES `GlobalSuperStore`.`Product` (`ProductID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_Order_shipping`
    FOREIGN KEY (`ShippingID`)
    REFERENCES `GlobalSuperStore`.`Shipment` (`ShipmentID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
