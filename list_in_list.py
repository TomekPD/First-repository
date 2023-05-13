def list_in_list(n_list):
    """
    Ta funkcja przyjmuje listę zagnieżdżoną jako argument i zwraca jedną płaską listę,
    zawierającą wszystkie elementy z list zagnieżdżonych.
    """

    flat_list = []

    for item in n_list:
        if isinstance(item, list):
            flat_list.extend(list_in_list(item))
        else:
            flat_list.append(item)

    return flat_list


n_list = [[1, 2, 3], 6, [4, 5], [6, 7, 8, 9]]
list_ready = list_in_list(n_list)
print(list_ready)
