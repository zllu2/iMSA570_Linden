
-- First we drop any tables if they exist

DROP TABLE IF EXISTS mySuppliers;
DROP TABLE IF EXISTS myProducts;

-- Suppliers Table
    
CREATE TABLE mySuppliers (
    supplierNumber INT NOT NULL,
    supplierName TEXT,
    PRIMARY KEY(supplierNumber)
) ;

-- Product Table
    
CREATE TABLE myProducts (
    itemNumber INT NOT NULL,
    price REAL,
    supplierNumber INT,
    stockDate TEXT,
    description TEXT,
    PRIMARY KEY(itemNumber),
    FOREIGN KEY(supplierNumber) REFERENCES mySuppliers(supplierNumber)
) ;
