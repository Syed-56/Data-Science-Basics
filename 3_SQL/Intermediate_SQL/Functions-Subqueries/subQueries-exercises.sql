-- Write a query to find the average salary of the five least-earning employees.
SELECT AVG(SALARY) FROM (
    SELECT SALARY FROM employees
    ORDER BY SALARY ASC
    LIMIT 5
)   AS MIN_AVG;

-- Write a query to find the records of employees older than the average age of all employees.
SELECT * FROM EMPLOYEES 
WHERE YEAR(FROM_DAYS(DATEDIFF(CURRENT_DATE,B_DATE))) > 
    (SELECT AVG(YEAR(FROM_DAYS(DATEDIFF(CURRENT_DATE,B_DATE)))) 
    FROM EMPLOYEES);
    -- we dont have age so wer caluclated it by finding days diff bw current and birth time

-- From the Job_History table, display the list of Employee IDs, years of service, and average years of service for all entries.
SELECT EMPL_ID, YEAR(FROM_DAYS(DATEDIFF(CURRENT_DATE,START_DATE))), (SELECT AVG(YEAR(FROM_DAYS(DATEDIFF(CURRENT_DATE,START_DATE)))) FROM Job_History) FROM Job_History;