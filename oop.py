class Star_Cinema:
    hall_list = []

    def __init__(self, name, location) -> None:
        self.name = name
        self.location = location

    def entry_hall(self, hall):
        self.hall_list.append(hall)
    
    def halls(self):
        return len(self.hall_list)

        
class Hall:
    hall_count = 0
    def __init__(self, rows, cols, number) -> None:
        self.seats = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = f'A-{int(number) + 1}'
    
    def entry_show(self, id, movie_name, time):
        self.show_list.append((id, movie_name, time))

    def book_seats():
        pass

    def view_show_list():
        pass
    
    def view_available_seats():
        pass

# Create a Cinema Hall
cinema_hall = Star_Cinema('Start Cinema', 'Dhaka')

# create a hall
hall1 = Hall(5, 10, cinema_hall.halls())
# entry the hall
cinema_hall.entry_hall(hall1)
hall1.entry_show('E1', 'Rajanikanta', '10:00 AM')
hall1.entry_show('E2', 'Rajanikanta', '12:00 PM')


for hall in cinema_hall.hall_list:
    print(hall.show_list)