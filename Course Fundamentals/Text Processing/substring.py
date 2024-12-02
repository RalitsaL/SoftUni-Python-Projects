
searched_string = input()
string_ = input()

while searched_string in string_:
    string_ = string_.replace(searched_string, "")

print(string_)