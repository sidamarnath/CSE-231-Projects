######################################################
# Project #6
# Algorithm
# Design a basic poker game
######################################################

import cards

def less_than(c1,c2):
    '''Return 
           True if c1 is smaller in rank, 
           True if ranks are equal and c1 has a 'smaller' suit
           False otherwise'''
    if c1.rank() < c2.rank():
        return True
    elif c1.rank() == c2.rank() and c1.suit() < c2.suit():
        return True
    return False
    
def min_in_list(L):
    '''Return the index of the mininmum card in L'''
    min_card = L[0]  # first card
    min_index = 0
    for i,c in enumerate(L):
        if less_than(c,min_card):  # found a smaller card, c
            min_card = c
            min_index = i
    return min_index
        
def cannonical(H):
    ''' Selection Sort: find smallest and swap with first in H,
        then find second smallest (smallest of rest) and swap with second in H,
        and so on...'''
    for i,c in enumerate(H):
        # get smallest of rest; +i to account for indexing within slice
        min_index = min_in_list(H[i:]) + i 
        H[i], H[min_index] = H[min_index], c  # swap
    return H

def flush_7(H):
    '''Return a list of 5 cards forming a flush,
       if at least 5 of 7 cards form a flush in H, a list of 7 cards, 
       False otherwise.'''
    # create empty lists for suits
    suit_1 = []
    suit_2 = []
    suit_3 = []
    suit_4 = []
    # for each card in H
    for card in H:
        # appending card to list if suits match
        if card.suit() == 1:
            suit_1.append(card)
        if card.suit() == 2:
            suit_2.append(card)
        if card.suit() == 3:
            suit_3.append(card)
        if card.suit() == 4:
            suit_4.append(card)
    # returning 5 cards
    # returns false if none passes
    if len(cannonical(suit_1)) >= 5:
        return suit_1[:5]
    if len(cannonical(suit_2)) >= 5:
        return suit_2[:5]
    if len(cannonical(suit_3)) >= 5:
        return suit_3[:5]
    if len(cannonical(suit_4)) >= 5:
        return suit_4[:5]
    return False

def straight_7(H):
    '''Return a list of 5 cards forming a straight,
       if at least 5 of 7 cards form a straight in H, a list of 7 cards, 
       False otherwise.'''
    # create empty dictionary
    # create empty lists
    temp_map = {}
    rank_list = []
    consecutive = []
    ret_list = []
    
    # goes through each card in H
    for card in H:
        # setting rank of card as key
        temp_map[card.rank()] = card
    
    rank_list = temp_map.keys()
    # sorting rank list
    rank_list = sorted(rank_list)
    
    prev_value = rank_list[0]
    
    # for each x in rank list
    for x in rank_list:
        if x - prev_value == 1:
            if prev_value not in consecutive:
                consecutive.append(prev_value)
            consecutive.append(x)
            prev_value = x
            # grabbing 5 cards
            if len(consecutive) == 5:
                break
    
    if len(consecutive) != 5:
        return False
    else:
        for x in consecutive:
            ret_list.append(temp_map.get(x))
        
        return ret_list
        
def straight_flush_7(H):
    '''Return a list of 5 cards forming a straight flush,
       if at least 5 of 7 cards form a straight flush in H, a list of 7 cards, 
       False otherwise.'''
    # create empty lists for suits
    suit_1 = []
    suit_2 = []
    suit_3 = []
    suit_4 = []
    ret_list = []
    # for each card in H
    for card in H:
        # appending card to list if suits match
        if card.suit() == 1:
            suit_1.append(card)
        if card.suit() == 2:
            suit_2.append(card)
        if card.suit() == 3:
            suit_3.append(card)
        if card.suit() == 4:
            suit_4.append(card)
    # checking len of suit to be 5 or greater
    if len(suit_1) >= 5:
        ret_list = suit_1
        
    if len(suit_2) >= 5:
        ret_list = suit_2
        
    if len(suit_3) >= 5:
        ret_list = suit_3
        
    if len(suit_4) >= 5:
        ret_list = suit_4
    
    ret_list = straight_7(H)
    
    if ret_list == False:
        return False
    else:
        return ret_list
    
    
