import streamlit as st
import pickle

st.title("Addiction_prediction")

st.set_page_config(page_title="prediction", page_icon=":smiley:", layout="centered")


def load_model():
    return pickle.load(open("rf_model.pkl", "rb")) 

model = load_model()

value1 = st.number_input("Avg_Daily_Usage_Hours")
st.write("Value entered:", value1)

value2 = st.selectbox("Affects_Academic_Performance",[1,0])
st.write("Value entered:", value2)

value3 = st.number_input("Sleep_Hours_Per_Night")
st.write("Value entered:", value3)

value4 = st.selectbox("Mental_Health_Score",[4,5,6,7,8,9])
st.write("Value entered:", value4)

value5 = st.selectbox("Conflicts_Over_Social_Media",[0,1,2,3,4,5])
st.write("Value entered:", value5)


if st.button('predict'):
    input_data = [[value1, value2, value3, value4, value5]]
    prediction = model.predict(input_data)
    st.write("Prediction:", prediction[0])
    



