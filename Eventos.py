
# Event class that contains all characteristics of a specific event
class event:
    def __init__(self, priority, name, description, fixed):
        self.priority = priority
        self.name = name
        self.description = description
        self.fixed = fixed
        
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
        priority = 1
        fixed = True

        # Select start weekday
        print("Select start day")
        for weekday_name in weekday_names:
            print("Press", weekday_names.index(weekday_name),"for", weekday_name)

        # IMPLEMENT CHECKS TO PREVENT NOT NUMBER INPUT AND BETWEEN 0 AND 6
        start_weekday = input("Activity starting day: ")
        start_weekday_idx = int(start_weekday)

        # ALLOW FURTHER DETAIL IN FUTURE, SMALLER RANGES THAN 1 HOUR
        # IMPLEMENT CHECKS TO PREVENT NOT NUMBER INPUT AND VALID HOUR
        # Select start hour
        start_hour = input("Activity start hour: ")
        start_hour = int(start_hour)

        # Select end weekday
        print("Select end day")
        for weekday_name in weekday_names[start_weekday_idx:]:
            print("Press",weekday_names.index(weekday_name),"for", weekday_name )

        # IMPLEMENT CHECKS TO PREVENT INVALID END WEEKDAY
        end_weekday = input("Activity end day: ")
        end_weekday_idx = int(end_weekday)        

        # ALLOW FURTHER DETAIL IN THE FUTURE, SMALLER RANGES THAN 1 HOUR
        # IMPLEMENT CHECKS TO PREVENT NOT NUMBER INPUT AND VALID END HOUR
        # Select end hour
        end_hour = input("Activity end hour: ")
        end_hour = int(end_hour) 

        # IMPLEMENT CHECK TO SEE IF SPACE IS NOT ALREADY TAKEN

        # Add the event into the schedule
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

        # Ask for next input       
        next = input("Add other event (Y/N): ")

def ask_adaptable(schedule, weekday_names):
    # Ask for activities with an adaptable schedule
    next = "Y"
    adaptable_events = []

    # Repeat while user adds activities
    while next != "N":     
        next = input("Add other event (Y/N): ")

def generate_schedule():
    return "Not yet implemented"


def main():
    # Define General Variables
    # Schedule size
    div_day = 24
    days = 7
    weekday_names = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

    events = []
    fixed_events = []

    # Create schedule Matrix
    schedule = [[ event(0," ", "Placeholder", True) for period in range(div_day)] for day in range(days)]

    ask_fixed(schedule, weekday_names, fixed_events)
    ask_adaptable(schedule, weekday_names)
    generate_schedule()
    display_schedule(schedule, weekday_names)

main()