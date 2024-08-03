from nltk.sentiment.vader import SentimentIntensityAnalyzer
sia=SentimentIntensityAnalyzer()
sentences=[
    input("Enter the review: ") 
  
]
for sent in sentences:
    sentiment=sia.polarity_scores(sent)
    print(f"{sent}")
    print(f"{sentiment}")
def analyze_sentiment(sent):
    sentiment =sia.polarity_scores(sent)
    if sentiment['compound']>=0.05:
        return 'positive'
    elif sentiment['compound']<=0.05:
        return 'negative'
    else:
        return 'nutral'
for sent in sentences:
    result= analyze_sentiment(sent)
    print(f"{sent}")
    print(f"{result}")