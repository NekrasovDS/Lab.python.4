# Вариант 8. Задание 2.
# Дан файл, содержащий текст на русском языке и некоторые два слова. Определить, сколько раз они встречаются в тексте и сколько из них – непосредственно друг за другом.

def find_word_occurrences(text, word1, word2):

    # Initialize the counters.
    word1_count = 0
    word2_count = 0
    consecutive_count = -1

    # Split the text into words.
    words = text.split()

    # Iterate over the words in the text.
    for word in words:
        # Check if the word is word1.
        if word == word1:
            # Increment the count of word1 occurrences.
            word1_count += 1

        # Check if the next word is word2.
        if word == word1 and words[words.index(word) + 1] == word2:
            # Increment the count of consecutive occurrences.
            consecutive_count += 1

        # Check if the word is word2.
        elif word == word2:
            # Increment the count of word2 occurrences.
            word2_count += 1

    # Return the counts.
    return word1_count, word2_count, consecutive_count


# Get the text from the file.
with open('C:/Python/text.txt', 'r') as f:
    wording = f.read()

# Get the two words to search for.
first_word = input('Enter the first word: ')
second_word = input('Enter the second word: ')

# Find the word occurrences.
count1, count2, count3 = find_word_occurrences(wording, first_word, second_word)

# Print the results.
print(f'{first_word} occurs {count1} times in the text.')
print(f'{second_word} occurs {count2} times in the text.')
print(f'{first_word} and {second_word} appear consecutively {count3} times in the text.')
