# Database
 -  A database is an organized collection of structured information, or data, typically stored electronically in a computer system. A database is usually controlled by a database management system (DBMS). Together, the data and the DBMS, along with the applications that are associated with them, are referred to as a database system, often shortened to just database.
  Data within the most common types of databases in operation today is typically modeled in rows and columns in a series of tables to make processing and 
  data querying efficient. The data can then be easily accessed, managed, modified, updated, controlled, and organized. Most databases use 
  structured query language (SQL) for writing and querying data.
  
  To begin with, the table creation command requires the following details −

      Name of the table
      Name of the fields
      Definitions for each field

Syntax

Here is a generic SQL syntax to create a MySQL table −

    CREATE TABLE table_name (column_name column_type);

Now, we will create the following table in the TUTORIALS database.

create table tutorials_tbl(
       tutorial_id INT NOT NULL AUTO_INCREMENT,
       tutorial_title VARCHAR(100) NOT NULL,
       tutorial_author VARCHAR(40) NOT NULL,
       submission_date DATE,
       PRIMARY KEY ( tutorial_id )
      );

Here, a few items need explanation −

    Field Attribute NOT NULL is being used because we do not want this field to be NULL. So, if a user will try to create a record with a NULL value, then MySQL will raise an error.

    Field Attribute AUTO_INCREMENT tells MySQL to go ahead and add the next available number to the id field.

    Keyword PRIMARY KEY is used to define a column as a primary key. You can use multiple columns separated by a comma to define a primary key.
