import psycopg2


class Db:

    def __init__(self):
        self.connect_db()
        

    def connect_db(self):
        self.conn = psycopg2.connect("host=localhost dbname=db user=user password=password")
        print("Connected to database")
        

    def desconect_db(self):
        self.conn.close()
        

    def execute_bd(self, command: str):
        
        command = command.lower()
        cur = self.conn.cursor()
        cur.execute(command)
        self.conn.commit()
        
        data = None
        if "select" in command:
            data = cur.fetchall()

        cur.close()
        return data