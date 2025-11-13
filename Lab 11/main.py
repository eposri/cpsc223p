'''
Name: Kayla Ngo
CWID: 885083436
Date: 11/12/2025
'''

from flights import Flights

def display_menu():
    print("\n*** TUFFY TITAN FLIGHT SCHEDULE MAIN MENU\n")
    print("1. Add flight")
    print("2. Print flight schedule")
    print("3. Set flight schedule filename")
    print("9. Exit the program\n")

def main():
    filename = "flights.json" # Default filename
    flights = Flights(filename)

    while True:
        display_menu()
        choice = input("Enter menu choice: ")

        if choice == "1":
            origin = input("Enter origin: ")
            destination = input("Enter destination: ")
            flight_number = input("Enter flight number: ")
            departure = input("Enter departure time (HHMM): ")
            arrival = input("Enter arrival time (HHMM): ")
            next_day = input("Is arrival next day (Y/N): ").upper()
            if flights.add_flight(origin, destination, flight_number, departure, arrival, next_day):
                print("Flight added successfully!")
            else:
                print("Invalid time format. Please use HHMM format.")
        elif choice == "2":
            flight_schedule = flights.get_flights()
            if flight_schedule:
            print("\n================== FLIGHT SCHEDULE ==================")
            print("Origin Destination Number Departure Arrival Duration")
            print("====== =========== ====== ========= ======== ========")
            for flight in flight_schedule:
                print(f"{flight['origin']:<6} {flight['destination']:<11} {flight['flight_number']:<6} {flight['departure']:>9} {flight['arrival']:>8} {flight['duration']:>8}")
            else:
                print("No flights scheduled.")
        elif choice == "3":
            filename = input("Enter new filename: ")
            flights = Flights(filename) # Re-initialize with the new filename
            print(f"Flight schedule filename set to {filename}")
        elif choice == "9":
            print("Exiting program.")
            break
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()