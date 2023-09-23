# Daniel Elsborg Johnsen, djohns22@student.aau.dk, cs-22-dvml-1-p1-01
# Programmet er ikke baseret på fælles arbejde i gruppen

from random import shuffle

class Card:
    suits = ["clubs", "diamonds", "hearts", "spades"]
    values = [None, None,"2","3","4","5","6","7","8","9","10","jack","queen","king","ace"]
    
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    # __gt__ er en speciel metode der beskriver "greater than" operatøren. Den sammenligner to kort og bestemmer hvorvidt det nuværende kort er højere end et andet kort eller ej
    def __gt__(self, other):
        if self.suit > other.suit:
            return True
        if self.suit == other.suit:
            if self.value > other.value:
                return True
            else:
                return False
        return False

    # Metoden returner objekt repræsentationen i strengformat
    def __repr__(self):
        return self.values[self.value] + " of " + self.suits[self.suit]

class Deck:
    def __init__(self):
        self.cards = []
        # Generer kortene
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i,j))
        # Bland kortene
        shuffle(self.cards)
    

class Player:
    def __init__(self, name):
        self.wins = 0
        self.cards = []
        self.name = name

class Game:
    def __init__(self):
        self.players = []
        # Tilføjer spillerne
        for i in range(1, int(input("amount of players: ")) + 1):
            self.players.append(Player(input("player number {}'s name: ".format(i))))
        # Laver et eksempel af Deck() klassen
        self.deck = Deck()
        
    def play_game(self):
        deck = self.deck.cards
        players = self.players
        print("beginning game")
        print("drawing cards")
        # Fjerner kortene der er tilovers, efter alle har fået lige mange
        deck = deck[:len(deck) - len(deck) % len(players)]
        for i in range(len(players)):
            players[i].cards = (deck[i::len(players)])
        print("cards drawn")
        
        # i er runde
        for i in range(1,11):
            print("\n\nnew round")
            # Tjekker om en spiller er løbet tør for kort
            new_players = []
            for player in players:
                if len(player.cards) != 0:
                    new_players.append(player)
                else:
                    print("{} has run out of cards and has been removed from the game".format(player.name))
            players = new_players
            
            # Beder hver spiller om at vælge et af deres kort ud fra kortets index position i listen
            cards_picked = []
            for j in range(len(players)):
                print("{}'s turn".format(players[j].name))
                print(players[j].cards)
                picked_card_index = int(input("pick index of one of your cards: "))
                cards_picked.append(players[j].cards[picked_card_index])
                players[j].cards.pop(picked_card_index)
                print("\n")
            
            # Udregner det højeste kort ud fra de valgte kort
            highest_card = None
            for card in cards_picked:
                if highest_card is None:
                    highest_card = card
                elif card > highest_card:
                    highest_card = card
            print("{} was the highest card".format(highest_card))
            print("{} won round {}".format(players[cards_picked.index(highest_card)].name, i))
            
            # Spilleren der valgte det højeste kort, for alle kortene spillet i runden
            for card in cards_picked:
                players[cards_picked.index(highest_card)].cards.append(card)
            
        # Efter alle runder udregnes hvem der har flest kort
        player_with_most_cards = []
        draw = False
        for player in players:
            if len(player_with_most_cards) == 0:
                player_with_most_cards = [player.name, len(player.cards)]
            elif len(player.cards) > int(player_with_most_cards[1]):
                player_with_most_cards = [player.name, len(player.cards)]
            elif len(player.cards) == int(player_with_most_cards[1]):
                draw = True
                player_with_most_cards = [player_with_most_cards[0], player.name, len(player.cards)]
        
        # Hvis de to spillere med flest kort har lige mange kort er draw=True
        if draw:
            return "\nThe game ended in a draw between {} and {}, who both got {} cards".format(player_with_most_cards[0], player_with_most_cards[1], player_with_most_cards[2])
        else:
            return "\nThe winner with most cards after 10 rounds is {} with {} cards".format(player_with_most_cards[0], player_with_most_cards[1])
                
        
# Kalder metoden play_game() fra klassen Game()
print(Game().play_game())