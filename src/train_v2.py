import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import scale
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import confusion_matrix
from sklearn.impute import SimpleImputer
import json
import seaborn as sns
import matplotlib.pyplot as plt

def load_data(filepath):
    return pd.read_csv(filepath)

def preprocess_features(X):
    X_scaled = scale(X)
    imp = SimpleImputer(missing_values=np.nan, strategy='mean')
    imp.fit(X_scaled)
    return imp.transform(X_scaled)

def train_and_evaluate_model(X, y):
    clf = LogisticRegression()
    yhat = cross_val_predict(clf, X, y, cv=5)
    acc = np.mean(yhat == y)
    tn, fp, fn, tp = confusion_matrix(y, yhat).ravel()
    specificity = tn / (tn + fp)
    sensitivity = tp / (tp + fn)
    return acc, specificity, sensitivity, yhat

def save_metrics_to_json(filepath, metrics):
    with open(filepath, 'w') as outfile:
        json.dump(metrics, outfile)

def plot_accuracy_by_category(df, category_col, output_file):
    sns.set_color_codes("dark")
    ax = sns.barplot(x=category_col, y="pred_accuracy", data=df, palette="Greens_d")
    ax.set(xlabel=category_col.capitalize(), ylabel="Model accuracy")
    plt.savefig(output_file, dpi=80)

def main():
    # Load and preprocess the data
    df = load_data("data/data_processed.csv")
    y = df.pop("cons_general").to_numpy()
    y = np.where(y < 4, 0, 1)
    X = preprocess_features(df.to_numpy())

    # Train the model and get metrics
    acc, specificity, sensitivity, yhat = train_and_evaluate_model(X, y)

    # Save metrics
    save_metrics_to_json("report/metrics.json", {
        "accuracy": acc,
        "specificity": specificity,
        "sensitivity": sensitivity
    })

    # Add predictions to the dataframe and plot
    df['pred_accuracy'] = yhat == y
    plot_accuracy_by_category(df, "region", "report/by_region.png")

if __name__ == '__main__':
    main()