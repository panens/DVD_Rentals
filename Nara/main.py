import psycopg2


def connect(): 
    conn=None
    conn = psycopg2.connect(host="localhost",database="dvdrental",user="postgres",password="sara")
    cur = conn.cursor() #creates cursor
    return cur #returns cursor
    

def datetable():
    
    cur.execute("SELECT DISTINCT rental_date as sk_date, Extract(QUARTER FROM rental_date) as quarter, Extract(year FROM rental_date) as year, Extract(month FROM rental_date) as month, Extract(day FROM rental_date) as day FROM RENTAL")
    values = cur.fetchall()
    return values
    
    
    
cur = connect()    
df = datetable()


