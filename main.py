from train_ticket_system.tts_system import TrainTicketSystem
from flask import Flask, request
from flask_restful import Resource, Api, reqparse

server = TrainTicketSystem()

block_ticket_args = reqparse.RequestParser()
block_ticket_args.add_argument("id", type=str, help="Id is required to block ticket", required=True)
block_ticket_args.add_argument("status", type=str, help="Whether the ticket is blocked", required=True)

class TTSResource(Resource):
    def get(self):
        if len(request.args) == 0:
            return server.get_all().to_dict(orient="records")
        else:
            return server.get_by(request.args).to_dict(orient="records")

    def post(self):
        args = block_ticket_args.parse_args()
        try:
            server.set_status(args["id"], args["status"])
            return {"id": str(args["id"]), "status": args["status"]}
        except:
            return {"id": str(args["id"]), "status": args["status"]}


if __name__ == "__main__":
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(TTSResource, "/tickets")
    app.run(port=8080, debug=True)
