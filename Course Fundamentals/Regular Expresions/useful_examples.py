import re

text = input()

pattern = r"fjigv"
regex_pattern = re.compile(pattern)  # компилира се веднъж и след това само се използва, не заема памет всеки път
nums = regex_pattern.findall(text)


# nums = re.findall(pattern, text) - това ще е опцията ако е без компилирането


#pattern = r"(?P<Day>\d{2})(?P<separator>[\/.-])(?P<Month>[A-Z][a-z][a-z])\2(?P<Year>\d{4})\b"
#(?P<Day>\d{2}) - name the group
#(?P<separator>[\/.-]) - one of those tree options /.-
# in this example I Use (?P<separator>[\/.-]) and after that before year \2 -> this means that the separator from first and second part will be the same. It is 2 because in this example the separator is on second position as group


#matched_dates = pattern_re.finditer(all_dates) - finditer will return match object and on it we can call dictionary --> see "match dates"
#matched_dates = pattern_re.findall(all_dates) - findall will return tuple

# positive lookbehind = (^|?<=\s) - преди ?<= нашия матч или има спейс (\s) или е начало на ред (^) - в група преди регекса ни
# positive lookahead = ($|?=\s) - след нашия матч или има спейс или е край на реда ($)
# negative lookbehind = (?!<\s) - преди нашия матч да няма нещотото
# negative lookahead = (?!\s) - след нащия матч да няма нещото
# lookbehind - в началото, lookahead - в края

#re.sub("find that", "replace with that", here)

# (?P<Day>\d{2})(?P<separator>[\/.-])(?P<Month>[A-Z][a-z][a-z])(?P=separator)(?P<Year>\d{4})\b  ---> this is how we can recall a named group (sep)