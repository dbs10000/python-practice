

def vowel_counter(text):
    vowels = "a", "e", "i", "o", "u"
    vowel_counter = 0
    lower_case = text.lower()

    for letter in lower_case:
        if letter in vowels:
            vowel_counter += 1
    print("-----------------------")
    print(f"Vowel count: \n{vowel_counter}") 
    print("-----------------------")

def reverse_string(text):
    reversed_str = ""
    reverse_counter = len(text)-1

    for i in range(reverse_counter, -1, -1):
        reversed_str += text[i]
    print(f"Reversed text: \n{reversed_str}") 
    print("-----------------------")
