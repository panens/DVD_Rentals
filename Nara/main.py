import psycopg2
#from psycopg2.conninfo import make_conninfo
#from psycopg2.conninfo 


def create_cursor(): 
    conn = psycopg2.connect(host="localhost",port="5432", dbname="dvdrental",user="postgres",password="sara")
    cur = conn.cursor() #creates cursor
    return cur, conn #returns cursor
    

def run_sql(sql, cur, conn):
    
    cur.execute(sql)
    conn.commit()
    #values = cur.fetchall()
    #return values 
    
"""CREATE TABLE article (
  id SERIAL PRIMARY KEY,
  author_id INT NOT NULL,
  title TEXT NOT NULL,
  content TEXT NOT NULL,
  CONSTRAINT fk_author FOREIGN KEY(author_id) REFERENCES author(id)
)"""

"""CREATE TABLE article_tag (
  article_id INT
  tag_id INT
  PRIMARY KEY (article_id, tag_id)
  CONSTRAINT fk_article FOREIGN KEY(article_id) REFERENCES article(id)
  CONSTRAINT fk_tag FOREIGN KEY(tag_id) REFERENCES tag(id)
)"""



cur, conn = create_cursor()  
sql = "CREATE TABLE IF NOT EXISTS dssa.DATE as (SELECT DISTINCT rental_date as sk_date, Extract(QUARTER FROM rental_date) as quarter, Extract(year FROM rental_date) as year, Extract(month FROM rental_date) as month, Extract(day FROM rental_date) as day FROM RENTAL)"    
    
df = run_sql(sql, cur, conn)


