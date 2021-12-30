import pandas as pd
from flask import Flask, request
from flask_restful import Resource, Api

df = pd.read_csv("data/tickets.csv", dtype=str)
page_size = 5000


class Provider4Resource(Resource):
    def get(self, page):
        print("page:", page)
        temp = df.iloc[page_size * (page - 1): min(page_size * page, len(df))]
        return temp.to_dict(orient="records")


if __name__ == "__main__":
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(Provider4Resource, "/tickets/<int:page>")
    app.run(port=8084, debug=True)
