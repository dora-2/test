
def filter_by_state(dictionary: list, state=['EXECUTED']) -> list:
    """сортировка по state"""
    new_dictionary = []
    for i in dictionary:
        if i['state'] in state:
            new_dictionary.append(i)
    return new_dictionary


def sort_by_date(dictionary_2: list, reverse=True) -> list:
    """сортировка по date"""
    dictionary_2.sort(key=lambda x: x['date'], reverse=reverse)
    return dictionary_2
