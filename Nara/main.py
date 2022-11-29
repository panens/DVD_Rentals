import psycopg2
#from psycopg2.conninfo import make_conninfo
#from psycopg2.conninfo 


def create_cursor(): 
    credent = []
    with open('.vscode/Credentials.txt') as file:
      for line in file: 
        line=line[0:-1]
        credent.append(line)
    print(credent)
    conn = psycopg2.connect(host=credent[0],port=credent[1], dbname=credent[2],user=credent[3],password=credent[4])
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
        
#breakdown_tables(cur,conn) #deletes all tables in order so no errors occur. 

