

 

#class branch:(Sb)
class branch:
    #class variable
    number_of_branch = 0

#import libary
import psycopg2

def __init__(sb, bid, bname, baddr, bphone):
        #instance variable
        sb.branch_id = bid
        sb.branch_name = bname
        sb.address = baddr
        sb.phone = bphone

connection = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="Saibaba.1915",
        host="localhost",
        port="5433"
)
print('table cretated sucessfully')


#connection
connection = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="Saibaba.1915",
        host="localhost",
        port="5433"
        )

def create_branch(sb):
 cursor = connection.cursor()
 cursor= sb.connection.cursor()

 query= f"insert into branch values(?,?,?,?)" . format(sb.branch_id, sb.branch_name, sb.address, sb.phone)
 cursor.execute(query)
 cursor.commit()

print('done')


  #retrive connection

def retrieve_branch(sb):
        cursor = connection.cursor()
        query=f"SELECT * FROM branch WHERE branch_id =?". format(sb.branch_id)
        cursor.execute(query)
        cursor.commit()
        
print('done')














        






