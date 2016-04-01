#ascii cards
length = 10
width = 11
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
            ]#10 deep, 11 wide
asciicard = \
          '''
 _________
|Ace      |
|         |
|   / \   |
|  /   \  |
|  \   /  |
|   \ /   |
|         |
|      Ace|
 ‾‾‾‾‾‾‾‾‾

 _________
|Ace      |
|         |
| /‾\_/‾\ |
| \     / |
|  \   /  |
|   \_/   |
|        |
|     Ace|
 ‾‾‾‾‾‾‾‾‾

 _________
|Ace      |
|         |
|   /‾\   |
|  /   \  |
| /     \ |
| \_/|\_/ |
|         |
|      Ace|
 ‾‾‾‾‾‾‾‾‾

 _________
|Ace      |
|         |
|  _|‾|_  |
| |_   _| |
|   / \   |
|   ‾‾‾   |
|         |
|      Ace|
 ‾‾‾‾‾‾‾‾‾ 

          '''
cards = {'diamond':[
              ' _________ ',
              '|{:<9}|',
              '|         |',
              '|   / \   |',
              '|  /   \  |',
              '|  \   /  |',
              '|   \ /   |',
              '|         |',
              '|{:>9}|',
              ' ‾‾‾‾‾‾‾‾‾ '
              ],
          'heart':[
              ' _________ ',
              '|{:<9}|',
              '|         |',
              '| /‾\_/‾\ |',
              '| \     / |',
              '|  \   /  |',
              '|   \_/   |',
              '|         |',
              '|{:>9}|',
              ' ‾‾‾‾‾‾‾‾‾ '
              ],
          'spade':[
              ' _________ ',
              '|{:<9}|',
              '|         |',
              '|   /‾\   |',
              '|  /   \  |',
              '| /     \ |',
              '| \_/|\_/ |',
              '|         |',
              '|{:>9}|',
              ' ‾‾‾‾‾‾‾‾‾ '
              ],
          'club':[
              ' _________ ',
              '|{:<9}|',
              '|         |',
              '|  _|‾|_  |',
              '| |_   _| |',
              '|   / \   |',
              '|   ‾‾‾   |',
              '|         |',
              '|{:>9}|',
              ' ‾‾‾‾‾‾‾‾‾ '
              ]
          }
def printcards():
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


def inttosuit(suit):
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
def handtoascii(hand):
    output = []
    for card in hand:
        lines = []
        for line in cards[inttosuit(card[1])]:
            lines.append(line.format(card[0]))
        output.append(lines)
    return output
def printhand(hand=[]):
    if not len(hand):
        hand = [[14, 0], [2, 1], [3, 2], [4, 3], [5, 0]]
    print('{:+^80}'.format('Reference: this is 80 chars'))
    for card in hand:
        card[1] = inttosuit(card[1])
    for i in range(length):
        line = ''
        for card in hand:
            line += str(cards[card[1]][i].format(card[0]) + ' ')
        print(line)
        
