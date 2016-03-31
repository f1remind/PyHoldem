'''
This script tests the value of a poker set following the texas hold 'em rules.
2016-04-01:00-13 404 lines total, 153 lines functional code without debug methods
'''
#TODO
#Use 14 for ace and only check ace for 1 in straight

#Test hands:
'''
Testcases:
One hand for every case (Royal Flush to high card)
Every evaluation should only return what it is supposed to do.
evalPair should only find a pair etc.
Uncommon hands should work with all evals but be stopped at verifyHand:
-Too many cards
-Invalid Color (4, -1, 10, 999999999999)
-Invalid Value (15, -1, 1, 0, 99999999999)
-Duplicate Cards

Hands to check and break once the best is found:
9. Royal Flush
8. Straight Flush
7. Four of a kind
6. Full house
5. Flush
4. Straight
3. Three of a kind
2. Two Pair
1. Pair
0. High card
'''
#Full hands, 7 cards
#Wanted cards right in the beginning
royalflush = [[10, 0], [11, 0], [12, 0], [13, 0], [14, 0], [2, 0], [3, 0]]
straightflush = [[14, 0], [2, 0], [3, 0], [4, 0], [5, 0], [13, 0], [12, 0]]
fourofakind = [[14, 0], [14, 1], [14, 2], [14, 3], [8, 2], [3, 1], [5, 0]]
fullhouse = [[1,0],[1,1],[2,2],[2,3],[2,2], [3, 1], [3,0]]
flush = [[1, 0], [3, 0], [5, 0], [7, 0], [9, 0], [11, 1], [13, 0]]
straight = [[14, 0], [2, 1], [3, 2], [4, 3], [5, 0], [13, 1], [12, 2]]
threeofakind = [[14, 0], [14, 1], [14, 2], [1, 3], [8, 2], [3, 1], [5, 0]]
twopair = [[12, 0], [12, 1], [14, 2], [14, 3], [8, 2], [3, 1], [5, 0]]
pair = [[12, 0], [4, 1], [14, 2], [14, 3], [8, 2], [3, 1], [5, 0]]
highcard =  [[1, 0], [3, 1], [5, 2], [7, 3], [9, 0], [11, 1], [13, 2]]

from random import shuffle
royalflushshuffled = royalflush[:]
straightflushshuffled = straightflush[:]
fourofakindshuffled = fourofakind[:]
fullhouseshuffled = fullhouse[:]
flushshuffled = flush[:]
straightshuffled = straight[:]
threeofakindshuffled = threeofakind[:]
twopairshuffled = twopair[:]
pairshuffled = pair[:]
highcardshuffled = highcard[:]
shuffle(royalflushshuffled)
shuffle(straightflushshuffled)
shuffle(fourofakindshuffled)
shuffle(fullhouseshuffled)
shuffle(flushshuffled)
shuffle(straightshuffled)
shuffle(threeofakindshuffled)
shuffle(twopairshuffled)
shuffle(pairshuffled)
shuffle(highcardshuffled)

royalflushend = royalflush[::-1]
straightflushend = straightflush[::-1]
fourofakindend = fourofakind[::-1]
fullhouseend = fullhouse[::-1]
flushend = flush[::-1]
straightend = straight[::-1]
threeofakindend = threeofakind[::-1]
twopairend = twopair[::-1]
pairend = pair[::-1]
highcardend = highcard[::-1]

#River, 5 cards, short names
royal = royalflush[:5]
sflush = straightflush[:5]
fourkind = fourofakind[:5]
house = fullhouse[:5]
flu = flush[:5]
strai = straight[:5]
threekind = threeofakind[:5]
twotwokind = twopair[:5]
twokind = pair[:5]
high = highcard[:5]
#Minimum, unless 5 is the minimum only add as little as possible here
four = [[14, 0], [14, 1], [14, 2], [14, 3]]
three = [[7, 0], [7, 1], [7, 3]]
twop = [[4, 0], [2, 1], [4, 1], [2, 2]]
p = [[4, 0], [4, 1]]
hi = [[6,0]]
#Invalid hands
emptyhand = []
emptycards = [[],[],[],[]]
negativecards = [[-1, -1]]
duplicates = [[1,2],[1,2]]
invalidcolor = [[1,2],[1, -1],[1,5],[1,9999999999999]]
invalidvalue = [[-1,2],[15,1],[999999999999,3]]


testingsuite = {'royalflush': [royalflush, royalflushshuffled, royalflushend, royal],
                'straightflush': [straightflush, straightflushshuffled, straightflushend, sflush],
                'fourofakind': [fourofakind, fourofakindshuffled, fourofakindend, fourkind, four],
                'fullhouse': [fullhouse, fullhouseshuffled, fullhouseend, house],
                'flush': [flush, flushshuffled, flushend, flu],
                'straight': [straight, straightshuffled, straightend, strai],
                'threeofakind': [threeofakind, threeofakindshuffled, threeofakindend, threekind, three],
                'twopair': [twopair, twopairshuffled, twopairend, twotwokind, twop],
                'pair': [pair, pairshuffled, pairend, twokind, p],
                'highcard': [highcard, highcardshuffled, highcardend, high, hi],
                #,'broken':   [emptyhand, emptycards, negativecards, duplicates, invalidcolor, invalidvalue]
                }



message = {'royalflush':['Royal Flush', 9],
             'straightflush':['Straight Flush', 8],
             'fourofakind':['Four Of A Kind', 7],
             'fullhouse':['Full House', 6],
             'flush':['Flush',5],
             'straight':['Straight',4],
             'threeofakind':['Three Of A Kind',3],
             'twopair':['Two Pair',2],
             'pair':['Pair',1],
             'highcard':['High Card',0],
             'broken':''}



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

#Helper Method to subtract the 'to_delete' cards from the 'cards' list
def removeCards(cards, to_delete):
    for card in to_delete:
        if card in cards:
            cards.remove(card)


#Evaluates if the cards contain a full house by checking for a flush and checking the returned subset for a straight            
def evalFullHouse(cards):
    cards = cards[:]
    #evalOfAKind sorts descending and returns the most valuable match first
    x = evalOfAKind(3, cards)
    removeCards(cards, x)
    y = evalOfAKind(2, cards)
    removeCards(cards, y)
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
def test():
    print('{:28}Expected:Calculated\n'.format('Testing possible hands:'))
    for key in testingsuite:
        for cards in testingsuite[key]:
            expected = message[key][1]
            calculated = evalHand(cards)
            if calculated != expected:
                print('!!![ERROR]!!! at: {:<25}{}:{} using {}'.format(message[key][0], expected, calculated, cards))
            else:
                print('[SUCCESS] {:<25}{}:{} using {}'.format(message[key][0], expected, calculated, cards))