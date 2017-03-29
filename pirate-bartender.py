# simulates a pirate bartender
# no credit to me for questions and ingredients

from random import choice

questions = {
    "strong": "do ye like yer drinks strong?",
    "salty": "do ye like it with a salty tang?",
    "bitter": "are ye a lubber who likes it bitter?",
    "sweet": "would ye like a bit of sweetness with yer poison?",
    "fruity": "are ye one for a fruity finish?",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

# sets an empty dictionary for user's drink preferences
usr_drink = {}

def drink_style():
    """ retrieves input from the user on their drink preferences, and
    stores the outcome in the dictionary usr_drink. each answer is lower-
    cased for easy manipulating, and the outcome is stored as preference:
    true / false """
    print(questions["strong"])

    usr_strong = input(">: ")
    usr_strong = usr_strong.lower()

    if usr_strong == "y" or usr_strong == "yes":
        usr_drink["strong"] = True
    else:
        usr_drink["strong"] = False

    print(questions["salty"])

    usr_salty = input(">: ")
    usr_salty = usr_salty.lower()

    if usr_salty == "y" or usr_salty == "yes":
        usr_drink["salty"] = True
    else:
        usr_drink["salty"] = False

    print(questions["bitter"])

    usr_bitter = input(">: ")
    usr_bitter = usr_bitter.lower()

    if usr_bitter == "y" or usr_bitter == "yes":
        usr_drink["bitter"] = True
    else:
        usr_drink["bitter"] = False

    print(questions["sweet"])

    usr_sweet = input(">: ")
    usr_sweet = usr_sweet.lower()

    if usr_sweet == "y" or usr_sweet == "yes":
        usr_drink["sweet"] = True
    else:
        usr_drink["sweet"] = False

    print(questions["fruity"])

    usr_fruity = input(">: ")
    usr_fruity = usr_fruity.lower()

    if usr_fruity == "y" or usr_fruity == "yes":
        usr_drink["fruity"] = True
    else:
        usr_drink["fruity"] = False


def construct_drink(drink_dict):
    """ creates a new drink out of a given drink dictionary. new drink
    is started as an empty list, and for each choice the user has made
    in taste a random ingredient is chosen and added to the list. making
    a new drink."""
    new_drink = []
    for key in drink_dict:
        if drink_dict["fruity"]:
            new_drink.append(choice(ingredients["fruity"]))

        if drink_dict["sweet"]:
            new_drink.append(choice(ingredients["sweet"]))

        if drink_dict["bitter"]:
            new_drink.append(choice(ingredients["bitter"]))

        if drink_dict["salty"]:
            new_drink.append(choice(ingredients["salty"]))

        if drink_dict["strong"]:
            new_drink.append(choice(ingredients["strong"]))

        return new_drink

def name_cocktail(new_drink):

    new_drink_adj = []
    new_drink_noun = []
    print(new_drink)
    for flavor in new_drink:
        if flavor == "glug of run" or flavor == "slug of whisky" or flavor == "splash of gin":
            new_drink_adj == "Tough"
            new_drink_noun == "Sea-Dog"

        if flavor == "olive on a stick" or flavor == "salt-dusted rim" or "rasher of bacon":
            new_drink_adj == "Salty"
            new_drink_noun == "Walrus"

        if flavor == "shake of bitters" or flavor == "splash of tonic" or flavor == "twist of lemon peel":
            new_drink_adj == "Mean Ol"
            new_drink_noun == "Crab"

        if flavor == "sugar cube" or flavor == "spoonful of honey" or flavor == "spash of cola":
            new_drink_adj == "Fluffy"
            new_drink_noun = "Bunny"

        if flavor == "slice of orange" or flavor == "dash of cassis" or flavor == "cherry on top":
            new_drink_adj == "Tropical"
            new_drink_noun == "Toucan"
        print(new_drink_adj)
        print(new_drink_noun)
#    print(choice(new_drink_adj), choice(new_drink_noun))


if __name__ == '__main__':

    usr_choice = input("would ye like a drink? ")
    usr_choice = usr_choice.lower()
    while usr_choice != "no":
        drink_style()
        print("your ingredients are", construct_drink(usr_drink))
        new_drink = construct_drink(usr_drink)
        print("your drink has been aptly named:", name_cocktail(new_drink))
        usr_choice = input("would ye like another? ")

