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
def __init__(sb, first_name, last_name, addr, phone):
        # instance variable
        sb.first_name = first_name
        sb.last_name = last_name
        sb.address = addr
        sb.phone = phone

def create_member(sb):
        cursor = connection.cursor()
        cursor.execute("""insert into member(first_name, last_name, addr, phone)
                          values(alice, wonderland, 123 oak, 1234567890)
                                 (john, doe, 456 court, 0987654321)
                                 (josph, stalin, 789 drive, 6789054321)
                                                             """),
        ((sb.first_name, sb.last_name, sb.address, sb.phone))
connection.commit()
print('done')

    # retrieve member
def retrieve_member(sb):
    cursor = connection.cursor()
    cursor.execute("""select * from member where first_name = alice""",
                       (sb.first_name,))
connection.commit()
print('done')

    # update member
def update_member(sb):
        cursor = connection.cursor()
        cursor.execute("""update member set first_name = jack where last_name = doe""",
                       (sb.first_name, sb.first_name))
        connection.commit()
print('done')

    # delete member
def delete_member(sb):
     cursor = connection.cursor()
     cursor.execute("""delete from member where first_name = %s""",
                       (sb.first_name,))
     connection.commit()
print('done')


