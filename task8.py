import streamlit as st

project = st.number_input("enter the project marks", min_value=0, max_value=100, value=0)
st.write("The current marks awarded are", project)
internal = st.number_input("enter the internal marks", min_value=0, max_value=100, value=0)
st.write("The current marks awarded are ", internal)
external = st.number_input("enter the external marks", min_value=0, max_value=100, value=0)
st.write("The current marks awarded are ", external)
if st.button("Grade"):
    if project >= 50 and internal >= 50 and external >= 50:
        total = (project * 0.70) + (internal * 0.10) + (external * 0.20)
        st.write(total)
        if total > 90:
            st.success("A grade")
        elif total>80 and total <= 90:
            st.success("B grade")
        else:
            st.success("C grade")
    if project < 50:
        st.error(f"failed in project {project}")
    if internal < 50:
        st.error(f"failed in internal {internal}")
    if external < 50:
        st.error(f"failed in external {external}")
