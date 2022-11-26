import streamlit as st
from datetime import datetime, time

st.title("Hello Streamlit App")

# time_now = time.now()

date_now = datetime.now()

# st.write(time_now)
st.write("Hello from codespace")
st.write(date_now)

st.header("This is added after deployment")