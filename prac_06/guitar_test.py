from prac_06.guitar import guitar_details
from prac_06.guitar import another_guitar
print("guitar_details")
print(f"gibson get_age() expected 102 - {guitar_details.get_age()}")
print(f"gibson is_vintage() expected True - {guitar_details.is_vintage()}")
print(f"another_guitar get_age() expected 25 - {another_guitar.get_age()}")
print(f"another_guitar is_vintage() expected False - {another_guitar.is_vintage()}")