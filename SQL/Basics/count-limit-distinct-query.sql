--retreives number of rows in table
SELECT COUNT(*) FROM mytable;
--retreieves number of rows where write is james cameron
SELECT COUNT(Locations) FROM mytable WHERE Writer="James Cameron";    

--retrieves unique titles from the table
SELECT DISTINCT Title FROM mytable;
--retrieves number of unique release years where production company is warner-bros
SELECT COUNT(DISTINCT "Release Year") FROM mytable WHERE "Production Company"="Warner Bros. Pictures";

--retrieves first 25 rows
SELECT * FROM mytable LIMIT 25;
--retrieves 15 rows starting from 10th row
SELECT * FROM mytable LIMIT 15 OFFSET 10;