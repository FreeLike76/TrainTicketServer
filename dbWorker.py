from singletonDB import SingletonDB


class dbWorker():
    def __init__(self):
        self.db = SingletonDB("TrainTickets")

    def get_all(self):
        cursor = self.db.conn.cursor()
        # do select
        cursor.close()
        # return
        return None