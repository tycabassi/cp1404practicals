from prac_09.taxi import Taxi

my_taxi = Taxi("Prius 1", 100, 1.23)
my_taxi.drive(40)
print(f"{my_taxi.fuel}, ${my_taxi.get_fare()}")
my_taxi.start_fare()
my_taxi.drive(100)
print(f"Distance travelled {my_taxi.odometer}km  Fare: ${my_taxi.get_fare()}")