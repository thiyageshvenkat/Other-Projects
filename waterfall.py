import random
import time

def waterfall(alphabet, depth, width, t):
    # width: how long the waterfall should be
    # depth: how many updates per print
    # alphabet: the list of characters that can be printed
    # t: how long should the program wait after each print
    text = []
    alphabet = list(alphabet)
    for i in range(width):
        text.append(random.choice(alphabet))
    while True:
        print(*text)
        for i in range(depth):
            text[random.randrange(len(text))] = random.choice(alphabet)
        time.sleep(t)

waterfall("--------------------║", 8, 100, 0.02)
