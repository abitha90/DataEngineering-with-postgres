INTRODUCTION AND PURPOSE OF THE PROJECT:
       A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app.The aim of this project is to create a Postgres Database schema with tables designed to optimize queries for songplay analysis. Also to create ETL pipeline that transfers data from files in the local directories into fact and dimension tables created in star schema in Postgres using Python and Sql.
       
RESULTS ACHIEVED:
       1. Data was extracted from the song and log files(json) from local directories.
       2. Tables are created in Postrgres in star schema
       3. Data was loaded successfully in to the created tables.
  Tools and Packages used to achieve the result:
       1. Extract data from song and log files(json) - Pandas API
       2. Load Song data into Songs and Artist tables - Postgres Sql
       3. Analyze the log file and filter records by "NextSong" action and extract the timestamp,hours,day,week of year, year, week, month, weekday - Pandas dt attribute
       4. Provide appropriate column lables and create time dataframe -Pandas API
       5. Insert the time dataframe into time table- Postgres Sql
       6. Extract users data, create user dataframe and insert into table-Postgres Sql
       7. Form the single fact table songplays 
       
Files:
create_tables.py - This file creates new database SparkifyDB and creates all the tables.
sql_queries.py - This file contains all the SQL statements used to create tables and insert data into all the tables.
etl.py - This file extracts the data from input files and load it into all the tables.
etl.ipynb - This notebook is used to test code in etl.py file.
test.ipynb - This notebook is used to test sql queries to verify the data loaded in the tables.

