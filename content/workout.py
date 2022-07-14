class Workout():
    def __init__(self, workout_name: str, sets: int):
        # To run validations
        assert sets >= 0, f'The value {sets} for sets is not greater than zero!'
        
        self.workout_name = workout_name
        self.sets = sets

    
class Chest(Workout):
    def __init__(self, workout_name: str, sets: int):
        super().__init__(workout_name, sets)



def workout_program_selection(workout_nb):
    workout_dict = {}
    if workout_nb == 1:
        chest_workout_name = str(input('Enter a chest workout program name: '))
        while True:
            try:
                chest_workout_sets = int(input('How many sets did you hit? '))
            except ValueError:
                print('Invalid input. Please input correct value for NUMBER of SET/S')
                continue
            else:
                break
        chest_sets = []
        workout_dict[f'{chest_workout_name}'] = []
        for i in range(chest_workout_sets):
            while True:
                try:
                    workout_reps = int(input(f'How many reps did you do on set {i + 1}? '))
                except ValueError:
                    print('Invalid input. Please input correct value for NUMBER of REPS')
                    continue
                else:
                    break
            chest_sets.append(workout_reps)
        
        for item in range(len(chest_sets)):
            workout_dict[f'{chest_workout_name}'].append((f'{item + 1} set', f'{chest_sets[item]} reps'))
    
    # else:
    #     return [None, None]

    return [chest_workout_name, workout_dict[f'{chest_workout_name}']]


def workout_to_dict(value=None):
    workout_dict_list = {}
    workout_prog_sel_list = workout_program_selection(value)
    workout_dict_list[f'{workout_prog_sel_list[0]}'] = workout_prog_sel_list[1]
    
    return workout_dict_list
    

class run_workout_program():
    workout_dictionary_list = []
    continue_workout_input = True
    while continue_workout_input:
        print(
            """
            \tWhat workout program did you hit today?
            \tPRESS THE FOLLOWING NUMBER OF YOU CHOICE:\n
            \t\t1 - Chest
            \t\t0 - Exit
            """
        )
        workout_val = int(input('Enter a valid number: '))
        if workout_val == 0:
            break
        else:
            workout_prog_output = workout_to_dict(workout_val)
            workout_dictionary_list.append(workout_prog_output)
    
    print(workout_dictionary_list)

print('Something I want to try in my repo!')