# put your python code here
duration = int(input())
food_day = int(input())
flight_one = int(input())
hotel_one = int(input())
print(duration * food_day + (duration - 1) * hotel_one + 2 * flight_one)
