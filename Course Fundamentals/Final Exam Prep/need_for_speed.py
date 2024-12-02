num_cars = int(input())
cars_dict = {}

for _ in range(num_cars):
    cars = input().split("|")
    car = cars[0]
    mileage = int(cars[1])
    fuel = int(cars[2])
    cars_dict[car] = [mileage, fuel]

while True:
    command = input()
    if command == "Stop":
        break
    command = command.split(" : ")
    action = command[0]
    car_ = command[1]
    if action == "Drive":
        distance = int(command[2])
        fuel_needed = int(command[3])
        if cars_dict[car_][1] < fuel_needed:
            print("Not enough fuel to make that ride")
        else:
            cars_dict[car_][1] -= fuel_needed
            cars_dict[car_][0] += distance
            print(f"{car_} driven for {distance} kilometers. {fuel_needed} liters of fuel consumed.")
            if cars_dict[car_][0] >= 100000:
                cars_dict.pop(car_)
                print(f"Time to sell the {car_}!")

    elif action == "Refuel":
        new_fuel = int(command[2])
        if cars_dict[car_][1] + new_fuel > 75:
            new_fuel = 75 - cars_dict[car_][1]
            cars_dict[car_][1] = 75
        else:
            cars_dict[car_][1] += new_fuel
        print(f"{car_} refueled with {new_fuel} liters")
    elif action == "Revert":
        kilometers = int(command[2])
        cars_dict[car_][0] -= kilometers
        if cars_dict[car_][0] < 10000:
            cars_dict[car_][0] = 10000
        else:
            print(f"{car_} mileage decreased by {kilometers} kilometers")

for car in cars_dict.keys():
    print(f"{car} -> Mileage: {cars_dict[car][0]} kms, Fuel in the tank: {cars_dict[car][1]} lt.")