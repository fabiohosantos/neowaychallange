import psycopg2
from database.database import CursorFromConnectionPool

def insert_batch(sql,data):
	try:
		with CursorFromConnectionPool() as cursor:
			cursor.execute(sql,data)
			cursor.close()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if cursor is not None:
			cursor.close()

