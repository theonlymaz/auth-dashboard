"""
Settings page - User profile and preferences
"""

import streamlit as st


def show_settings_page():
    """Display the settings page"""

    st.title("⚙️ Settings")
    st.markdown("---")

    # Account Information
    st.subheader("Account Information")
    st.text_input("Email Address", value=st.session_state.user_email, disabled=True)
    st.caption("Your email address cannot be changed")

    st.markdown("---")

    # Profile Settings
    st.subheader("Profile Settings")

    if "display_name" not in st.session_state:
        st.session_state.display_name = st.session_state.user_email.split("@")[0]

    new_display_name = st.text_input(
        "Display Name",
        value=st.session_state.display_name,
        help="This is how your name will appear in the dashboard",
    )

    if st.button("Save Changes", type="primary"):
        st.session_state.display_name = new_display_name
        st.success("✅ Settings saved successfully!")
        st.balloons()

    st.markdown("---")

    # Preferences
    st.subheader("Preferences")
    email_notifications = st.checkbox("Email notifications", value=True)
    dark_mode = st.checkbox("Dark mode (coming soon)", value=False, disabled=True)

    st.markdown("---")

    # Account Stats
    st.subheader("Account Statistics")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Account Age", "3 days")
        st.metric("Total Logins", "12")

    with col2:
        st.metric("Last Login", "Just now")
        st.metric("Projects Created", "5")

    st.markdown("---")

    # Danger Zone
    st.subheader("⚠️ Danger Zone")
    with st.expander("Delete Account"):
        st.warning("This action cannot be undone!")
        st.write("Deleting your account will permanently remove all your data.")

        if st.button("Delete My Account", type="secondary"):
            st.error("Account deletion is not implemented in this demo")
