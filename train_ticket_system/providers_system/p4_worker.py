import requests
import pandas as pd


class Provider4Worker:
    def __init__(self):
        self.endpoint = "http://127.0.0.1:8084/tickets/"

    def get_all(self):
        # read page 1
        page = 1
        response = requests.get(self.endpoint + str(page))
        temp = pd.DataFrame(response.json(), dtype=str)

        # while there are more pages
        while True:
            page += 1
            response = requests.get(self.endpoint + str(page))
            if str(response.json()) == "[]":
                break
            # if data comes append
            temp.append(pd.DataFrame(response.json(), dtype=str), ignore_index=True)

        temp["provider_id"] = ["4" for x in range(len(temp))]
        return temp

    def get_by(self, args):
        # read page 1
        page = 1
        response = requests.get(self.endpoint + str(page))
        temp = pd.DataFrame(response.json(), dtype=str)
        # while there are more pages
        while True:
            page += 1
            response = requests.get(self.endpoint + str(page))
            if str(response.json()) == "[]":
                break

            # if data comes append and filter
            temp.append(pd.DataFrame(response.json(), dtype=str), ignore_index=True)
            for key, value in args.items():
                if key in temp.columns:
                    temp = temp[temp[key] == value]

        temp["provider_id"] = ["4" for x in range(len(temp))]
        return temp
