import random

def main():
    numbers = [16.2, 75.1, 52.3]
    words_list = ["dog", "cat", "bird"]

    print(numbers)
    print(words_list)

    append_random_numbers(numbers)
    print(numbers)

    append_random_numbers(numbers, 3)
    print(numbers)

    append_random_words(words_list)
    print(words_list)

    append_random_words(words_list, 3)
    print(words_list)

def append_random_numbers(numbers_list, quantity = 1):
    """Append quantity random numbers onto the numbers list.
    The random numbers are between 0 and 100, inclusive.
    Parameters
        numbers_list: A list of numbers where this function will
            append random numbers.
        quantity: The number of random numbers that this function
            will append onto numbers_list.
    Return: nothing. It's unnecessary for this function to return
        anything because this function changes the numbers_list.
    """
    for _ in range(quantity):
        random_number = random.uniform(0, 100)
        numbers_list.append(round(random_number, 1))

def append_random_words(words_list, quantity = 1):
    """Append quantity randomly chosen words onto the words list.
    Parameters
        words_list: A list of words where this function will
            append random words.
        quantity: The number of random words that this function
            will append onto words_list.
    Return: nothing. It's unnecessary for this function to return
        anything because this function changes the words_list.
    """
    words = [
        "dog", "cat", "bird", "elephant", "snake", "fish", "rabbit", "turtle", "hamster", "lizard",
        "mouse", "horse", "cow", "pig", "goat", "sheep", "chicken", "duck", "goose", "deer",
        "fox", "wolf", "bear", "lion", "tiger", "leopard", "zebra", "giraffe", "monkey", "kangaroo",
        "penguin", "seal", "whale", "dolphin", "shark", "octopus", "squid", "jellyfish", "starfish",
        "crab", "lobster", "spider", "bee", "ant", "butterfly", "dragonfly", "mosquito", "snail",
        "worm", "apple", "banana", "orange", "strawberry", "blueberry", "grape", "watermelon", "pineapple", "kiwi",
        "peach", "pear", "plum", "cherry", "lemon", "lime", "coconut", "mango", "papaya", "fig",
        "date", "avocado", "broccoli", "carrot", "cucumber", "lettuce", "potato", "tomato", "onion", "garlic",
        "pepper", "pumpkin", "eggplant", "corn", "peas", "beans", "rice", "bread", "pasta", "cheese"
    ]

    for _ in range(quantity):
        word = random.choice(words)
        words_list.append(word)

if __name__ == "__main__":
    main()

