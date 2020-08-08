#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    ticktionary = {ticket.source: ticket.destination for ticket in tickets}
    
    route = [ticktionary["NONE"]] # initialize the list  with source
    
    city = ticktionary["NONE"] # start a loop variable 
    while city != "NONE":
        city = ticktionary[city]
        route.append(city)

    return route
