import psycopg2
from queue_module import create_queue
from tasks import ConcreteTask as Task
from worker import execute_queue
import schedule 
import time
import threading

'''
================Creating a Connection================
'''
def create_cursor(): #defines function
    '''Opens a connection.
    Args: 
      None, but takes in values from Credentials.txt
      
    Returns: 
      cur object that can be used later for executing SQL querries on the database
      conn objects that can be used later to commit executed SQL querries to the database 
    '''
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
    '''Executes and commits an SQL Statement stored as a string
    Args: 
      sql (str): SQL statement as string to be executed
      cur (object): cursor object that executes the SQL statement
      conn (object): connection object that commits the executed SQL statement
    '''
    
    cur.execute(sql) #runs the given sql command
    conn.commit() #commits the sql command that was ran. 
'''
================Runs given SQL statement on Given Connection================
'''

'''
================Iterates Through SQL statements in sql_practicum_dimensions.txt file and uses run_sql funct================
'''
def create_table(cur, conn):
  '''Creates dimension tables
    Args: 
      cur (object): cursor object that executes the SQL statement
      conn (object): connection object that commits the executed SQL statement
    
    The function will execute all statements in the sql_practicum_dimensions.txt file per line
  '''
  with open('Nara/sql_practicum_dimensions.txt') as file: #open the txt file that has a sql statement in every line
    for line in file: #for each line in the file 
      run_sql(line,cur,conn) #use the line as the sql statement to be run. 
  print("Table Created") #after using the file and running all statements, prints Dimension Tables Created
'''
================Iterates Through SQL statements in sql_practicum_dimensions.txt file and uses run_sql funct================
'''

'''
================Iterates Through SQL statements in sql_practicum_delete.txt file and uses run_sql funct================
'''
def breakdown_table(cur, conn):
  '''Deletes all tables
    Args: 
      cur (object): cursor object that executes the SQL statement
      conn (object): connection object that commits the executed SQL statement
    
    The function will execute all statements in the sql_practicum_delete.txt file
  '''
  
  with open('Nara/sql_practicum_delete.txt') as file: 
    for line in file: 
        run_sql(line, cur, conn)
  print("Table Deleted")
'''
================Iterates Through SQL statements in sql_practicum_delete.txt file and uses run_sql funct================
'''

'''
================Close Connection================
'''
def close_connection(cur, conn): #calling this function closes the connection
  '''Closes the connection
    Args: 
      cur (object): cursor object that will close
      conn (object): connection object that will close
  '''
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
create_dim = Task(create_table)
breakdown = Task(breakdown_table)
close_conn = Task(close_connection)
'''
================Assigning Tasks================
'''

'''
================Creating Queues================
'''
#Calls on the creqte_queue function from the queue module. 
instanciate_queue = create_queue(create_conn,create_dim,close_conn)
breakdown_queue = create_queue(create_conn,breakdown,close_conn)
'''
================Creating Queues================
'''

'''
================Creating a Schedule================
'''

#The following 2 lines ensure that every day all tables get created at 9:00am, and they get broken down at 9:30am
schedule.every().day.at("09:00").do(execute_queue, instanciate_queue)
schedule.every().day.at("09:30").do(execute_queue, breakdown_queue)

def working_hours():
  while True:
      schedule.run_pending()
      time.sleep(1)
      
def concurent():
  time.sleep(40)
  print("In case a concurent thread is needed, code can be written in this block")

t1 = threading.Thread(target=working_hours)

t2 = threading.Thread(target=concurent)

'''
================Creating a Schedule================
'''

def main() -> None: 
  t1.start() #runs first thread that runs the schedule working_hours 
  t2.start() #runs second thread that has the concurent function in it 

  
  
if __name__ == "__main__": 
  main()

