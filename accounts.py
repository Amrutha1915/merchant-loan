import psycopg2
class Account:
    #class variable
    number_of_Account = 0

    def __init__(sb, aid, atype, abalance, bid):
        super().__init__(bid)
        #instance variable
        sb.account_id = aid
        sb.account_type = atype
        sb.account_balance = abalance
        sb.branch_id = bid

connection = psycopg2.connect(
        dbname="postgres",
        dbuser="postgres",
        password="Saibaba.1915",
        host="localhost",
        port="5433"
        )
print('table created sucessfully')

# create_account
def create_account(sb):
  cursor=connection.cursor()
  query= f"insert into account values(?,?,?,?)" . format(sb.account_id, sb.account_type, sb.account_balance, sb.branch_id)
  cursor.execute(query)
  cursor.commit()
print('done')

#retrive account
def retrive_account_id(sb):
 cursor=connection.cursor()
 query=f"SELECT * FROM account WHERE account_id = ?". format(sb.account_id)
 cursor.execute(query)
 cursor.commit()
print('done')

#update account
def update_account_id(sb):
 cursor=connection.cursor()
 query=f"UPDATE account SET account_balance = ? WHERE account_id = ?". format(sb.account_balance, sb.account_id)
 cursor.execute(query)
 cursor.commit()
print('done')

#delete account
def delete_account_id(sb):
 cursor=connection.cursor()
 query=f"DELETE FROM account WHERE account_id = ?". format(sb.account_id)
 cursor.execute(query)
 cursor.commit()
 print('done')



