NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']

def dedup_and_title_case_names(names):
    """Should return a list of names, each name appears only once"""
    NAMES2 = []
    for item in names:
        if item.title() in NAMES2:
            pass
        else:
            NAMES2.append(item.title())
    return NAMES2

def sort_by_surname_desc(names):
    NAMES3 = []
    NAMES4 = []
    names = dedup_and_title_case_names(names)
    for item in names:
        NAMES3.append(item.split())
        NAMES3 = sorted(NAMES3, key=lambda x: x[1], reverse=True)
        NAMES4 = [x+" "+y for x,y in NAMES3]
    return NAMES4

def shortest_first_name(names):
    names = dedup_and_title_case_names(names)
    NAMES5 = []
    for item in names:
        NAMES5.append(item.split())
        NAMES5 = sorted(NAMES5, key=lambda x: x[0])
    return NAMES5[0][0]


print(dedup_and_title_case_names(NAMES))
print(sort_by_surname_desc(NAMES))
print(shortest_first_name(NAMES))