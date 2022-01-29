import pandas as pd
import numpy as np


def outliers(dataset, labels, column):
    first_quar = dataset[column].quantile(0.25)
    third_quar = dataset[column].quantile(0.75)

    IQR = third_quar - first_quar
    out_range = np.array([first_quar - 1.5 * IQR, third_quar + 1.5 * IQR])
    mask = dataset[(dataset[column] < out_range[0]) | (dataset[column] > out_range[1])].index
    data = dataset.drop(mask, axis=0)
    targets = labels.drop(mask, axis=0)
    return data, targets