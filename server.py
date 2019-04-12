import os

from webservice import app
from database import Database
from configuration import Config


if __name__ == '__main__':
    app.debug = True
    host = os.environ.get('IP', '0.0.0.0')
    port = int(os.environ.get('PORT', 8080))
    
    Config.initialise()
    db = Config.get_value('database')
    user = Config.get_value('user')
    passwd = Config.get_value('password')
    server=Config.get_value('host')

    Database.initialise(database=db, user=user,password=passwd, host=server)
    app.run(host=host, port=port)
    

