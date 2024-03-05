def note_change(leftover_price, note):
    counter = 0
    while(leftover_price - note) >= 0:
        leftover_price = leftover_price - note
        counter += 1

    return leftover_price, {f'{note}': counter}

def vending_machine(drinks, number_of_choices, payment):
    # Expect user will insert starting from 1 but not 0
    item_price = drinks[number_of_choices - 1]['price']
    remainding_price = payment - item_price
    amount_of_notes = {}
    for i in notes:
        remainding_price, amount_of_note = note_change(remainding_price, i)
        amount_of_notes.update(amount_of_note)
    
    return amount_of_notes

# Predefined Value
item1 = {
"name": "A",
"price": 13
}

item2 = {
"name": "B",
"price": 9
}

item3 = {
"name": "C",
"price": 7
}

drinks = [item1, item2, item3]
notes = [100, 50, 20, 10, 5, 2, 1]

# Input
number_of_choices = 1
payment = 50

notes = vending_machine(drinks, number_of_choices, payment)
print(notes)