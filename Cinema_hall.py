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
            self._show_list.append((f'Show id : {id}.', f'Movie name : {movie_name}.', f'Time : {time}.'))
            self._seats[id] = []
            for i in range(self._rows):
                row = []
                for j in range(self._cols):
                    row.append("Available")
                self._seats[id].append(row)
        else:
            print('* All inputs Should be string')

    def book_seats(self, id, seat_list):
        if id in self._seats:
            seats = self._seats[id]

            for row, col in seat_list:
                if 1 <= row <= self._rows and 1 <= col <= self._cols:
                    if seats[row - 1][col - 1] == 'Available':
                        seats[row - 1][col - 1] = 'Booked'
                        print(f'=> Seat Booked Succesfully for : ({row}, {col})')
                    else:
                        print(f"=> * Seat ({row}, {col}) is already booked")
                else:
                    print("=> Invalid seat selection")
        else:
            print(f'=> Invalid show ID : {id}')

    def view_show_list(self):
        print('Show List of hall: ',self._hall_no, ' => ')
        # print(self._show_list)
        for show in self._show_list:
            for val in show:
                print(val, end= ' ')
            print()
    
    def view_available_seats(self, id):
        if id in self._seats:
            print(f'Available seats for show {id}: ')
            for i in range(self._rows):
                for j in range(self._cols):
                    if self._seats[id][i][j] == "Available":
                        print(f"{(i + 1, j + 1)}", end=' ')
            print()
            print("Seats in Matrics :")
            for i in range(self._rows):
                for j in range(self._cols):
                    if self._seats[id][i][j] == "Available":
                        print(f'0', end=' ')
                    else:
                        print('1', end= ' ')
                print()
            print()
        else:
            print(f"Show with ID {id} not found.")

# Create a Cinema Hall
cinema_hall = Star_Cinema('Start Cinema', 'Dhaka')

#
hall1 = Hall(5, 10, cinema_hall.halls())
cinema_hall.entry_hall(hall1)
hall1.entry_show('11', 'Rajanikanta', '10:00 AM')
hall1.entry_show('12', 'hello dear', '2:00 PM')

# ticketing system
while True:
    print('1. View All Show')
    print('2. View Available sits')
    print('3. Book A Ticket')
    print('4. Exit')

    x = int(input('Enter a Option : '))
    if 1 > x or x > 4:
        print('=> Invalid Selection')
        print('--------------')
    elif x == 1:
        print('--------------')
        hall1.view_show_list()
        print('--------------')
    elif x == 2:
        print('--------------')
        v = input('= > Please Input Movie Id : ')
        hall1.view_available_seats(v)
        print('--------------')
    elif x == 3:
        print('--------------')
        v = input('=> Please Input Movie Id : ')
        n = int(input('=> How many Tickets You want to Buy : '))
        t_list = []
        for i in range(n):
            r = int(input(f'= > Please enter Row for person {i + 1}: '))
            c = int(input(f'= > Please enter Col for person {i + 1}: '))
            t_list.append((r, c))
        # print(t_list)
        hall1.book_seats(v, t_list)
        print('--------------')

    elif x == 4:
        break