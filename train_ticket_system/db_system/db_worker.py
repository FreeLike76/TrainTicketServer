import pandas as pd
from train_ticket_system.db_system.db_singleton import SingletonDB
from train_ticket_system.db_system.query_builder import QueryBuilder


class DBWorker:
    def __init__(self):
        self.query_builder = QueryBuilder()
        SingletonDB("TrainTickets")

    def get_all(self):
        # query select preset
        self.query_builder.query_select()

        temp = pd.read_sql(self.query_builder.get_query(),
                           SingletonDB("TrainTickets").conn)
        temp = temp.applymap(str)
        temp["provider_id"] = "0"
        return temp

    def get_by(self, args):
        # query select preset
        self.query_builder.query_select()

        # add args
        for key, value in args.items():
            self.query_builder.add_select_arg(key, value)

        # do sql
        temp = pd.read_sql(self.query_builder.get_query(),
                           SingletonDB("TrainTickets").conn)
        # to str
        temp = temp.applymap(str)
        temp["provider_id"] = "0"
        return temp
