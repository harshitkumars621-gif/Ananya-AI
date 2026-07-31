from memory.database import connect

class Memory:

    def save_preference(self, key, value):
        conn = connect()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT OR REPLACE INTO preferences(key, value) VALUES(?, ?)",
            (key, value)
        )

        conn.commit()
        conn.close()

    def get_preference(self, key):
        conn = connect()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT value FROM preferences WHERE key=?",
            (key,)
        )

        row = cursor.fetchone()

        conn.close()

        return row[0] if row else None

    def add_task(self, task):
        conn = connect()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO tasks(task) VALUES(?)",
            (task,)
        )

        conn.commit()
        conn.close()

    def get_tasks(self):
        conn = connect()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT task FROM tasks WHERE done=0"
        )

        rows = cursor.fetchall()

        conn.close()

        return [row[0] for row in rows]