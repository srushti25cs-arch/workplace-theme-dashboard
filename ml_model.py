import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


CONFIDENCE_THRESHOLD = 0.60


def train_model():

    df = pd.read_csv("survey_data.csv")

    training_data = df[
        (df["category"] != "Unclear") &
        (df["input_text"].fillna("").str.strip() != "")
    ]

    X_text = training_data["input_text"]

    y = training_data["category"]

    vectorizer = TfidfVectorizer(
        lowercase=True,
        stop_words="english"
    )

    X = vectorizer.fit_transform(X_text)

    model = LogisticRegression(
        max_iter=1000
    )

    model.fit(X, y)

    return vectorizer, model


def classify_comment(text, vectorizer, model):

    if not text or not text.strip():

        return "Needs Review", 0.0

    X = vectorizer.transform([text])

    probabilities = model.predict_proba(X)[0]

    best_index = probabilities.argmax()

    category = model.classes_[best_index]

    confidence = probabilities[best_index]

    if confidence < CONFIDENCE_THRESHOLD:

        category = "Needs Review"

    return category, round(float(confidence), 2)