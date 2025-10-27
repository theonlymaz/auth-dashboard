"""
Authentication utility functions
Handles signup, login, logout with Supabase
"""


def signup(supabase, email, password):
    """
    Creates a new user account in Supabase
    Returns: (success: bool, message: str)
    """
    try:
        response = supabase.auth.sign_up({"email": email, "password": password})

        if response.user:
            return True, "Account created! Please check your email to confirm."
        else:
            return False, "Signup failed. Please try again."
    except Exception as e:
        return False, f"Error: {str(e)}"


def login(supabase, email, password):
    """
    Logs in an existing user
    Returns: (success: bool, message: str)
    """
    try:
        response = supabase.auth.sign_in_with_password(
            {"email": email, "password": password}
        )

        if response.user:
            return True, response.user.email
        else:
            return False, None
    except Exception as e:
        return False, None


def logout(supabase):
    """
    Logs out the current user
    """
    try:
        supabase.auth.sign_out()
        return True
    except:
        return False
