--retrieves whole table
SELECT * FROM mytable;   
 --retrieves mentioned columns from table
SELECT Title, Writer, Director FROM mytable; 

--retrieves columns wrt specified condition
SELECT Title, "Release Year", Locations FROM mytable WHERE "Release Year">=2001;    
--write is not james
SELECT Title, "Production Company", Locations, "Release Year" FROM mytable WHERE Writer<>"James Cameron";   