from sklearn.metrics import classification_report, accuracy_score
from logger import log_event

def evaluate_model(model, X_test, y_test):
    log_event("Evaluating model performance...")
    predictions = (model.predict(X_test) > 0.5).astype(int)
    accuracy = accuracy_score(y_test, predictions)
    report = classification_report(y_test, predictions)
    log_event(f"Model Accuracy: {accuracy}")
    log_event(f"Classification Report:\n{report}")
