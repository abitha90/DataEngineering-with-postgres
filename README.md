#INTRODUCTION AND PURPOSE OF THE PROJECT:
       A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app.The aim of this project is to create a Postgres Database schema with tables designed to optimize queries for songplay analysis. Also to create ETL pipeline that transfers data from files in the local directories into fact and dimension tables created in star schema in Postgres using Python and Sql.
       

#RESULTS ACHIEVED:
       1. Data was extracted from the song and log files(json) from local directories.
       2. Tables are created in Postrgres in star schema
       3. Data was loaded successfully in to the created tables.
  #Tools and Packages used to achieve the result:
       1. Extract data from song and log files(json) - Pandas API
       2. Load Song data into Songs and Artist tables - Postgres Sql
       3. Analyze the log file and filter records by "NextSong" action and extract the timestamp,hours,day,week of year, year, week, month, weekday - Pandas dt attribute
       4. Provide appropriate column lables and create time dataframe -Pandas API
       5. Insert the time dataframe into time table- Postgres Sql
       6. Extract users data, create user dataframe and insert into table-Postgres Sql
       7. Form the single fact table songplays 
       
#TABLES AND SCHEMA:
   Using the song and data set create a star schema with fact and dimension tables optimized on songplay queries.
     #Fact Table
        1.songplays - records in log data associated with song plays i.e. records with page NextSong
           Columns: songplay_id, start_time, _id, level, song_id, artist_id, session_id, location, user_agent
     #Dimension Tables
       1.users - users in the app
          Columns:user_id, first_name, last_name, gender, level
       2.songs - songs in music database
          Columns: song_id, title, artist_id, year, duration
       3.artists - artists in music database
          Columns: artist_id, name, location, latitude, longitude
       4.time - timestamps of records in songplays broken down into specific units
          Columns: start_time, hour, day, week, month, year, weekday

#FILES:
create_tables.py - This file creates new database SparkifyDB and creates all the tables.
sql_queries.py - This file contains all the SQL statements used to create tables and insert data into all the tables.
etl.py - This file extracts the data from input files and load it into all the tables.
etl.ipynb - This notebook is used to test code in etl.py file.
test.ipynb - This notebook is used to test sql queries to verify the data loaded in the tables.

#STEPS:
1. Download all the files under FILES in the local
2. Open the command window
3. Run create_tables.py by typing python create_tables.py
4. After the successful run, run etl.py
5. Should run successfully.
6. Query the Database and check the tables for the values.

