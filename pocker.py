import random


numbers = ["A","2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
symbols = ['♣', '♦', '♥', '♠']
strik = numbers + ['A']
players_score = []


def generate_deck(numbers,symbols):
    deck = [number + symbol for number in numbers for symbol in symbols]
    random.shuffle(deck)
    return deck

the_deck=generate_deck(numbers,symbols)

def deal_hand(the_deck, size):
    return [the_deck.pop() for _ in range(size)]

def players(amount_of_players,):
    return [deal_hand(the_deck, 2) for _ in range(int(amount_of_players))]

def put_cards_on_table(player_hands, on_table):
    all_players_cards = []
    for player_index in range(len(player_hands)):
        player_hand = player_hands[player_index]
        current_pot = player_hand + on_table[:]
        all_players_cards.append(current_pot)
    return all_players_cards



def sep_sym(num,numt,heart,tiltan,dimon,leaf):
    for i in num:
            if i == '♥' or i == '♦' or i == '♠' or i =='♣':
                if i == '♥' or i == '♦':
                    if i == '♥':
                        heart[0] +=1
                    else:
                        dimon[0] += 1
                else:
                    if i == '♠':
                        leaf[0] += 1
                    else:
                        tiltan[0] += 1
            else:
                numt += [i]
                

def card_num(stra_table,list2,list1):
    for element in list2:
        stra_table.extend([index for index, el in enumerate(list1) if el == element])
        stra_table.sort()

    
def duplicate(numbers,score,full_house,four_du):
    occurrences = {}
    stra_table = []
    for i in numbers:
        if i not in occurrences:
            occurrences[i] = 1
            stra_table.append(i)
        else:
            occurrences[i] += 1
            score[0] += (i*2)
            if occurrences[i] == 4:
                four_du[0]=True
                #1500 points to 4 duplicate
            elif occurrences[i] == 3:
                for e in occurrences.values():
                    if e == 2:
                        full_house[0]=True
                    else:
                        score[0] += 15
            


def combo(lst,score,longest_sequence):
    current_sequence = [lst[0]]

    for i in range(1, len(lst)):
        if lst[i] == lst[i - 1] + 1:
            current_sequence.append(lst[i])
        else:
            if len(current_sequence) > len(longest_sequence):
                longest_sequence = current_sequence.copy()
            current_sequence = [lst[i]]

    # Check for the last sequence
    if len(current_sequence) > len(longest_sequence):
        longest_sequence = current_sequence

    if len(longest_sequence) >= 5:
        score[0] += 90



    
        

    


def main():
    edmon = []
    amount_of_players = 4
    player_hands = players(amount_of_players)
    on_table = deal_hand(the_deck, 5)
    for i, hand in enumerate(player_hands):
        edmon_1 =hand
        edmon.append(edmon_1)
    print(edmon)
    print(on_table)
    all_players_cards = put_cards_on_table(player_hands, on_table)
    for i in all_players_cards:
        Numbers_and_symbols_separated=[]
        numt =[]
        stra_table = []
        score = [0]
        leaf =[0]
        tiltan = [0]
        heart = [0]
        dimon = [0]
        full_house = [False]
        four_du = [False]
        longest_sequence = []
        for e in i:
            if len(e) == 3:
                Numbers_and_symbols_separated.append("10")
                Numbers_and_symbols_separated.append(i[-1])
            else:
                for mon in e:
                    Numbers_and_symbols_separated += mon
        sep_sym(Numbers_and_symbols_separated,numt,heart,tiltan,dimon,leaf)
        card_num(stra_table,numt,strik)
        duplicate(stra_table,score,full_house,four_du)
        combo(stra_table,score,longest_sequence)
        for i in stra_table:
            score[0] +=i
        if len(longest_sequence) >=4 and (leaf[0] >=5 or heart[0] >=5 or dimon[0] >=5 or tiltan[0] >=5):
            score[0] += 100000
        elif four_du[0] == True:
            score[0] += 10000
        elif full_house[0] == True:
            score[0] += 1555
        elif leaf[0] >=5 or heart[0] >=5 or dimon[0] >=5 or tiltan[0] >=5:
            score[0] += 1000
        # print(score)
        players_score.append(score)

    max_number = max(players_score)
    max_number_index = [index for index, value in enumerate(players_score) if value == max_number]
    for i in max_number_index:
        i +=1
        print(f"the winner is player {i}")
        





if __name__ == "__main__":
    main()
