import streamlit as st

st.title(":red[Innomatics] Data App :sunglasses:")
st.header("Data Science Internship")
st.subheader("Feb 2023")

CODE = '''print("Hello World!")'''

st.code(CODE, language="python")

st.snow()

btn_click = st.button("Click Me!")

if btn_click == True:
    st.subheader("You clicked me :cry:")
    st.balloons()
