from flask_restx import Resource

from server.instance import server

delivery_ns = server.delivery_name_space


class Delivery(Resource):
    def get(self, ):
        return {'hello': 'world'}
