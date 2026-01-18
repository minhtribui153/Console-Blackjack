import random
from time import sleep

import utils


def run(cards_at_hand = 2):
    print("Shuffling...\n")

    deck = utils.create_deck()

    for _ in range(len(deck)^2):
        random.shuffle(deck)

    def perform_card_action():
        while deck[0].card_type == "A":
            random.shuffle(deck)
        return deck.pop(0)

    player_card = [perform_card_action() for _ in range(cards_at_hand)]
    dealer_card = [perform_card_action() for _ in range(cards_at_hand)]

    while True:
        utils.show_player_info(player_card)
        print('Your move. ["hit", "stay", or "quit"]')
        choice = input(">>> ")
        while choice not in ["hit", "stay", "quit"]:
            print("Invalid choice. Try again.")
            choice = input(">>> ")
        if choice == "quit":
            utils.show_player_info(player_card, dealer_card)
            print("You left the game! Dealer wins!")
            exit(0)

        elif choice == "hit":
            drawed_card = deck.pop(0)
            print("You drawed: ")
            print(drawed_card)
            sleep(1.5)
            if drawed_card.card_type == "A":
                # Ask user to choose the value of the Ace card. Either 1, 10 or 11
                value = input("Choose the value of the Ace card. [1, 10, or 11]: ")
                while value not in ["1", "10", "11"]:
                    print("Invalid choice. Try again.")
                    value = input("Choose the value of the Ace card. [1, 10, or 11]: ")
                drawed_card.a_value = int(value)
                print("Please wait...")
                sleep(0.5)

            player_card.append(drawed_card)
            player_score = sum(card.get_value() for card in player_card)

            if player_score > 21:
                print("Your score > 21. Dealer's turn next!")
            elif len(player_card) > 9:
                print("Max cards reached! Dealer's turn next!")
            if len(player_card) > 9 or player_score > 21:
                sleep(1.5)
                break
        else:
            break

    player_score = sum(card.get_value() for card in player_card)
    dealer_score = sum(card.get_value() for card in dealer_card)

    if player_score == 21:
        print("Blackjack!")
        sleep(1)

    utils.show_player_info(player_card)
    print("Please wait...")
    sleep(2)

    # Dealer's turn
    print("Dealer's move.")
    sleep(1)
    while dealer_score < 17:
        print("Dealer chose to hit...")
        sleep(1)

        new_card = deck.pop(0)
        print("Dealer drawed: ")
        print(new_card)
        sleep(1.5)
        if new_card.card_type == "A":
            if dealer_score > 11:
                new_card.a_value = 1
            elif dealer_score > 7:
                new_card.a_value = 10
            else:
                new_card.a_value = random.choice([10, 11])
            print(f"Dealer chose value of A to be {new_card.a_value}")
            sleep(1)
        dealer_card.append(new_card)
        dealer_score = sum(card.get_value() for card in dealer_card)
    print("Dealer chose to stay...")
    sleep(1)

    if dealer_score == 21:
        print("Blackjack!")
        sleep(1)

    utils.show_player_info(player_card, dealer_card)
    print("Please wait...")
    sleep(2)

    # Get winning information
    if player_score > 21 and dealer_score > 21:
        if player_score < dealer_score:
            print("You win! Your score < Dealer")
        elif dealer_score < player_score:
            print("Dealer wins! Your score > Dealer")
        else:
            print("Draw! Your score = Dealer")
    elif player_score > 21:
        print("Dealer wins! Your score > 21")
    elif dealer_score > 21:
        print("You win! Dealer's score > 21")
    elif player_score > dealer_score:
        print("You win! Your score > Dealer")
    elif player_score < dealer_score:
        print("Dealer wins! Your score < Dealer")
    else:
        print("Draw! Your score = Dealer")

running = True
while running:
    run()
    play_again = input("Do you want to play again? [y/n]: ")
    while play_again not in ["y", "n"]:
        play_again = input("Do you want to play again? [y/n]: ")
    running = play_again == "y"
