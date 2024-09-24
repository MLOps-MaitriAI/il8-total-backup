import time
import pymysql

def wait_for_db():
    while True:
        try:
            conn = pymysql.connect(
                host='db',
                user='root',
                password='Maitri*5051#',
                database='lms_db'
            )
            conn.close()
            print("Database is ready!")
            break
        except pymysql.Error as e:
            print("Database is not ready yet. Waiting...")
            time.sleep(1)

if __name__ == "__main__":
    wait_for_db()

