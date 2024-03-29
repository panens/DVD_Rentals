## About Nara
Nara is a light python project that easily connects to a database, builds a small relational database in a separate schema, and breaks it down. The original database is querried by SQL statements, and relations between tables are set up using SQL statements as well. This project also allows the scheduler to automate this task for us and it implements the use of threads so other threads can be ran while the scheduler is active. 

## The Idea Behind Nara
Nara acts as a small data warehouse. Using a separate schema it creates a relational database that can then be used to interact with data in a faster way. Instead of using the ETL process that Extracts, Transforms, and Loads data in a traditional way, this project uses a python script to read SQL statements that do the ETL process far faster and cleaner. The process is separated into the following steps, or tasks: connect, create dimension tables, create aggregated table, breakdown tables, disconnect. The reason behind separating creating dimension tables, creating aggregated tables, and breaking down tables is so one can easily change which dimension tables are needed and which aggregated information one is looking for. Simply by adjusting the SQL statements in sql_dimensions.txt file and sql_aggregate.txt one can get just about any information the initial database has to offer. In addition, the schema is populated each morning at 09:00 am and broken down at 05:00pm so each morning the user will have the refreshed schema to work out of. In case an immediate refresh is needed, it could be done by manually executing the breakdown queue then the creation queue. Lastly, the scheduler does the work on thread 1, so other processes can be ran on the second thread if needed.

## Project Structure

*   `Nara` - This is the source code folder containing all application code and modules.
    1. `main.py` contains the main code for execution of the code as well as base functions that are called
    2. `tasks.py` This module has contains the ConcreteTask class
    3. `queue_module.py` This module defines a create_queue function that creates a queue from given tasks
    4. `worker.py` This module creates a function that executes all the tasks in a given queue. 
    5. `dag.py` creates a DAG based on nodes and edges given and saves the graph under the DAGs folder
    6. `sql_dimensions.txt` Text file with SQL statements used to create and alter dimension tables
    7. `sql_aggregate.txt` Text file with SQL statements used to create and alter aggregate table(s)
    8. `sql_breakdown_tables.txt` Text file with SQL statements used to breakdown all tables
*   `DAGs` - Directed Acyclic Graph describing the workflow. 
*   `README` - Markdown file describing the project
*   `requirements.txt` - list of python libraries to install with `pip`

## Data Practicum Project 2023/07/16 edit

## The Practicum Project Idea
Nara code from main.py was slightly edited and saved as practicum.py. The code changes are reflected mainly in the data that is getting pulled from the database and it is stored in a new schema - practicum. Using a separate schema it creates a separate storage place for the table to be accessed by the PowerBI. It also allows to interact with data in a faster way. Instead of using the ETL process that Extracts, Transforms, and Loads data in a traditional way, this project uses a python script to read SQL statements that do the ETL process far faster and cleaner. The process is separated into the following steps, or tasks: connect, create payments table,breakdown table, and disconnect. If the potential sales team would like to include any additional data that becomes available, this can be simply done by adjusting the SQL statements in sql_practicum_dimension.txt file. In addition, the schema is populated each morning at 09:00 am and broken down at 09:30pm so each morning the user will have the refreshed schema to work out of. The PowerBI report that runs of this data is set to refresh at 9:10, but in case of large volume of data, it is easy to adjust these times. In case an immediate refresh is needed, it could be done by manually executing the queue and manually refreshing the PowerBI report. Lastly, the scheduler works on thread 1, so other processes can be ran on the second thread if needed. If set to thread 2, this process can run concurently with the thread 1 initially created for the nara project. 

## Structural Edits

*   `Nara` 
    1. `practicum.py` - New python file that contains the main code for execution for the Data Practicum Project
    2. `sql_practicum_dimension.txt` Text file with SQL statements used to create the required table in practicum schema
    3. `sql_practicum_breakdown.txt` Text file with SQL statement used to delete the table created in the practicum schema
*   `Dashboard` - New Folder
    1. `Sales Performance Dashboard.png` - Screenshot of how the completed dashboard looks after a refresh. 

