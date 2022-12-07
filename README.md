# dssa_dw_final_project_panens
This repository contains the final project for course DSSA 5102 - Data Gathering & Warehousing. 

## About Nara
Nara is a light python project that easily connects to a database, builds a small relational database in a separate schema, and breaks it down. The original database is querried by SQL statements, and relations between tables are set up using SQL statements as well. This project also allows the scheduler to automate this task for us and it implements the use of threads so other threads can be ran while the scheduler is active. 

## The Idea Behind Nara
Nara acts as a small data warehouse. Using a separate schema it creates a relational database that can then be used to interact with data in a faster way. Instead of using the ETL process that Extracts, Transforms, and Loads data in a traditional way, this project uses a python script to read SQL statements that do the ETL process far faster and cleaner. The process is separated into the following steps, or tasks: connect, create dimension tables, create aggregated table, breakdown tables, disconnect. The reason behind separating creating dimension tables, creating aggregated tables, and breaking down tables is so one can easily change which dimension tables are needed and which aggregated information one is looking for. Simply by adjusting the SQL statements in sql_dimensions.txt file and sql_aggregate.txt one can get just about any information the initial database has to offer. In addition, the schema is populated each morning at 09:00 am and broken down at 05:00pm so each morning the user will have the refreshed schema to work out of. In case an immediate refresh is needed, it could be done by manually executing the breakdown queue then the creation queue. Lastly, the scheduler does the work on thread 1, so other processes can be ran on the second thread if needed.

## Project Structure

*   `maellin` - This is the source code folder containing all application code and modules.
*   `DAGs` - Directed Acyclic Graph describing the workflow. 
*   `README` - Markdown file describing the project
*   `requirements.txt` - list of python libraries to install with `pip`
