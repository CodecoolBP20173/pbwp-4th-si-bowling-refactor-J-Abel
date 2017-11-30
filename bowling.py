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
        if game[i] == '/': #ez benne van getvalueban! vmelyikből töröl. nem tud ez lenni a legelső karakter, ezért lehet a last
            result += 10 - get_value(game[i - 1]) #EZ AZÉRT, HOGY /-NÉL AZ ELŐZŐ ÉRTÉKET TÖRÖLNI, MERT A / = 10
        else:
            result += get_value(game[i]) #ez tkp mindenképp fog kelleni

        if frame < 10 and get_value(game[i]) == 10:
            result += get_value(game[i + 1])
            if game[i] == 'X' or game[i] == 'x':
                if game[i+2] == '/':
                    result += 10 - get_value(game[i+1]) #?????
                else:
                    result += get_value(game[i+2])

        if game[i] == 'X' or game[i] == 'x':
            frame += 1

        elif in_first_half:
            in_first_half = False
        else:
            frame += 1
            in_first_half = True

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
