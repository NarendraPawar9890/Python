# Mobile Recharge Validation System

def recharge(phoneNo, amount):

    if len(phoneNo) != 10:
        return "Invalid Number... Number must be exactly 10 digits."
    if not phoneNo.isdigit():
            return "Mobile number should contain only digits."

    try:
        amount = int(amount)
    except ValueError:
         return "Recharge amount must be a number."
    
    if amount < 10: 
        return "Recharge amount must be greater than ₹10."
    
    return f"Recharge of {amount} is successfully done on {phoneNo}"
    

phoneNo = str(input("Enter your 10 digit mobile number.: "))
amount = input("Enter the recharge amount.: ")

print(recharge(phoneNo, amount))

###################################################################################

# Online Movie Ticket Booking

def book_movie_ticket(movie_name, available_seats, tickets_requested, price_per_ticket):
    
    if not movie_name.strip():
        return "Movie name cannot be empty."

    try:
        tickets_requested = int(tickets_requested)
    except ValueError:
        return "Number of tickets must be a valid number."
    
    if tickets_requested <= 0 or tickets_requested > 6:
        return "You must atleast book 1 ticket and at max 6 tickets."
    if tickets_requested > available_seats:
        return f"Only {available_seats} seats are available."
    
    total_cost = tickets_requested * price_per_ticket

    return f"Booking successful! 🎉\nMovie: {movie_name}\nTickets: {tickets_requested}\nTotal Cost: ₹{total_cost}"


movie = input("Enter the Movie name: ")
available = 50
tickets = input("Enter mumber of tickets: ")
price = 250

print(book_movie_ticket(movie, available, tickets, price))


###########################################################################################

# 3️⃣ Electricity Bill Calculator

def make_bill(units):
    try:
        units = float(units)
    except ValueError:
        return "Invalid input... Units must be a number"
    
    if units <= 0:
        return "Units must be a positive number."
    
    if units <= 100:
        rate = units * 5
    elif units <= 300:
        rate = units * 7
    else:
        rate = units * 10

    return f"Total electricity bill for {units} units is ₹{rate}"


unit_count = input("Enter electricity units consumed: ")
print(make_bill(unit_count))
