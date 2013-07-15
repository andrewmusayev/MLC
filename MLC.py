from twython import Twython
import requests
from bs4 import BeautifulSoup


APP_KEY = "AAmMPoQPdVy8zFkylH1Q"
APP_SECRET = "Kas31gUy0IBLo9jd4i48jlz6ml4098sacQbb58wwf84"
OAUTH_TOKEN = "1295080538-dakBRTjEDsPq33IjjjaOr4hpIfmthPJsMqIZ35j"
OAUTH_TOKEN_SECRET = "8bKQgUARvCQzIEtPWw562LGWG9KgpthkortFFdjnkyk"

MAX_NUMER = 999


def txt_list( url ):
  response = requests.get(url)
	soup = BeautifulSoup(response.content)

	with open('listik.txt', 'a+') as fo:
		fo.write(soup.title.string);
		fo.write("\n\n");

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
user_timeline = twitter.get_user_timeline(screen_name='dreikanterfm', count=50)

for tweet in user_timeline:
	tweets = tweet['text']

tweet_list = tweets.split()

for n in range(len(tweet_list)):
	if 'http' in tweet_list[n]:
		txt_list(tweet_list[n])
