# Putting together a basic REPL together
UNIT_CARD_NAME = "Banehound"
UNIT_CARD_COST = "B"
UNIT_CARD = [UNIT_CARD_NAME, UNIT_CARD_COST]
BASIC_LAND_NAME = "Swamp"
BASIC_LAND_TYPE = "B"
BASIC_LAND = [BASIC_LAND_NAME, BASIC_LAND_TYPE]
INSTANT_CARD_NAME = "Dark Remedy"
INSTANT_CARD_COST = "BB"
INSTANT_EFFECT = "+1/+3"
INSTANT_CARD = [INSTANT_CARD_NAME, INSTANT_CARD_COST]

def add(op1, op2):
    deck = []
    mana_needed = len(UNIT_CARD[1]) + (op1 + op2 - 1)*len(INSTANT_CARD[1])
    for _ in range(mana_needed):
        deck.append(BASIC_LAND)
    deck.append(UNIT_CARD)
    for _ in range(op2 + op1 - 1):
        deck.append(INSTANT_CARD)
    return deck


def sub(op1, op2):
    pass

def mul(op1, op2):
    pass

def div(op1, op2):
    pass

if __name__ == '__main__':
    while True:
        input_expr = input('>')
        add_index = input_expr.find('+')
        sub_index = input_expr.find('-')
        mul_index = input_expr.find('*')
        div_index = input_expr.find('/')
        if not(add_index is -1 and sub_index is -1 and mul_index is -1 and div_index is -1):
            if add_index is not -1:
                op1 = int(input_expr[:add_index])
                op2 = int(input_expr[add_index+1:])
                print(add(op1, op2))
            elif sub_index is not -1:
                op1 = int(input_expr[:sub_index])
                op2 = int(input_expr[sub_index+1:])
                sub(op1, op2)
            elif mul_index is not -1:
                op1 = int(input_expr[:mul_index])
                op2 = int(input_expr[mul_index+1:])
                mul(op1, op2)
            elif div_index is not -1:
                op1 = int(input_expr[:div_index])
                op2 = int(input_expr[div_index+1:])
                div(op1, op2)
            