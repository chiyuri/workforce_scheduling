
import pandas as pd
def Extract_solution(filepath2):
    daily_hrs_employees = pd.read_excel(filepath2, sheet_name="Schedule").set_index("Employee")
    weeklyHours = pd.read_excel(filepath2, sheet_name="weeklyHours").set_index("WeeklyHours")

    return daily_hrs_employees, weeklyHours