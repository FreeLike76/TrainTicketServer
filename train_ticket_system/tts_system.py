from train_ticket_system.db_system.db_worker import DBWorker
from train_ticket_system.providers_system.providers_facade import Facade


class TrainTicketSystem:
    def __init__(self):
        self.providers = Facade()
        self.db = DBWorker()

    def get_all(self):
        db_res = self.db.get_all()
        res_providers = self.providers.get_all()
        return db_res.append(res_providers, ignore_index=True)

    def get_by(self, args):
        db_res = self.db.get_by(args)
        res_providers = self.providers.get_by(args)
        return db_res.append(res_providers, ignore_index=True)

    def set_status(self, args):
        self.db.set_status(args["id"], args["status"])

    def delete_ticket(self, args):
        self.db.delete_ticket(args["id"])

    def insert_ticket(self, args):
        self.db.insert_ticket(args["trip_id"], args["seat_type"], args["seat_num"])
