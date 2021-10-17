import re
class book_my_show():
    def __init__(self):
        self.rows = int(input("Enter number of rows::"))
        self.col = int(input("Enter number of seats in a row::"))
        self.seats = [['s' for i in range(self.col+1)] for j in range(self.rows+1)]
        self.total_booked = 0
        self.sales = 0
        self.first_half = range(self.rows//2)
        self.second_half = range(self.rows//2+1,self.rows+1)
        self.customers = {}
        quitter = 0
        while quitter == 0:
            choice = self.choices()
            if choice == "0":
                quitter = 1
            elif choice == "1":
                self.seat_matrix()
            elif choice =="2":
                g = True
                while g:
                    self.book_ticket()
                    self.total_booked += 1
                    print ("\n1. Purchase another Ticket")
                    print ("0. Exit")
                    choice = input("Enter Choice::")
                    if choice == '1':
                        pass
                    else:
                        g = False
            elif choice == "3":
                self.stats()
            elif choice == "4":
                h = True
                while h:
                    self.user_info()
                    print ("\n1. check another user")
                    print ("0. Exit")
                    choice = input("Enter Choice::")
                    if choice == '1':
                        pass
                    else:
                        h = False
            else:
                print("no valid option selected ")

    def choices(self):
        print(" ")
        print("1. Show the seats")
        print("2. Buy a Ticket")
        print("3. Statistics")
        print("4. Show booked ticket user info")
        print("0. Exit")
        self.x = input("\nEnter your choice::")
        return(self.x)
    
    def seat_matrix(self):   
        for i in range(self.rows+1):
            for j in range(self.col+1):
                if i == 0:
                    if j == 0:
                        self.seats[i][j] = ' '
                    else:
                        self.seats[i][j] = j
                else:
                    self.seats[i][0] = i
        print('\nCinema:')
        for r in self.seats:
            for c in r:
                print(c,end = " ")
            print()
    
    def book_ticket(self):
        read = 'y|n'
        q = 0
        while q == 0:
            get = input("Would you like to see current seating plan? y/n::")
            if re.fullmatch(read,get):
                q = 1
                if get == "y":
                    self.seat_matrix()
            else:
                print("Enter valid choice")
        r,c = map(int,input("Enter Row and Column of your choice::").split(','))
        booked = False
        while booked == False:
            if self.seats[r][c] == 'B':
                print("\nThis seat is already Booked")
            else:
                if self.rows*self.col<=60:
                    price_of_ticket = 10
                else:
                    if r in self.first_half:
                        price_of_ticket = 10
                    else:
                        price_of_ticket = 8    
            print("\nPrice of your selected seat is:: Rs",price_of_ticket)
            q1 = 0
            while q1 == 0:
                res = input("Do you want to book this ticket?y or n::")
                if re.fullmatch(read,res):
                    q1 = 1
                    booked = True
                    if res == 'y':
                        regx1='[A-Za-z\s]{2,25}'
                        n = 0
                        while n == 0:
                            name = input("\nPlease Enter your Name (avoid numbers and special characters)::")
                            if re.fullmatch(regx1,name):
                                n = 1
                            else:
                                print("Please Enter a valid name")
                        g = 0
                        regx3 = '^[m|M]ale$|^[f|F]emale$'
                        while g == 0:
                            gender = input("Please Enter your Gender (Male/Female)::")
                            if re.match(regx3,gender):
                                g = 1
                            else:
                                print("Try with valid entry")
                        a = 0
                        regx2 = '[1-9]{1,2}'
                        while a == 0:
                            age = input("Enter your Age (should be between 1-99)::")
                            if re.fullmatch(regx2,age):
                                a = 1
                            else:
                                print("Try again with valid entry")
                        regx = re.compile("[6-9][0-9]{9}")
                        m = 0
                        while m == 0:
                            mobile = input("Enter Valid 10 digit contact number::")
                            if len(mobile) > 10:
                                print("only 10 digits are allowed")
                            else:
                                if regx.match(mobile):
                                    m = 1
                                else:
                                    print("try again with valid contact number")
                        self.customers[r,c] = [name,gender,age,mobile,price_of_ticket]
                        self.seats[r][c] = 'B'
                        self.sales += price_of_ticket
                        print("\nBooked Successfully")
                else:
                    print("\nEnter valid choice")
    
    def stats(self):
        total = self.rows*self.col
        f = self.rows//2
        self.seat_matrix()
        per = round((self.total_booked/total)*100,2)
        print("\nNumber of Purchased Tickets :",self.total_booked)
        print("Percentage :",str(per)+'%')
        print("Current Income: Rs",self.sales)
        if total<=60:
            print("Total Income: Rs",total*10)
        else:
            print("Total Income: Rs",(((f)*self.col)*10)+(((self.rows-f)*self.col)*8))

    def user_info(self):
        r,c = map(int,input("Enter Row and Column of your choice::").split(','))
        if self.seats[r][c] == "B":
            print("\nName :",self.customers[r,c][0])
            print("Gender :",self.customers[r,c][1])
            print("Age :",self.customers[r,c][2])
            print("Mobile :",self.customers[r,c][3])
            print("Ticket price : Rs",self.customers[r,c][4])
        else:
            print("\nThis seat is not booked yet")

if __name__ == '__main__':
    obj = book_my_show()
