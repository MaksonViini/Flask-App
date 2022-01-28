from flask import Flask, Blueprint
from flask_restx import Api


class Server():
    def __init__(self,) -> None:
        self.app = Flask(__name__)
        self.blueprint = Blueprint('api', __name__, url_prefix='/api')
        self.api = Api(self.blueprint, doc='/docs', title='Api Flask-SQLAlchemy',
                       version='1.0', description='API for the server')
        self.app.register_blueprint(self.blueprint)

        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.app.config['PROPAGATE_EXCEPTIONS'] = True

        self.delivery_name_space = self.delivery_name_space()

        super().__init__()

    def delivery_name_space(self):
        return self.api.namespace('delivery', description='Book operations', path='/')

    def run(self, ):
        self.app.run(debug=False)


server = Server()
