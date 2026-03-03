from sklearn.metrics import r2_score, mean_absolute_error

def evaluate_model(y_test, predictions):
    return {
        "R2 Score": r2_score(y_test, predictions),
        "MAE": mean_absolute_error(y_test, predictions)
    }