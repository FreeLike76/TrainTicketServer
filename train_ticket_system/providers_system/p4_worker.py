import requests
import pandas as pd
import threading


class Provider4Worker:
    def __init__(self, cache_update_time):
        self.endpoint = "http://127.0.0.1:8084/tickets/"

        self.cache_df = None
        self.cache_update_time = cache_update_time
        self.update_stop = threading.Event()
        self.update()

    def get_all(self):
        return self.cache_df.copy()

    def get_by(self, args):
        temp = self.cache_df.copy()
        for key, value in args.items():
            if key in temp.columns:
                temp = temp[temp[key] == value]
        return temp

    def update(self):
        # send response
        page = 1
        response = requests.get(self.endpoint + str(page))
        self.cache_df = pd.DataFrame(response.json(), dtype=str)
        # while there are more pages
        while True:
            page += 1
            response = requests.get(self.endpoint + str(page))
            if str(response.json()) == "[]":
                break
            # if data comes append
            self.cache_df.append(pd.DataFrame(response.json(), dtype=str), ignore_index=True)
        self.cache_df["provider_id"] = ["4" for x in range(len(self.cache_df))]
        print("p4_worker cache updated")
        if not self.update_stop.is_set():
            # call update() again in # seconds
            threading.Timer(self.cache_update_time, self.update, []).start()
