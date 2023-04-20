
# Event class that contains all characteristics of a specific event
class event:
    def __init__(self, priority, name, description, fixed, constraints = None):
        self.priority = priority
        self.name = name
        self.description = description
        self.fixed = fixed
        self.constraints = constraints

# Ask repetitively until it fulfils requierements
def ask_repetitive(initial_answer, thing_asked, ask_range):

    requirements_met = False
    if initial_answer.isnumeric():
        if int(initial_answer) >= ask_range[0] and int(initial_answer) <= ask_range[1]:
            requirements_met = True
            answer = initial_answer

    while not requirements_met:
            answer = input(thing_asked)
            if answer.isnumeric():
                if int(answer) >= ask_range[0] and int(answer) <= ask_range[1]:
                    requirements_met = True    

    return int(answer)
        
# Display the schedule in the command line
def display_schedule(schedule, weekday_names):
    # Turn the schedule matrix to be like a normal displayed schedule
    transposed_schedule = list(zip(*schedule))

    # Print titles
    print("      |", end="")
    for day in weekday_names:
        num_spaces = 15 - len(day)
        print(" ", end="")
        print(day.upper(), end="")
        print(" "*num_spaces,"|", end="")
    print()
    
    # Print rows of the schedule and their hours
    for i in range(len(transposed_schedule)):
        num_spaces = 2 - i
        print(" "*num_spaces, i, ":00 ", end="")
        for j in range(len(transposed_schedule[i])):
            num_spaces = 15 - len(transposed_schedule[i][j].name)
            print("| ", transposed_schedule[i][j].name, end="")
            print(" "*num_spaces, end="")
        print("|")


# Ask for fixed activities and place them in schedule
def ask_fixed(schedule, weekday_names, fixed_events):
    next = "Y"

    # Repeat while user adds activities
    while next != "N":
        print("You will now add a fixed activity: ")
        name = input("Activity name: ") 
        description = input("Activity description: ")
        priority = 10
        fixed = True

        # Select start weekday
        print("Select start day")
        for weekday_name in weekday_names:
            print("Press", weekday_names.index(weekday_name),"for", weekday_name)

        start_weekday_idx = input("Activity starting day: ")

        # Check wether input is valid, if not, ask until it is
        start_weekday_idx = ask_repetitive(start_weekday_idx,"Please input a valid activity starting day: ", (0,6))

        # ALLOW FURTHER DETAIL IN FUTURE, SMALLER RANGES THAN 1 HOUR
        # IMPLEMENT CHECKS TO PREVENT NOT NUMBER INPUT AND VALID HOUR
        # Select start hour
        start_hour = input("Activity start hour: ")
        start_hour = ask_repetitive(start_hour, "Please input a valid activity starting hour: ", (0,23))
        start_hour = int(start_hour)

        # Select end weekday
        print("Select end day")
        for weekday_name in weekday_names[start_weekday_idx:]:
            print("Press",weekday_names.index(weekday_name),"for", weekday_name )

        # Select end weekday and check validity
        end_weekday_idx = input("Activity end day: ")
        end_weekday_idx = ask_repetitive(end_weekday_idx, "Please input a valid activity end day: ", (start_weekday_idx,6))     

        # ALLOW FURTHER DETAIL IN THE FUTURE, SMALLER RANGES THAN 1 HOUR
        # Select end hour
        end_hour = input("Activity end hour: ")
        if start_weekday_idx == end_weekday_idx:
            end_hour = ask_repetitive(end_hour, "Please input a valid activity end hour: ", (start_hour,23))
        else:
            end_hour = ask_repetitive(end_hour, "Please input a valid activity end hour: ", (0,23))

        # IMPLEMENT CHECK TO SEE IF SPACE IS NOT ALREADY TAKEN
        space_taken = False
        for weekday_number in range(start_weekday_idx,end_weekday_idx + 1):
            if weekday_number == start_weekday_idx:
                start = start_hour
            else:
                start = 0

            if weekday_number == end_weekday_idx:
                end = end_hour + 1
            else:
                end = len(schedule[weekday_number])           

            for time in range(start, end):
                if schedule[weekday_number][time].name != " ":
                    space_taken = True

        # Add the event into the schedule if all checks are satisfied

        if space_taken == False:
            fixed_event = event(priority, name, description, fixed)
            fixed_events.append(fixed_event)

            for weekday_number in range(start_weekday_idx,end_weekday_idx + 1):
                if weekday_number == start_weekday_idx:
                    start = start_hour
                else:
                    start = 0

                if weekday_number == end_weekday_idx:
                    end = end_hour + 1
                else:
                    end = len(schedule[weekday_number])           

                for time in range(start, end):
                    schedule[weekday_number][time] = fixed_event
        else:
            print("Space already taken, impossible to add into schedule. Please try again.")

        # Ask for next input       
        next = input("Add other event (Y/N): ")

