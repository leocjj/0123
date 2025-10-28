---------------------------------------------------------------------
-- Module 02
--
-- Exercise 1
---------------------------------------------------------------------

USE AdventureWorks2019;
GO


-- Task 1
-- 
-- Execute the script by clicking Execute on the toolbar (or press F5 on the keyboard). 
-- This will execute the whole script.
--
-- Observe the result and the database context. 
--
-- Which database is selected in the Available Databases box?
--
-- A: AdventureWorks2019
---------------------------------------------------------------------

SELECT   [NameStyle]
		,[Title] 
		,[FirstName]
		,[MiddleName]
		,[LastName]
		,[Suffix]
		,[EmailPromotion]
FROM Person.Person

---------------------------------------------------------------------
-- Task 2
-- 
-- Highlight the SELECT statement in the T-SQL script under the task 1 
-- description and click Execute.
--
-- Observe the result. You should get the same result as in task 1. 
--
-- Tip: One way to highlight a portion of code is to hold down the Alt
-- key while drawing a rectangle around it with your mouse. The code inside 
-- the drawn rectangle will be selected. Try it.
--
-- A: same result as task 1
---------------------------------------------------------------------
---------------------------------------------------------------------
-- Task 3
-- 
-- Observe the results. Why is the result window empty?
--
-- A: if the questions means why there is an error if delete comment
-- simbols from the following lines and execute the code, it is
-- because there is a misplaced semicolon at the end of the 'WHERE'.
-- Deleting this semicolon, code executed successfully and throws
-- 5044 rows instead of 19972 rows in Task 1.
---------------------------------------------------------------------


SELECT  [NameStyle]
		,[Title] 
		,[FirstName]
		,[MiddleName]
		,[LastName]
		,[Suffix]
		,[EmailPromotion]
FROM Person.Person
WHERE	EmailPromotion =1
ORDER BY lastname;
