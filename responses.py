import random

player_hand = []
dealer_hand = []
player_total = 0
dealer_total = 0

def handle_response(message) -> str:
    global player_hand
    global dealer_hand
    global player_total
    global dealer_total

    p_message = message.lower()
    if p_message == '!hello':
        return 'what do you want'

    if p_message == '!roll':
        return str(random.randint(1, 6))
        
    