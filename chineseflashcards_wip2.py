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
    for i in xrange(len(current)):
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
    while True: 
        # if the the current deck is empty or the timestamp on the first card of 
        # the current deck is more than the current time
        if len(current) == 0 or current[0]['time'] > datetime.datetime.now():
            # insert the first card from the waiting deck into the current deck and disply it
            display_char_and_meaning(waiting[0])
            insert_card(waiting.pop(0))
            answer = ""
            while not answer.lower() == "next":
                answer = raw_input("Please type 'next' to continue > ")
            diagnostics()
        else:
            # display the card
            display_character(current[0])
            # then prompt the user for the meaning of the card
            answer = ""
            answer = raw_input("What does this character mean? ")
            # if the answer is correct, increase the card's level
            if answer.lower() == current[0]['meaning']:
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
        
        
play_cards()
        
        
        


            