import pandas as pd
import psycopg2
import networkx as nx
import json




#connect to dvdrental
#should this have conn as input in main? (so I can close at the end of main)

def connect(): 
    
    conn=None
    
    try: 
        #create a variable from the settings.json file that can be called on in line 11 
        #parameters =
        conn = psycopg2.connect(host="localhost",database="dvdrental",user="postgres",password="sara")
        
        cur = conn.cursor() #creates cursor
        
        return cur #returns cursor


        #i just used the following to see if cursor was working before adding return cur
        #print ("Current Version: ") 
        #cur.execute('SELECT version()') 
        #db_version = cur.fetchone() cursor catches the value of version and puts it into variable 
        #print(db_version) #prints out variable that has version stored
        
    except (Exception, psycopg2.DatabaseError) as error: 
        print(error)

'''
#Used to check if it works outside the function
print("outside connect")
cur=connect()
cur.execute('SELECT version()')
db_version = cur.fetchone()
print(db_version)
'''

#this provides the right SQL to be executed, but it does not show up when ran. 
#I tried ending it with ; or / and it did not help
#I have the dssa schema manually created through dvdrental.session.sql file, but this would be a neat option to create it 
'''def create_schema(name:str): so cursor can use selects, but not create things?
    
    #sqldelete = f"DROP SCHEMA IF EXISTS {name};"
    #cur.execute(sqldelete) 
    #cur = connect()
    #sqlcreate = f"CREATE SCHEMA IF NOT EXISTS {name}"
    #print(sqlcreate)
    #cur.execute(sqlcreate)

#create_schema("test") 

#ask how to use the cursor to execute querries on the database. 
#Extraction would be lead by all the following SQL statements. 
#Confused on what I would be counting under count_rentals, wouldn't there be just 1 count that is the same for all 5 dimensions? 
#how to store these SQL statements in a df? '''

#Table creation before extraction? 

'''EXTRACTION'''

# some good notes for tomorrow https://www.dataquest.io/blog/sql-insert-tutorial/

def values(): #should change it to take in sql string as input so it can be used for each table
    cur=connect()
    sqltest = "SELECT staff_id as sk_staff, CONCAT(first_name, ' ', last_name) as name, email from staff"
    cur.execute(sqltest)
    values = cur.fetchall()
    #https://www.dataquest.io/blog/sql-insert-tutorial/
    return values


customers = values() #this is returned as list of tuples 

def header(): #should take the sql as input as well. 
    cur=connect()
    sqltest = "SELECT staff_id as sk_staff, CONCAT(first_name, ' ', last_name) as name, email from staff"
    cur.execute(sqltest)
    #https://www.geeksforgeeks.org/creating-a-pandas-dataframe-using-list-of-tuples/.
    headers = [i[0] for i in cur.description]
    return headers

headers = header()
print(headers)
print(customers) 

df = pd.DataFrame(customers, columns = headers) #Create a task out of this that calls previous 2 tasks within it. 
print(df)
    


print(type(customers[1]))

"""SELECT 
COUNT (rental_id),
(SELECT customer_id as sk_customer FROM customer where customer_id = rental.customer_id), 
rental_date as sk_date, 
(SELECT store_id as sk_store FROM store where store_id = (SELECT store_id from inventory where inventory_id = rental.inventory_id)), 
(SELECT film_id as sk_film FROM film where film_id = (SELECT film_id from inventory where inventory_id = rental.inventory_id)),
(SELECT staff_id as sk_staff FROM staff where staff_id = rental.staff_id)
from rental 
GROUP BY """

'''
#Fact_rentals
SELECT 
rental_id,
(SELECT customer_id as sk_customer FROM customer where customer_id = rental.customer_id), 
rental_date as sk_date, 
(SELECT store_id as sk_store FROM store where store_id = (SELECT store_id from inventory where inventory_id = rental.inventory_id)), 
(SELECT film_id as sk_film FROM film where film_id = (SELECT film_id from inventory where inventory_id = rental.inventory_id)),
(SELECT staff_id as sk_staff FROM staff where staff_id = rental.staff_id)
from rental 
'''

#Staff Table
#SELECT staff_id as sk_staff, CONCAT(first_name, ' ', last_name) as name, email from staff
#Customer Table 
#SELECT customer_id as sk_customer, CONCAT(first_name, ' ', last_name) as full_name, email as email FROM customer 
#Date Table 
#SELECT DISTINCT rental_date as sk_date, Extract(QUARTER FROM rental_date) as quarter, Extract(year FROM rental_date) as year, Extract(month FROM rental_date) as month, Extract(day FROM rental_date) as day FROM RENTAL
'''
Store Table
SELECT store_id as sk_store, 
(SELECT CONCAT(first_name, ' ', last_name) as name from staff where store_id = STORE.store_id), 
(SELECT address from address where address_id = store.address_id), 
(SELECT city from city where city_id = (SELECT city_id from address where address_id = store.address_id)),
(SELECT district as state from address where address_id = store.address_id), 
(SELECT country from country where country_id = (SELECT country_id from city where city_id = (SELECT city_id from address where address_id = store.address_id)))
from STORE
'''

'''
Film Table 
select film_id as sk_film, 
rating as rating_code, 
length as film_duration, 
rental_duration, 
release_year, 
(SELECT name from language where language_id = film.language_id), 
title 
from film;
'''

#Once this part is complete, extrction is complete. 

"""TRANSFORM"""
#fact_rental table would need to be transformed to aggregate the count rentals - not sure what it should be counting exactly

"""LOAD"""
#def create_table(df:df, name:str): 
    #https://www.dataquest.io/blog/sql-insert-tutorial/
    #
    
    #RUN SQL CREATE TABLE {name} (df)

