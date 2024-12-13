import streamlit as st

st.title("Gross Salary")
sal = st.number_input("enter the salary", value=0)
st.write("The current number is ", sal)
if sal < 10000:
    hra = 0.67 * sal
    da = 0.73 * sal
elif 10000 <= sal <= 20000:
    hra = 0.69 * sal
    da = 0.76 * sal
else:
    hra = 0.73 * sal
    da = 0.89 * sal
gross_salary = sal + hra + da
if st.button("calculate gross salary"):
    st.write(f"Gross Salary: {gross_salary}")
