import psycopg2
from queue_module import creation_queue, deletion_queue, full_queue_time
from tasks import ConcreteTask as Task 
from dag import visualize_dag1, visualize_dag2, visualize_dag3 

'''
================Creating a Connection================
'''

def create_cursor(): #defines function
    credent = [] #creates empty list
    with open('.vscode/Credentials.txt') as file: #opens file with credentials 
      for line in file: #each line is a separate thing in the credentials file 
        line=line[0:-1] #i need each line without the /n at the end 
        credent.append(line) #adding it to the list
    conn = psycopg2.connect(host=credent[0],port=credent[1], dbname=credent[2],user=credent[3],password=credent[4]) #using psycopg2 to create a connection
    cur = conn.cursor() #creates cursor on the connection
    print("Connection Established") #prints that the connection is established 
    return cur, conn #returns cursor and connection objects that can be used later 
    
'''
================Creating a Connection================
'''

'''
================Runs given SQL statement on Given Connection================
'''
def run_sql(sql, cur, conn): 
    
    cur.execute(sql) #runs the given sql command
    conn.commit() #commits the sql command that was ran. 
    
'''
================Runs given SQL statement on Given Connection================
'''

'''
================Iterates Through SQL statements in sql_dimensions.txt file and uses run_sql funct================
'''
def create_dimension_tables(cur, conn):
    with open('Nara/sql_dimensions.txt') as file: #open the txt file that has a sql statement in every line
      for line in file: #for each line in the file 
        run_sql(line,cur,conn) #use the line as the sql statement to be run. 
    print("Dimension Tables Created") #after using the file and running all statements, prints Dimension Tables Created
'''
================Iterates Through SQL statements in sql_dimensions.txt file and uses run_sql funct================
'''

'''
================Iterates Through SQL statements in sql_aggregate.txt file and uses run_sql funct================
'''
def create_aggregated_table(cur, conn): 
  #identical to create_dimension_tables, just uses a different filepath
    with open('Nara/sql_aggregate.txt') as file: 
        for line in file: 
          run_sql(line, cur, conn)
    print("Aggregated Table Created")
'''
================Iterates Through SQL statements in sql_aggregate.txt file and uses run_sql funct================
'''
          
'''
================Iterates Through SQL statements in sql_breakdown_tables.txt file and uses run_sql funct================
'''
def breakdown_tables(cur, conn):
  #identical to create_dimension_tables, just uses a different filepath
  with open('Nara/sql_breakdown_tables.txt') as file: 
    for line in file: 
        run_sql(line, cur, conn)
  print("Tables Deleted")
'''
================Iterates Through SQL statements in sql_breakdown_tables.txt file and uses run_sql funct================
'''
'''
================Close Connection================
'''
def close_connection(cur, conn): #calling this function closes the connection
  cur.close() #closes the cursor first
  conn.close() #then closes the conn object
  print("Connection Closed") #prints the connection is closed 
'''
================Close Connection================
''' 

'''
================Assigning Tasks================
'''
#Tasks are created in tasks.py file and imported from there
#They are just assigned to variables so they can be used with .run()
create_conn = Task(create_cursor) 
create_dim = Task(create_dimension_tables)
create_agg = Task(create_aggregated_table) 
breakdown = Task(breakdown_tables)
close_conn = Task(close_connection)
'''
================Assigning Tasks================
'''
'''
================Creating Queues================
'''
create_queue = creation_queue() 
delete_queue = deletion_queue()
full_queue = full_queue_time(30)
'''
================Creating Queues================
'''


'''
================Creating DAGs================
'''
visualize_dag1() #creates a visualization of a dag for creating the tables
visualize_dag2() #creates a visualization of a dag for deleting the tables 
visualize_dag3() #creates a visualization of both dags together in one picture. 
'''
================Creating DAGs================
'''

def main() -> None: 
  
  
  
  
  
  
  
  """cur, conn = create_conn.run()
  create_dim.run(cur, conn)
  create_agg.run(cur, conn)
  #breakdown.run(cur, conn)
  close_conn.run(cur, conn)"""
  
  
  
if __name__ == "__main__": 
  main()

