import pandas as pd
from datetime import datetime
import datetime as dt
import math
# load the input data with constraints
def readData_input(filepath):
    data_employees = pd.read_excel(filepath, sheet_name="Employees").set_index("Name")
    demand = pd.read_excel(filepath, sheet_name="Demand").set_index("Day")
    parameters = pd.read_excel(filepath, sheet_name="Parameters").set_index("Parameter")
    input_days = pd.read_excel(filepath, sheet_name="Days").set_index("Day")
    optimization_parameters = pd.read_excel(filepath, sheet_name="Optimization_Parameters").set_index("Parameter")

    return data_employees, demand, parameters, input_days, optimization_parameters


# load the data from solution
def readData_Solution(filepath2):
    daily_hrs_employees = pd.read_excel(filepath2, sheet_name="Schedule").set_index("Employee")
    weeklyHours = pd.read_excel(filepath2, sheet_name="weeklyHours").set_index("WeeklyHours")

    return daily_hrs_employees, weeklyHours


def main():
    input_datafile = "../../data/InputData.xlsx"
    input_datafile2 = "../../Solution.xlsx"

    data_employees, demand, parameters, input_days, optimization_parameters = readData_input(input_datafile)
    list_employees = list(data_employees.index)
    days = list(input_days.index)
    slots = list(demand.columns)

    nr_employees = len(list_employees)
    nr_days = len(days)
    nr_slots = len(slots)

    print('days', days[1], input_days['Date'][1])

    daily_hrs_employees, weeklyHours = readData_Solution(input_datafile2)
    emp_hrs_sched = list(daily_hrs_employees.index)
    emp_wk_hrs = list(weeklyHours)

    nr_sched = (len(emp_hrs_sched))

    print('hrs_sched ', emp_hrs_sched)
    print('col', daily_hrs_employees.columns)
    print('data_employees', data_employees['Monday']['Paul'], days[1], emp_hrs_sched[1])
    print(daily_hrs_employees['Duration_hrs'][1])

    emp = []
    for n in range(nr_sched):
        employee = emp_hrs_sched[n]
        print(employee)
        day = daily_hrs_employees['Day'][n]
        hours_work = daily_hrs_employees['Duration_hrs'][n]
        # print('hrs_wrked',hours_work)

        hrs_available = data_employees[daily_hrs_employees['Day'][n]][emp_hrs_sched[n]]
        if hrs_available == 0:
            hrs_available = dt.timedelta(seconds=0)
        else:
            # hrs_available = data_employees[daily_hrs_employees['Day'][n]][emp_hrs_sched[n]]*3600
            hrs_available = dt.timedelta(seconds=int(data_employees[daily_hrs_employees['Day'][n]][emp_hrs_sched[n]]*3600))
        print('hrs_available', hrs_available)
        if pd.isnull(hours_work):
            print('NaN')
            hours_work = dt.timedelta(seconds=0)
        else:

            # hours_work = datetime.strptime((daily_hrs_employees['Duration_hrs'][n]) + ':00','%H:%M:%S')
            hours_work = int((dt.datetime.strptime(str(daily_hrs_employees['Duration_hrs'][n]) + ':00','%H:%M:%S') - dt.datetime(1900, 1,
                                                                                                1)).total_seconds())
            # print('hrs_wrked', hours_work)
            hours_work = dt.timedelta(seconds=int(hours_work))
            print('hrs_wrked', hours_work)
            # hours_work = datetime.strptime(str(daily_hrs_employees['Duration_hrs'][n]), '%H:%M:%S')
            # hours_work = dt.timedelta(seconds=int(daily_hrs_employees['Duration_hrs'][n]*3600))


        # print('hrs_available', hrs_available)
        hrs_free = str(hrs_available - hours_work)
        # hrs_free = str(dt.timedelta(hours=hrs_free))
        emp.append([employee, day, str(hours_work), str(hrs_available), hrs_free])

    #
    #
    print(emp)


main()
