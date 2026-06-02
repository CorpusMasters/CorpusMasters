import pandas as pd
import numpy as np

from datasets import Dataset

from sklearn.metrics import (
    accuracy_score,
    precision_recall_fscore_support,
    confusion_matrix
)

from unsloth import FastLanguageModel

from transformers import TrainingArguments

from transformers import Trainer

train_df = pd.read_csv("/content/drive/MyDrive/TRAIN_1234.csv")

test1_df = pd.read_csv("/content/drive/MyDrive/test_1.csv")
test2_df = pd.read_csv("/content/drive/MyDrive/test_2.csv")
test3_df = pd.read_csv("/content/drive/MyDrive/test_3.csv")
test4_df = pd.read_csv("/content/drive/MyDrive/test_4.csv")

for df in [train_df, test1_df, test2_df, test3_df, test4_df]:

    df.columns = df.columns.str.strip().str.lower()

    df.dropna(subset=["text", "label"], inplace=True)

def create_prompt(text, label=None):

    if label is not None:

        return f"""
Classify the sentiment of the following review.

Review:
{text}

Sentiment:
{label}
"""

    else:

        return f"""
Classify the sentiment of the following review.

Review:
{text}

Sentiment:
"""

train_prompts = []

for _, row in train_df.iterrows():

    prompt = create_prompt(
        row["text"],
        row["label"]
    )

    train_prompts.append({
        "text": prompt
    })

train_dataset = Dataset.from_list(train_prompts)

max_seq_length = 512

model, tokenizer = FastLanguageModel.from_pretrained(

    model_name = "unsloth/gemma-2-2b-it",

    max_seq_length = max_seq_length,

    dtype = None,

    load_in_4bit = True,

)

model = FastLanguageModel.get_peft_model(

    model,

    r = 16,

    target_modules = [
        "q_proj",
        "k_proj",
        "v_proj",
        "o_proj",
        "gate_proj",
        "up_proj",
        "down_proj",
    ],

    lora_alpha = 16,

    lora_dropout = 0,

    bias = "none",

    use_gradient_checkpointing = "unsloth",

    random_state = 42,

    use_rslora = False,

    loftq_config = None,
)

def tokenize(example):

    return tokenizer(

        example["text"],

        truncation=True,

        padding="max_length",

        max_length=512,
    )

def tokenize(example):

    tokens = tokenizer(

        example["text"],

        truncation=True,

        padding="max_length",

        max_length=512,
    )

    tokens["labels"] = tokens["input_ids"].copy()

    return tokens

train_dataset = train_dataset.map(tokenize)

# remove original text column
train_dataset = train_dataset.remove_columns(["text"])

trainer = Trainer(

    model = model,

    train_dataset = train_dataset,

    args = TrainingArguments(

        per_device_train_batch_size = 2,

        gradient_accumulation_steps = 4,

        warmup_steps = 5,

        num_train_epochs = 1,

        learning_rate = 2e-4,

        fp16 = False,

        bf16 = False,

        logging_steps = 10,

        optim = "adamw_8bit",

        weight_decay = 0.01,

        lr_scheduler_type = "linear",

        seed = 42,

        output_dir = "outputs",

        report_to = "none",

        remove_unused_columns=False,
    ),
)


trainer.train()


FastLanguageModel.for_inference(model)

def predict_sentiment(text):

    prompt = create_prompt(text)

    inputs = tokenizer(
        prompt,
        return_tensors="pt"
    ).to("cuda")

    outputs = model.generate(

        **inputs,

        max_new_tokens = 10,

        use_cache = True
    )

    decoded = tokenizer.batch_decode(
        outputs,
        skip_special_tokens=True
    )[0]

    prediction = decoded.split("Sentiment:")[-1].strip()

    prediction = prediction.split()[0].lower()

    return prediction


def evaluate_model(test_df, test_name):

    true_labels = []
    predicted_labels = []

    for _, row in test_df.iterrows():

        text = row["text"]

        true_label = row["label"]

        prediction = predict_sentiment(text)

        true_labels.append(true_label)
        predicted_labels.append(prediction)

    accuracy = accuracy_score(
        true_labels,
        predicted_labels
    )

    precision, recall, f1, _ = precision_recall_fscore_support(

        true_labels,
        predicted_labels,

        average="weighted",

        zero_division=0
    )

    print(f"\n===== {test_name} =====")

    print("Accuracy :", round(accuracy, 4))
    print("Precision:", round(precision, 4))
    print("Recall   :", round(recall, 4))
    print("F1-score :", round(f1, 4))

    print("\nConfusion Matrix:")

    print(
        confusion_matrix(
            true_labels,
            predicted_labels
        )
    )



evaluate_model(test1_df, "TEST 1")
evaluate_model(test2_df, "TEST 2")
evaluate_model(test3_df, "TEST 3")
evaluate_model(test4_df, "TEST 4")



model.save_pretrained("gemma_sentiment_model")

tokenizer.save_pretrained("gemma_sentiment_model")

print("\nModel saved successfully.")


model.save_pretrained(
    "/content/drive/MyDrive/gemma_sentiment_model"
)

tokenizer.save_pretrained(
    "/content/drive/MyDrive/gemma_sentiment_model"
)
