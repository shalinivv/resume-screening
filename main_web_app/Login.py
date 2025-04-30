import streamlit as st

st.title(":blue[Resume Screening]")
placeholder = st.empty()

uname = "hrofabc"
pwd = "password"

with placeholder.form("login"):
    st.markdown("#### Enter your credentials")
    Username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    submit = st.form_submit_button("Login")

if submit and Username == uname and password == pwd:
    placeholder.empty()
    st.success("Login successful")
    st.markdown('<a href="/app" target="_self">Resume Screening</a>', unsafe_allow_html=True)
elif submit and Username != uname and password != pwd:
    st.error("Login failed")
else:
    pass
