import numpy as np

def find_card_position(deck_size, instructions, card):
    deck = np.arange(deck_size)

    for instruction in instructions:
        if instruction.startswith("c"):
            n = int(instruction.split()[-1])
            deck = np.concatenate((deck[n:], deck[:n]))
        elif instruction.startswith("d"):
            deck = np.flip(deck)
        elif instruction.startswith("s"):
            half = len(deck) // 2
            new_deck = np.empty_like(deck)
            new_deck[0::2] = deck[:half]
            new_deck[1::2] = deck[half:]
            deck = new_deck

    # Find position of the card directly in the deck
    return np.where(deck == card)[0][0]
