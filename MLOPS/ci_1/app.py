import streamlit as st

# create a stremlit ui
st.title("power calculator")
st.write("enter the value to calculate square, cube and fifth power")

#get user input
n = st.number_input("Enter an integer" , value=1, step=1)

#calculate the result
square = n**2
cube = n**3
fifth  = n**5

#display the result
st.write(f"The square of the value is {square}")
st.write(f"The cube of the value is {cube}")
st.write(f"The fifth power of the value is {fifth}")