import joblib
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model = joblib.load(os.path.join(BASE_DIR, "spam_model.joblib"))
tfidf = joblib.load(os.path.join(BASE_DIR, "tfidf_vectorizer.joblib"))

def predict(text : str) -> str:
    """
    Predict if the given text is spam or not.
    
    Args:
        text (str): The text to predict.
        
    Returns:
        str: "spam" if the text is spam, "not spam" otherwise.
    """
    X = tfidf.transform([text])
    pred = model.predict(X)[0]
    return pred