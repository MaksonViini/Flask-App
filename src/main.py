from database import db

from controllers.delivery import Delivery

from server.instance import server

app, api = server.app, server.api

api.add_resource(Delivery, '/home/')

if __name__ == '__main__':
    server.run()