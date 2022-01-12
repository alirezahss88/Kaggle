# Kaggle Prediction Competitions


## 1- TITANIC-MACHINE LEARNING FROM DISASTER

- [Kaggle link to the competition](https://www.kaggle.com/c/titanic)
- [You may download the dataset directly from kaggle](https://storage.googleapis.com/kaggle-competitions-data/kaggle-v2/3136/26502/bundle/archive.zip?GoogleAccessId=web-data@kaggle-161607.iam.gserviceaccount.com&Expires=1641753668&Signature=mVWdYUIokHpLi5XSfd1s8uvhnfv%2B3COQxjGdn1OhVeLA37si%2FN3j0osa9Pj7%2FxdIbg%2FV3XVXwRkhI99WPWbEUaS1rhafBeYg4Gkz6H2vgQ0PAkKWGepJA14W8plFSBgXrvZHrrJxS6Pz3elBDYqcF71YLWIFfLMeferIud5AOA%2B1WzhdKAuz5o5qJZheEg2A6M2I%2Bx%2F8%2FJWkquz%2BHwyBp2obVrRpsn7ON5A6Nv1gi7A4u5O7sRnXyFGVs8Epi3bd4szg3fWDUoXXQI%2Bns%2BZKKA4rLcGqC3tfySQ3%2F%2FNTAz%2B0eqste%2FobFiFN8eAkG%2FDkoMRyVv010poO0fgA39Nicg%3D%3D&response-content-disposition=attachment%3B+filename%3Dtitanic.zip)

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