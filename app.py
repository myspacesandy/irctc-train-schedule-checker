import requests

class IRCTC:
    def __init__(self):
        user_input = input(
            """\n==============================
    Welcome to IRCTC Service
==============================

How would you like to proceed?

1. Enter 1 to check Live Train Status
2. Enter 2 to check PNR Status
3. Enter 3 to check Train Schedule

Your choice: """
        )

        if user_input == "1":
            print("\nLive train status - Feature coming soon.")
        elif user_input == "2":
            print("\nPNR status - Feature coming soon.")
        elif user_input == "3":
            self.train_schedule()
        else:
            print("\n❌ Invalid input. Please enter 1, 2 or 3.")

    def train_schedule(self):
        train_no = input("\nPlease enter the train number: ")
        self.fetch_data(train_no)

    def fetch_data(self, train_no):
        url = f"https://indianrailapi.com/api/v2/TrainSchedule/apikey/{API_KEY}/TrainNumber/{train_no}/"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            print(f"\n📅 Train Schedule for Train No: {train_no}")
            print("=" * 75)
            print(f"{'Station Name'.ljust(25)} | {'Arrival'.ljust(10)} | {'Departure'.ljust(10)} | {'Distance (km)'}")
            print("-" * 75)

            for station in data.get("Route", []):
                name = station["StationName"].ljust(25)
                arrival = station["ArrivalTime"].ljust(10)
                departure = station["DepartureTime"].ljust(10)
                distance = str(station["Distance"]).rjust(5)
                print(f"{name} | {arrival} | {departure} | {distance} km")

            print("=" * 75)

        except requests.exceptions.RequestException as e:
            print("\n❌ API request failed:", e)
        except KeyError:
            print("\n❌ Unexpected response format or train number not found.")

# Start the application
if __name__ == "__main__":
    IRCTC()
