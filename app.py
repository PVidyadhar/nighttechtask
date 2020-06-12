from flask import Flask,jsonify
from flask_restful import Api
from resources.login import Login
app = Flask(__name__)


api=Api(app)
api.add_resource(Login,'/login')



if __name__ == "__main__":
    app.run(debug=True)
    