class Member:
    number_of_members = 0

import psycopg2
connection=psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="Saibaba.1915",        
    host="localhost",
    port="5433"
)
print('table created successfully')
def __init__(sb, first_name, last_name, addr, phone,bid):
        # instance variable
        sb.first_name = first_name
        sb.last_name = last_name
        sb.address = addr
        sb.phone = phone
        sb.branch_id = bid
        Member.number_of_members += 1
def create_member(sb):
        cursor = connection.cursor()
        query=f"insert into member(first_name,last_name,addr,phone,bid)"
        "values(alice, wonderland, 123 oak, 1234567890,03),(john, doe, 456 court, 0987654321,01),(josph, stalin, 789 drive, 6789054321,02)" .format((sb.first_name, sb.last_name, sb.address, sb.phone))
        cursor.execute(query)
        cursor.commit()
print('done')
    # retrieve member
def retrieve_member(sb):
    cursor = connection.cursor()
    query=f"select * from member where first_name = alice" .format(sb.first_name),
    cursor.execute(query)
    cursor.commit()
print('done')

    # update member
def update_member(sb):
        cursor = connection.cursor()
        query=f"update member set first_name = jack where last_name = doe" .format(sb.first_name, sb.last_name)
     
        cursor.execute(query)
        cursor.commit()
print('done')

    # delete member
def delete_member(sb):
    cursor = connection.cursor()
    query=f"delete from member where first_name = josph".format(sb.first_name)
    cursor.execute(query)
    cursor.commit()
print('done')

   
