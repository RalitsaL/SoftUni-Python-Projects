counter_coffees = 0
while True:
    command = input()
    if command == "END":
        break
    elif command == "coding" or command == "dog" or command == "cat" or command == "movie":
        counter_coffees += 1
    elif command == "CODING" or command == "DOG" or command == "CAT" or command == "MOVIE":
        counter_coffees += 2
    else:
        continue
if counter_coffees > 5:
    print("You need extra sleep")
else:
    print(counter_coffees)


