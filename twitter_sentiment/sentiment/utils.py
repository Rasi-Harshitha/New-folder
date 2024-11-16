import re
import pickle
import joblib
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import nltk
import os

nltk.download('stopwords')
current_dir = os.path.dirname(__file__)
# Initialize the stemmer
port_stem = PorterStemmer()

def stemming(content):
    stemmed_content = re.sub('[^a-zA-Z]', ' ', content)  # Remove non-alphabetical characters
    stemmed_content = stemmed_content.lower()
    stemmed_content = stemmed_content.split()
    stemmed_content = [port_stem.stem(word) for word in stemmed_content if word not in stopwords.words('english')]
    stemmed_content = ' '.join(stemmed_content)
    return stemmed_content

# Load pre-trained models
model_path = os.path.join(current_dir, "models/trained_model.sav") 
vectorizer_path = os.path.join(current_dir,"models/vectorizer (1).sav")

loaded_model = pickle.load(open(model_path, 'rb'))
vectorizer = joblib.load(vectorizer_path)

def predict_sentiment(tweet):
    # Process the tweet,
    processed_tweet = stemming(tweet)

    # Transform using the vectorizer
    transformed_tweet = vectorizer.transform([processed_tweet])

    # Predict the sentiment
    prediction = loaded_model.predict(transformed_tweet)
    if prediction[0] == 1:
        return "Positive"
    elif prediction[0]==0:
        return "Negative"
    else:
        return "Neutral"
