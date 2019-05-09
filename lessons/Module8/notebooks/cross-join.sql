
-- Product table query
SELECT p.itemNumber, p.description FROM myProducts as p
    WHERE p.itemNumber == 5 ;
    
-- Display separator
SELECT '----------------------------------------' ;

-- Vendor table query

SELECT itemNumber, vendorName from myVendors
    WHERE vendorName NOT LIKE 'Luna%';
    
-- Display separator
SELECT '----------------------------------------' ;

-- Cross join query
SELECT p.itemNumber, p.description, v.itemNumber, v.vendorName
    FROM myVendors as v 
    CROSS JOIN myProducts as p 
    WHERE p.itemNumber == 5 AND
        v.vendorName NOT LIKE 'Luna%';
