--Write a query that displays the average cost of rescuing a single dog
SELECT AVG(COST/QUANTITY) FROM petrescue
WHERE ANIMAL = "Dog";

--Write a query that displays the animal name in each rescue in uppercase without duplication
SELECT DISTINCT UCASE(ANIMAL) FROM petrescue;

--Write a query that displays all the columns from the PETRESCUE table in lowercase where the animal(s) rescued are cats
SELECT * FROM petrescue
WHERE LCASE(ANIMAL) = "cat";

--Write a query that displays the number of rescues in the 5th month.
SELECT SUM(QUANTITY) FROM petrescue
WHERE MONTH(RESCUEDATE="05");

--The rescue shelter is supposed to find good homes for all animals within 1 year of their rescue. Write a query that displays the ID and the target date.
SELECT ID, DATE_ADD(RESCUEDATE, INTERVAL 1 YEAR) FROM petrescue;