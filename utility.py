import random
def dumbBsGenerator():
    '''
    Primarily intended to say something silly at my launch of app
    '''
    sayings = {
    'rm1': 'IM MR MEESEEKS LOOK AT ME',
    'crs1': 'Well atleast youre not bitter about it',
    'APL1': 'Oh uhhh. Your battery isnt as charged anymore! Gotta slow down that phone dude',
    'GOG': 'Because a free search engine is so profitable',
    'TalDeg': 'Take that pain, and bury it deep down. It hurts...but I love you!',
    'CClick': '307 quntillion CpS',
    'ithd1': 'Opened ticket for 3 monitors and watches netflix',
    'mgnmt1': 'We are paying him for two jobs and now have to fire him because of our great judgement',
    'WFH1': 'WFH: pajama pants while you toil away in an actual office',
    'ithd2': 'Ticket 002: Please make sure to label all staplers with your department. This is a high priority',
    'CHD1': 'Hi, Youve reacehd the helpless desk, how may I ignore you and transfer your call?',
    'pol1': 'Youre just trumping me up to trickle me down, man.',
    'mgnmt2': 'You arent in charge of adding new infrastructure, just adding new servers and software and networks.',
    'ithd03':'Sends ticket to parent IT; gets response back: thats not my job',
    'ithd04':' for (specialSnowFlake in office): pass',
    'rm2': 'El Solenya, salmuera, mi archienemigo...',
    'rm3': 'Wubba dubba dub dub!'}
    saying = random.choice(sayings.values())
    return saying
