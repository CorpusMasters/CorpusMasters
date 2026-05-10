import pandas as pd
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import (
    accuracy_score,
    precision_recall_fscore_support
)

from xgboost import XGBClassifier

train_df = pd.read_excel("TRAIN_1234.xlsx")
test1_df = pd.read_excel("test_1.xlsx")
test2_df = pd.read_excel("test_2.xlsx")
test3_df = pd.read_excel("test_3.xlsx")
test4_df = pd.read_excel("test_4.xlsx")

train_df.columns = train_df.columns.str.strip().str.lower()
test1_df.columns = test1_df.columns.str.strip().str.lower()
test2_df.columns = test2_df.columns.str.strip().str.lower()
test3_df.columns = test3_df.columns.str.strip().str.lower()
test4_df.columns = test4_df.columns.str.strip().str.lower()

X_train = train_df["text"].astype(str)
y_train = train_df["label"]

encoder = LabelEncoder()

y_train_encoded = encoder.fit_transform(y_train)

# save encoder
joblib.dump(encoder, "label_encoder.pkl")

vectorizer = TfidfVectorizer()

X_train_tfidf = vectorizer.fit_transform(X_train)

# save vectorizer
joblib.dump(vectorizer, "tfidf_vectorizer.pkl")

model = XGBClassifier(
    objective="multi:softmax",
    num_class=len(encoder.classes_),
    eval_metric="mlogloss",
    random_state=42
)

model.fit(X_train_tfidf, y_train_encoded)

# save model
joblib.dump(model, "xgboost_model.pkl")

print("Model trained successfully.")

def evaluate(test_df, test_name):

    X_test = test_df["text"].astype(str)
    y_test = test_df["label"]

    y_test_encoded = encoder.transform(y_test)

    X_test_tfidf = vectorizer.transform(X_test)

    predictions = model.predict(X_test_tfidf)

    accuracy = accuracy_score(y_test_encoded, predictions)

    precision, recall, f1, _ = precision_recall_fscore_support(
        y_test_encoded,
        predictions,
        average="weighted",
        zero_division = 0
    )

    print(f"\n===== {test_name} =====")
    print("Accuracy :", round(accuracy, 4))
    print("Precision:", round(precision, 4))
    print("Recall   :", round(recall, 4))
    print("F1-score :", round(f1, 4))

evaluate(test1_df, "TEST 1")
evaluate(test2_df, "TEST 2")
evaluate(test3_df, "TEST 3")
evaluate(test4_df, "TEST 4")