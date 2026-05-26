from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import json

from datasets import load_dataset
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    Trainer,
    TrainingArguments,
    DataCollatorWithPadding
)
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, precision_recall_fscore_support

# ----------------------------
# 1. LOAD DATASET (YOUR FILE)
# ----------------------------
dataset = load_dataset(
    "csv",
    data_files="OPJ_korpus_anotiran_finalno.csv",
    delimiter=";"
)

dataset = dataset["train"]

TEXT_COLUMN = "text"
LABEL_COLUMN = "label"

# ----------------------------
# 2. ENCODE LABELS
# ----------------------------
label_encoder = LabelEncoder()
dataset = dataset.add_column(
    "labels",
    label_encoder.fit_transform(dataset[LABEL_COLUMN])
)

dataset = dataset.remove_columns([LABEL_COLUMN])

# ----------------------------
# 3. TRAIN / TEST SPLIT
# ----------------------------
dataset = dataset.train_test_split(test_size=0.2, seed=42)

# ----------------------------
# 4. TOKENIZER + MODEL
# ----------------------------
checkpoint = "bert-base-uncased"

tokenizer = AutoTokenizer.from_pretrained(checkpoint)

def tokenize(batch):
    return tokenizer(batch[TEXT_COLUMN], truncation=True)

dataset = dataset.map(tokenize, batched=True)

model = AutoModelForSequenceClassification.from_pretrained(
    checkpoint,
    num_labels=len(label_encoder.classes_)
)

# ----------------------------
# 5. DATA COLLATOR
# ----------------------------
data_collator = DataCollatorWithPadding(tokenizer=tokenizer)

# ----------------------------
# 6. METRICS
# ----------------------------
def compute_metrics(eval_pred):
    logits, labels = eval_pred
    preds = np.argmax(logits, axis=1)

    precision, recall, f1, _ = precision_recall_fscore_support(
        labels, preds, average="weighted"
    )
    acc = accuracy_score(labels, preds)

    return {
        "accuracy": acc,
        "precision": precision,
        "recall": recall,
        "f1": f1
    }

# ----------------------------
# 7. TRAINING ARGS 
# ----------------------------
training_args = TrainingArguments(
    output_dir="./results",
    eval_strategy="epoch",
    save_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    num_train_epochs=3,
    weight_decay=0.01,
    logging_dir="./logs"
)

# ----------------------------
# 8. TRAINER 
# ----------------------------
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset["train"],
    eval_dataset=dataset["test"],
    data_collator=data_collator,
    compute_metrics=compute_metrics
)

# ----------------------------
# 9. TRAIN
# ----------------------------
trainer.train()

# ----------------------------
# 10. EVALUATE
# ----------------------------
print(trainer.evaluate())

# ----------------------------
# 11. SAVE MODEL (FOR HUGGINGFACE)
# ----------------------------
model.save_pretrained("./bert-opj-model")
tokenizer.save_pretrained("./bert-opj-model")

# 12. CONFUSION MATRIX SAVING

predictions = trainer.predict(dataset["test"])

preds = np.argmax(predictions.predictions, axis=1)
labels = predictions.label_ids

cm = confusion_matrix(labels, preds)

# Save matrix as JSON
with open("confusion_matrix.json", "w") as f:
    json.dump(cm.tolist(), f, indent=4)

# Plot image
plt.figure(figsize=(8,6))

sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues"
)

plt.title("Confusion Matrix - BERT")
plt.xlabel("Predicted")
plt.ylabel("Actual")

plt.savefig("confusion_matrix.png")
plt.close()

print("Confusion matrix saved.")