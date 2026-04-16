import streamlit as st
from kinetics_engine import predict_parenteral_stability

st.title("💉 Parenteral Stability Prediction Agent")

pH = st.slider("pH",1.0,10.0,7.0)
temp = st.slider("Temperature (°C)",5,60,25)
oxygen = st.selectbox(
"Oxygen Exposure",
["Low","Medium","High"]
)

if st.button("Predict Stability"):

    k,t90 = predict_parenteral_stability(
        pH,temp,oxygen
    )

    st.write("Rate Constant:",k)
    st.write("t90 (days):",t90)
