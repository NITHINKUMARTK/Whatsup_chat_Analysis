from urlextract import URLExtract
from wordcloud import WordCloud
import pandas as pd
from collections import Counter
import emoji

extract = URLExtract()

def fetch_stats(selected_user, df):

## fetching the total number of messages and words

	if selected_user == "Overall":
		num_messages = df.shape[0]
		words = []
		for message in df["message"]:
			message = message.split()
			words.extend(message)
	else:
		df = df[df["users"] == selected_user]
		num_messages = df.shape[0]
		words = []
		for message in df["message"]:
			message = message.split()
			words.extend(message)

	## fetching the number of media files shared
	 
	num_mediafiles_shared = df[df["message"] ==  " <Media omitted>\n"].shape[0]
	
	## fetching the number of links shared

	links = []
	for message in df["message"]:
	  url = extract.find_urls(message)
	  links.extend(url)

	return num_messages, len(words), num_mediafiles_shared, len(links)

