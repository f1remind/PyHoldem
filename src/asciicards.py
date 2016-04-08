_length = 10
_width = 11

template = [
            ' _________ ',
            '|         |',
            '|         |',
            '|         |',
            '|         |',
            '|         |',
            '|         |',
            '|         |',
            '|         |',
            ' ‾‾‾‾‾‾‾‾‾ '
            ]

cards = {'diamond':[
              ' _________ ',
              '|{:<9}|',
              '|         |',
              '|   /\    |',
              '|  /  \   |',
              '|  \  /   |',
              '|   \/    |',
              '|         |',
              '|{:>9}|',
              ' ‾‾‾‾‾‾‾‾‾ '
              ],
          'heart':[
              ' _________ ',
              '|{:<9}|',
              '|         |',
              '| /‾\/‾\  |',
              '| \    /  |',
              '|  \  /   |',
              '|   \/    |',
              '|         |',
              '|{:>9}|',
              ' ‾‾‾‾‾‾‾‾‾ '
              ],
          'spade':[
              ' _________ ',
              '|{:<9}|',
              '|    .    |',
              '|   /.\   |',
              '|  / . \  |',
              '| /  .  \ |',
              '| \_/|\_/ |',
              '|         |',
              '|{:>9}|',
              ' ‾‾‾‾‾‾‾‾‾ '
              ],
          'club':[
              ' _________ ',
              '|{:<9}|',
              '|    _    |',
              '|  _( )_  |',
              '| (_   _) |',
              '|   / \   |',
              '|   ‾‾‾   |',
              '|         |',
              '|{:>9}|',
              ' ‾‾‾‾‾‾‾‾‾ '
              ]
          }

def intToCardname(i):
    val = ''
    if i == 14:
        val = 'Ace'
    elif i == 13:
        val = 'King'
    elif i == 12:
        val = 'Queen'
    elif i == 11:
        val = 'Jack'
    else:
        val = str(i)
    return val

def printAllCards():
    for suit in cards:
        for i in range(2,15):
            print('\n' + str(i) + ' of ' + str(suit) + 's:')
            for line in cards[suit]:
                if i == 14:
                    val = 'Ace'
                elif i == 13:
                    val = 'King'
                elif i == 12:
                    val = 'Queen'
                elif i == 11:
                    val = 'Jack'
                else:
                    val = str(i)
                print(line.format(val))

def intToSuit(suit):
    output = ''
    if suit == 0:
        output = 'heart'
    elif suit == 1:
        output = 'diamond'
    elif suit == 2:
        output = 'club'
    elif suit == 3:
        output = 'spade'
    return output

def handToAscii(hand):
    output = []
    for card in hand:
        lines = []
        for line in cards[intToSuit(card[1])]:
            lines.append(line.format(card[0]))
        output.append(lines)
    return output

def printHand(hand=[]):
    if not len(hand):
        print('This is the default print without parameters to demonstrate this function')
        hand = [[14, 0], [2, 1], [3, 2], [4, 3], [5, 0]]
        print('{:+^80}'.format('Reference: this is 80 chars'))
    for card in hand:
        card[1] = intToSuit(card[1])
    for i in range(_length):
        line = ''
        for card in hand:
            line += str(cards[card[1]][i].format(intToCardname(card[0])) + ' ')
        print(line)
        



