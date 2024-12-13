import streamlit as st
st.title("even or odd")
n=st.number_input("enter the number",min_value=1,step=1)
if st.button("even/odd"):
    if n%2==0:
       st.success("even number")
    else:
        st.error("odd number")
