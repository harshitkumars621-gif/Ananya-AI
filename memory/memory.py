from memory.database import connect

class Memory:

    def save_preference(self, key, value):

        conn = connect()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT OR REPLACE INTO preferences(key,value)
        VALUES(?,?)
        """,(key,value))

        conn.commit()
        conn.close()

    def get_preference(self,key):

        conn=connect()
        cursor=conn.cursor()

        cursor.execute("""
        SELECT value FROM preferences
        WHERE key=?
        """,(key,))

        row=cursor.fetchone()

        conn.close()

        if row:
            return row[0]

        return None