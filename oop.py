class Passenger:
    def __init__(self, first_name, last_name, passport_number):
        self.first_name = first_name
        self.last_name = last_name
        self._passport_number = passport_number

    def passport_number_show(self):
        return self._passport_number

    def show__info(self):
        print(f"Passenger: {self.first_name} {self.last_name} Passport: {self._passport_number}")

    def update_passport(self, new_passport_number):
        self._passport_number = new_passport_number
        print(f"New passport number of {self.first_name} {self.last_name} is {self._passport_number}")

    @staticmethod
    def aeroport_name():
        print("Name of the airport where the passenger is staying: Lviv Airport")

class Ticket:
    def __init__(self, passenger, flight_number, airline, seat_number):
        self._passenger = passenger
        self.flight_number = flight_number
        self.airline = airline
        self.seat_number = seat_number

    @property
    def passenger_id_show(self):
        return self._passenger._passport_number

    def display_info(self):
        print(f"Ticket for passenger with id: {self._passenger._passport_number}: \nFlight: {self.flight_number}, Airline: {self.airline}")

    def change_flight(self, new_flight):
        self.flight_number = new_flight
        print(f"Flight changed to {self.flight_number}")


class EconomyTicket(Ticket):
    def __init__(self, passenger, flight_number, airline, seat_number, meals_):
        super().__init__(passenger, flight_number, airline, seat_number)
        self.meals = meals_

    def display_info(self):
        super().display_info()
        print(f"Economy seat: {self.seat_number}")

    def display_info_about_meals(self):
        print("Menu for economy class:")
        for meal in self.meals:
            print(meal)

    def add_meal(self):
        print(f"Meal added for {self._passenger.first_name}")


class BusinessServices:
    def __init__(self, lounge_access, meals_and_alcohol_):
        self.lounge_access = lounge_access
        self.meals_and_alcohol = meals_and_alcohol_

    def display_services(self):
        print(f"Lounge access: {'Yes' if self.lounge_access else 'No'}")


class BusinessTicket(Ticket, BusinessServices):
    def __init__(self, passenger, flight_number, airline, seat_number, lounge_access, meals_and_alcohol):
        Ticket.__init__(self, passenger, flight_number, airline, seat_number)
        BusinessServices.__init__(self, lounge_access, meals_and_alcohol)

    def display_info(self):
        Ticket.display_info(self)
        print(f"Bussiness seat: {self.seat_number}")
        self.display_services()

    def display_info_about_meals(self):
        print("Menu for business class:")
        for meal in meals_and_alcohol:
            print(meal)

    def add_premium_meal(self):
        print(f"Premium meal added for {self._passenger.first_name}")





passenger1 = Passenger("Sofia", "Mazur", "1234567890")
passenger2 = Passenger("Petro", "Malko", "0987654321")

passenger1.aeroport_name()

passenger1.show__info()
passenger2.show__info()
passenger2.update_passport("1111111111")
passenger2.show__info()

meals = ["fried potatoes", "chicken", "water", "tea"]
meals_and_alcohol = ["caviar", "sushi", "peking duck", "tea", "coffee", "vine", "whiskey"]

economy_ticket = EconomyTicket(passenger1, "AA123", "American Airlines", "12A", meals)
economy_ticket.display_info()
economy_ticket.display_info_about_meals()
economy_ticket.add_meal()

business_ticket = BusinessTicket(passenger2, "BA456", "British Airways", "1B", True, meals_and_alcohol)
business_ticket.display_info()
business_ticket.display_info_about_meals()
business_ticket.add_premium_meal()

list_of_tickets = [economy_ticket, business_ticket]
for ticket in list_of_tickets:
    if ticket._passenger == passenger1:
        print("Info about ticket that belongs to " + ticket._passenger.first_name + " " + ticket._passenger.last_name + ":")
        ticket.display_info()
