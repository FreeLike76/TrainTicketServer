import requests
import threading
import pandas as pd


class Provider3Worker:
    def __init__(self):
        self.endpoint = "http://127.0.0.1:8083/tickets"

        self.cache_df = None
        self.update_stop = threading.Event()
        self.update()
        # to stop
        # self.update_stop.set()

    def get_all(self):
        return self.cache_df.copy()

    def get_by(self, args):
        temp = self.cache_df.copy()
        for key, value in args.items():
            if key in temp.columns:
                temp = temp[temp[key] == value]
        return temp

    def update(self):
        # send responce
        response = requests.get(self.endpoint)
        self.cache_df = pd.DataFrame(response.json(), dtype=str)
        self.cache_df["provider_id"] = ["3" for x in range(len(self.cache_df))]
        if not self.update_stop.is_set():
            # call f() again in 60 seconds
            threading.Timer(5, self.update, []).start()
