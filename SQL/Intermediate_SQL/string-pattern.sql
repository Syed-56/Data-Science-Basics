SELECT F_NAME, L_NAME, ADDRESS
FROM EMPLOYEES
WHERE ADDRESS LIKE '%Elgin,IL%';
-- look using where address = "elgin IL" will only return employee with exact address elgin il but we have stored address like 2134 street elgin,il so we want the employees in city elgin so we use this string pattern

SELECT F_NAME, L_NAME, B_DATE
FROM EMPLOYEES
WHERE B_DATE LIKE '197%';
-- this will return employees born in 70s, here we use % wildcard in end because we have to find employees who have any value after 7 but note with 19 because we are talking abt 1970s. If we also used % in start it can also return employees from 2070