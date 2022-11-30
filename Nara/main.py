import psycopg2
from tasks import ConcreteTask as Task

'''
================Creating a Connection================
'''

def create_cursor(): 
    credent = []
    with open('.vscode/Credentials.txt') as file:
      for line in file: 
        line=line[0:-1]
        credent.append(line)
    conn = psycopg2.connect(host=credent[0],port=credent[1], dbname=credent[2],user=credent[3],password=credent[4])
    cur = conn.cursor() #creates cursor
    print("Connection Established")
    return cur, conn #returns cursor
    
'''
================Creating a Connection================
'''

'''
================Runs SQL on Given Connection================
'''
def run_sql(sql, cur, conn):
    
    cur.execute(sql)
    conn.commit()
    #values = cur.fetchall()
    #return values 
'''
================Runs given SQL statement on Given Connection================
'''

'''
================Iterates Through SQL statements in sql_dimensions.txt file and uses run_sql funct================
'''
def create_dimension_tables(cur, conn):
    with open('Nara/sql_dimensions.txt') as file:
      for line in file: 
        run_sql(line,cur,conn)
    print("Dimension Tables Created")
'''
================Iterates Through SQL statements in sql_dimensions.txt file and uses run_sql funct================
'''
        
#create_dimension_tables(cur, conn) #just for me to test in the beginning
'''
================Iterates Through SQL statements in sql_aggregate.txt file and uses run_sql funct================
'''
def create_aggregated_table(cur, conn): 
    with open('Nara/sql_aggregate.txt') as file: 
        for line in file:
          run_sql(line, cur, conn)
    print("Aggregated Table Created")
'''
================Iterates Through SQL statements in sql_aggregate.txt file and uses run_sql funct================
'''
          
#create_aggregated_table(cur, conn) #just for me to test in the beginning
'''
================Iterates Through SQL statements in sql_breakdown_tables.txt file and uses run_sql funct================
'''
def breakdown_tables(cur, conn):
  with open('Nara/sql_breakdown_tables.txt') as file: 
    for line in file: 
        run_sql(line, cur, conn)
  print("Tables Deleted")
'''
================Iterates Through SQL statements in sql_breakdown_tables.txt file and uses run_sql funct================
'''

def close_connection(cur, conn): 
  cur.close()
  conn.close()
  print("Connection Closed")
            
#breakdown_tables(cur,conn) #deletes all tables in order so no errors occur. 

'''
================Assigning Tasks================
'''
create_conn = Task(create_cursor)
create_dim = Task(create_dimension_tables)
create_agg = Task(create_aggregated_table) 
breakdown = Task(breakdown_tables)
close_conn = Task(close_connection)
'''
================Assigning Tasks================
'''

def main() -> None: 
  cur, conn = create_conn.run()
  create_dim.run(cur, conn)
  create_agg.run(cur, conn)
  #breakdown.run(cur, conn)
  close_conn.run(cur, conn)
  
  
  
if __name__ == "__main__": 
  main()

