use flask_database;
DELETE FROM flask_table WHERE flask_table.PrimaryID = 1;
DELETE FROM flask_table WHERE (flask_table.fname='fnameblah' and flask_table.PrimaryID > 0);
DROP table flask_table;
DROP Database flask_database;