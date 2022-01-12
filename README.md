# Kaggle Prediction Competitions


## 1- TITANIC-MACHINE LEARNING FROM DISASTER

- [Kaggle link to the competition](https://www.kaggle.com/c/titanic)

### Achieved roughly 88% of validation accuracy(cv=5), and 82% of accuracy on the test dataset.

Dependencies:
- Pandas
- Numpy
- Matplotib
- Seaborn
- Sci-Kit learn

Employed algorithms:
- [KNNimputer](https://scikit-learn.org/stable/modules/generated/sklearn.impute.KNNImputer.html)
- [OneHotEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html)
- [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html)
- [RandomOverSampler](https://imbalanced-learn.org/stable/references/generated/imblearn.over_sampling.RandomOverSampler.html)
- [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html)
- [RandomForestClassification](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)

 

## 2- MNIST - DIGIT RECOGNIZER

- [Kaggle link to the competition](https://www.kaggle.com/c/digit-recognizer)

### The training and test accuracies are 99.46% and 99.44%.

Two convolutional and one fully connected linear layers are employed.

Dependencies:
- Numpy
- Matplotlib
- Seaborn
- Pytorch
- Torchvision