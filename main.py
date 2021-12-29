from train_ticket_system.tts_system import TrainTicketSystem
from flask import Flask, request
from flask_restful import Resource, Api

server = TrainTicketSystem()


class TTSResource(Resource):
    def get(self):
        if len(request.args) == 0:
            return server.get_all().to_dict(orient="records")
        else:
            return server.get_by(request.args).to_dict(orient="records")


if __name__ == "__main__":
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(TTSResource, "/tickets")
    app.run(port=8080, debug=True)
