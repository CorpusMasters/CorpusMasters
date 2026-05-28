import pickle
import pandas as pd
import numpy as np

from datasets import Dataset
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    Trainer,
    TrainingArguments,
    DataCollatorWithPadding
)

from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import (
    accuracy_score,
    precision_recall_fscore_support
)

# =========================
# CONFIG
# =========================
TRAIN_FILE = "train.xlsx"
MODEL_NAME = "bert-base-multilingual-cased"
OUTPUT_MODEL_DIR = "./bert-opj-model"
TEXT_COLUMN = "text"
LABEL_COLUMN = "label"

# =========================
# LOAD DATA
# =========================
def load_file(path):
    if path.endswith(".csv"):
        return pd.read_csv(path, encoding="utf-8-sig")
    elif path.endswith(".xlsx"):
        return pd.read_excel(path)
    else:
        raise ValueError(f"Unsupported format: {path}")

train_df = load_file(TRAIN_FILE)

# clean text/labels
train_df[TEXT_COLUMN] = train_df[TEXT_COLUMN].astype(str)
train_df[LABEL_COLUMN] = train_df[LABEL_COLUMN].astype(str).str.strip()

# =========================
# LABEL ENCODING
# =========================
label_encoder = LabelEncoder()
train_df["labels"] = label_encoder.fit_transform(train_df[LABEL_COLUMN])

train_df = train_df.drop(columns=[LABEL_COLUMN])

dataset = Dataset.from_pandas(train_df)

# =========================
# TOKENIZER
# =========================
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

def tokenize(batch):
    return tokenizer(batch[TEXT_COLUMN], truncation=True)

dataset = dataset.map(tokenize, batched=True)

# =========================
# MODEL
# =========================
model = AutoModelForSequenceClassification.from_pretrained(
    MODEL_NAME,
    num_labels=len(label_encoder.classes_)
)

data_collator = DataCollatorWithPadding(tokenizer)

# =========================
# METRICS
# =========================
def compute_metrics(eval_pred):
    logits, labels = eval_pred
    preds = np.argmax(logits, axis=1)

    precision, recall, f1, _ = precision_recall_fscore_support(
        labels,
        preds,
        average="weighted",
        zero_division=0
    )

    acc = accuracy_score(labels, preds)

    return {
        "accuracy": acc,
        "precision": precision,
        "recall": recall,
        "f1": f1
    }

# =========================
# TRAINING ARGS
# =========================
training_args = TrainingArguments(
    output_dir="./results",
    learning_rate=2e-5,
    per_device_train_batch_size=8,
    num_train_epochs=4,
    weight_decay=0.01,
    logging_dir="./logs",
    save_strategy="epoch",
    report_to="none"
)

# =========================
# TRAINER
# =========================
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset,
    data_collator=data_collator,
    compute_metrics=compute_metrics
)

trainer.train()

# =========================
# SAVE MODEL + TOKENIZER
# =========================
model.save_pretrained(OUTPUT_MODEL_DIR)
tokenizer.save_pretrained(OUTPUT_MODEL_DIR)

# =========================
# SAVE LABEL ENCODER
# =========================
with open("label_encoder.pkl", "wb") as f:
    pickle.dump(label_encoder, f)

print("Training complete. Model + encoder saved.")
