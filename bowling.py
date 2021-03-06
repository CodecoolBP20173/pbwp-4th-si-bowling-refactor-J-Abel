def score(game):
    '''
    Counts and returns the final result of the parametered bowling game.

    Arguments: string

    Returns: integer number
    '''

    result = 0
    frame = 1
    first_try = True

    for CharNumber in range(len(game)):
        result += get_value(game[CharNumber])

        if frame < 10:
            result = RaisingResultIfHighValues(CharNumber, game, result, frame)

        frame += 1
        if first_try:
            if not x_or_X(game[CharNumber]):  # If 'X', there is no second try
                frame -= 1
                first_try = False
        else:
            first_try = True
            result = ReducingResultIfSpare(result, CharNumber, game)

    return result


def ReducingResultIfSpare(outcome, iternumber, play):
    '''
    If play[iternumber] is '/', outcome is reducing.
    (spare: 10 points for 2nd try, 1st try needs to be deleted. 10 points are previously done, not in this function)

    iternumber: integer
    play: string, list
    outcome: integer

    Returns: outcome
    '''

    if play[iternumber] == '/':
        outcome -= get_value(play[iternumber - 1])

    return outcome


def RaisingResultIfHighValues(iternumber, play, outcome, turn):
    '''
    High values of play[iternumber] raises the 'outcome' significantly

    iternumber: integer
    play: string, list
    outcome: integer
    turn: integer

    Returns: outcome
    '''

    if get_value(play[iternumber]) == 10:
        outcome += get_value(play[iternumber + 1])
        if x_or_X(play[iternumber]):
            outcome += get_value(play[iternumber + 2])
            outcome = ReducingResultIfSpare(outcome, iternumber + 2, play)

    return outcome


def get_value(char):
    '''
    Returns the score of the actual parameter.

    Argumenets: string

    Returns: integer number
    '''

    for scores in range(1, 10):
        if char == str(scores):
            return int(char)

    for scores in ['X', 'x', '/']:
        if char == scores:
            return 10

    if char == '-':
        return 0

    raise ValueError()


def x_or_X(data):
    '''
    Returns True if parameter is "x" or "X" and False if not

    Arguments: string

    Returns: boolean
    '''

    if data == "X" or data == "x":
        return True
    else:
        return False
