
class Transaction():
    #class variable
    number_of_transcation = 0 
import  psycopg2  
connection = psycopg2.connect(
    dbname="postgres",
    user="postgres",      
    password="Saibaba.1915",
    host="localhost",
    port="5433"
)
print('table created successfully')

def __init__(sb, td, tdate, tamount, bid,ttype="online"):
        super().__init__(bid)
    
        sb.transaction_details= td
        sb.transaction_date = tdate
        sb.transaction_amount = tamount
        sb.transaction_type = ttype
        sb.branch_id = bid


# create_transaction
def create_transaction(sb):
 cursor = connection.cursor()
 cursor.execute("""insert into transaction(transaction_id, transaction_date, amount, type, branch_id)
values(%s, %s, %s, %s, %s) RETURNING transaction_id;""", (sb.transaction_id, sb.transaction_date, sb.transaction_amount, sb.transaction_type, sb.branch_id))
connection.commit()
print('done')

# retrieve transaction
def retrieve_transaction_id(sb):
 cursor = connection.cursor()
 cursor.execute("""SELECT * FROM transaction WHERE transaction_id = %s""", (sb.transaction_id,))
 transaction = cursor.fetchone()
 print(transaction)
 cursor.close()
connection.commit() 
print('done')
 
