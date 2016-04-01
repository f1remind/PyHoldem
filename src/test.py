import poker
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
straightflush = [[9, 0], [10, 0], [11, 0], [12, 0], [13, 0], [5, 0], [7, 0]]
fourofakind = [[14, 0], [14, 1], [14, 2], [14, 3], [8, 2], [3, 1], [5, 0]]
fullhouse = [[5,0],[5,1],[8,1],[8,3],[8,2], [3, 1], [3,0]]
flush = [[5, 0], [3, 0], [8, 0], [7, 0], [9, 0], [11, 1], [13, 0]]
straight = [[14, 0], [6, 1], [3, 2], [4, 3], [5, 0], [13, 1], [12, 2]]
threeofakind = [[14, 0], [14, 1], [14, 2], [6, 3], [8, 2], [3, 1], [5, 0]]
twopair = [[12, 0], [12, 1], [14, 2], [14, 3], [8, 2], [3, 1], [5, 0]]
pair = [[12, 0], [4, 1], [14, 2], [14, 3], [8, 2], [3, 1], [5, 0]]
highcard =  [[6, 0], [3, 1], [5, 2], [7, 3], [9, 0], [11, 1], [13, 2]]

straightflushinferior = [[14, 0], [2, 0], [3, 0], [4, 0], [5, 0], [13, 0], [12, 0]]
fourofakindinferior = [[12, 0], [12, 1], [12, 2], [12, 3], [8, 2], [3, 1], [5, 0]]
fullhouseinferior = [[2,0],[2,1],[2,1],[3,3],[3,2], [4, 1], [4,0]]
flushinferior = [[5, 0], [3, 0], [8, 0], [7, 0], [9, 0], [11, 1], [4, 0]]
straightinferior = [[14, 0], [2, 1], [3, 2], [4, 3], [5, 0], [13, 1], [12, 2]]
threeofakindinferior = [[12, 0], [12, 1], [12, 2], [6, 3], [8, 2], [3, 1], [5, 0]]
twopairinferior = [[11, 0], [11, 1], [14, 2], [14, 3], [8, 2], [3, 1], [5, 0]]
pairinferior = [[12, 0], [4, 1], [8, 2], [8, 3], [8, 2], [3, 1], [5, 0]]
highcardinferior =  [[6, 0], [3, 1], [5, 2], [7, 3], [9, 0], [11, 1], [10, 2]]

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
halfhand = [[1,],[2]]


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
                'broken':   [emptyhand, emptycards, negativecards, duplicates, invalidcolor, invalidvalue, halfhand]
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
             'broken':['Catching Exceptions', -1]}

def test():
    errors = 0
    tests = 0
    print('{:15}{:^25}{:^20}'.format('Result', 'Hand', ' Expected:Calculated'))
    for key in testingsuite:
        for cards in testingsuite[key]:
            tests += 1
            expected = message[key][1]
            calculated = poker.evalHand(cards)
            if calculated != expected:
                print('{:<15}{:^25}{:^20} using {}'.format('!!![ERROR]!!!', message[key][0], str(expected) + ':' + str(calculated), cards))
                errors += 1
            else:
                print('{:<15}{:^25}{:^20}'.format('[SUCCESS]', message[key][0], str(expected) + ':' + str(calculated)))
    print('\n{:=^80}'.format('Completed with ' + str(errors) + ' Errors in ' + str(tests) + ' Tests.'))
