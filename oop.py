class Star_Cinema:
    _hall_list = []

    def __init__(self, name, location) -> None:
        self._name = name
        self._location = location

    def entry_hall(self, hall):
        self._hall_list.append(hall)
    
    def halls(self):
        return len(self._hall_list)

        
class Hall:
    def __init__(self, rows, cols, number) -> None:
        self._seats = {}
        self._show_list = []
        self._rows = rows
        self._cols = cols
        self._hall_no = f'A-{number + 1}'
        for i in range(self._rows):
            for j in range(self._cols):
                self._seats[(i + 1, j + 1)] = "Available"
    
    def entry_show(self, id, movie_name, time):
        if type(id) == str and type(movie_name) == str and type(time) == str:        
            self._show_list.append((id, movie_name, time))
            self._seats[id] = []
            for i in range(self._rows):
                row = []
                for j in range(self._cols):
                    row.append("Available")
                self._seats[id].append(row)
        else:
            print('All inputs Should be string')

    def book_seats(self, id, seat_list):
        if id in self._seats:
            seats = self._seats[id]

            for row, col in seat_list:
                if 1 <= row <= self._rows and 1 <= col <= self._cols:
                    if seats[row - 1][col - 1] == 'Available':
                        seats[row - 1][col - 1] = 'Booked'
                        print('Seat Booked Succesfully')
                    else:
                        print(f"Seat ({row}, {col}) is already booked")
                else:
                    print("Invalid seat selection")
        else:
            print(f'Invalid show ID : {id}')

    def view_show_list(self):
        print('Show List of hall: ',self._hall_no, end=' => ')
        print(self._show_list)
    
    def view_available_seats(self, id):
        if id in self._seats:
            print(f'Available seats for show {id}: ')
            for i in range(self._rows):
                for j in range(self._cols):
                    if self._seats[id][i][j] == "Available":
                        print(f"{(i + 1, j + 1)}", end=' ')
            print()
        else:
            print(f"Show with ID {id} not found.")

# Create a Cinema Hall
cinema_hall = Star_Cinema('Start Cinema', 'Dhaka')

# create a hall and entry
hall1 = Hall(5, 10, cinema_hall.halls())
cinema_hall.entry_hall(hall1)
hall1.entry_show('E1', 'Rajanikanta', '10:00 AM')
hall1.entry_show('E1', 'Hero The Nayok', '12:00 AM')
hall1.entry_show('E2', 5, '2:00 PM')
hall1.entry_show('E2', 'hello dear', '2:00 PM')
hall1.book_seats('E1', [(1, 1)])
hall1.book_seats('E1', [(1, 1)])
hall1.book_seats('E1', [(2, 4)])

hall1.view_show_list()
hall1.view_available_seats('E1')

# create another hall and entry
hall2 = Hall(5, 4, cinema_hall.halls())
cinema_hall.entry_hall(hall2)
hall2.entry_show('E4', 'Kopa Samsu', '10:30 AM')
hall2.entry_show('E4', 'Samsu The King', '11:30 AM')
hall2.book_seats('E4', [(1, 4)])
hall2.view_available_seats('E4')