from database.database import CursorFromConnectionPool

class Score:
    def __init__(self, pk, score):
        self.pk = pk
        self.score = score

    def __repr__(self):
        return "<Score {}>".format(self.pk)

    def save_to_db(self):
        with CursorFromConnectionPool() as cursor:
            cursor.execute('INSERT INTO scores (pk,score) VALUES (%s, %s)',
                            (self.pk, self.score))

    