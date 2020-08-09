def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    # perhaps a dictionary of dictionaries??
    # {
    # {value: idx, value:idx},
    # {value: idx, value:idx, value: idx},
    # {value: idx, value:idx}
    # }
    #   no, can't loop through the numbers to compare efficiently

    # let's add all numbers to a dictionary and a count as the value.
    # when the value reaches len(array), then we pop champagne
    arraytionary = {} # all nums go in here
    result = [] # nums intersecting all the arrays
    for array in arrays:
        for number in array:
            if number not in arraytionary:
                arraytionary[number] = 1 # initialize the count
            else:
                arraytionary[number] += 1 
                if arraytionary[number] == len(arrays):
                    result.append(number)
            
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
