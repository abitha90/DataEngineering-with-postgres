import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *


def process_song_file(cur, filepath):
    # open song file
    df = pd.read_json(filepath,typ='series')

    # insert song record
    song_data = df[["song_id","title","artist_id","year","duration"]]
    cur.execute(song_table_insert, song_data)
    
    # insert artist record
    artist_data = df[['artist_id','name','location','lattitude','longitude']]
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    # open log file
    log_files = get_files(filepath)
    df = pd.read_json(filepath,lines=True)
    df['ts'] = pd.to_datetime(df['ts'], unit='ms')

    # filter by NextSong action
    df_filtered_records = df[(df.page=="NextSong")]

    # convert timestamp column to datetime
    t = df_filtered_records.ts
    
    # insert time data records
    timestamp1=pd.to_datetime(df['ts'],unit='ms',errors='coerce')
    timestamp= timestamp1.to_frame()

    month1=pd.to_datetime(df['ts'],unit='ms',errors='coerce').dt.month
    month= month1.to_frame()

    year1=pd.to_datetime(df['ts'],unit='ms',errors='coerce').dt.year
    year= year1.to_frame()

    hour1=pd.to_datetime(df['ts'],unit='ms',errors='coerce').dt.hour
    hour= hour1.to_frame()

    day1=pd.to_datetime(df['ts'],unit='ms',errors='coerce').dt.day
    day= day1.to_frame()

    weekday1=pd.to_datetime(df['ts'],unit='ms',errors='coerce').dt.weekday_name
    weekday= weekday1.to_frame()

    dayofweek1=pd.to_datetime(df['ts'],unit='ms',errors='coerce').dt.dayofweek
    dayofweek= dayofweek1.to_frame()

    week1=pd.to_datetime(df['ts'],unit='ms',errors='coerce').dt.week
    week= week1.to_frame()
    time_df=pd.DataFrame(columns=['timestamp','hour','day','week','month,''year','weekday'])
    time_df= pd.concat([timestamp1,hour1,day1,week1,month1,year1,dayofweek1],axis=1)
    time_df.columns=['starttime','hour','day','week','month','year','weekday']
  

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_df = df[['userId','firstName','lastName','gender','level']]

    # insert user records
    for i, row in user_df.iterrows():
        try:
            cur.execute(user_table_insert, row)
        except psycopg2.DataError as de:
            print(f'Received DataError for i={i} and row={row}')
            raise de

    # insert songplay records
    for index, row in df.iterrows():
        
        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        
        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        # insert songplay record
        songplay_data = (index,row.ts,row.userId,row.level,songid,artistid,row.sessionId,row.location,row.userAgent)
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))

def get_files(filepath):
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))
    
    return all_files

def main():
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()