USE alx_book_store;

-- task_4.sql
SELECT 
       COLUMN_NAME,
       COLUMN_TYPE,
       
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'alx_book_store' 
  AND TABLE_NAME = 'Books';
