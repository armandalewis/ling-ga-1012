#integrate with Hugging Face pipeline (datasets.Metric library) for eval of model predictions
#one step with https://huggingface.co/docs/datasets/using_metrics.html

import datasets
metric = datasets.load_metric('my_metric')
model_predictions = model(model_inputs)
final_score = metric.compute(predictions=model_predictions, references=gold_references)


#general
from sklearn.metrics import accuracy_score, precision_recall_fscore_support

def compute_metrics(pred):
    labels = pred.label_ids
    preds = pred.predictions.argmax(-1)
    precision, recall, f1, _ = precision_recall_fscore_support(labels, preds, average='binary')
    acc = accuracy_score(labels, preds)
    return {
        'accuracy': acc,
        'f1': f1,
        'precision': precision,
        'recall': recall
    }


