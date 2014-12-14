import string


alphabet = list(string.ascii_lowercase + string.ascii_uppercase)


current = []
waiting = []


for a in alphabet:
    temp = {}
    temp['character'] = a
    temp['level'] = 0 
    temp['meaning'] = a
    waiting.append(temp)

    