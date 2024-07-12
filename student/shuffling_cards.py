import numpy as np

def find_card_position(deck_size, instructions, card):
    deck = np.arange(deck_size)

    # for instruction in instructions:
    #     if instruction.startswith("c"):
    #         n = int(instruction.split()[-1])
    #         deck = np.concatenate((deck[n:], deck[:n]))
    #     elif instruction.startswith("d"):
    #         deck = np.flip(deck)
    #     elif instruction.startswith("s"):
    #         half = len(deck) // 2
    #         new_deck = np.empty_like(deck)
    #         new_deck[0::2] = deck[:half]
    #         new_deck[1::2] = deck[half:]
    #         deck = new_deck

    for instruction in instructions:
        if instruction[0] == "c":  # Cut operation
            n = int(instruction.split()[-1])
            deck = np.roll(deck, -n)
        elif instruction[0] == "d":  # Deal into new stack (reverse)
            deck = deck[::-1]
        elif instruction[0] == "s":  # Shuffle operation
            half = len(deck) // 2
            # Use advanced indexing for shuffling
            deck = np.ravel(np.column_stack((deck[:half], deck[half:])))

    # Find position of the card directly in the deck
    return np.where(deck == card)[0][0]
