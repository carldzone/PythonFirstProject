import json

def workout_program_selection(workout_nb=None):
    """
    This function will ask the user to input a program name that will continously ask for the number
    of sets, reps, and weight the user done on the program. The sequence of input will be: 
            Name > Sets > Reps > Weight
    If the user input more than 1 set, it will first ask how many reps the user did per set, then will
    ask the user how many weight the user used per set also respectively.
            EXAMPLE:
                3 SETS:
                    1 set: 10 reps
                    2 set: 10 reps
                    3 set: 10 reps
                    
                    1 set: 15 kgs
                    2 set: 17.5 kgs
                    3 set: 20 kgs
    """
    workout_dict = {}
    workout_name = str(input('Enter the workout program name: '))
    while True:
        try:
            workout_sets = int(input('How many sets did you hit? '))
        except ValueError:
            print('Invalid input. Please input correct value for NUMBER of SET/S')
            continue
        else:
            break
    
    sets = []
    weight = []
    workout_dict[f'{workout_name}'] = []
    for i in range(workout_sets):
        while True:
            try:
                workout_reps = int(input(f'How many REPS did you do on set {i + 1}? '))
            except ValueError:
                print('Invalid input. Please input correct value for NUMBER of REPS')
                continue
            else:
                break
    
        sets.append(workout_reps)
        
    
    for i in range(workout_sets):    
        while True:    
            try:
                workout_weight = float(input(f'WEIGHT used in your {i + 1} set? (in kilograms): '))
            except ValueError:
                print('Invalid input. Please input correct value for WEIGHT USED')
                continue
            else:
                break
        
        weight.append(workout_weight)
    
    
    for item in range(len(sets)):
        workout_dict[f'{workout_name}'].append((f'{item + 1} set', f'{sets[item]} reps', f'{weight[item]} kgs'))
    
    return workout_dict
    
class run_workout_program():
    """
    This method will run workout_program_selection function that will ask the user what workout he/she
    did. This will return a dictionary of the workout the user entered during the runtime.
    """
    workout_dictionary = {
        'Chest': [],
        'Shoulder': [],
        'Back': [],
        'Tricep': [],
        'Bicep': [],
        'Quads': [],
        'Hamstring': [],
        'Glutes': [],
        'Calves': [],
        'Core/Abs': []
    }
    
    while True:
        try:
            print(
                """
                \tWhat workout program did you hit today?
                \tPRESS THE FOLLOWING NUMBER OF YOU CHOICE:\n
                \t\t1 - Chest
                \t\t2 - Shoulder
                \t\t3 - Back
                \t\t4 - Tricep
                \t\t5 - Bicep
                \t\t6 - Quads
                \t\t7 - Hamstring
                \t\t8 - Glutes
                \t\t9 - Calves
                \t\t10 - Core/Abs
                \t\t0 - Exit
                """
            )
            workout_val = int(input('Enter a valid number: '))
            if workout_val == 0:
                break
            if workout_val == 1:
                workout_prog_output = workout_program_selection(workout_val)
                workout_dictionary['Chest'].append(workout_prog_output)
            if workout_val == 2:
                workout_prog_output = workout_program_selection(workout_val)
                workout_dictionary['Shoulder'].append(workout_prog_output)
            if workout_val == 3:
                workout_prog_output = workout_program_selection(workout_val)
                workout_dictionary['Back'].append(workout_prog_output)
            if workout_val == 4:
                workout_prog_output = workout_program_selection(workout_val)
                workout_dictionary['Tricep'].append(workout_prog_output)
            if workout_val == 5:
                workout_prog_output = workout_program_selection(workout_val)
                workout_dictionary['Bicep'].append(workout_prog_output)
            if workout_val == 6:
                workout_prog_output = workout_program_selection(workout_val)
                workout_dictionary['Quads'].append(workout_prog_output)
            if workout_val == 7:
                workout_prog_output = workout_program_selection(workout_val)
                workout_dictionary['Hamstring'].append(workout_prog_output)
            if workout_val == 8:
                workout_prog_output = workout_program_selection(workout_val)
                workout_dictionary['Glutes'].append(workout_prog_output)
            if workout_val == 9:
                workout_prog_output = workout_program_selection(workout_val)
                workout_dictionary['Calves'].append(workout_prog_output)
            if workout_val == 10:
                workout_prog_output = workout_program_selection(workout_val)
                workout_dictionary['Core/Abs'].append(workout_prog_output)
            else:
                print('Number input out of range. Select only from the following program number shown.')
                continue
        except ValueError:
            print('Invalid input. Select only from the following program number shown.')
            continue
        else:
            break
    
    empty_dict_key = []
    for k, v in workout_dictionary.items():
        if len(v) == 0:
            empty_dict_key.append(k)
    
    for key in empty_dict_key:
        del workout_dictionary[key]
        
    
    # print(workout_dictionary)
    print(json.dumps(workout_dictionary, sort_keys=True, indent=4))