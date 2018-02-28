__author__ = 'lanceli'

def remove_dups(unsorted_linkedlist):
    visited_nodes = []

    while (unsorted_linkedlist.next() is not None):
        if (unsorted_linkedlist.next() in visited_nodes):
            unsorted_linkedlist.next().next() = unsorted_linkedlist.next()
        else:
            visited_nodes.append(unsorted_linkedlist.next()

    return unsorted_linkedlist





    
