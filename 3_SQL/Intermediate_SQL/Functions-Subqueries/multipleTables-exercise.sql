-- Retrieve only the list of employees whose JOB_TITLE is Jr. Designer.
SELECT * FROM EMPLOYEES
WHERE JOB_ID IN (
    SELECT JOB_IDENT FROM JOBS
    WHERE JOB_TITLE = "Jr. Designer"
);

-- using full join, upper example was using sub-queries
SELECT * FROM employees E, jobs J
WHERE E.JOB_ID = J.JOB_IDENT AND J.JOB_TITLE = "Jr. Designer";

-- Retrieve JOB information and a list of employees whose birth year is after 1976.
SELECT * FROM jobs
WHERE JOB_IDENT IN (
    SELECT JOB_ID FROM employees
    WHERE YEAR(B_DATE) > 1976
);

SELECT * FROM jobs J, employees E
WHERE J.JOB_IDENT = E.JOB_ID AND YEAR(E.B_DATE) > 1976;