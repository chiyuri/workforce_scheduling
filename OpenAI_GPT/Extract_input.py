import pandas as pd

def Extract_input(filepath):
    data_employees = pd.read_excel(filepath, sheet_name="Employees")
    demand = pd.read_excel(filepath, sheet_name="Demand").set_index("Day")
    parameters = pd.read_excel(filepath, sheet_name="Parameters").set_index("Parameter")
    input_days = pd.read_excel(filepath, sheet_name="Days").set_index("Day")
    optimization_parameters = pd.read_excel(filepath, sheet_name="Optimization_Parameters").set_index("Parameter")

    return data_employees, demand, parameters, input_days, optimization_parameters
