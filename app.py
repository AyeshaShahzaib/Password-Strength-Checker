import streamlit as st
import pandas as pd
import re
import math
from st_aggrid import AgGrid, GridOptionsBuilder

# Initialize password history
if "password_history" not in st.session_state:
    st.session_state.password_history = []

# Function to check password strength
def check_password(password):
    errors = []
    if len(password) < 8:
        errors.append("❌ Password should be at least 8 characters long.")
    if not any(char.isupper() for char in password):
        errors.append("❌ Password should contain at least one uppercase letter.")
    if not any(char.islower() for char in password):
        errors.append("❌ Password should contain at least one lowercase letter.")
    if not any(char.isdigit() for char in password):
        errors.append("❌ Password should contain at least one digit.")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        errors.append("❌ Password should contain at least one special character.")
    
    return errors

# Function to estimate time to crack password
def estimate_crack_time(password):
    charset_size = 0
    if any(char.islower() for char in password):
        charset_size += 26
    if any(char.isupper() for char in password):
        charset_size += 26
    if any(char.isdigit() for char in password):
        charset_size += 10
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        charset_size += 32  # Approximate number of special characters
    
    total_combinations = charset_size ** len(password)
    guesses_per_second = 1e12  # Approximate modern brute-force speed (1 trillion guesses/sec)
    seconds_to_crack = total_combinations / guesses_per_second

    # Convert to readable time
    if seconds_to_crack < 60:
        return f"{seconds_to_crack:.2f} seconds"
    elif seconds_to_crack < 3600:
        return f"{seconds_to_crack / 60:.2f} minutes"
    elif seconds_to_crack < 86400:
        return f"{seconds_to_crack / 3600:.2f} hours"
    elif seconds_to_crack < 31536000:
        return f"{seconds_to_crack / 86400:.2f} days"
    elif seconds_to_crack < 3.154e+9:
        return f"{seconds_to_crack / 31536000:.2f} years"
    else:
        return f"{seconds_to_crack / 3.154e+9:.2f} centuries"

# Function to mask password except for last 3 characters
def mask_password(password):
    return "*" * (len(password) - 3) + password[-3:] if len(password) > 3 else "*" * len(password)

# Streamlit UI
st.title("🔐 Password Strength Checker")

password = st.text_input("Enter your password:", type="password")

if password:
    errors = check_password(password)
    
    if errors:
        st.error("Your password is **weak**. Please fix the following issues:")
        for err in errors:
            st.write(err)
    else:
        st.success("✅ Your password is **strong**!")
        crack_time = estimate_crack_time(password)
        st.info(f"Estimated time to crack this password: **{crack_time}**")

        # Store password history
        st.session_state.password_history.append({
            "Masked Password": mask_password(password),
            "Crack Time": crack_time
        })

# Display password history
if st.session_state.password_history:
    st.subheader("🔍 Password History")

    # Convert to DataFrame
    df = pd.DataFrame(st.session_state.password_history)

    # Configure AgGrid options
    gb = GridOptionsBuilder.from_dataframe(df)
    gb.configure_pagination(paginationAutoPageSize=True)  # Enable pagination
    gb.configure_side_bar()  # Enable sidebar for filtering
    gb.configure_default_column(filterable=True, sortable=True, resizable=True)  # Make columns sortable and resizable
    grid_options = gb.build()

    # Display AgGrid
    AgGrid(df, gridOptions=grid_options, height=300, fit_columns_on_grid_load=True)

