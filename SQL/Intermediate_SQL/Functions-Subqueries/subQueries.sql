-- SELECT * FROM EMPLOYEES 
-- WHERE salary < AVG(salary);
-- this query wil not work bcz avg is a group function so we will use sub queries

SELECT *
FROM EMPLOYEES
WHERE SALARY < (SELECT AVG(SALARY) FROM EMPLOYEES);

-- if u want to print max salary in each row
SELECT EMP_ID, SALARY, (SELECT MAX(SALARY) FROM EMPLOYEES) AS MAX_SALARY 
FROM EMPLOYEES;

-- finding oldest employee
SELECT F_NAME, L_NAME
FROM EMPLOYEES
WHERE B_DATE = (SELECT MIN(B_DATE) FROM EMPLOYEES);

--pov: you are finding avg salary of the top 5 employees. so you group them decreasingly to limit 5 and then select avg(salary)
SELECT AVG(SALARY) 
FROM (SELECT SALARY 
      FROM EMPLOYEES 
      ORDER BY SALARY DESC 
      LIMIT 5) AS SALARY_TABLE;