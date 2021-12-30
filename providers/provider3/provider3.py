import time
import pandas as pd
from flask import Flask, request
from flask_restful import Resource, Api

df = pd.read_csv("data/tickets.csv", dtype=str)


class Provider3Resource(Resource):
    def get(self):
        print("sleep")
        time.sleep(5)
        temp = df
        for key, value in request.args.items():
            if key in temp.columns:
                temp = temp[temp[key] == value]
        return temp.to_dict(orient="records")


if __name__ == "__main__":
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(Provider3Resource, "/tickets")
    app.run(port=8083, debug=True)
