# --------------
# import packages
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings("ignore")

# Load the dataset
df = pd.read_csv(path,sep="\t")
df.info()
# Converting date attribute from string to datetime.date datatype 
df['date'] = pd.to_datetime(df['date'])

# calculate the total length of word
length = []
leng=0
for row in df['verified_reviews']:
    leng = len(row)
    length.append(leng)

df['length'] = length


# --------------
## Rating vs feedback

# set figure size
plt.figure(figsize=(5,7))
# generate countplot
sns.countplot(x='rating',hue='feedback',data=df)
# display plot
plt.show()
## Product rating vs feedback

# set figure size


# generate barplot
sns.barplot(x='rating',y='variation',hue='feedback',data=df)

# display plot
plt.show()



# --------------
# import packages
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# declare empty list 'corpus'
corpus = []

# for loop to fill in corpus
for i in range(0,3150):
    # retain alphabets
    review=[]
    review = re.sub('[^a-zA-z\s]','',df['verified_reviews'][i])
    # convert to lower case
    review = review.lower()
    # tokenize
    review = review.split()
    # initialize stemmer object
    ps = PorterStemmer()
    # perform stemming
    stop = stopwords.words('english')
    review = [x for x in review if x not in stop]
    review = [ps.stem(i) for i in review ]

    # join elements of list
    review = ' '.join(review)
    
    # add to 'corpus'
    corpus.append(review)
# display 'corpus'
print(corpus)


# --------------
# import libraries
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split

# Instantiate count vectorizer
cv = CountVectorizer(max_features=1500)

# Independent variable
X = cv.fit_transform(corpus).toarray()

# dependent variable
y = df['feedback']
# Counts
count = y.value_counts()
# Split the dataset
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=0)
X_train.shape


# --------------
# import packages
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix, f1_score

# Instantiate classifier
rf = RandomForestClassifier(random_state=2)
# fit model on training data
rf.fit(X_train,y_train)
# predict on test data
y_pred = rf.predict(X_test)
# calculate the accuracy score
score = accuracy_score(y_test,y_pred)
# calculate the precision
precision = precision_score(y_test,y_pred)
# display 'score' and 'precision'
print(score,precision)
precision = 0.947107438016529


# --------------
# import packages
from imblearn.over_sampling import SMOTE

# Instantiate smote
smote = SMOTE(random_state=9)
# fit_sample onm training data
X_train,y_train = smote.fit_sample(X_train,y_train)
# fit modelk on training data
rf.fit(X_train,y_train)
# predict on test data
y_pred = rf.predict(X_test)
# calculate the accuracy score
score = accuracy_score(y_test,y_pred)
# calculate the precision
precision = precision_score(y_test,y_pred)
# display precision and score
print(score,precision)
score = 0.8904761904761904 
precision = 0.9439579684763573



