# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplay"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS song"
artist_table_drop = "DROP TABLE IF EXISTS artist"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = (""" CREATE TABLE IF NOT EXISTS songplays 
                          (songplay_id serial PRIMARY KEY NOT NULL, 
                           start_time timestamp NOT NULL, 
                           user_id integer NOT NULL, 
                           level varchar, 
                           song_id varchar, 
                           artist_id varchar, 
                           session_id varchar, 
                           location varchar, 
                           user_agent varchar
                           )
                           """);

user_table_create = ("""CREATE TABLE IF NOT EXISTS users 
                      (user_id integer PRIMARY KEY NOT NULL, 
                      first_name varchar, 
                      last_name varchar, 
                      gender varchar, 
                      level varchar
                      )""");

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs 
                      (song_id varchar PRIMARY KEY, 
                      title varchar NOT NULL, 
                      artist_id varchar NOT NULL, 
                      year varchar, 
                      duration float
                      )""");

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists 
                        (artist_id varchar PRIMARY KEY NOT NULL, 
                         name varchar NOT NULL, 
                         location varchar, 
                         lattitude float, 
                         longitude float
                         )""");

time_table_create = ("""CREATE TABLE IF NOT EXISTS time 
                       (start_time timestamp PRIMARY KEY NOT NULL, 
                        hour int, 
                        day int, 
                        week int, 
                        month int, 
                        year int, 
                        weekday int
                        )""");

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO SONGPLAYS                                                     
                          (start_time,
                           user_id,
                           level,
                           song_id,
                           artist_id,
                           session_id,
                           location,
                           user_agent) 
                          VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
                        """)

user_table_insert = ("""INSERT INTO USERS 
                       (user_id,
                        first_name,
                        last_name,
                        gender,
                        level) 
                        VALUES (%s,%s,%s,%s,%s)
                        ON CONFLICT (user_id) DO UPDATE SET level=EXCLUDED.level                         
                        """)

song_table_insert = ("""INSERT INTO SONGS
                      (song_id,
                       title,
                       artist_id,
                       year,
                       duration)
                       VALUES (%s,%s,%s,%s,%s)
                       ON CONFLICT(song_id) DO NOTHING 
                       """)

artist_table_insert = ("""INSERT INTO ARTISTS
                        (artist_id,
                         name,
                         location,
                         lattitude,
                         longitude) 
                         VALUES (%s,%s,%s,%s,%s) 
                         ON CONFLICT(artist_id) DO NOTHING
                        """)


time_table_insert = ("""INSERT INTO TIME
                      (start_time,
                      hour,
                      day,
                      week,
                      month,
                      year,
                      weekday)
                      VALUES(%s,%s,%s,%s,%s,%s,%s)
                      ON CONFLICT(start_time) DO NOTHING
                       """)

# FIND SONGS

#song_select = ("""SELECT SONG_ID,ARTIST_ID
#                   FROM SONGS 
#                   INNER JOIN ARTISTS 
#                   ON SONGS.ARTIST_ID = ARTISTS.ARTIST_ID""")

song_select = ("""SELECT s.song_id, a.artist_id
                 FROM songs s
                 INNER JOIN artists a ON s.artist_id = a.artist_id
                 WHERE s.title = (%s) AND a.name = (%s) 
                 AND cast(s.duration as float) = (%s) AND song_id is NOT NULL
                 AND a.artist_id is NOT NULL
               """)

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
