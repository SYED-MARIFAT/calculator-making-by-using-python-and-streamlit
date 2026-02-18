import streamlit as st

# Page configuration
st.set_page_config(
    page_title="MARTIN'S CALCULATOR",
    page_icon="🧮",
    layout="centered"
)

# Title and description
st.title("🧮 MARTIN'S CALCULATOR")
st.markdown("---")

# Create two columns for input fields
col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input("Enter first number", value=0.0, step=0.1, format="%.2f")

with col2:
    num2 = st.number_input("Enter second number", value=0.0, step=0.1, format="%.2f")

# Operation selection
operation = st.selectbox(
    "Select operation",
    ["Addition (+)", "Subtraction (-)", "Multiplication (×)", "Division (÷)"]
)

# Calculate button
if st.button("Calculate", type="primary"):
    st.markdown("---")
    
    # Perform calculation based on selected operation
    if operation == "Addition (+)":
        result = num1 + num2
        st.success(f"Result: {num1} + {num2} = {result}")
        
    elif operation == "Subtraction (-)":
        result = num1 - num2
        st.success(f"Result: {num1} - {num2} = {result}")
        
    elif operation == "Multiplication (×)":
        result = num1 * num2
        st.success(f"Result: {num1} × {num2} = {result}")
        
    elif operation == "Division (÷)":
        if num2 != 0:
            result = num1 / num2
            st.success(f"Result: {num1} ÷ {num2} = {result}")
        else:
            st.error("Error: Division by zero is not allowed!")

# Advanced features (optional)
with st.expander("Advanced Options"):
    st.write("Additional calculations:")
    
    # Square root
    if st.button("Square Root of First Number"):
        if num1 >= 0:
            sqrt_result = num1 ** 0.5
            st.info(f"√{num1} = {sqrt_result:.2f}")
        else:
            st.error("Cannot calculate square root of negative number!")
    
    # Percentage
    if st.button("Calculate Percentage"):
        if num2 != 0:
            percentage = (num1 / num2) * 100
            st.info(f"{num1} is {percentage:.2f}% of {num2}")
        else:
            st.error("Second number cannot be zero!")

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit")