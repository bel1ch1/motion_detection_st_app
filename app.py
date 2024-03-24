import streamlit as st
import requests
import streamlit_authenticator as stauth
from streamlit_lottie import st_lottie


st.set_page_config(page_title='app', page_icon=':tada:', layout='wide')


# Initialize connection.
conn = st.connection("postgresql", type="sql")
df = conn.query('SELECT * FROM users;', ttl="10m")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_coding = load_lottieurl("https://lottie.host/f16d83f9-e03f-4ec1-9859-49df40c5d3e9/xxBliHlv9K.json")


with st.container():
    st.subheader("textt")
    st.write(df.username)


with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.write("tstststst")

    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")
