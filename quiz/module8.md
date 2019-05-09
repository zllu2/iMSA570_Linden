Format:
Question: ...  
Type: Multiple Choice (Single Correct Answer),  Multiple Choice (Multiple Correct Answers), Free Response (Text Answers, Code Expression)
Answer: ...  
Choices: ...  

# Lesson 1
- Question 1.1: In RDBMS operations, either all operations are performed successfully or none of them are performed. What is this feature called?
  - Type: Multiple Choice (Single Correct Answer)
  - Answer: Atomicity
  - Choices: Atomicity; Consistency; Isolation; Durability
- Question 1.2: In RDBMS system, only valid data are written to the database. What is this feature called?
  - Type: Multiple Choice (Single Correct Answer)
  - Answer: Consistency
  - Choices: Atomicity; Consistency; Isolation; Durability
- Question 2.1: In RDBMS system, independent sets of database transactions are performed in such a way that they don't conflict with each other. What is this feature called?
  - Type: Multiple Choice (Single Correct Answer)
  - Answer: Isolation
  - Choices: Atomicity; Consistency; Isolation; Durability
- Question 2.2: In RDBMS system, database is safe against unexpected terminations. What is this feature called?
  - Type: Multiple Choice (Single Correct Answer)
  - Answer: Durability
  - Choices: Atomicity; Consistency; Isolation; Durability

- Question 3.1: True or False? SQLite is an ACID-compliant database.
  - Type: Multiple Choice (Single Correct Answer)
  - Answer: True
  - Choices: True, False
- Question 3.1: True or False? SQLite has datetime data type.
  - Type: Multiple Choice (Single Correct Answer)
  - Answer: False
  - Choices: True, False

# Lesson 2
- Question 4.1: True or False? Primary key must be unique.
  - Type: Multiple Choice (Single Correct Answer)
  - Answer: True
  - Choices: True, False
- Question 4.2: True or False? Values in a column that has foreign key constraint must be unique.
  - Type: Multiple Choice (Single Correct Answer)
  - Answer: False
  - Choices: True, False

- Question 5.1: Only those rows that share a common value in a specific column in both tables are combined in the final joined table. What is this kind of join?
  - Type: Multiple Choice (Single Correct Answer)
  - Answer: inner join
  - Choices: inner join; left outer join; right outer join; outer join

- Question 5.2: All rows from left table are placed into the joined table, and an inner join is performed with right table. Any row in the new table that does not have a match in right is padded with null values. What is this kind of join?
  - Type: Multiple Choice (Single Correct Answer)
  - Answer: left outer join
  - Choices: inner join; left outer join; right outer join; outer join


- Question 6.1: If you want to insert data into a table which SQL statement should you use?
  - Type: Multiple Choice (Single Correct Answer)
  - Answer: INSERT INTO
  - Choices: INSERT INTO; WRITE; APPEND; UPDATE;
- Question 6.2: If you want to delete some data from a table which SQL statement should you use?
  - Type: Multiple Choice (Single Correct Answer)
  - Answer: DELETE
  - Choices: DEL; DELETE; REMOVE; CLEAR
- Question 6.3: If you want to modify some data in a table which SQL statement should you use?
  - Type: Multiple Choice (Single Correct Answer)
  - Answer: UPDATE
  - Choices: INSERT INTO; WRITE; APPEND; UPDATE;

- Question 7.1: Which python module deal with SQLite database?
  - Type: Multiple Choice (Single Correct Answer)
  - Answer: sqlite3
  - Choices: sqlite3; sqlite; sql
- Question 7.2: Which sqlite3 function returns a SQLite database connection?
  - Type: Multiple Choice (Single Correct Answer)
  - Answer: connect()
  - Choices: connection(); connect(); read_sql()

- Question 8.1: Which pandas function load a dataframe from a database with a SQL query?
  - Type: Multiple Choice (Single Correct Answer)
  - Answer: read_sql()
  - Choices: read_database(); read_sql(); load_sql(); to_sql()
- Question 8.2: Which pandas DataFrame function write a dataframe into a database?
  - Type: Multiple Choice (Single Correct Answer)
  - Answer: to_sql()
  - Choices: write_database(); write_sql(); dump_sql(); to_sql()

- Question 9.1: When calling DataFrame function to_sql() to write a dataframe into database, which function argument setting prevents from writing dataframe index as a column?
  - Type: Multiple Choice (Single Correct Answer)
  - Answer: index=False
  - Choices: index=False; index=True; as_index=False; as_index=True
- Question 9.2: When calling DataFrame function to_sql() to write a dataframe into database, which function argument setting will write dataframe index as a column?
  - Type: Multiple Choice (Single Correct Answer)
  - Answer: index=True
  - Choices: index=False; index=True; as_index=False; as_index=True

- Question 10.1: When calling DataFrame function to_sql() to write a dataframe into database, if the table already exists, which function argument setting raises a ValueError?
  - Type: Multiple Choice (Single Correct Answer)
  - Answer: if_exists='fail'
  - Choices: if_exits='fail'; if_exits='append'; if_exists='replace'
- Question 10.2: When calling DataFrame function to_sql() to write a dataframe into database, if the table already exists, which function argument setting inserts new values to the existing table?
  - Type: Multiple Choice (Single Correct Answer)
  - Answer: if_exists='append'
  - Choices: if_exits='fail'; if_exits='append'; if_exists='replace'
- Question 10.3: When calling DataFrame function to_sql() to write a dataframe into database, if the table already exists, which function argument setting drops the table first then creates new table and inserts the values?
  - Type: Multiple Choice (Single Correct Answer)
  - Answer: if_exists='replace'
  - Choices: if_exits='fail'; if_exits='append'; if_exists='replace'
