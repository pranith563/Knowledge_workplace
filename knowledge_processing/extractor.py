import nltk
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer

def pre_processing(text):
	
	#convert all the text to lowercase
	text = text.lower()

	#remove whitespaces
	#text = text.strip()
	#print(text);
	
	import string
	#tokenization	- Remove punctuation and white spaces.
	tokenizer = RegexpTokenizer(r'\w+')
	tokens = tokenizer.tokenize(text)
	print(tokens)
	#tokens = nltk.word_tokenize(text)


	table = str.maketrans('','', string.punctuation)
	stripped = [w.translate(table) for w in tokens]
	print(stripped)
	
	#Lemmatization
	lemmatizer=WordNetLemmatizer()

	for word in tokens :
		word = lemmatizer.lemmatize(word)


def extract_entities(text):

	tokens = nltk.word_tokenize(text)
	
	entities = nltk.chunk.ne_chunk(tokens)
	
	return entities

sentence = " Arthur didn't, feel, very. Good "

pre_processing(sentence)
