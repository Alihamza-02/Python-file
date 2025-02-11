import streamlit as st

# Initialize session state for count if not already initialized
if 'count' not in st.session_state:
    st.session_state.count = 0

# Create a button and display the current count
if st.button('Click me'):
    st.session_state.count += 1  # Increment count by 1

# Show the updated count
st.write(f"Count: {st.session_state.count}")
