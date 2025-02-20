#class branch:(Sb)
class branch:
    #class variable
    number_of_branches = 0

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
 cursor.execute(''' insert into branch( bid, bname, baddr, bphone)
    #values(?,?,?,?)

  ''',) (sb.branch_id, sb.branch_name, sb.address, sb.phone)
 cursor.commit()




  #retrive connection

def retrieve_branch(sb):
        cursor = connection.cursor()
        cursor.execute("""SELECT * FROM branch WHERE branch_id = ?""", 
                       (sb.branch_id,))

        cursor.commit()
        
print('done')
