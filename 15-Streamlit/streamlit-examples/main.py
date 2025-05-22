import streamlit as st

st.title("Hello World!")

st.header("This is a header")
st.subheader("This is a subheader")
st.text("This is a text")
st.markdown("This is a markdown")
st.code("This is a code")
st.latex("This is a latex")
st.write("This is a write")
st.write("This is a write", "with multiple arguments")
st.write("This is a write", 1, 2, 3)
st.write("This is a write", {"key": "value"})


chai = st.selectbox("Select a color", ["red", "green", "blue"])
st.write("You selected", chai)
