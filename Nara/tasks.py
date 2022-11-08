import pandas as pd
import psycopg2
import networkx as nx
import json




#connect to dvdrental
def connect(): #should this return conn if it's a task? 
    
    conn=None
    
    try: 
        #create a variable from the settings.json file that can be called on in line 11 
        #parameters =
        conn = psycopg2.connect(host="localhost",database="dvdrental",user="postgres",password="sara")
        
        #creates cursor
        cur = conn.cursor()

        print ("Current Version: ")
        cur.execute('SELECT version()')

        db_version = cur.fetchone()
        print(db_version)
        
    except (Exception, psycopg2.DatabaseError) as error: 
        print(error)

def disconnect():
    print(conn)
    
    if conn is not None: 
        conn.close()
        print("Connection Terminated")
        
connect()

disconnect()


