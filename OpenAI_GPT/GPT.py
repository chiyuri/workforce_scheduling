# ------------------Copyright (C) 2023 University of Strathclyde and Author ---------------------------------
# --------------------------------- Author: Cheyenne Powell -------------------------------------------------
# ------------------------- e-mail: cheyenne.powell@strath.ac.uk --------------------------------------------

# Loads the schedule data into openAI GPT3.5 with constraints provided to see how it responds due to conditions
# ===========================================================================================================


import os
import openai
import pandas as pd
from Extract_solution import Extract_solution
from Extract_input import Extract_input




def OpenAI_connect():
    openai.api_key = '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'
    # Loading the solvers results.
    data_path1 = "../data/InputData.xlsx"
    data_path2 = '../Solution.xlsx'

    data_employees, demand, parameters, input_days, optimization_parameters = Extract_input(data_path1)
    daily_hrs_employees, weeklyHours = Extract_solution(data_path2)
    emp_hrs_sched = list(daily_hrs_employees.index)
    emp_wk_hrs = list(weeklyHours)

    print('hrs_sched ', emp_hrs_sched)
    print('col', daily_hrs_employees.columns)
    # print('data_employees', data_employees['Monday']['Paul'], days[1], emp_hrs_sched[1])
    print(daily_hrs_employees['Duration_hrs'][1])


    # data = pd.read_excel(r''+data_path)
    # df = pd.DataFrame(data, columns=['Employee', 'Date', 'Day', 'Start', 'End Duration_hrs'])
    # gpt_prompt = str(df)
    # print(str(df), '\n', daily_hrs_employees)


    # print(gpt_prompt)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=[{"role": "system", "content": "This is a schedule with constraints:\n"},
        {"role": "system", "content": "image_mem = 2688\n"},
        {"role": "system", "content": "downlink = 2800\n"},
        {"role": "system", "content": "process = 250\n"},
        {"role": "system", "content": "land_access and day_access must be 1 for image_mem to be taken\n"},
        {"role": "system", "content": "station_access must be 1 for downlink to occur\n"},
        {"role": "system", "content": "0 means take_images, 1 means processing, and 2 means downlinking for the extracted_action at start_time\n"},
        # {"role": "system", "content": "if processing is replaced, the process value is subtracted from memory_used\n"},
        # {"role": "system", "content": "if take_images is replaced, the image_mem value is subtracted from memory_used\n"},
        # {"role": "system", "content": "if downlinking is replaced, the downlink value is added to the memory_used\n"},
        {"role": "system", "content": "if processing replaces the extracted action, the memory changes by adding the process value to the previous memory_used\n"},
        {"role": "system", "content": "if take_images replaces the extracted action, the memory changes by adding the image_mem value to the previous memory_used\n"},
        {"role": "system", "content": "if downlinking replaces the extracted action, the memory_used changes by reducing the previous value by the value of downlink\n"},
        {"role": "system", "content": "For the extracted_action to be true, action_possible must be YES at the start_time\n"},
        {"role": "system", "content": "maximum_memory = 1920000\n"},
        {"role": "system", "content": "actions are replaceable on the condition, that memory_used is less than maximum_memory and the other conditions are met\n"},
        {"role": "system", "content": gpt_prompt},
        {"role": "user", "content": "\n\n Is it possible to replace processing with image taking at time 14991? Provide an explanation\n"}],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=1,
        presence_penalty=0
    )
    print(response)
#
OpenAI_connect()