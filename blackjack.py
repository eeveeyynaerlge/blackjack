deck = [] # Create a deck of cards
from random import shuffle
for a in range (1, 4):
    for card in range(1, 14):
        if card > 10:
            card = 10
        if card == 1:
            card = 11 
        deck.append(card)
shuffle(deck)
card1 = deck.pop(0)
card2 = deck.pop(0)
card3 = 0
card4 = 0
card5 = 0

while card1 + card2 + card3 + card4 + card5 < 21: # Player's turn
    print("Your cards are: ", card1, card2, card3, card4, card5)
    print("Your total is: ", card1 + card2 + card3 + card4 + card5)
    print("Hit or stay?")
    choice = input()
    if choice == "hit":
        if card3 == 0:
            card3 = deck.pop(0)
        elif card4 == 0:
            card4 = deck.pop(0)
        elif card5 == 0:
            card5 = deck.pop(0)
        else:
            break
    elif choice == "stay":
        break
    if card1 + card2 + card3 + card4 + card5 > 21 and (card1 == 11 or card2 == 11 or card3 == 11 or card4 == 11 or card5 == 11):
        if card1 == 11:
            card1 = 1
        elif card2 == 11:
            card2 = 1
        elif card3 == 11:
            card3 = 1
        elif card4 == 11:
            card4 = 1
        elif card5 == 11:
            card5 = 1


dcard1 = deck.pop(0)
dcard2 = deck.pop(0)
dcard3 = 0
dcard4 = 0
dcard5 = 0

while dcard1 + dcard2 + dcard3 + dcard4 + dcard5 < card1 + card2 + card3 + card4 + card5 and dcard1 + dcard2 + dcard3 + dcard4 + dcard5 < 21: 
    # Dealer's turn
    if dcard3 == 0:
        dcard3 = deck.pop(0)
    elif dcard4 == 0:
        dcard4 = deck.pop(0)
    elif dcard5 == 0:
        dcard5 = deck.pop(0)
    else:
        break

print("Your cards were: ", card1, card2, card3, card4, card5) #end of game
print("Your total was: ", card1 + card2 + card3 + card4 + card5)
print("Dealer's cards were: ", dcard1, dcard2, dcard3, dcard4, dcard5)
print("Dealer's total was: ", dcard1 + dcard2 + dcard3 + dcard4 + dcard5)

if card1 + card2 + card3 + card4 + card5 > 21:
    print("You busted!")
elif dcard1 + dcard2 + dcard3 + dcard4 + dcard5 > 21:
    print("Dealer busted!")
elif card1 + card2 + card3 + card4 + card5 > dcard1 + dcard2 + dcard3 + dcard4 + dcard5:
    print("You win!")
elif card1 + card2 + card3 + card4 + card5 < dcard1 + dcard2 + dcard3 + dcard4 + dcard5:
    print("Dealer wins!")
else:
    print("It's a tie!")

print("Thanks for playing!")