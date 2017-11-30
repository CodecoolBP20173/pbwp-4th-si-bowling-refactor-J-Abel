def score(game):
    '''
    Counts and returns the final result of the parametered bowling game.

    Arguments: string

    Returns: integer number
    '''

    result = 0
    frame = 1
    first_try = True

    for i in range(len(game)):
        result += get_value(game[i])

        if game[i] == '/': #ez benne van getvalueban! vmelyikből töröl. nem tud ez lenni a legelső karakter, ezért lehet a last
            result -= get_value(game[i - 1])  # '/': 10 points for 2nd try, but 1st grade needs to be deleted

        if frame < 10 and get_value(game[i]) == 10:
            result += get_value(game[i + 1])
            if x_or_X(game[i]):
                if game[i+2] == '/':
                    result += 10 - get_value(game[i+1]) #?????
                else:
                    result += get_value(game[i+2])

        frame += 1
        if first_try:
            if not x_or_X(game[i]):
                frame -= 1
                first_try = False
        else:
            first_try = True

    return result


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
    Returns boolean if parameter is "x" or "X"

    Arguments: string

    Returns: boolean
    '''

    if data == "X" or data == "x":
        return True
    else:
        return False
