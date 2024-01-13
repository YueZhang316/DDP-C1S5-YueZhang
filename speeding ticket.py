def speeding_ticket(speed, is_birthday):
    # Define speed limits
    no_ticket_limit = 60
    small_ticket_limit = 80

    # Increase speed limits on birthday
    if is_birthday:
        no_ticket_limit += 5
        small_ticket_limit += 5

    # Evaluate speed and return ticket category
    if speed <= no_ticket_limit:
        return "No Ticket"
    elif no_ticket_limit < speed <= small_ticket_limit:
        return "Small Ticket"
    else:
        return "Big Ticket"

# Test cases
print(speeding_ticket(60, False)) 
print(speeding_ticket(75, False))  
print(speeding_ticket(85, False))  
print(speeding_ticket(65, True)) 
print(speeding_ticket(85, True))  
