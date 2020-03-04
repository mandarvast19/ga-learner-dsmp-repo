# --------------
import pandas as pd
from collections import Counter

# Load dataset
data = pd.read_csv(path)
print(data.isna().sum())
print(data.describe())


# --------------
import seaborn as sns
from matplotlib import pyplot as plt
sns.set_style(style='darkgrid')

# Store the label values 
label = data.iloc[:,-1]
sns.countplot(label)
plt.xticks(rotation=90)

# plot the countplot



# --------------
# make the copy of dataset
data_copy = data.copy()


# Create an empty column 
data_copy['duration'] = ""


# Calculate the duration
mask1 = (label == 'WALKING_UPSTAIRS')
mask2 = (label == 'WALKING_DOWNSTAIRS')
duration_df = data_copy.groupby([label[mask1|mask2],'subject'])['duration'].count()*1.28
duration_df=pd.DataFrame(duration_df)

# Sort the values of duration
plot_data=duration_df.sort_values(by='duration').reset_index()
sns.barplot(data=plot_data, x='subject', y='duration', hue='Activity')



# --------------
#exclude the Activity column and the subject column
feature_cols = data.drop(['subject','Activity'],axis=1).columns

#Calculate the correlation values
correlated_values = data[feature_cols].corr()

#stack the data and convert to a dataframe
correlated_values =  pd.DataFrame(correlated_values.stack().reset_index())
correlated_values.rename(columns={'level_0':'Feature1','level_1':'Feature2',0:'Correlation_score'},inplace=True)

#create an abs_correlation column
correlated_values['abs_correlation'] = correlated_values['Correlation_score'].abs()

#Picking most correlated features without having self correlated pairs
s_corr_list = correlated_values.sort_values(by = 'abs_correlation')
top_corr_fields = s_corr_list[s_corr_list['Feature1']!=s_corr_list['Feature2']]
top_corr_fields = top_corr_fields[top_corr_fields['abs_correlation']>0.8]
top_corr_fields



# --------------
# importing neccessary libraries
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import precision_recall_fscore_support as error_metric
from sklearn.metrics import confusion_matrix, accuracy_score

# Encoding the target variable
le = LabelEncoder()
data['Activity'] = le.fit_transform(data['Activity'])

# split the dataset into train and test
X = data.iloc[:,:-1]
y = data.iloc[:,-1]

# Baseline model 
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=40)
classifier = SVC()
clf = classifier.fit(X_train,y_train)
y_pred = clf.predict(X_test)
precision,accuracy,f_score,support = error_metric(y_test,y_pred,average='weighted')
model1_score = accuracy_score(y_test,y_pred)
print(accuracy,precision,f_score,model1_score)



# --------------
# importing libraries
from sklearn.svm import LinearSVC
from sklearn.feature_selection import SelectFromModel

# Feature selection using Linear SVC
lsvc = LinearSVC(C=0.01,penalty='l1',dual=False,random_state=42)
lsvc.fit(X_train,y_train)


# model building on reduced set of features
model_2 = SelectFromModel(lsvc,prefit=True)
new_train_features = model_2.transform(X_train)
new_test_features = model_2.transform(X_test)
classifier_2 = SVC()
clf_2 = classifier_2.fit(new_train_features,y_train)
y_pred_new = clf_2.predict(new_test_features)
model2_score = accuracy_score(y_test,y_pred_new)
precision,recall,f_score,support = error_metric(y_test,y_pred_new,average='weighted')
print(model2_score,precision,recall,f_score)



# --------------
# Importing Libraries
from sklearn.model_selection import GridSearchCV

# Set the hyperparmeters
parameters = {'kernel':['linear','rbf'],'C':[100,20,1,0.1]}

# Usage of grid search to select the best hyperparmeters
selector = GridSearchCV(SVC(),scoring='accuracy',param_grid=parameters)
selector.fit(new_train_features,y_train)
params = selector.best_params_
print(selector.best_score_)
means = selector.cv_results_['mean_test_score']
stds = selector.cv_results_['std_test_score']
print(params,means,stds)

# Model building after Hyperparameter tuning
classifier_3 = SVC(kernel='rbf',C=20)
clf_3 = classifier_3.fit(new_train_features,y_train)
y_pred_final = clf_3.predict(new_test_features)
model3_score = accuracy_score(y_test,y_pred_final)
precision,recall,f_score,support = error_metric(y_test,y_pred_final,average='weighted')
print(model3_score,precision,recall,f_score)




