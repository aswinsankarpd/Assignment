def relation_to_luke(name):
    dct = {"Darth Vader":"father", "Leia":"sister", "Han":"brother in law", "R2D2":"droid",}
    print(dct[name])

name = input("")
relation_to_luke(name)