def ask_adaptable(adaptable_events):
    # Ask for activities with an adaptable schedule
    next = "Y"

    # TO DO
    # Repeat while user adds activities
    while next != "N":
        print()     
        print("You will now add activities without a fixed time: ")
        print("When selecting priority, choose 10 for mandatory tasks such as sleeping or studying, and lower for optional tasks")
        print()
        print("Remember to add sleep times")
        print("In this version, sleep should be added twice, morning and noon sleep")
        print()
        constraints = {}

        # Activity name and description
        name = input("Activity name: ") 
        description = input("Activity description: ")

        # Piority
        priority = input("Activity priority (number between 0 and 10): ")
        priority = ask_repetitive(priority, "Please input a valid activity priority between 1 and 10", (1,10))

        time_goal = input("How many hours per week?: ")
        time_goal = ask_repetitive(time_goal, "Please input a valid time between 1 and 168", (1,168))
        constraints["time_goal_counter"] = time_goal
        constraints["time_goal"] = time_goal


        earliest_hour = input("What is the earliest you would do this activity?: ")
        earliest_hour = ask_repetitive(earliest_hour, "Please input a valid hour", (0,23))
        constraints["earliest_hour"] = earliest_hour

        latest_hour = input("What is the latest you would do this activity?: ")
        latest_hour = ask_repetitive(latest_hour, "Please input a valid hour", (0,23))
        constraints["latest_hour"] = latest_hour


        max_time = input("What is the max duration you would do this activity for?: ")
        max_time = ask_repetitive(max_time, "Please input a valid time (maximum 24 hours)", (1,24))
        constraints["max_time"] = max_time
        """
        min_time = input("What is the min duration you would do this activity for?: ")
        min_time = ask_repetitive(min_time, "Please input a valid time (minimum 1 hour)", (1,24))
        constraints["min_time"] = min_time
        """          
        fixed = False

        adaptable_events.append(event(priority, name, description, fixed, constraints))

        next = input("Add other event (Y/N): ")

def generate_schedule(schedule, adaptable_events):
    # TO DO
    repeats = 0
    # Go over each hour in schedule
    for day in range(len(schedule)):
        repeats = 0
        for hour in range(len(schedule[day])):
            adaptable_events.sort(key = lambda event: event.priority, reverse = True)

            event_idx = 0

            # Go over each element by priority
            while schedule[day][hour].name == " " and event_idx < len(adaptable_events):
                # Check if it is in valid range, or if it already spent
                if hour in range(adaptable_events[event_idx].constraints["earliest_hour"], adaptable_events[event_idx].constraints["latest_hour"]+1) and adaptable_events[event_idx].constraints["time_goal_counter"] != 0:
                    
                    # Check maximum time
                    if  hour > 0:
                        if adaptable_events[event_idx] == schedule[day][hour - 1]:
                            repeats += 1

                    if repeats != adaptable_events[event_idx].constraints["max_time"]:
                        schedule[day][hour] = adaptable_events[event_idx]
                        adaptable_events[event_idx].constraints["time_goal_counter"] = adaptable_events[event_idx].constraints["time_goal_counter"] - 1
                        

                event_idx += 1
    return schedule

def interface(schedule, adaptable_events, fixed_events, weekday_names):
    print("                   +---------------------------+")
    print("                   | Kronos Time Management V1 |")
    print("                   +---------------------------+")
    print()
    print('''Create your own personalized schedule based on your goals and objectives.
             Assign your fixed hours and goals for the week, and a new schedule will be generated based on your demands.
          ''')
    print()

    user_data = 0

    while user_data != "4":
        print('''Menu:
                Press:
                    1 to select fixed activities
                    2 to select adaptable activities
                    3 to generate schedule
                    4 to exit
                    ''')
        user_data = input("Select option: ")

        if user_data == "1":
            ask_fixed(schedule, weekday_names, fixed_events)
        elif user_data == "2":
            ask_adaptable(adaptable_events)
        elif user_data == "3":
            generate_schedule(schedule, adaptable_events)
            display_schedule(schedule, weekday_names)
        elif user_data == "4":
            print("Exiting")
        else:
            print("Invalid input")





    # Go over each element by priority
    # Check if the element´s minimum time can fit on the time alloted
    # If not, take next element
    # If it fits, test the next series until it fails

def main():
    # Define General Variables
    # Schedule size
    div_day = 24
    days = 7
    weekday_names = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

    adaptable_events = []
    fixed_events = []

    # Create schedule Matrix
    schedule = [[ event(0," ", "Placeholder", True) for period in range(div_day)] for day in range(days)]

    interface(schedule, adaptable_events, fixed_events,  weekday_names)

main()