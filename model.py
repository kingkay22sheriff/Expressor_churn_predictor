import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import pickle


model = pickle.load(open('model.pkl', 'rb'))
categorical_columns = pickle.load(open('married_fuga.pkl', 'rb'))


def prediction(data):

    le = LabelEncoder()
    df = pd.DataFrame(data)

    #columns = #[0, 1, 2, 14, 16]

    for i in data:
        if type(i) == str:
        #print(data.iloc[i])
            df.iloc[data.index(i)] = le.fit_transform(df.iloc[data.index(i)])

    pred = model.predict(df.values.reshape(1,-1))

    if pred[0] == 1:
        return "The Customer Left the Telecommunication Service"
    else:
        return "The Customer Enjoys the Telecommunication Service"
    


print(prediction(['00001dd6fa45f7ba044bd5d84937be464ce78ac2', 'DAKAR', 'K > 24 month', 13500.0, 15.0, 13502.0, 4501.0, 18.0,
 43804.0, 41.0, 102.0, 2.0, 1.0, 1.0, 'NO', 62, 'Data:1000F=5GB,7d', 11.0]))

