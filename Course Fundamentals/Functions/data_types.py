def data_types(a, b):
    if a == "int":
        return int(b) * 2
    elif a == "real":
        formatted_number = f"{(float(b) * 1.5):.2f}"
        return formatted_number
    elif a == "string":
        return f"${b}$"


command = input()
command2 = input()

print(data_types(command, command2))
