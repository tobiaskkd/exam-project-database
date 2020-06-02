-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema Store
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema Store
-- -----------------------------------------------------
-- CREATE SCHEMA IF NOT EXISTS Store DEFAULT CHARACTER SET utf8 ;
-- USE Store ;

-- -----------------------------------------------------
-- Table Customers
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Customers (
  customer_id INT NOT NULL AUTO_INCREMENT,
  first_name VARCHAR(45) NOT NULL,
  middle_name VARCHAR(45) NOT NULL,
  last_name VARCHAR(45) NOT NULL,
  customer_phone VARCHAR(11) NOT NULL,
  customer_email VARCHAR(45) NOT NULL,
  customer_address VARCHAR(45) NOT NULL,
  PRIMARY KEY (customer_id))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table Store
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Store (
  store_id INT NOT NULL AUTO_INCREMENT,
  store_title VARCHAR(45) NOT NULL,
  store_address VARCHAR(45) NOT NULL,
  store_phone VARCHAR(45) NOT NULL,
  PRIMARY KEY (store_id))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table Employees
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Employees (
  employee_id INT NOT NULL AUTO_INCREMENT,
  first_name VARCHAR(45) NOT NULL,
  last_name VARCHAR(45) NOT NULL,
  employee_title VARCHAR(45) NOT NULL,
  employee_start_date VARCHAR(45) NOT NULL,
  employee_end_date DATETIME NULL,
  employee_salary DECIMAL(25) NOT NULL,
  employee_gender VARCHAR(45) NOT NULL,
  Store_store_id INT NOT NULL,
  PRIMARY KEY (employee_id),
  INDEX fk_Employee_Store1_idx (Store_store_id ASC) ,
  CONSTRAINT fk_Employee_Store1
    FOREIGN KEY (Store_store_id)
    REFERENCES Store (store_id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table Card
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Card (
  card_id INT NOT NULL AUTO_INCREMENT,
  card_number VARCHAR(45) NOT NULL,
  card_expire_date DATETIME NOT NULL,
  Customers_customer_id INT NOT NULL,
  PRIMARY KEY (card_id),
  UNIQUE INDEX card_number_UNIQUE (card_number ASC) ,
  INDEX fk_Card_Customers1_idx (Customers_customer_id ASC) ,
  CONSTRAINT fk_Card_Customers1
    FOREIGN KEY (Customers_customer_id)
    REFERENCES Customers (customer_id)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table Orders
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Orders (
  order_id INT NOT NULL AUTO_INCREMENT,
  order_placed DATETIME NOT NULL,
  total_order_price VARCHAR(45) NOT NULL,
  Employee_employee_id INT NOT NULL,
  Customers_customer_id INT NULL,
  Card_card_id INT NOT NULL,
  PRIMARY KEY (order_id),
  INDEX fk_Orders_Employee1_idx (Employee_employee_id ASC) ,
  INDEX fk_Orders_Customers1_idx (Customers_customer_id ASC) ,
  INDEX fk_Orders_Card1_idx (Card_card_id ASC) ,
  CONSTRAINT fk_Orders_Employee1
    FOREIGN KEY (Employee_employee_id)
    REFERENCES Employees (employee_id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_Orders_Customers1
    FOREIGN KEY (Customers_customer_id)
    REFERENCES Customers (customer_id)
    ON DELETE SET NULL
    ON UPDATE NO ACTION,
  CONSTRAINT fk_Orders_Card1
    FOREIGN KEY (Card_card_id)
    REFERENCES Card (card_id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table Supplier
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Supplier (
  supplier_id INT NOT NULL AUTO_INCREMENT,
  supplier_name VARCHAR(45) NOT NULL,
  supplier_phone VARCHAR(11) NOT NULL,
  PRIMARY KEY (supplier_id))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table Products
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Products (
  product_id INT NOT NULL AUTO_INCREMENT,
  product_name VARCHAR(45) NOT NULL,
  product_brand VARCHAR(45) NOT NULL,
  Supplier_supplier_id INT NOT NULL,
  product_stock INT NOT NULL,
  product_is_active TINYINT NOT NULL,
  PRIMARY KEY (product_id),
  INDEX fk_Products_Supplier1_idx (Supplier_supplier_id ASC) ,
  UNIQUE INDEX product_name_UNIQUE (product_name ASC) ,
  CONSTRAINT fk_Products_Supplier
    FOREIGN KEY (Supplier_supplier_id)
    REFERENCES Supplier (supplier_id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table Order_Delivery
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Order_Delivery (
  order_delivery_id INT NOT NULL AUTO_INCREMENT,
  delivery_status_code INT(3) NOT NULL,
  delivery_date DATETIME NOT NULL,
  Orders_order_id INT NOT NULL,
  PRIMARY KEY (order_delivery_id),
  INDEX fk_Order_Deliveries_Orders1_idx (Orders_order_id ASC) ,
  CONSTRAINT fk_Order_Deliveries_Orders1
    FOREIGN KEY (Orders_order_id)
    REFERENCES Orders (order_id)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table Campaigns
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Campaigns (
  campaign_id INT NOT NULL AUTO_INCREMENT,
  campaign_name VARCHAR(45) NOT NULL,
  campaign_discount INT NOT NULL,
  campaign_start_date DATETIME NOT NULL,
  campaign_end_date DATETIME NOT NULL,
  PRIMARY KEY (campaign_id))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table Orders_has_Products
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Orders_has_Products (
  Orders_order_id INT NOT NULL,
  Products_product_id INT NOT NULL,
  quantity INT NOT NULL,
  PRIMARY KEY (Orders_order_id, Products_product_id),
  INDEX fk_Orders_has_Products_Products1_idx (Products_product_id ASC) ,
  INDEX fk_Orders_has_Products_Orders1_idx (Orders_order_id ASC) ,
  CONSTRAINT fk_Orders_has_Products_Orders1
    FOREIGN KEY (Orders_order_id)
    REFERENCES Orders (order_id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_Orders_has_Products_Products1
    FOREIGN KEY (Products_product_id)
    REFERENCES Products (product_id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table Products_has_Campaigns
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Products_has_Campaigns (
  Products_product_id INT NOT NULL,
  Campaigns_campagn_id INT NOT NULL,
  PRIMARY KEY (Products_product_id, Campaigns_campagn_id),
  INDEX fk_Products_has_Campagns_Campagns1_idx (Campaigns_campagn_id ASC) ,
  INDEX fk_Products_has_Campagns_Products1_idx (Products_product_id ASC) ,
  CONSTRAINT fk_Products_has_Campagns_Products1
    FOREIGN KEY (Products_product_id)
    REFERENCES Products (product_id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_Products_has_Campagns_Campagns1
    FOREIGN KEY (Campaigns_campagn_id)
    REFERENCES Campaigns (campaign_id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table Prices
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Prices (
  price_id INT NOT NULL AUTO_INCREMENT,
  price_start_date DATETIME NOT NULL,
  price_end_date DATETIME NOT NULL,
  price FLOAT NOT NULL,
  Products_product_id INT NOT NULL,
  PRIMARY KEY (price_id),
  INDEX fk_Prices_Products1_idx (Products_product_id ASC) ,
  CONSTRAINT fk_Prices_Products1
    FOREIGN KEY (Products_product_id)
    REFERENCES Products (product_id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;


-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema supershop
-- -----------------------------------------------------
CREATE ROLE IF NOT EXISTS customer;

GRANT SELECT ON TABLE supershop.* TO customer;

CREATE ROLE IF NOT EXISTS manager;

GRANT ALL ON supershop.* TO manager;
GRANT SELECT, INSERT, TRIGGER ON TABLE supershop.* TO manager;
GRANT SELECT, INSERT, TRIGGER, UPDATE, DELETE ON TABLE supershop.* TO manager;

CREATE ROLE IF NOT EXISTS warehouseEmployee;

GRANT SELECT ON TABLE supershop.* TO warehouseEmployee;
GRANT SELECT, INSERT, TRIGGER ON TABLE supershop.* TO warehouseEmployee;

CREATE ROLE IF NOT EXISTS salesAssistant;

GRANT SELECT, INSERT, TRIGGER ON TABLE supershop.* TO salesAssistant;
GRANT SELECT ON TABLE supershop.* TO salesAssistant;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

FLUSH PRIVILEGES;
