from django.shortcuts import render
from .utils import predict_sentiment

def analyze_tweet(request):
    sentiment = None
    emoji = None

    if request.method == 'POST':
        tweet = request.POST.get('tweet')  # Get the input tweet from the form
        if tweet:
            sentiment = predict_sentiment(tweet)
            if sentiment == "Positive":
                emoji = "😊"
            elif sentiment=="Negative":
                emoji="😞"
            else:
                emoji = "😐"

    return render(request, 'home.html', {'sentiment': sentiment, 'emoji': emoji})
