def remove_common_letters(name1, name2):
    common_letters = set(name1) & set(name2)
    for letter in common_letters:
        name1 = name1.replace(letter, '')
        name2 = name2.replace(letter, '')
    return name1, name2

def count_remaining_letters(name1, name2):
    total_letters = len(name1) + len(name2)
    return total_letters

def calculate_flames(total_letters):
    flames_word = "FLAMES"
    index = (total_letters % len(flames_word)) - 1
    return flames_word[index]

def display_result(result):
    relationships = {
        'F': 'Friends',
        'L': 'Lovers',
        'A': 'Affection',
        'M': 'Marriage',
        'E': 'Enemies',
        'S': 'Siblings'
    }
    print(f"The relationship between the two names is: {relationships[result]}")


if __name__ == "__main__":
   
    name1 = input("Enter the first name: ").upper().replace(" ", "")
    name2 = input("Enter the second name: ").upper().replace(" ", "")

    name1, name2 = remove_common_letters(name1, name2)
    total_letters = count_remaining_letters(name1, name2)
    result = calculate_flames(total_letters)
    display_result(result)