def tennisMatch(p1 : str,p2 : str,record : str):
    
    """
    Determines the winner of a tennis-style match based on a record string.

    Each round is separated by a dash.
    A '1' represents a point for player 1.
    A '2' represents a point for player 2.

    The player with more points in each round wins that round.
    If both players have the same number of points in a round, both get a round point.
    """

    record_split = record.split('-')
    p1_score = 0
    p2_score = 0
    ones = 0
    twos = 0
    for k in record_split:
        for b in k:
            if b == '':
                continue
            if b == '1':
                ones+=1
            elif b == '2':
                twos += 1
        if ones > twos:
            p1_score +=1
        elif twos > ones:
            p2_score += 1
        else : 
            p1_score +=1
            p2_score += 1
        
        ones = 0
        twos = 0

    if p1_score == p2_score:
        return "It's a tie!"
    elif p1_score > p2_score:
        return "{} won! The score was {}-{}.".format(p1,p1_score,p2_score)
    elif p2_score > p1_score:
        return "{} won! The score was {}-{}.".format(p2,p2_score,p1_score)
    
max = tennisMatch("Anthony", "Caitlin", "1122-22211-11122-1212-")
print(max)
