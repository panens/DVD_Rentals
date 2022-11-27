import psycopg2
#from psycopg2.conninfo import make_conninfo
#from psycopg2.conninfo 


def create_cursor(): 
    with open('.vscode/MasterPassword.txt') as MasterPassword:
      MasterPass = MasterPassword.read()
    conn = psycopg2.connect(host="localhost",port="5432", dbname="dvdrental",user="postgres",password=MasterPass)
    cur = conn.cursor() #creates cursor
    return cur, conn #returns cursor
    

def run_sql(sql, cur, conn):
    
    cur.execute(sql)
    conn.commit()
    #values = cur.fetchall()
    #return values 

cur, conn = create_cursor()  

def create_dimension_tables(cur, conn):
    with open('Nara/sql_dimensions.txt') as file:
      for line in file: 
        run_sql(line,cur,conn)
        
create_dimension_tables(cur, conn)

def create_aggregated_table(cur, conn): 
    with open('Nara/sql_aggregate.txt') as file: 
        for line in file:
          run_sql(line, cur, conn)
          
create_aggregated_table(cur, conn) 

def breakdown_tables(cur, conn):
  with open('Nara/sql_breakdown_tables.txt') as file: 
    for line in file: 
        run_sql(line, cur, conn)
        
#breakdown_tables(cur,conn)

