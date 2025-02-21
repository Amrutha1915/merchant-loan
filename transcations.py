
import psycopg2

class Transaction():
    #class variable
    number_of_transcation = 0



    def __init__(sb, td, tdate, tamount, bid,ttype="online"):
        super().__init__(bid)
    
        sb.transaction_details= td
        sb.transaction_date = tdate
        sb.transaction_amount = tamount
        sb.transaction_type = ttype
        sb.branch_id = bid
connection=psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="Saibaba.1915",            
    host="localhost",
    port="5433"
)
print('table created successfully')


# create_transaction
def create_transaction(sb):
    cursor=connection.cursor()
    query= f"insert into transaction values(?,?,?,?)" . format(sb.transaction_id, sb.transaction_date, sb.transaction_amount, sb.transaction_type, sb.branch_id)
    cursor.execute(query)
    cursor.commit()   
print('done')

# retrieve transaction
def retrieve_transaction_id(sb):
  cursor = connection.cursor()
  query=f"SELECT * FROM transaction WHERE transaction_id = ?". format (sb.transaction_id,)
  cursor.execute(query)
  cursor.commit()
print('done')



