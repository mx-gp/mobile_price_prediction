#EDA PACKAGES
import pandas as pd
import numpy as np

# ML PACKAGES
from sklearn.model_selection import train_test_split
from joblib import dump

csv_file_path = "/path_to_csv/train.csv"
df = pd.read_csv(csv_file_path)

# features
include = ['battery_power','dual_sim','fc','pc','int_memory','n_cores','ram']
df_features = df[include]
df_features

# label 
label = 'price_range'
y = df[label]

X_train,X_test,y_train,y_test = train_test_split(df_features,y,test_size=0.33,random_state=0)


from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier()
knn.fit(X_train,y_train)

#  accuracy of trained knn
print(knn.score(X_train,y_train))

################################### save model ###################################

model_path_where_you_have_to_save_it = '/model_path_where_you_have_to_your_model/test.pkl'
dump(knn,model_path_where_you_have_to_save_it)
print("Model dumped!")
