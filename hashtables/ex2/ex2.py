#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length
    
    # set up hash table with sources as keys, destinations as values
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)
    # set first route to starting route (route with NONE source)
    route[0] = hash_table_retrieve(hashtable, 'NONE')
    # Add routes to route list, skipping starting route
    # and finding the ith location in the route by checking the hash table for the i-1th location
    for i in range(1, length):
        route[i] = hash_table_retrieve(hashtable, route[i - 1])

    return route
