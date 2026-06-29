--insert an entry with following values of thea attributes
INSERT INTO country_data(ins_id, lastname, firstname, city, country)
VALUES(10, 'Sultan', 'Syed', 'NewYork', 'US');
SELECT * FROM country_data

--upates the city element to utah for an object whose first name is syed
UPDATE country_data
SET city = "Utah"
WHERE firstname = "Syed";
SELECT * FROM country_data;

--we ran te insert 2 times so we got syed sultan inserted twice so we will be deleting 1
DELETE FROM country_data
WHERE ins_id = 10;
SELECT * FROM country_data;