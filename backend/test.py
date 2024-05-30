from supabase_setup import supabase
import auth
import db_access as db

# Sign in user
auth.user_sign_in('justtesting@gmail.com', 'yoyo123')

# Sign out user
auth.user_sign_out()