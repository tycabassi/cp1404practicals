from prac_09.taxi import Taxi

my_taxi = Taxi("Prius 1", 100, 1.23)
my_taxi.drive(40)
print(f"{my_taxi.fuel}, ${my_taxi.get_fare()}")