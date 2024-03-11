def note_change(remainding_price, note, quantity):
    counter = 0
    while(remainding_price - int(note)) >= 0 and quantity != 0:
        remainding_price = remainding_price - int(note)
        counter += 1
        quantity -= 1

    return remainding_price, {f'{note}': counter}

def vending_machine(drinks, number_of_choices, payment):
    # Expect user will insert starting from 1 but not 0
    item_price = drinks[number_of_choices - 1]['price']
    remainding_price = payment - item_price
    amount_of_notes = {}
    for i in notes:
        remainding_price, amount_of_note = note_change(remainding_price, i['name'], i['quantity'])
        amount_of_notes.update(amount_of_note)
    
    return amount_of_notes

# Predefined Value
item1 = {
"name": "A",
"price": 33
}

item2 = {
"name": "B",
"price": 9
}

item3 = {
"name": "C",
"price": 7
}

item4 = {
"name": "D",
"price": 3
}

drinks = [item1, item2, item3, item4]
notes = [{'name':'100', 'quantity': 0}, 
        {'name':'50', 'quantity': 1},
        {'name':'20', 'quantity': 1},
        {'name':'10', 'quantity': 1},
        {'name':'5', 'quantity': 1},
        {'name':'2', 'quantity': 1},
        {'name':'1', 'quantity': 20}]

# Input
number_of_choices = 1
payment = 100

results = vending_machine(drinks, number_of_choices, payment)
# key name will be note, key value will be the amount of notes
# {'100': 0, '50': 0, '20': 1, '10': 1, '5': 1, '2': 1, '1': 0}
for k, v in results.items():
    print(f"{v} pieces of note {k}")
# print(results)