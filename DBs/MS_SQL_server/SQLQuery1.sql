/* long comment
*/
-- In line comment

use AdventureWorks2019	-- use db_name
--go
begin
	declare @var1 int=10
	set @var1 = 1
	select @var1
end
go  -- Batch separator. go 10 repeats ten times the batch.
-- each batch can run in parallel, if not used, sentences run serially.
begin
	declare @var1 varchar(4) = 'Hola'
	select @var1
end
begin transaction Demo	-- For data update only, not select.
	--insert/update/delete 
commit transaction Demo

/*
SELECT ...	--
FROM Sales.Orders
WHERE city = 'Berlin'
GROUP BY
HAVING  -- filtro del group by
ORDER BY

cast(col1 as int)	-- Explicit conversion is better than implicit
*/

select distinct Country from Sales.Orders

SELECT ...,
	CASE discontinued
		WHEN 0 THEN 'Active'
		WHEN 1 THEN 'Discontinued'
	END AS [status]
FROM ...