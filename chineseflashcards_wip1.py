import string
import datetime

from decks_wip1 import *
from timelevels import *


# helper functions

def insert_card(card):
    # add a timestamp to the card based on its level
    seconds_added = timelevels[card['level']]
    card['time'] = datetime.datetime.now() + datetime.timedelta(seconds=seconds_added)
    # and add it into the current deck
    added = False
    for i in range(len(current)):
        if current[i]['time'] > card['time']:
            current.insert(i, card)
            added = True
            break
    if added == False:
        current.append(card)
    
    
def display_character(card):
    print "Remember this one?"
    print card['character']
    
def display_char_and_meaning(card):
    print "The next character is:"
    print card['character']
    print "Which means:"
    print card['meaning']
    
def diagnostics():
    print
    print "the current deck contains the following cards: ",
    for c in current:
        print c['character'],
    print
    print


# main function

def play_cards():
    # if there are no cards in the current deck
    if len(current) == 0:
        # take the card at the beginning of the waiting deck,
        # display it, and add it to the current deck
        card = waiting.pop(0)
        display_char_and_meaning(card)
        seconds_added = timelevels[card['level']]
        card['time'] = datetime.datetime.now() + datetime.timedelta(seconds=seconds_added)
        current.append(card)
        answer = ""
        while not answer == "next":
            answer = raw_input("Please type 'next' to continue > ")
        diagnostics()
        
    # otherwise
    while True: 
        # if the timestamp on the first card of the current deck is less than
        # or equal to the current time, display the card
        if current[0]['time'] <= datetime.datetime.now():
            display_character(current[0])
            # then prompt the user for the meaning of the card
            answer = ""
            answer = raw_input("What does this character mean? ")
            # if the answer is correct, increase the card's level
            if answer == current[0]['meaning']:
                print "That's correct!"
                current[0]['level'] += 1
            # else lower the card's level
            else:
                print "Nope - better luck next time!"
                if current[0]['level'] > 0:
                    current[0]['level'] -= 1
            # and reinsert it into the deck
            insert_card(current.pop(0))
            diagnostics()
            
        # else insert the first card from the waiting list
        # into the current list and disply it
        else:
            display_char_and_meaning(waiting[0])
            insert_card(waiting.pop(0))
            answer = ""
            while not answer == "next":
                answer = raw_input("Please type 'next' to continue > ")
            diagnostics()
        
        
play_cards()
        
        
        


            