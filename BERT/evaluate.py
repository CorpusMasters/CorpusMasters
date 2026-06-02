import numpy as np
from sklearn.metrics import classification_report, confusion_matrix

preds = trainer.predict(dataset["validation"])

y_pred = np.argmax(preds.predictions, axis=1)
y_true = preds.label_ids

print(classification_report(y_true, y_pred))
print(confusion_matrix(y_true, y_pred))