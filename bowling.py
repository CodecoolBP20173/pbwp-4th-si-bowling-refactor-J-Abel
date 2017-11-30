def score(game):
    '''
    Counts and returns the final result of the parametered bowling game.

    Arguments: string

    Returns: integer number
    '''

    result = 0
    frame = 1
    in_first_half = True
    for i in range(len(game)):
        if game[i] == '/':
            result += 10 - last
        else:
            result += get_value(game[i])
        # if not in_first_half:
            # frame += 1
        if frame < 10 and get_value(game[i]) == 10:
            if game[i] == '/':
                result += get_value(game[i+1])
            elif game[i] == 'X' or game[i] == 'x':
                result += get_value(game[i+1])
                if game[i+2] == '/':
                    result += 10 - get_value(game[i+1])
                else:
                    result += get_value(game[i+2])
        last = get_value(game[i])
        if not in_first_half:
            frame += 1
        if in_first_half:
            in_first_half = False
        else:
            in_first_half = True
        if game[i] == 'X' or game[i] == 'x':
            in_first_half = True
            frame += 1
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
