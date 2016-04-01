'''
This script tests the value of a poker set following the texas hold 'em rules.
2016-04-01:00-13 404 lines total, 153 lines functional code without debug methods
'''
#TODO Compare hands, return the higher valued one and its value.
#If both have the same value calculate the winning hand
#TODO encode the type of tiebraker once the tiebreaking has been implemented
##Higher Straight [Flush]{Straight Flush | Straight} | Pair {Full House | Two Pair | Pair} | Three Of A Kind {Full House | Three Of A Kind}
##<x> Kicker {Four Of A Kind | Flush | Three Of A Kind | Two Pair | Pair | Highcard}
def compareHands(value1, cards1, value2, cards2):#1: a > b; 0: a == b; -1: a < b
    #Compare values. If one is higher return the winning one
    #When comparing straights (8 or 4) and an ace is apparent, skip that ace and check for the next value since the ace CAN be a one
    #If it's a full house compare the tripple
    #Else if it's four/three/two of a kind compare the highest match
    #Else sort them by value and find the one with one card higher than the other
    #Else return draw
    pass

#TODO Catch any invalid hands and return true/false
def validateHand(cards):
    #Are there impossible values?
    #Are there impossible colors?
    #Are there any duplicates?
    pass

#Evaluates the value of the given cards returning the value
#TODO return the winning cards aswell
def evalHand(cards):#return winning cards
    #Check all possibilities:
    #validate cards, if invalid exit!
    value = 0
    x, y, z = evalFullHouse(cards[:])
    tmp = []
    if(x):
        value = 3# Three of a kind
        tmp = evalOfAKind(4, cards)
        if tmp:
            cards = tmp
            value = 7
        elif(y):
            tmp = x            
            value = 6 # Full house
            if(z): #Get the biggest full house
                if z[0][0] > y[0][0]:
                    tmp.append(z[0])
                    tmp.append(z[1])
                else:
                    tmp.append(y[0])
                    tmp.append(y[1])
            else:
                tmp.append(y[0])
                tmp.append(y[1])
    if not tmp:
        tmp = evalFlush(cards)
        if tmp:
            value = 5
            straightflush = evalStraight(tmp)
            if straightflush:
                value = 8
                tmp = straightflush
                royalflush = evalRoyalFlush(straightflush)
                if royalflush:
                    value = 9
                    tmp = royalflush
        if not tmp:
            tmp = evalStraight(cards)
            if tmp:
                value = 4
            
        if not value:
            if len(y) & len(z):
                value = 2
                tmp = y
                tmp.append(z[0])
                tmp.append(z[1])
            elif len(y):
                tmp = y
                value = 1
    return value
        
                
                    
    #1. Check for full house:
        #Checks for Pair, Two Pair, Tripple and Full House
    #If at least the tripple was found check for four of a kind
    #If only tripple or less check these:
        #Flush
        #Straight
        #If either is True check:
            #Straight Flush
            #If Straight Flush check:
                #Royal Flush
    #If nothing has been true so far it's highcard

#Evaluates whether the cards contain a royal flush or not
def evalRoyalFlush(cards):
    cards = cards[:]
    cards = evalStraightFlush(cards)
    if len(cards) > 0:
        cards.sort()
        if not cards[0][0] == 10:
            cards = []
    else:
        cards = []
    return cards

#Evaluates whether the cards are a straight flush or not
def evalStraightFlush(cards):
    x = evalFlush(cards)
    if len(x) > 0:
        x = evalStraight(x)
    return x




#Evaluates if the cards contain a full house by checking for a flush and checking the returned subset for a straight            
def evalFullHouse(cards):
    cards = cards[:]
    x = evalOfAKind(3, cards)
    helper.removeCards(cards, x)
    y = evalOfAKind(2, cards)
    helper.removeCards(cards, y)
    z = evalOfAKind(2, cards)
    return x,y,z


#Checks if there is a flush and returns the first instance of a suit containing at least 5 cards
def evalFlush(cards):
    cards = cards[:]

    #initiate empty lists for the different suits
    zero = []#0
    one = []#1
    two = []#2
    three = []#3

    #Split the cards into lists based on their suit
    for card in cards:
        x = card[1]
        if x == 0:
            zero.append(card)
        elif x == 1:
            one.append(card)
        elif x == 2:
            two.append(card)
        elif x == 3:
            three.append(card)

    #Save the first suit with 5 or more members to the cards list and return it        
    if len(zero) >= 5:
        cards = zero
    elif len(one) >= 5:
        cards = one
    elif len(two) >= 5:
        cards = two
    elif len(three) >= 5:
        cards = three
    else:
        cards = []
    return cards

#Checks the cards for containing a straight and returning ONLY the found straight or an empty list
def evalStraight(cards):
    cards = cards[:]

    #Add aces as ones
    for card in cards:
        if card[0] == 14:
            cards.append([1,card[1]])
    cards.sort(reverse=True)
    
    #Remove double values
    value = -1
    nodoubles = []
    for card in cards:
        if card[0] != value:
            nodoubles.append(card)
            value = card[0]
    
    
    #Find 5 consecutive cards and save them
    count = 0
    value = -1    
    for i in range(len(nodoubles)):
        if nodoubles[i][0] == value-1:
            value = nodoubles[i][0]
            count += 1
        else:
            value = nodoubles[i][0]
            count = 1
            cards = []
        if count == 5:
            cards = nodoubles[i-4:i+1]
            count = 0
            break

    #Clean the output by replacing the one with ace and return the result  
    for card in cards:
        if card[0] == 1:
            card[0] = 14
    return cards

#Evaluate wether there is a 'n Of A Kind' in the provided cards and returns the highest valued one
def evalOfAKind(n, cards):
    cards = cards[:]
    cards.sort(reverse=True)
    value = -1
    count = 0

    #Iterate the list until it's too small
    for i in range(len(cards)):
        if cards[i][0] == value:
            count += 1
        else:
            value = cards[i][0]
            count = 1

            #If the end is unreachable, break and return
            if (len(cards) - i) < n:
                cards = []
                break

        #If a 'n Of A Kind' is found, break and return
        if count == n:
            cards = cards[i-(n-1):i+1]
            count = 0
            break
    return cards


#debug
def displayCardInfo(value, cards=[]):
    if value == 9:
        print('You have got a Royal Flush!')
    elif value == 8:
        print('You have got a Straight Flush!')
    elif value == 7:
        print('You have got Four Of A Kind!')
    elif value == 6:
        print('You have got a Full House!')
    elif value == 5:
        print('You have got a Flush!')
    elif value == 4:
        print('You have got a Straight!')
    elif value == 3:
        print('You have got Three Of A Kind!')
    elif value == 2:
        print('You have got Two Pair!')
    elif value == 1:
        print('You have got a Pair!')
    elif value == 0:
        print('You have got a High Card!')
    else:
        print('Your hand is invalid')

def play(cards):
    displayCardInfo(evalHand(cards), cards)

class helper:
    #Helper Method to subtract the 'to_delete' cards from the 'cards' list
    def removeCards(cards, to_delete):
        for card in to_delete:
            if card in cards:
                cards.remove(card)
