import tweepy
from secrets import API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
from flask import Flask

from random import randint
from time import sleep

#Tweepy setup
auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

class EurobeatBot(object):

    def __init__(self):
        auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        self.api = tweepy.API(auth)

    nouns =     ['Night','Fire','Boy','Beat','Sun','Heart','Speed','Heartbeat','Love',
                    'Gas','Power','Race','Game','Car','Fantasy','Eurobeat']
    locations = ['Space','Tokyo','The 90s','Danger','Japan']
    verbs =     ['Sleep','Dance','Rise','Beat','Remember','Run','Burn','Stand','Love',
                    'Kill']
    titles = [
        'noun1 of noun2',
        'location noun',
        'No One verb in location',
        'verbing',
        'noun1 of the verbing noun2',
        'noun',
        'verb Me',
        'verbing in location',
        'verbing Up For You',
        'Don\'t verb So Close',
        'nounAY nounA noun',
        'noun verber',
        'noun noun noun',
        'verbing my noun',
        'Get me noun',
        'The noun1 is the noun2',
        'The noun1 of the noun2',
        'My noun1 is noun2',
        'noun is in location',
        'Need noun',
        'Crazy for noun',
        'verbing noun',
        'location Fever',
        'noun Flight to location',
        'I need your noun',
        'noun Rhapsody',
        'Made in location',
        'Disco noun',
        'Super noun',
        ]

    def getWord(self,category,rule=None):
        w = ''
        if category == 'nouns':
            w = self.nouns[randint(0,len(self.nouns)-1)]
        elif category == 'locations':
            w = self.locations[randint(0,len(self.locations)-1)]
        elif category == 'verbs':
            w = self.verbs[randint(0,len(self.verbs)-1)]
            if rule == 'ing':
                if w[-1] is 'e':
                    w = w[:-1]
                elif w in ['Run']:
                    w+=w[-1]
                w+='ing'
            elif rule is 'er':
                if w in ['Run']:
                    w+=w[-1]
                if w[-1] != 'e':
                    w+='e'
                w+='r'
        return w

    def addY(self,w):
        if w == 'Fire':
            w = 'Fier'
        elif w in ['Sun','Gas','Car']:
            w+=w[-1]
        elif w in ['Race']:
            w = w[:-1]
        w+='y'
        if w == 'Boyy':
            w = 'Boyish'
        elif w == 'Powery':
            w = 'Powerful'
        elif w == 'Fantasyy':
            w = 'Fantastical'
        return w

    def generateTitle(self):
        title = self.titles[randint(0,len(self.titles)-1)]
        types = [
            ['noun2','nouns',None],
            ['noun1','nouns',None],
            ['verber','verbs','er'],
            ['verbing','verbs','ing'],
            ['noun','nouns',None],
            ['verb','verbs',None],
            ['location','locations',None]
            ]
        if 'nounAY' in title:
            randWord = self.getWord('nouns')
            randWordY = self.addY(randWord)
            title = title.replace('nounAY',randWordY)
            title = title.replace('nounA',randWord)
        for type in types:
            if type[0] in title:
                title = title.replace(type[0],self.getWord(type[1],type[2]))
        return title

    def tweet(self):
        title = self.generateTitle()
        try:
            self.api.update_status(title)
        except tweepy.TweepError as error:
            print(error.reason)

    def runBot(self, delay):
        while True:
            self.tweet()
            sleep(delay)

def main():
    bot = EurobeatBot()
    bot.runBot(3600)

if __name__ == "__main__":
    main()


app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'This is the source site for @EurobotNames, coded by @Capn__Handsome on twitter. Bother him if the bot isn\'t working. Don\'t really know what else to put here...'
