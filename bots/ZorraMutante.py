#Bot basado en MarkovBot con la funcion autoreply_start, tomando como fuente de texto el Manifiesto "Zorra Mutante" del colectivo ciberfeminista VNS Matrix

#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import os
import time
import sys
from markovbot import MarkovBot

reload(sys)
sys.setdefaultencoding('utf-8')

# Initialise a MarkovBot instance
tweetbot = MarkovBot()

# Make your bot read the book!
tweetbot.read('https://github.com/gini10/akelarreciberfeminista/blob/master/bots/ZorraMutante.py')

my_first_text = tweetbot.generate_text(10, seedword=[u'código', u'límite', u'hay'])
print(u'\ntweetbot says: "%s"' % (my_first_text))


# ALL YOUR SECRET STUFF!
# Consumer Key (API Key)
cons_key = '[ copy this value from Consumer Settings ]'
# Consumer Secret (API Secret)
cons_secret = '[ copy this value from Consumer Settings ]'
# Access Tokenf
access_token = '[ copy this value from Your Access Token ]'
# Access Token Secret
access_token_secret = '[ copy this value from Your Access Token ]'

# Log in to Twitter
tweetbot.twitter_login(cons_key, cons_secret, access_token, access_token_secret)

# Set some parameters for your bot
targetstring = '#feminazi'
keywords = ['machista','feminismo', 'stopmachitrols', '💜','✊', 'machirulo','feminista','machismo' ]
prefix = '#akelarreCiberfeminista'
suffix = '💜✊'
maxconvdepth = 3

# Start auto-responding to tweets
tweetbot.twitter_autoreply_start(targetstring, keywords=keywords, prefix=prefix, suffix=suffix, maxconvdepth=maxconvdepth)

# Start periodically tweeting
#tweetbot.twitter_tweeting_start(days=0, hours=0, minutes=5, keywords=keywords, prefix=prefix, suffix=suffix)

secsinweek = 1 * 2 * 60 * 60
time.sleep(secsinweek)

