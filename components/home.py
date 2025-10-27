"""
Home page - Main dashboard view
"""

import streamlit as st


def show_home_page():
    """Display the home dashboard"""

    st.title("🏠 Dashboard Home")
    st.markdown("---")

    # Welcome message
    st.success(f"Welcome back, {st.session_state.user_email}! 🎉")

    # Dashboard Overview
    st.subheader("Dashboard Overview")

    # Create 3 metric cards
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Projects", "12", "+2")

    with col2:
        st.metric("Active Users", "48", "+5")

    with col3:
        st.metric("Revenue", "$1,234", "+15%")

    st.markdown("---")

    # Recent Activity
    st.subheader("Recent Activity")
    st.write("Here's what's happening with your dashboard...")

    activities = [
        ("✅", "Project Alpha deployed", "2 hours ago"),
        ("✅", "New user registered", "5 hours ago"),
        ("✅", "Database backup completed", "1 day ago"),
        ("⏳", "Update scheduled for tomorrow", "Upcoming"),
    ]

    for icon, activity, time in activities:
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write(f"{icon} {activity}")
        with col2:
            st.caption(time)
