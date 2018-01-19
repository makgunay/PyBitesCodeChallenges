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

print(dedup_and_title_case_names(NAMES))

def sort_by_surname_desc(names):
    names = dedup_and_title_case_names(names)


    # ...


def shortest_first_name(names):
    names = dedup_and_title_case_names(names)
    # ...
