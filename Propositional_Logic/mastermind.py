from logic import *

colors = ["red", "blue", "green", "yellow"]
symbols = []
for i in range(4):
    for color in colors:
        symbols.append(Symbol(f"{color}{i}"))



Knowledge = And()

Knowledge = KnowledgeBase()

# Each color has a position
for color in colors:
    Knowledge.add(Or(
        Symbol(f"{color}0"),
        Symbol(f"{color}1"),
        Symbol(f"{color}2"),
        Symbol(f"{color}3")
    ))

# Only one position per color
for color in colors:
    for i in range(4):
        for j in range(4):
            if i != j:
                Knowledge.add(Implication(Symbol(f"{color}{i}"), Not(Symbol(f"{color}{j}"))))

# Each position can only have one color
for i in range(4):
    for c1 in colors:
        for c2 in colors:
            if c1 != c2:
                Knowledge.add(Implication(Symbol(f"{c1}{i}"), Not(Symbol(f"{c2}{i}"))))

# Add clues (example: red is not in position 0, blue is in position 2)
Knowledge.add(Not(Symbol("red0")))
Knowledge.add(Symbol("blue2"))

# Solve the puzzle
def find_one_model(knowledge):
    symbols = knowledge.symbols()
    for values in itertools.product([True, False], repeat=len(symbols)):
        model = dict(zip(symbols, values))
        if knowledge.evaluate(model):
            return model
    return None

model = find_one_model(Knowledge)
if model:
    print("Solution:")
    for symbol in symbols:
        if model.get(symbol.name):
            print(symbol.name)
else:
    print("No valid assignment found.")