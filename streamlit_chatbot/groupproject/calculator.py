import streamlit as st

# Title
st.title("🧮 Simple Calculator Web App")

# Input numbers
num1 = st.number_input("Enter the first number", format="%.2f")
num2 = st.number_input("Enter the second number", format="%.2f")

# Select operation
operation = st.selectbox("Choose operation", ("Add", "Subtract", "Multiply", "Divide"))

# Calculate when button is pressed
if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
        st.success(f"Result: {result}")
    elif operation == "Subtract":
        result = num1 - num2
        st.success(f"Result: {result}")
    elif operation == "Multiply":
        result = num1 * num2
        st.success(f"Result: {result}")
    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
            st.success(f"Result: {result}")
        else:
            st.error("Error: Cannot divide by zero.")
