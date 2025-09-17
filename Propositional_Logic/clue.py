import termcolor

from logic import *

mustard = Symbol("ColMustard")
plum = Symbol("ProfPlum")
scarlet = Symbol("MsScarlet")
characters = [mustard, plum, scarlet]

ballroom = Symbol("ballroom")
kitchen = Symbol("kitchen")
library = Symbol("library")
rooms = [ballroom, kitchen, library]

knife = Symbol("knife")
revolver = Symbol("revolver")
wrench = Symbol("wrench")
weapons = [knife, revolver, wrench]

symbols = characters + rooms + weapons

def check_knowledge(knowledge):
    for symbol in symbols:
        if model_check(knowledge, symbol):
            termcolor.cprint(f"{symbol}: YES", "green")
        elif not model_check(knowledge, Not(symbol)):
            print(f"{symbol}: MAYBE")

knowledge = And(
    Or(mustard, plum, scarlet),
    Or(ballroom, kitchen, library),
    Or(knife, revolver, wrench),
    Not(mustard),
    Not(kitchen),
    Not(revolver),
    Or(
        Not(scarlet), Not(library), Not(wrench)
    ),
    Not(plum),
    Not(ballroom)
)
# We can change knowledge (line 29), based on the information we have
# We can remove or add symbols

#print(knowledge.formula())

# knowledge.add(Not(mustard))
# knowledge.add(Not(kitchen))
# knowledge.add(Not(revolver))

check_knowledge(knowledge)