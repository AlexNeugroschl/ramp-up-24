def reverse(word:str):
    vowels = 0
    reversed = ""
    for i in word:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or i == "A" or i == "E" or i == "I" or i == "O" or i == "O":
            vowels += 1
        reversed = i + reversed
    print(reversed)
    print(vowels)

reverse("Granite")