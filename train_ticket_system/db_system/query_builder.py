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

    def query_update(self, key, value):
        self.query = "update Tickets set " + key + " = " + value + " "

    def query_delete(self):
        self.query = "delete from Tickets "

    def query_insert(self, trip, seat_type, seat_num):
        self.query = "insert into Tickets([Trip], [Type], [SeatNum], [Status]) " \
                     "values(" + str(trip) + ", " + str(seat_type) + ", " + str(seat_num) + ", " + "0);"

    def add_where_arg(self, key, value, maps=False):
        # if first specification => add where
        if not self.has_where:
            self.query = self.query + "where "
            self.has_where = True

        # if previously had specification => add and

        if self.has_specification:
            self.query = self.query + "and "

        # add specification
        if maps:
            self.query = self.query + self.column_mapper[key] + " = '" + str(value) + "' "
        else:
            self.query = self.query + key + " = '" + str(value) + "' "

        self.has_specification = True

    def get_query(self):
        temp = self.query
        self.reset()
        print("Query:", temp)
        return temp
