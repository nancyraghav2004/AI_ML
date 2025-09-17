from logic import *

people = ["Gilderoy", "Pomona", "Minerva", "Horace"]
houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

symbols = []

knowledge = And()



for person in people:
    for house in houses:
        symbols.append(Symbol(f"{person}{house}"))

knowledge = KnowledgeBase()

# Each person belongs to a house.
for person in people:
    knowledge.add(
        Or(
            Symbol(f"{person}Gryffindor"),
            Symbol(f"{person}Hufflepuff"),
            Symbol(f"{person}Ravenclaw"),
            Symbol(f"{person}Slytherin")
        )
    )

# Only one house per person
for person in people:
    for h1 in houses:
        for h2 in houses:
            if h1 != h2:
                knowledge.add(
                    Implication(Symbol(f"{person}{h1}"), Not(Symbol(f"{person}{h2}")))
                )
                
# Only one person per house
for house in houses:
    for p1 in people:
        for p2 in people:
            if p1 != p2:
                knowledge.add(
                    Implication(Symbol(f"{p1}{house}"), Not(Symbol(f"{p2}{house}")))
                )

#print(knowledge.formula())

knowledge.add(Not(Symbol("PomonaSlytherin")))
knowledge.add(Symbol("MinervaGryffindor"))

# # # TODO
# for symbol in symbols:
#     if model_check(knowledge, symbol):
#         print(symbol)


def find_one_model(knowledge):
    symbols = knowledge.symbols()
    for values in itertools.product([True, False], repeat=len(symbols)):
        model = dict(zip(symbols, values))
        if knowledge.evaluate(model):
            return model
    return None

model = find_one_model(knowledge)
if model:
    print("Solution:")
    for symbol in symbols:
        if model.get(symbol.name):
            print(symbol.name)
else:
    print("No valid assignment found.")
