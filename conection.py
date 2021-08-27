import pymysql

def db_connect():
    db= pymysql.connect(host='localhost',
                        user="root",
                        passwd="123456789",
                        db="task_archivament"
                        )

    return db
def add_task(name,duration):

    db= db_connect()

    with db.cursor() as cursor:
        #cursor.execute("DROP TABLE task_archivament;")
        #cursor.execute("CREATE TABLE task_archivament(task_id int NOT NULL AUTO_INCREMENT PRIMARY KEY, task_name varchar(25), task_duration int);")


        sql= """INSERT INTO task_archivament(task_name, task_duration)
                VALUES (%s,%s);"""


        try:
            #Execute the SQL command
            cursor.execute(sql,(name,duration,))
            #Commit your changes in the database
            db.commit()
        
        except:
            #Rollback in case there is any error
            db.rollback()
            print("Database Rollback!")
        finally:
            if db:
                cursor.close()
                db.close()
        
        
def view_duplicate(name):
    db=db_connect()

    with db.cursor() as cursor:
        
        sql="SELECT task_name FROM task_archivament WHERE task_name=%s"

        result=None
        try:
            cursor.execute(sql,(name,))
            result=list(cursor.fetchone())
        except:
            db.rollback()
            #print("Database Rollback!")
        finally:
            cursor.close()
            db.close()
    return False if (result==None) else True



def view():
    db= db_connect()

    result=None

    with db.cursor() as cursor:        

        sql= "SELECT * FROM task_archivament"

        try:
            cursor.execute(sql)
            result= list(cursor.fetchall())
        except:
            db.rollback()
            print("Database Rollback!")
        finally:
            cursor.close()
            db.close()
    
    return result

def search(name):
    db= db_connect()

    result= None

    with db.cursor() as cursor:

        sql= "SELECT task_name,task_duration FROM task_archivament WHERE task_name=%s"

        try:
            cursor.execute(sql,(name,))
            result=list(cursor.fetchone())
        except:
            db.rollback()
            print("Database Rollback")
        finally:
            cursor.close()
            db.close()
    
    return result

def delete(name):
    db= db_connect()

    with db.cursor() as cursor:
        
        #Nunca olvides el WHERE en el DELETE FROM 
        sql="DELETE FROM task_archivament WHERE task_name=%s"

        
        try:
            #cursor.execute("SET SQL_SAFE_UPDATES=0")
            cursor.execute(sql,(name,))
            #cursor.execute("SET SQL_SAFE_UPDATES=1")
            #Commit your changes in the database
            db.commit()
            print("Remove \"{}\" task successfully!".format(name))        
        except:
            db.rollback()
            print("Database Rollback")
        finally:
            cursor.close()
            db.close()
        
        
