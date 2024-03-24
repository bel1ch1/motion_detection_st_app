import streamlit as st


st.set_page_config(page_title='app', page_icon=':tada:', layout='wide')


with st.container():
    st.subheader("textt")
    st.title("data")
    st.write("text    text")


with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column():
        st.header("what i do")
        st.write("##")
