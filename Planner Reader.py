
CREDITS_SEM = 16

def semester_calculator(credits):
    global CREDITS_SEM
    # round up
    return  credits / CREDITS_SEM 

def main():
    total_credits = 0
    
    print("Welcome to the Planner Reader")
    # Open the file
    file = open("2nd Year.txt", "r")
    
    # Read the file
    for line in file:
        value = line.strip().split(" ")
        # Check if line is a number also convert string number to int
        if value[0].isdigit():
            # Add the number to the total
            total_credits += int(line)
    
    print("Total Credits {}".format(total_credits))
    
    semesters = semester_calculator(total_credits)
    
    print("Semesters {}".format(semesters))
    
    # Check how many credits needed to reach 6 semesters
    if semesters > 4:
        print("You are over the 4 semester limit")
        limit = round( (semesters - 4) * CREDITS_SEM )
        print("You need to drop {} credits to reach the limit".format(limit))
        print("You could also overload and take {} credits".format(limit))
    else:
        print("You are under the 4 semester limit")
        free_creds = round( (4 - semesters) * CREDITS_SEM )
        print("You have {} free credits".format(free_creds))
        
    
    file.close()
    return 

if __name__ == "__main__":
    main()