def four_7(H):
    '''Return a list of 4 cards with the same rank,
       if 4 of the 7 cards have the same rank in H, a list of 7 cards, 
       False otherwise.'''
    # return list set as empty
    ret_list = []
    index = 0
    # goes through each card in the hand
    for card in H:
        comp_card = H[index]
        index += 1
        count = 1
        # reset return list 
        ret_list.clear()
        # cycles through each card in rest of hand
        for sub_card in H[index:]:
            # if card rank is same, the count increases by 1
            if comp_card.rank() == sub_card.rank():
                count += 1
                # adding furst card into return list
                if comp_card not in ret_list:
                    ret_list.append(comp_card)
                ret_list.append(sub_card)
            # set count = 4 for number of cards
            if count == 4:
                return ret_list           
    return False

def three_7(H):
    '''Return a list of 3 cards with the same rank,
       if 3 of the 7 cards have the same rank in H, a list of 7 cards, 
       False otherwise.
       You may assume that four_7(H) is False.'''
    # return list set as empty
    ret_list = []
    index = 0
    # goes through each card in the hand
    for card in H:
        comp_card = H[index]
        index += 1
        count = 1
        # reset return list 
        ret_list.clear()
        # cycles through each card in rest of hand
        for sub_card in H[index:]:
            # if card rank is same, the count increases by 1
            if comp_card.rank() == sub_card.rank():
                count += 1
                # adding furst card into return list
                if comp_card not in ret_list:
                    ret_list.append(comp_card)
                ret_list.append(sub_card)
            # set count = 3 for number of cards
            if count == 3:
                return ret_list           
    return False
        
def two_pair_7(H):
    '''Return a list of 4 cards that form 2 pairs,
       if there exist two pairs in H, a list of 7 cards, 
       False otherwise.  
       You may assume that four_7(H) and three_7(H) are both False.'''
    # pair list set to empty
    pair_list = []
    index = 0
    # cycles through each card in the hand
    for card in H:
        # first card is comparing card
        comparing_card = H[index]
        index = index + 1
        # syscles through remaining cards
        for subset_card in H[index : 7]:
            # checks for equal rank
            if comparing_card.rank() == subset_card.rank():
                # adds cards to pair list
                if comparing_card not in pair_list:
                    pair_list.append(comparing_card)
                if subset_card not in pair_list:
                    pair_list.append(subset_card)
    # checks for two pairs
    if len(pair_list) >= 4:
        return pair_list
    else:
        return False

def one_pair_7(H):
    '''Return a list of 2 cards that form a pair,
       if there exists exactly one pair in H, a list of 7 cards, 
       False otherwise.  
       You may assume that four_7(H), three_7(H) and two_pair(H) are False.'''
    # return list set as empty
    ret_list = []
    index = 0
 
    
    # goes through each card in the hand
    for card in H:
        comp_card = H[index]
        index += 1
        count = 1
        # reset return list 
        #ret_list.clear()
        # cycles through each card in rest of hand
        for sub_card in H[index:]:
            # if card rank is same, the count increases by 1
            if comp_card.rank() == sub_card.rank():
                count += 1
                # adding furst card into return list
                if comp_card not in ret_list:
                    ret_list.append(comp_card)
                if sub_card not in ret_list:
                    ret_list.append(sub_card)
                    
    l1 = three_7(H)
    # if 3 is found, remove from list
    if l1 != False:
        for i in l1:
            ret_list.remove(i)
    if len(ret_list) >0:
        return ret_list
    else:
        return False

def full_house_7(H):
    '''Return a list of 5 cards forming a full house,
       if 5 of the 7 cards form a full house in H, a list of 7 cards, 
       False otherwise.
       You may assume that four_7(H) is False.'''    
    # calls three of a kind and one pair functions
    three_kind = three_7(H)
    one_pair = one_pair_7(H)
    
    # if statement to check for true/false
    if three_kind == False or one_pair == False:
        return False   
    else:
        # return combination of both functions results
        return cannonical(one_pair + three_kind)[:5]

 #--------------------------------------------------------------------------       
    
