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

---

# 🚀 Conclusion

The fine-tuned Gemma 2 2B IT model achieves strong performance on Croatian sentiment classification, with the best F1-score reaching **0.8820**. 
