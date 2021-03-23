# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplay"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS song"
artist_table_drop = "DROP TABLE IF EXISTS artist"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = (""" CREATE TABLE IF NOT EXISTS 
                          songplays (songplay_id varchar, start_time Bigint, user_id varchar, level varchar, song_id varchar, artist_id varchar, session_id varchar, location varchar, user_agent varchar )""");

user_table_create = ("""CREATE TABLE IF NOT EXISTS
                      users (user_id varchar, first_name varchar, last_name varchar, gender varchar, level varchar)""");

song_table_create = ("""CREATE TABLE IF NOT EXISTS
                      songs (song_id varchar PRIMARY KEY, title varchar, artist_id varchar , year varchar, duration float)""");

artist_table_create = ("""CREATE TABLE IF NOT EXISTS
                        artists (artist_id varchar PRIMARY KEY, name varchar, location varchar, lattitude float, longitude float)""");

time_table_create = ("""CREATE TABLE IF NOT EXISTS
                      time (start_time timestamp, hour int, day int, week int, month int, year int, weekday int)""");

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO SONGPLAYS                            (songplay_id,start_time,user_id,level,song_id,artist_id,session_id,location,user_agent) 
VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
""")

user_table_insert = ("""INSERT INTO USERS (user_id,first_name,last_name,gender,level) VALUES (%s,%s,%s,%s,%s)
""")

song_table_insert = ("""INSERT INTO SONGS (song_id,title,artist_id,year,duration) VALUES (%s,%s,%s,%s,%s) ON CONFLICT(song_id) DO NOTHING """)

artist_table_insert = ("""INSERT INTO ARTISTS(artist_id,name,location,lattitude,longitude) VALUES (%s,%s,%s,%s,%s) ON CONFLICT(artist_id) DO NOTHING
""")


time_table_insert = ("""INSERT INTO TIME(start_time,hour,day,week,month,year,weekday) VALUES(%s,%s,%s,%s,%s,%s,%s)
""")

# FIND SONGS

#song_select = ("""SELECT SONG_ID,ARTIST_ID
#                   FROM SONGS 
#                   INNER JOIN ARTISTS 
#                   ON SONGS.ARTIST_ID = ARTISTS.ARTIST_ID""")

song_select = ("""
SELECT cast(s.song_id as varchar), cast(a.artist_id as varchar)
FROM songs s
INNER JOIN artists a ON s.artist_id = a.artist_id
WHERE s.title = (%s) AND a.name = (%s) AND cast(s.duration as float) = (%s);
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
