import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split 

def marks_prediction(marks):
    data = pd.read_csv ('https://raw.githubusercontent.com/AdiPersonalWorks/Random/master/student_scores%20-%20student_scores.csv')
    data.head(10)

    X = data.iloc[:, :-1].values  
    y = data.iloc[:, 1].values

    model = LinearRegression()
    model.fit(X,y)
    
    x_test = np.array(marks)
    x_test = x_test.reshape(1,-1)
    return model.predict(x_test)[0]
