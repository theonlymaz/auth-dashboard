"""
Main application entry point
Handles routing and session management
"""

import streamlit as st
from supabase import create_client
import os
from dotenv import load_dotenv

# Import our pages
from components.auth import show_auth_page
from components.home import show_home_page
from components.settings import show_settings_page
from components.tasks import show_tasks_page
from utils.auth_functions import logout

# Hide Streamlit branding
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Load environment variables
load_dotenv()

# Connect to Supabase
supabase = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user_email = None

if "current_page" not in st.session_state:
    st.session_state.current_page = "Home"


def show_dashboard():
    """Display dashboard with navigation"""

    # Sidebar navigation
    with st.sidebar:
        st.title("Navigation")
        st.write(f"Logged in as:")
        st.write(f"**{st.session_state.user_email}**")
        st.markdown("---")

        # Navigation buttons
        if st.button("🏠 Home", use_container_width=True):
            st.session_state.current_page = "Home"
            st.rerun()

        if st.button("✅ Tasks", use_container_width=True):
            st.session_state.current_page = "Tasks"
            st.rerun()

        if st.button("⚙️ Settings", use_container_width=True):
            st.session_state.current_page = "Settings"
            st.rerun()

        st.markdown("---")

        # Logout button
        if st.button("🚪 Logout", type="secondary", use_container_width=True):
            logout(supabase)
            st.session_state.logged_in = False
            st.session_state.user_email = None
            st.rerun()

    # Show correct page
    if st.session_state.current_page == "Home":
        show_home_page()
    elif st.session_state.current_page == "Tasks":
        show_tasks_page()
    elif st.session_state.current_page == "Settings":
        show_settings_page()


def main():
    """Main application logic"""

    if st.session_state.logged_in:
        show_dashboard()
    else:
        show_auth_page(supabase)


if __name__ == "__main__":
    main()
