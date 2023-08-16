import mysql.connector
import json
try:
    con = mysql.connector.connect(host="database-1.chiajkhhkirg.ap-south-1.rds.amazonaws.com",user="admin",password="abhishek",database="rest")
    con.autocommit=True
    cur = con.cursor(dictionary = True)
    table_schema = (
        "CREATE TABLE IF NOT EXISTS users ("
        "id INT AUTO_INCREMENT PRIMARY KEY NOT NULL UNIQUE,"
        "name VARCHAR(45),"
        "email VARCHAR(45),"
        "phone VARCHAR(45),"
        "role VARCHAR(45),"
        "password VARCHAR(45)"
        ")"
    )
    cur.execute(table_schema)
    print("connected to database")
except:
    print("database error")

def user_getall_model():
    cur.execute("SELECT * FROM users")
    result = cur.fetchall()
    print(result)
    if len(result)>0:
        return json.dumps(result)
    else:
        return("Database is empty")
    


def user_getbyid_model(id):
    cur.execute(f"SELECT * FROM users WHERE ID={int(id)}")
    er2 = cur.fetchall()
    
    if cur.rowcount> 0:
        print("er2 = ",er2)
        return json.dumps(er2)
    else:
        return "enty with specified ID is not available"
    

def user_addone_model(data):

    cur.execute(f"INSERT INTO users(name,email,phone,role,password) VALUES('{data['name']}','{data['email']}','{data['phone']}','{data['role']}','{data['password']}')")
    
    return "user successfully created"
#{(json.dumps(data)[1:-13]).replace(':','=')}


def user_update_model(data):
    set_value = ', '.join([f'{key} = "{value}"' for key, value in data.items() if key != 'id'])
    print("str = ",set_value)
    try:
        cur.execute(f"UPDATE users SET name='{data['name']}',email='{data['email']}',phone='{data['phone']}',role='{data['role']}',password='{data['password']}' WHERE id={data['id']}")
    except:
        cur.execute(f"UPDATE users SET {set_value} WHERE id={data['id']}")
    if cur.rowcount> 0:
        cur.execute("SELECT * FROM users")
        er2 = cur.fetchall()
        print("er2 = ",er2)

        return "user updated successfully "
    else:
        return "User is not available"
    


def user_delete_model(id):

    cur.execute(f"DELETE FROM users WHERE ID={id}")
    if cur.rowcount> 0:
        cur.execute("SELECT * FROM users")
        er2 = cur.fetchall()
        print("er2 = ",er2)

        return "user deleted successfully "
    else:
        return "User is not available"
    



    

