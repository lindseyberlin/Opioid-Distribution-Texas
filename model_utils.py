'''
Note! This utility file is currently non-functional.
'''

mport numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.utils.multiclass import unique_labels

# Visualizing a confusion matrix
def vis_cm(y_true, y_pred):
    # Takes true values first, then predicted values
    c_mat = confusion_matrix(y_true, y_pred)

    plt.subplots()
    # Visualizes the matrix
    sns.heatmap(c_mat, annot=True, cmap="Blues", fmt='g')

    # Adds title and axis labels
    plt.title('Confusion Matrix')
    plt.ylabel('True Label')
    plt.xlabel('Predicted Label')

    # Adds appropriate axis scales
    class_names = unique_labels(y_true, y_pred)
    tick_marks = np.arange(len(class_names))
    # The +.5 here just centers the labels, red or white, since it's 2x2
    plt.xticks(tick_marks + .5, class_names)
    plt.yticks(tick_marks + .5, class_names)

    plt.show()

# Printing scores for each model
def print_scores(model, X_train, X_test, y_train, y_test, y_pred):
    print("Training Accuracy: {}".format(model.score(X_train, y_train)))
    print("Testing Accuracy: {}".format(model.score(X_test, y_test)))
    print(classification_report(y_test, y_pred))