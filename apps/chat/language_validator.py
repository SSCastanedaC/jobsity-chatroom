from textblob import TextBlob

def valid_language(msg):
	if len(msg) >= 3:
		return (True if TextBlob(msg).detect_language() == 'es' else False)
	else:
		return True