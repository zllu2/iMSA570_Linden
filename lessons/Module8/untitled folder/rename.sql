.headers on

-- Create New table with extra column

CREATE TABLE newProducts (
    itemNumber INT NOT NULL,
    price REAL,
    stockDate TEXT,
    count INT NOT NULL DEFAULT 0,
    description TEXT
) ;

-- Now copy old table into new table

INSERT INTO newProducts(itemNumber, price, stockDate, description) 
    SELECT itemNumber, price, stockDate, description FROM myProducts ;

-- Drop old table
DROP TABLE myProducts ;

-- Now Rename new table to old table name
ALTER TABLE newProducts RENAME TO myProducts ;

-- Show the results
SELECT * FROM myProducts ;
