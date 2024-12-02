banned_words = input().split(", ")
my_text = input()


for word in banned_words:
    while word in my_text:
        my_text = my_text.replace(word, '*'*len(word))

print(my_text)