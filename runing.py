import streamlit as st
import time

# Set the page layout
st.set_page_config(page_title="Man Running Behind Football", layout="wide")

# Load images (replace with your images or use URLs if hosted)
man_image = "man_running.png"  # You can use your own image or a GIF
football_image = "football.png"  # Similarly, use a football image or a GIF

# Set initial positions
man_pos = 0
football_pos = 100

# Run the animation in a loop
for i in range(100):
    st.empty()  # Clear previous frame

    # Update positions
    man_pos += 5
    football_pos += 3

    # Display the man and football
    col1, col2 = st.columns([1, 6])  # Create columns to layout images

    with col1:
        st.image(man_image, width=100, use_column_width=False)  # Display the man
    with col2:
        st.image(football_image, width=50, use_column_width=False)  # Display the football

    # Add space between the man and football based on positions
    time.sleep(0.1)  # Control animation speed