def main():
    
    # c1 = cards.Card(2,3)
    # c2 = cards.Card(3,3)
    # c3 = cards.Card(1,4)
    # c4 = cards.Card(2,1)
    # c5 = cards.Card(3,4)
    # c_list = [c1,c2,c3,c4,c5]
    
    # c6 = cards.Card(2,2)
    # c7 = cards.Card(1,2)
    
    # c8 = cards.Card(8,4)
    # c9 = cards.Card(1,1)

    # h1 = [c6,c7]
    # h2 = [c8,c9]
    
    # print("Community cards:",c_list)
    # print("Player 1:",h1)
    # print("Player 2:",h2)
    
    # L1 = full_house_7(h1 + c_list)
    # L2 = full_house_7(h2 + c_list)
    # print(L1)
    # print(L2)
    
    
    D = cards.Deck()
    D.shuffle()
      
    count = 0
     
    while True:
        # create community cards
        # create Player 1 hand
        # create Player 2 hand
        hand_1_list = []
        hand_2_list = []
        community_list = []
        
        # check for less than ideal cards
        if len(D) < 9:
            print("Deck has too few cards so game is done.")
            break

        choice = ''
        if count != 0:
            choice = input("Do you wish to play another hand?(Y or N) ")
            
        if choice.lower() == 'n':
            break
        count += 1
        
        # dealing community list
        for i in range(5):
            community_list.append(D.deal())
        
        # dealing both player two cards 
        for j in range(2):
            hand_1_list.append(D.deal())
        for k in range(2):
            hand_2_list.append(D.deal())
        
        
        print("-"*40)
        print("Let's play poker!\n")
        print("Community cards:",community_list)
        print("Player 1:",hand_1_list)
        print("Player 2:",hand_2_list)
        print()
        
        # printing hand list and community list
        h1 = hand_1_list + community_list
        h2 = hand_2_list + community_list
        
        # testing rank of hands for each player
        L1 = straight_flush_7(h1) 
        L2 = straight_flush_7(h2)
        if L1 and L2:
            print("TIE with a straight flush:", cannonical(L1))
            continue
        elif L1 and not L2:
            print("Player 1 wins with straight flush:", cannonical(L1))
            continue
        elif not L1 and L2:
            print("Player 2 wins with straight flush:", cannonical(L2))
            continue
        else:
            do_nothing = True
        
        L1 = four_7(h1) 
        L2 = four_7(h2)
        if L1 and L2:
            print("TIE with four of a kind:", cannonical(L1))
            continue
        elif L1 and not L2:
            print("Player 1 wins with four of a kind:", cannonical(L1))
            continue
        elif not L1 and L2:
            print("Player 2 wins with four of a kind:", cannonical(L2))
            continue
        else:
            do_nothing = True
            
            
        L1 = full_house_7(h1) 
        L2 = full_house_7(h2)
        if L1 and L2:
            print("TIE with a full house:", cannonical(L1))
            continue
        elif L1 and not L2:
            print("Player 1 wins with a full house:", cannonical(L1))
            continue
        elif not L1 and L2:
            print("Player 2 wins with a full house:", cannonical(L2))
            continue
        else:
            do_nothing = True
            
        L1 = flush_7(h1) 
        L2 = flush_7(h2)
        if L1 and L2:
            print("TIE with a flush:", cannonical(L1))
            continue
        elif L1 and not L2:
            print("Player 1 wins with a flush:", cannonical(L1))
            continue
        elif not L1 and L2:
            print("Player 2 wins with a flush:", cannonical(L2))
            continue
        else:
            do_nothing = True
            
        L1 = straight_7(h1) 
        L2 = straight_7(h2)
        if L1 and L2:
            print("TIE with a straight:", cannonical(L1))
            continue
        elif L1 and not L2:
            print("Player 1 wins with a straight:", cannonical(L1))
            continue
        elif not L1 and L2:
            print("Player 2 wins with a straight:", cannonical(L2))
            continue
        else:
            do_nothing = True
            
        L1 = three_7(h1) 
        L2 = three_7(h2)
        if L1 and L2:
            print("TIE with 3 of a kind:", cannonical(L1))
            continue
        elif L1 and not L2:
            print("Player 1 wins with 3 of a kind:", cannonical(L1))
            continue
        elif not L1 and L2:
            print("Player 2 wins with 3 of a kind:", cannonical(L2))
            continue
        else:
            do_nothing = True
            
        L1 = two_pair_7(h1) 
        L2 = two_pair_7(h2)
        if L1 and L2:
            print("TIE with two pairs:", cannonical(L1))
            continue
        elif L1 and not L2:
            print("Player 1 wins with two pair:", cannonical(L1))
            continue
        elif not L1 and L2:
            print("Player 2 wins with two pair:", cannonical(L2))
            continue
        else:
            do_nothing = True
        
        L1 = one_pair_7(h1) 
        L2 = one_pair_7(h2)
        if L1 and L2:
            print("TIE with one pair:", cannonical(L1))
            continue
        elif L1 and not L2:
            print("Player 1 wins with one pair:", cannonical(L1))
            continue
        elif not L1 and L2:
            print("Player 2 wins with one pair:", cannonical(L2))
            continue
        else:
            do_nothing = True
            
            
     
if __name__ == "__main__":
    main()