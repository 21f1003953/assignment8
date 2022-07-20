import streamlit as st


def mul(a, b):
  return a * b
def main():
    st.title("TDS Assignment 8 - Param Chordiya 21f1003953 - Multiplication App")
#     st.write("This is a simple calculator app")
    a = st.number_input("Enter 1st Number")
    b = st.number_input("Enter 2nd Number")

    st.write(mul(a, b))

if __name__ == '__main__':
    main()
