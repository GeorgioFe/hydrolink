from supabase_setup import supabase

# User Sign-Up
def user_sign_up(email: str, password: str) -> bool:
    
    credentials = {
        "email": email,
        "password": password,
    }
    
    reponse = supabase.auth.sign_up(credentials)
    
    return True

# User Sign-In
def user_sign_in(email: str, password: str) -> bool:
    
    response = supabase.auth.sign_in_with_password({"email": email, "password": password})
    
    return True

# User Sign-Out
def user_sign_out() -> bool:
    
    response = supabase.auth.sign_out()
    
    return True

# Get User Info
def get_user_info():
    data = supabase.auth.get_user()
    
    return data.user
