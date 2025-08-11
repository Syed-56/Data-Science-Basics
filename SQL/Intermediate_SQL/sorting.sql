SELECT F_NAME, L_NAME, DEP_ID 
FROM EMPLOYEES
ORDER BY DEP_ID;
-- employess retreived with their order of ids

SELECT F_NAME, L_NAME, DEP_ID 
FROM EMPLOYEES
ORDER BY DEP_ID DESC, L_NAME DESC;
-- desc keyword means in descending order instead of ascending. Also this means that employess are sorted with decreasing dept_id but in those dept they also sorted with descending last name