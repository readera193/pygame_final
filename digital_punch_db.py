import mysql.connector


class Digital_punch_DB:
    def __init__(self, host="localhost", user="root", password="", db="pygame"):
        self.con = mysql.connector.connect(
            host=host,
            user=user,
            passwd=password,
            database=db
        )
        self.cursor = self.con.cursor(buffered=True)

    def user_login(self, tup):
        self.cursor.execute(
            "SELECT * FROM players WHERE user_id=%s AND password=%s", tup)
        return (self.cursor.fetchone())

    def winner_add_score(self, user_id):
        self.cursor.execute(
            "UPDATE players SET score=score+1 WHERE user_id=%s", (user_id,))
        self.con.commit()
