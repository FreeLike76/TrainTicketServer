class QueryBuilder:
    def __init__(self):
        self.column_mapper = {
            "id": "[Id]",
            "date": "[CityFromDate]",
            "time": "[CityFromTime]",
            "from_city": "[CityFrom]",
            "to_city": "[CityTo]",
            "travel_time": "[TravelTime]",
            "seat_type": "[Type]",
            "seat_num": "[SeatNum]",
            "cost": "[Price]",
            "trip_id": "[Trip]"}

        self.query = None
        self.has_where = None
        self.has_specification = None
        self.reset()

    def reset(self):
        self.query = ""
        self.has_where = None
        self.has_specification = False

    def query_select(self):
        self.query = "select * from TicketsInfo "

    def add_select_arg(self, key, value):
        if key in self.column_mapper.keys():
            # if first specification => add where
            if not self.has_where:
                self.query = self.query + "where "
                self.has_where = True

            # if previously had specification => add and
            if self.has_specification:
                self.query = self.query + "and "

            # add specification
            self.query = self.query + key + " = '" + str(value) + "' "
            self.has_specification = True
        else:
            print("Error no such column in DB!")

    def get_query(self):
        temp = self.query
        self.reset()
        print("Query:", temp)
        return temp
