from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from src.utils import *

class TextClassifier(object):

    def __init__(self, preprocess_text, vectorizer, classifier):
        self.preprocess_text = np.vectorize(preprocess_text)
        self.vectorizer = vectorizer
        self.classifier = classifier

    def fit(self, X, y):

        print('Preprocessing texts...', end=' ')
        X_preprocessed = self.preprocess_text(X)
        print('Done.')

        print('Vectorizing texts...', end=' ')
        X_vectorized = self.vectorizer.fit_transform(X_preprocessed)
        print('Done.')

        print('Fitting classifier...', end=' ')
        self.classifier.fit(X_vectorized, y)
        print('Done.')

        return None

    def predict(self, X, y=None):

        X_preprocessed = self.preprocess_text(X)
        X_vectorized = self.vectorizer.transform(X_preprocessed)
        y_proba = self.classifier.predict_proba(X_vectorized)
        y_proba = y_proba[:, 1]

        return y_proba
