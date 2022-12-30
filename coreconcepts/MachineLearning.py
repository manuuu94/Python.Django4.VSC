#machine learning which is subset of AI
#we build a model or engine and give lots of datas, pictures or whatever, based on that it will determine based on the xp it already received
#self driving cars, robotics, language processing, vision processing, forecasting stock market trends, weather, games, etc.

#FIRST WE IMPORT THE DATA, CLEAN THE DATA, SPLIT IT AND CREATE A MODEL. TRAIN THE MODEL AND ASK IT TO MAKE PREDICTIONS. EVALUATE.
#1. import the data (csv file, for example).
#2. clean the data (remove duplicates or unnecessary data) text values should be converted to numeric values
#3. split the data into trainings/test sets (for example, if images, use 80% for trainings, 20% for testing
#4. create a model - selecting an algorithm to analyze the data. decision trees, neural networks, etc. Depends on the type of problem and input data.
#note:there are many libraries that include the algorithms to use, for example, side kick learn.
#5. traing the model
#6. make predictions
#7. evaluate and improve by measuring accuracy

#each algorithm has parameters we may modify to improve accuracy

#LIBRARIES
#numpy - provides a multidimensional array - very popular library
#pandas - dataframe which is a data structure similar to an excel spreadsheet. we have rows and columns
#matplotlib - is a twod imenisonal pltoggin library for
#sci-kit learn most popular machine learning library in python

#JUPITER for writing our code because it makes it really easy to inspect it
#how to load data set saved CSV file in jupiter

#kaggle.com is a placed where to do data science projects.

#import pandas as pd
#df = pd.read_csv('vgsales.csv')
#df

#its different because jupiter notebook will save the results too, as if it was the console.

#import pandas as pd
#from sklearn.tree import DecisionTreeClassifier
#from sklearn.externals import joblib
#from sklearn import tree

##music_data = pd.read_csv('filename.csv')
#x=music_data.drop(columns=['genre'])
#y=music_data['genre']
#model = DecisionTreeClassifier()
#model.fit(x,y)

#store training module in file
#joblib.dump(model,'filename.joblib')
#model = joblib.load(model,'filename.joblib')

#tree.export_graphviz(model,out_file='filename.dot',feature_names=['age','gender'],class_names=sorted(y.unique()),label='all',rounded=True,filled=True)

#predicitions=model.predict([[21,1],[22,0]])

#4:59:22

