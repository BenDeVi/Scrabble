import random

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4,
    'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3,
    'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8,
    'y': 4, 'z': 10
}

def get_letter_value(letter):
    return SCRABBLE_LETTER_VALUES.get(letter, 0)

def deal_hand(hand_size):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    hand = random.choices(letters, k=hand_size)
    hand_dict = {}
    for letter in hand:
        hand_dict[letter] = hand_dict.get(letter, 0) + 1
    return hand_dict

def calculate_word_score(word, n):
    word_length = len(word)
    letter_sum = sum(get_letter_value(letter) for letter in word)
    second_component = 7 * word_length - 3 * (n - word_length)
    if second_component < 1:
        second_component = 1
    return letter_sum * second_component


def load_valid_words(filename):
    try:
        with open(filename, 'r') as file:
            valid_words = set(word.strip().lower() for word in file.readlines())
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        valid_words = set()
    return valid_words

def play_game(hand_size, valid_words_filename):
    hand = deal_hand(hand_size)
    n = hand_size
    valid_words = load_valid_words(valid_words_filename) 
    print("Your hand is:", hand)
    total_score = 0

    while True:
        word = input("Enter a word (or 'exit' to quit): ").lower()
        if word == "exit":
            break

        
        if word in valid_words:
            if all(hand.get(letter, 0) >= word.count(letter) for letter in word):
                word_score = calculate_word_score(word, n)
                total_score += word_score
                print(f"'{word}' is a valid word! Score for this word: {word_score}")

                for letter in word:
                    hand[letter] -= 1
                    if hand[letter] == 0:
                        del hand[letter]

                print("Remaining hand:", hand)
            else:
                print(f"'{word}' is not a valid word with the current hand.")
        else:
            print(f"'{word}' is not a valid word according to the dictionary.")

    print(f"Total score: {total_score}")

HAND_SIZE = 7
WORDS_FILE = 'words.txt' 
play_game(HAND_SIZE, WORDS_FILE)
