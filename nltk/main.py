import nltk
pos_tweets = [('I love this car', 'positive'),
			  ('This view is amazing', 'positive'),
			  ('I feel great this morning', 'positive'),
			  ('I am so excited about the concert', 'positive'),
			  ('He is my best friend', 'positive')
			]

neg_tweets = [('I do not like this car', 'negative'),
			('This view is horrible', 'negative'),
			('I feel tired this morning', 'negative'),
			('I am not looking forward to the concert', 'negative'),
			('He is my enemy', 'negative')
			]

tweets = []

for (words, sentiment) in pos_tweets + neg_tweets:
	words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
	tweets.append((words_filtered, sentiment))

"""
tweets = [
	    (['love', 'this', 'car'], 'positive'),
    	(['this', 'view', 'amazing'], 'positive'),
	    (['feel', 'great', 'this', 'morning'], 'positive'),
	    (['excited', 'about', 'the', 'concert'], 'positive'),
    	(['best', 'friend'], 'positive'),
	    (['not', 'like', 'this', 'car'], 'negative'),
	    (['this', 'view', 'horrible'], 'negative'),
	    (['feel', 'tired', 'this', 'morning'], 'negative'),
	    (['not', 'looking', 'forward', 'the', 'concert'], 'negative'),
	    (['enemy'], 'negative')]
"""




test_tweets = [
	(['feel', 'happy', 'this', 'morning'], 'positive'),
	(['larry', 'friend'], 'positive'),
	(['not', 'like', 'that', 'man'], 'negative'),
	(['house', 'not', 'great'], 'negative'),
	(['your', 'song', 'annoying'], 'negative')
]

# classifier
def get_word_features(wordlist):
	wordlist = nltk.FreqDist(wordlist)
	word_features1 = wordlist.keys()
	return word_features1

def get_words_in_tweets(tweets):
	all_words = []
	for (words, sentiment) in tweets:
		all_words.extend(words)
	return all_words


word_features = get_word_features(get_words_in_tweets(tweets))




"""
<FreqDist:
    'this': 6,
    'car': 2,
    'concert': 2,
    'feel': 2,
    'morning': 2,
    'not': 2,
    'the': 2,
    'view': 2,
		'about': 1,
		'amazing': 1,
    ..
>
"""

"""
word_features = [
    'this',
    'car',
    'concert',
    'feel',
    'morning',
    'not',
    'the',
    'view',
    'about',
    'amazing',
    ...
]
"""

def extract_features(document):
	document_words = set(document)
	features = {}
	# what's happening here?
	for word in word_features:
		features['contains(%s)' %word] = (word in document_words)
	return features

"""
Result of the above code

	{
	'contains(not)': False,
	'contains(view)': False,
	'contains(best)': False
	'contains(excited)': False,
	'contains(morning)': False, 
	'contains(about)': False,
	'contains(horrible)': False,
	'contains(like)': False,
	'contains(this)': True,
	'contains(friend)': False,
	'contains(concert)': False,
	'contains(feel)': False,
	'contains(love)': True,
	'contains(looking)': False,
	'contains(tired)': False,
	'contains(forward)': False7
	'contains(car)': True,
	'contains(the)': False,
	'contains(amazing)': False,
	'contains(enemy)': False,
	'contains(great)': False
	}
"""
tweet = "larry is my friend"


# above, along with the tweets are fed as training data set
training_set = nltk.classify.apply_features(extract_features, tweet)


# as we have our training set, we can classify them
classifier = nltk.NaiveBayesClassifier.train(training_set)


# now classify: larry is my friend



print classifier.classify(extract_features(tweet.split()))
