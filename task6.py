import streamlit as st

st.title("Shopping Bills")


sal = st.number_input("Enter the salary", value=0)
st.write(f"The current salary is: ${sal}")


bill1 = st.number_input("Enter the bill1", value=0)
st.write(f"The current bill1 is: ${bill1}")

bill2 = st.number_input("Enter the bill2", value=0)
st.write(f"The current bill2 is: ${bill2}")

bill3 = st.number_input("Enter the bill3", value=0)
st.write(f"The current bill3 is: ${bill3}")

total = bill1 + bill2 + bill3
if st.button("total amount"):
    if sal != 0:
        percentage = (total / sal) * 100
        st.write(f"Total shopping amount: ${total}")
        st.write(f"Percentage of salary spent on shopping: {percentage:.2f}%")
    else:
        st.error("Salary cannot be zero. Cannot calculate percentage.")
