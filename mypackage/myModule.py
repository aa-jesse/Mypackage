def top_n (items, n):
    """" returns the top n items in an array in descending order

    Args:
        item (array) list or array-like object
        n (int): num of items to return

        Return:
            array: top n items, desc order

        Example:
            top_n ([2,4,56,7], 2)
            [56,7]

    """
    for i in range(n):
        for j in range(len(items) - 1 - i):

            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]
    
    top_n = items[-n:]

    return top_n[::-1]
 