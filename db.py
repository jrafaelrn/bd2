import psycopg2


class Db:

    def __init__(self):
        self.connect_db()
        

    def connect_db(self):
        self.conn = psycopg2.connect("dbname=postgres user=postgres password=postgres")
        print("Connected to database")
        

    def desconect_db(self):
        self.conn.close()
        

    def execute_bd(self, command: str):
        
        cur = self.conn.cursor()
        cur.execute(command)
        self.conn.commit()
        cur.close()
        
        if command.startswith("SELECT"):
            return cur.fetchall()