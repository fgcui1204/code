x = {"cui":28, "cherry":18, "zhou":16}

def find_max(dict):
    max_age = 0
    for key, value in dict.items():
        if value > max_age:
            max_age = value
            name = key
    print (name,max_age)
find_max(x)