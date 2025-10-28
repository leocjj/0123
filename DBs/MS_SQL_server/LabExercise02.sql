---------------------------------------------------------------------
-- LAB Module 2
--
-- Exercise 1
---------------------------------------------------------------------


USE AdventureWorks2019;
GO

---------------------------------------------------------------------
-- Task 1
-- 
-- Using SSMS, connect to your instance using Windows authentication (if you are connecting to an on-premises instance of SQL Server) or SQL Server authentication (if you are using SQL Azure).
--
-- In Object Explorer, expand the TSQL database and expand the Tables folder.
--
-- Take a look at the names of the tables in the Sales schema.
---------------------------------------------------------------------




---------------------------------------------------------------------
-- Task 2
-- 
-- Write a SELECT statement that will return all rows and all columns from the Sales.Customer table. 
-- Tip: You can use drag-and-drop functionality to drag items like table and column names from Object Explorer to the query window. Write the same SELECT statement using the drag-and-drop functionality.
--

---------------------------------------------------------------------
SELECT [CustomerID], [PersonID], [StoreID], [TerritoryID], [AccountNumber], [rowguid], [ModifiedDate] FROM [Sales].[Customer];



---------------------------------------------------------------------
-- Task 3
-- 
-- Expand the Sales.Customer table in Object Explorer and expand the Columns folder. Observe all columns in the table.
--
-- Write a SELECT statement to return the[CustomerID] ,[PersonID],[rowguid] columns.
--
--
-- What is the number of rows affected by the last query? (Tip: Because you are issuing a SELECT statement against the whole table, the number of rows will be the same as number of rows for the whole Sales.Customer table.)
--
---------------------------------------------------------------------
SELECT [CustomerID], [PersonID], [rowguid] FROM [Sales].[Customer];



---------------------------------------------------------------------
-- Task 4
-- 
-- Write a SELECT statement against the Sales.Person table showing only the TerritoryID column.
--
---------------------------------------------------------------------
SELECT [TerritoryID] FROM [Sales].[SalesPerson];



---------------------------------------------------------------------
-- Task 5
-- 
-- Copy the SELECT statement in Task 4 and modify it to return only distinct values.
--
-- Execute the written statement and export it to a File
--
---------------------------------------------------------------------
SELECT DISTINCT [TerritoryID] FROM [Sales].[SalesPerson];



-- Task 6
---------------------------------------------------------------------
-- Under which circumstances do the following queries against the Sales.Customer table return the same result?
--
-- Is the DISTINCT clause being applied to all columns specified in the query or just the first column?
--
-- A1: The following queries will return the same result only if we
-- have a unique value of StoreID for each row.
--
-- A2: The DISTINCT clause is being applied only to StoreID column.
---------------------------------------------------------------------

SELECT StoreID,TerritoryID 
FROM Sales.Customer;

SELECT DISTINCT StoreID,TerritoryID 
FROM Sales.Customer;


---------------------------------------------------------------------
-- Task 7
-- Write a  SELECT statement to display the Type of Person based on the table [Person].[Person]
--adding a CASE expression that generates a result column named Person Type  using the next values: 
--"EM": Employee,
--"IN": Individual,
--SP = Sales person, 
--any other type:Other type   
--The new column should hold the translation of the Person Type to its respective Person Type, based on the mapping table supplied . 
--Use the value “Other” for any Type not found in the mapping table.
---------------------------------------------------------------------