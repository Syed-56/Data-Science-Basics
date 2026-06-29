-- Retrieve the list of all employees, first and last names, whose first names start with ‘S’
SELECT F_NAME, L_NAME FROM employees
WHERE F_NAME LIKE "S%";

-- Arrange all the records of the EMPLOYEES table in ascending order of the date of birth.
SELECT * FROM employees
ORDER BY B_DATE;

-- Group the records in terms of the department IDs and filter them of ones that have average salary more than or equal to 60000. Display the department ID and the average salary. Sort result by decreasing avg salary
SELECT DEP_ID, COUNT(*) AS "Department-ID", AVG(SALARY) as "Average-Salary" FROM employees
GROUP BY DEP_ID
HAVING AVG(SALARY) >= 60000
ORDER BY AVG(SALARY) DESC;