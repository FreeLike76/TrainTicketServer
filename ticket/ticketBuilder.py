from ticket import Ticket


class TicketBuilder:
    def __init__(self):
        self._ticket = Ticket()

    def reset(self):
        self._ticket = Ticket()

    def build(self):
        temp = self._ticket
        self.reset()
        return temp

    def set_id(self, _id):
        self._ticket.id = _id

    def set_provider_id(self, _provider_id):
        self._ticket.provider_id = _provider_id

    def set_date(self, _date):
        self._ticket.date = _date

    def set_time(self, _time):
        self._ticket.time = _time

    def set_from_city(self, _from_city):
        self._ticket.from_city = _from_city

    def set_to(self, _to_city):
        self._ticket.to_city = _to_city

    def set_travel_time(self, _travel_time):
        self._ticket.id = _travel_time

    def set_seat_type(self, _seat_type):
        self._ticket.seat_type = _seat_type

    def set_seat_num(self, _seat_num):
        self._ticket.seat_num = _seat_num

    def set_cost(self, _cost):
        self._ticket.cost = _cost
