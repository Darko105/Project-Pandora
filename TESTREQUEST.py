import requests


def getSteamProfile(id):
    rep = requests.get(f'https://steamcommunity.com/profiles/{id}/')
    content = rep.text[280:350]
    char = temp = ''
    i = 0
    while char != '<':
        char = content[i]
        temp += char
        i +=1
    return str(temp[:-1])

print(getSteamProfile(str(76561199396705820)))
    



