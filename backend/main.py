def calculate_daily_water_intake(age, weight_pounds, weekly_exercise_hours):
    # Convert weekly exercise hours to daily exercise minutes
    daily_exercise_minutes = (weekly_exercise_hours * 60) / 7
    
    # Baseline water intake
    baseline_intake_oz = weight_pounds / 2
    
    # Additional water intake for exercise
    exercise_intake_oz = (daily_exercise_minutes / 30) * 12
    
    # Total daily water intake
    total_intake_oz = baseline_intake_oz + exercise_intake_oz
    
    return total_intake_oz