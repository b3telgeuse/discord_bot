import random

player_hand = []
dealer_hand = []
player_total = 0
dealer_total = 0
player_record = {'wins': 0, 'losses': 0}

def handle_response(message) -> str:
    global player_hand
    global dealer_hand
    global player_total
    global dealer_total
    global player_record

    p_message = message.lower()
    if p_message == '!hello':
        return 'what do you want'

    if p_message == '!roll':
        return str(random.randint(1, 6))
        
    if p_message == '!blackjack':
        player_hand = [random.randint(1, 11), random.randint(1, 11)]
        dealer_hand = [random.randint(1, 11), random.randint(1, 11)]
        player_total = sum(player_hand)
        dealer_total = sum(dealer_hand)

        return 'Blackjack! Your hand is {} for a total of {}. Type "hit" to hit or "stay" to stay.'.format(player_hand, player_total)
        
    if p_message == 'hit':
        player_hand.append(random.randint(1, 11))
        player_total = sum(player_hand)
        if player_total > 21:
            player_record['losses'] += 1
            return 'You bust with a total of {}. Your win-loss record is {}-{}'.format(player_total, player_record['wins'], player_record['losses'])
        else:
            return 'You hit! Your new hand is {} for a total of {}. Type "hit" to hit or "stay" to stay.'.format(player_hand, player_total)

    if p_message == 'stay':
        while dealer_total < 17:
            dealer_hand.append(random.randint(1, 11))
            dealer_total = sum(dealer_hand)
            if dealer_total > 21:
                player_record['wins'] += 1
                return 'Dealer busts with a total of {}. You win! Your win-loss record is {}-{}'.format(dealer_total, player_record['wins'], player_record['losses'])
        
        if dealer_total == player_total:
            return 'Push. Both you and dealer have {}'.format(dealer_total)
        elif dealer_total > player_total:
            player_record['losses'] += 1
            return 'Dealer wins with a total of {} to your {}. Your win-loss record is {}-{}'.format(dealer_total, player_total, player_record['wins'], player_record['losses'])
        else:
            player_record['wins'] += 1
            return 'You win with a total of {} to dealer\'s {}. Your win-loss record is {}-{}'.format(player_total, dealer_total, player_record['wins'], player_record['losses'])