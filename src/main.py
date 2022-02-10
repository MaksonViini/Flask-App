from database import db
from controllers.delivery import Delivery
from server.instance import server

app, api = server.app, server.api

api.add_resource(Delivery, '/hello/')

if __name__ == '__main__':
    server.run()