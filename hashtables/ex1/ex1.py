#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    if length == 2:
        return 1,0

    for weight in weights:
        hash_table_insert(ht, weight, weights.index(weight))
        if hash_table_retrieve(ht, limit - weight) is not None:
            if weights.index(weight) > hash_table_retrieve(ht, limit - weight):
                return int(weights.index(weight)), int(hash_table_retrieve(ht, limit - weight))
            else:
                return int(hash_table_retrieve(ht, limit - weight)), int(weights.index(weight))

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
