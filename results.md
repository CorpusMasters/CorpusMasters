# Fine-Tuning Results — Gemma 2 2B IT Model

##  Task
Sentiment classification on Croatian review dataset.

---

##  Model
- Model: Gemma 2 2B IT
- Framework: Hugging Face Transformers
- Fine-tuning method: Supervised fine-tuning (SFT-style classification setup)
- Task type: Multi-class text classification

---

##  Dataset
- Source: Croatian review dataset
- Input: text sentences
- Labels: sentiment classes
- Split:
  - Train: 80%
  - Validation: 10%
  - Test: 10%

---

#  Hyperparameter Experiments

| Test | Learning Rate | Batch Size | Epochs | Max Length | Optimizer | Weight Decay | Accuracy | Precision | Recall | F1-score |
|------|--------------|------------|---------|------------|-----------|--------------|----------|-----------|--------|----------|
| TEST 1 | 2e-5 | 8 | 3 | 128 | AdamW | 0.01 | 0.8338 | 0.8666 | 0.8338 | 0.8314 |
| TEST 2 | 3e-5 | 16 | 3 | 128 | AdamW | 0.01 | 0.8154 | 0.7877 | 0.8154 | 0.8000 |
| TEST 3 | 2e-5 | 16 | 4 | 128 | AdamW | 0.01 | 0.8852 | 0.8822 | 0.8852 | 0.8820 |
| TEST 4 | 1e-5 | 16 | 5 | 128 | AdamW | 0.01 | 0.8768 | 0.8896 | 0.8768 | 0.8811 |

---

#  Best Model

- **Best run: TEST 3**
- Reason: Highest F1-score (0.8820) and best overall balance between precision and recall.

---

#  Evaluation Results

## TEST 1
- Accuracy: 0.8338  
- Precision: 0.8666  
- Recall: 0.8338  
- F1-score: 0.8314  

Confusion Matrix:

[[ 2 0 0 0]
[ 1 45 3 2]
[ 0 33 57 16]
[ 0 7 3 222]]


---

## TEST 2
- Accuracy: 0.8154  
- Precision: 0.7877  
- Recall: 0.8154  
- F1-score: 0.8000  

Confusion Matrix:

[[ 1 15 7 2 0]
[ 2 335 25 8 0]
[ 0 25 75 14 0]
[ 4 7 5 119 0]
[ 0 3 1 2 0]]


---

## TEST 3
- Accuracy: 0.8852  
- Precision: 0.8822  
- Recall: 0.8852  
- F1-score: 0.8820  

Confusion Matrix:

[[ 6 4 3 3 0]
[ 0 130 11 9 0]
[ 1 13 50 8 0]
[ 1 7 9 354 0]
[ 0 0 0 1 0]]


---

## TEST 4
- Accuracy: 0.8768  
- Precision: 0.8896  
- Recall: 0.8768  
- F1-score: 0.8811  

Confusion Matrix:

[[ 1 0 1 1 0]
[ 0 80 12 1 0]
[ 1 4 19 4 0]
[ 0 2 7 142 0]
[ 0 1 0 0 0]]


---

#  Observations

- The model performs consistently well across all runs.
- Best performance achieved with moderate learning rate (2e-5) and longer training (4 epochs).
- Slight overfitting observed in longer training runs (TEST 4).
- Some confusion persists in minority classes.

  #  Conclusion

The fine-tuned Gemma 2 2B IT model achieves strong performance on Croatian sentiment classification, with the best F1-score reaching **0.8820**. 


# Fine-Tuning Results — BERT Sentiment Classification Model

## Task

Sentiment classification on Croatian medical review datasets.

---

## Model

* Model: BERT-base-multilingual-cased
* Framework: Hugging Face Transformers
* Fine-tuning method: Supervised fine-tuning for sequence classification
* Task type: Multi-class text classification

---

## Dataset

- Source: Croatian medical corpora dataset
- Input: text sentences
- Labels: sentiment classes
- Split:
  - Train: 80%
  - Validation: 10%
  - Test: 10%

---

## Training Configuration

| Parameter       | Value                              |
| --------------- | ---------------------------------- |
| Base checkpoint | `bert-base-multilingual-cased`                |
| Epochs          | 4                                  |
| Learning rate   | 2e-5                               |
| Batch size      | 8                                  |
| Weight decay    | 0.01                               |
| Optimizer       | AdamW                              |
| Tokenizer       | AutoTokenizer                      |
| Framework       | PyTorch + Transformers Trainer API |

---

## Evaluation Metrics

The following evaluation metrics were used:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix

Weighted averaging was applied for multi-class metric computation.

---

## Evaluation Results

Evaluation Results
## TEST 1
- Accuracy: 0.6240
- Precision: 0.6429
- Recall: 0.6240
- F1-score: 0.5751

Confusion Matrix:

[[ 0, 0, 0, 2],
 [ 0, 36, 2, 13],
 [ 0, 54, 8, 44],
 [ 0, 27, 5, 200]]

## TEST 2
- Accuracy: 0.5583
- Precision: 0.5759
- Recall: 0.5583
- F1-score: 0.5299

Confusion Matrix:

[[ 0, 11, 2, 12],
 [ 0, 235, 13, 121],
 [ 0, 51, 11, 52],
 [ 0, 21, 1, 113]]
 
## TEST 3
- Accuracy: 0.7028
- Precision: 0.6578
- Recall: 0.7028
- F1-score: 0.6696

Confusion Matrix:

[[ 0, 7, 0, 9],
 [ 0, 112, 7, 31],
 [ 0, 33, 5, 34],
 [ 0, 53, 7, 311]]

## TEST 4
- Accuracy: 0.7572
- Precision: 0.7194
- Recall: 0.7572
- F1-score: 0.7289

Confusion Matrix:

[[ 0, 0, 0, 3, 0],
 [ 0, 77, 3, 13, 0],
 [ 0, 10, 3, 15, 0],
 [ 0, 20, 2, 129, 0],
 [ 0, 1, 0, 0, 0]]

---

## Average Results

| Metric    | Average Score |
| --------- | ------------- |
| Accuracy  | 0.6606        |
| Precision | 0.6490        |
| Recall    | 0.6606        |
| F1-score  | 0.6259        |

---

## Observations

* The model achieved the strongest performance on Test 4, suggesting better alignment between the training data distribution and the evaluation dataset.
* Lower performance on Test 2 indicates potential domain or annotation differences between datasets.
* Test 3 demonstrated strong generalization capability despite being loaded from CSV format with heterogeneous preprocessing conditions.
* Overall results confirm that transformer-based architectures can successfully perform sentiment classification on Croatian-language medical review corpora.

---

## Conclusion

Based on the experimental evaluation, Gemma 2 2B IT achieved significantly better sentiment classification performance than BERT across all evaluation metrics and datasets.

The results indicate that larger instruction-tuned transformer models can provide substantial improvements in sentiment classification tasks for Croatian-language review datasets. Gemma consistently produced higher accuracy and F1-scores, demonstrating stronger contextual understanding and better overall classification capability.

However, BERT still represents a computationally lighter and more efficient alternative, while Gemma provides superior predictive performance at the cost of increased computational complexity.
