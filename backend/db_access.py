from supabase_setup import supabase
import auth
# Functions to get data.

# Get User Params
def get_params() -> dict:
    user_info = auth.get_user_info()
    user_id = user_info.id
    
    response = supabase.table('user_params').select('age', 'weight', 'activity_hours').eq('user_id', user_id).execute()
    data = response.data[0]
    
    return data

# Functions to set data.

# Set User Params
def set_params(age: int, weight: float, activity_hours: float) -> bool:
    response = supabase.table('user_params').insert({"age":age, "weight":weight, "activity_hours":activity_hours}).execute()
    
    return True

# Set Recommended Water intake
def set_recommended_intake(recommended_intake: float) -> bool:
    response = supabase.table('misc').insert({"recommended_intake":recommended_intake}).execute()
    
    return True

# Functions to update data.

# Update Recommended Water Intake
def update_recommended_intake(recommended_intake: float) -> bool:
    user_info = auth.get_user_info()
    user_id = user_info.id
    
    response = supabase.table('misc').update({"recommended_intake":recommended_intake}).eq('user_id', user_id).execute()
    
    return True


