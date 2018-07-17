directions = ['north', 'south', 'east']
verbs = ['go', 'kill', 'eat']
stops = ['the', 'in', 'of']
nouns = ['bear', 'princess']


def tuple(word):
    string = word.lower()
    if string in directions:
        return('direction', string)

    elif string in verbs:
        return('verb', string)

    elif string in nouns:
        return('noun', string)

    elif string in stops:
        return('stop', string)

    else:
        try:
            return('number', int(word))
        except ValueError:
            return('error', word)


def scan(sentence):
    words = sentence.split()
    return [tuple(word) for word in words]
