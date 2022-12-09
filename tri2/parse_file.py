# ----------------------
# Made by Brady Hodge
# Status: In Progress
# Assignment 11A; 1/2
# Module
# ----------------------

def get_data(rel_filepath):
    data_list = []
    line_number = 0
    try:
        with open(rel_filepath) as file_object:
            for line in file_object:
                line_number += 1
                if line_number != 1:
                    data_list.append(line)
            return data_list
    except:
        return []

def get_average_grade(list_survey_results):
    
