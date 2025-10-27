# Task page - This page lets users create, edit and delete tasks

import streamlit as st


def show_tasks_page():
    # Display the task page

    # Initialize tasks list in session state if it doesn't exist
    if "tasks" not in st.session_state:
        st.session_state.tasks = []

    st.title("📋 Task Manager")
    st.markdown("---")

    # Add a new task section
    st.subheader("➕ Add New Task")

    new_task = st.text_input(
        "Task Desctiption", placeholder="What needs to be done today?"
    )

    # add task button

    if st.button("Add task", type="primary"):
        if new_task:
            task = {"description": new_task, "completed": False}

            st.session_state.tasks.append(task)
            st.success("✅ Task added!")
            st.rerun()  # Refresh to show new task
        else:
            st.warning("Please enter a task description")

    st.markdown("---")

    # Display tasks section
    st.subheader("📝 Your Tasks")

    # Check if there are any tasks
    if len(st.session_state.tasks) == 0:
        st.info("No tasks yet! Add one above to get started.")
    else:
        # Filter options
        filter_option = st.radio(
            "Filter:", ["All", "Active", "Completed"], horizontal=True
        )

        # Loop through each task
        for index, task in enumerate(st.session_state.tasks):
            # Apply filter
            if filter_option == "Active" and task["completed"]:
                continue
            if filter_option == "Completed" and not task["completed"]:
                continue

            # Create columns for task layout
            col1, col2, col3 = st.columns([0.1, 0.7, 0.2])

            with col1:
                # Checkbox to mark complete
                completed = st.checkbox(
                    "Done",
                    value=task["completed"],
                    key=f"task_{index}",
                    label_visibility="collapsed",
                )

                # Update task status if checkbox changed
                if completed != task["completed"]:
                    st.session_state.tasks[index]["completed"] = completed
                    st.rerun()

            with col2:
                # Show task description (strikethrough if completed)
                if task["completed"]:
                    st.markdown(f"~~{task['description']}~~")
                else:
                    st.write(task["description"])

            with col3:
                # Delete button
                if st.button("🗑️", key=f"delete_{index}"):
                    st.session_state.tasks.pop(index)
                    st.rerun()

        # Show task count
        st.markdown("---")
        completed_count = sum(1 for task in st.session_state.tasks if task["completed"])
        total_count = len(st.session_state.tasks)
        st.caption(f"✅ {completed_count} of {total_count} tasks completed")
