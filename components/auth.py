"""
Authentication page - Login and Signup forms
"""

import streamlit as st
from utils.auth_functions import signup, login


def show_auth_page(supabase):
    """Display login/signup page"""

    # Center the content
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.title("🚀 Welcome to Auth Dashboard")
        st.markdown("---")

        # Create tabs for Login and Signup
        tab1, tab2 = st.tabs(["Login", "Sign Up"])

        # LOGIN TAB
        with tab1:
            st.subheader("Login to your account")

            login_email = st.text_input("Email", key="login_email")
            login_password = st.text_input(
                "Password", type="password", key="login_password"
            )

            if st.button("Login", type="primary", use_container_width=True):
                if login_email and login_password:
                    success, user_email = login(supabase, login_email, login_password)

                    if success:
                        st.session_state.logged_in = True
                        st.session_state.user_email = user_email
                        st.success("Login successful!")
                        st.rerun()
                    else:
                        st.error("Invalid credentials")
                else:
                    st.warning("Please fill in all fields")

        # SIGNUP TAB
        with tab2:
            st.subheader("Create a new account")

            signup_email = st.text_input("Email", key="signup_email")
            signup_password = st.text_input(
                "Password", type="password", key="signup_password"
            )
            signup_password_confirm = st.text_input(
                "Confirm Password", type="password", key="signup_password_confirm"
            )

            if st.button("Sign Up", type="primary", use_container_width=True):
                if signup_email and signup_password and signup_password_confirm:
                    if signup_password == signup_password_confirm:
                        success, message = signup(
                            supabase, signup_email, signup_password
                        )

                        if success:
                            st.success(message)
                            st.info("You can now log in with your credentials!")
                        else:
                            st.error(message)
                    else:
                        st.error("Passwords don't match!")
                else:
                    st.warning("Please fill in all fields")
