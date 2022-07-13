from datetime import datetime
import locale

print("Hotel Reservation Program")

again = "y"
while again.lower() =="y":
    #Arrival date
    while True:
        date_str = input("Enter arrival date (YYYY-MM-DD): ")
        try:
            arrival_date = datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            print("invalid date format. Try again.")
            print()
            continue #skip next if statetment and restart loop

        # strip non-zer time values from datetime object
        now = datetime.now()
        today = datetime(now.year, now.month, now.day)
        if arrival_date < today:
            print("arrival date must be today or later. Try again.")
            print()
        else:
            break
    # get departure date 
    while True:
        date_str = input("Enter departure date (YYYY-MM-DD): ")
        try:
            departure_date = datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            print("invalid date format. Try again.")
            print()
            continue #skip next if statement and re-start loop

        if departure_date <= arrival_date:
            print("Departure date must be after arrival date. Try again.")
            print()
        else:
            break

        print()

        #calculate nights and cost
        rate = 85.0
        rate_message = ""
        if arrival_date.month == 8: #August is high season
            rate = 105.0
            rate_message = "(High season)"
        total_nights = (departure_date - arrival_date).days
        total_cost = rate * total_nights

        #format results
        date_format = "%B %d, %Y"
        locale.setlocale(locale.LC_ALL, "en_US")
        print(f"Arival_date:     {arrival_date:{date_format}}")
        print(f"Departure Date:  {departure_date:{date_format}}")
        print(f"Nightly rate:    {locale.currency(rate)} {rate_message}")
        print(f"Total nights:    {total_nights}")
        print(f"Total price:     {locale.currency(total_cost)}")
       

        #ask if user wants to continue
        again = input("Continue? (y/n): ")
        print()
        if again =="n":
            print("Bye!")
            break
print("Thanks for booking with us!")






