import streamlit as st

# st.title(“Simple Calculator”)
# st.write(“This is a simple calculator app”)
# a = st.number_input(“Enter a number”)
# b = st.number_input(“Enter another number”)
# operation = st.selectbox(“Select Operation”, [“Add”, “Subtract”, “Multiply”, “Divide”])

# if operation == “Add”:
#     st.write(add(a, b))

# elif operation == “Subtract”:
#     st.write(sub(a, b))

# elif operation == “Multiply”:
#     st.write(mul(a, b))

# elif operation == “Divide”:
#     st.write(div(a, b))


# def add(a, b):
#   return a + b
# def sub(a, b):
#   return a - b
def mul(a, b):
  return a * b
# def div(a, b):
#   return a / b
def main():
    st.title("TDS Assignment 8 - Param Chordiya 21f1003953 - Multiplication App")
#     st.write("This is a simple calculator app")
    a = st.number_input("Enter 1st Number")
    b = st.number_input("Enter 2nd Number")
    operation = st.selectbox(["Multiply"])
#     if operation == "Add":
#         st.write(add(a, b))
#     elif operation == "Subtract":
#         st.write(sub(a, b))
    if operation == "Multiply":
        st.write(mul(a, b))
#     elif operation == "Divide":
#         st.write(div(a, b))
if __name__ == '__main__':
    main()
