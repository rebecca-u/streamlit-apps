#import libraries
import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

#markdown text with the iris flower type names.
st.write("""
# Simple Iris Flower Prediction App
This app predicts thetype of **Iris flower** using different features of the flower!

There are **three** different types of irises' which are called *Iris Setosa, Iris Versicolor* and *Iris Virginica*.
In 1936, British statistician and biologist **Ronald Fisher** created the Iris flower data set.
\n\nThe dataset consists of 50 samples from each of the three species of Iris flowers, with a total of 150 samples altogether.
Four features were measured from each sample: the length and the width of the sepals and petals, in centimeters(cm).
\n\n*The sepal is the outer parts of the flower, often green and leaf-like, and enclose a developing bud.

""")

#Including images and  dropdowns using st.image.
st.header("Images")
pics = {
    "Iris Setosa": "https://en.wikipedia.org/wiki/Iris_setosa#/media/File:Kosaciec_szczecinkowaty_Iris_setosa.jpg",
    "Iris Versicolor": "https://en.wikipedia.org/wiki/Iris_versicolor#/media/File:Blue_Flag,_Ottawa.jpg",
    "Iris Virginica": "https://en.wikipedia.org/wiki/Iris_virginica#/media/File:Iris_virginica_2.jpg"
}
pic = st.selectbox("Picture choices", list(pics.keys()), 0)
st.image(pics[pic], use_column_width=True, caption=pics[pic])

#header name of the sidebar
st.sidebar.header('User Input Parameters')

#custom function used to accept the 4 input parameters from the sidebar and it will create a pandas df
def user_input_features():
    sepal_length = st.sidebar.slider('Sepal length', 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider('Sepal width', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider('Petal length', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider('Petal width', 0.1, 2.5, 0.2)
    data = {'sepal_length': sepal_length,
            'sepal_width': sepal_width,
            'petal_length': petal_length,
            'petal_width': petal_width}
    features = pd.DataFrame(data, index=[0])
    return features

#store the custom function in a variable
df = user_input_features()


st.subheader('User Input parameters')
st.write(df)#this will print out the dataframe

#load in the iris dataset
iris = datasets.load_iris()
X = iris.data
Y = iris.target

#create a classifier variable consisting of the random forest classifier
clf = RandomForestClassifier()
clf.fit(X, Y) #apply the classifier to build a training model 

prediction = clf.predict(df) #make the prediction
prediction_proba = clf.predict_proba(df) #this will give the prediction probabalility

#print out of the class label and their corresponding index number 
st.subheader('Class labels and their corresponding index number')
st.write(iris.target_names)

#to get the prediction
st.subheader('Prediction')
st.write(iris.target_names[prediction])
#st.write(prediction)

#to get the prediction probablility
st.subheader('Prediction Probability')
st.write(prediction_proba)
