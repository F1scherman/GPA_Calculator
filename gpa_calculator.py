# Brayden Jonsson, October 2023

import argparse


def calculate_required_credits(curr_gpa, goal_gpa, curr_credits, new_gpa):
    """Calculates the required amount of credits at the new gpa to get to the goal gpa.
    Returns 0 if the goal is already reached, returns -1 if it's unreachable"""
    if goal_gpa <= curr_gpa:
        return 0
    elif goal_gpa >= new_gpa:
        return -1

    return round((-curr_credits * (curr_gpa - goal_gpa)) / (new_gpa - goal_gpa))


if __name__ == '__main__':
    description = ("This script takes in the given arguments to calculate a GPA/GPA Goal. "
                   "All values rounded to 3 decimals.")

    parser = argparse.ArgumentParser(description)

    parser.add_argument("-g", "--Goal_GPA", help="Give your goal GPA, as a float", type=float, default=-1)
    parser.add_argument("-c", "--Credits",
                        help="Give your current credits and GPA, formatted as credits_GPA, or \"16_4.0\" as an example."
                             " This command is repeatable to add up credits.",
                        action="append", required=True)
    parser.add_argument("-n", "--New_GPA", help="This is the GPA you project to receive in new credits",
                        type=float, default=4.0)

    args = parser.parse_args()

    creds = 0.0
    summed_gpa = 0.0

    for pair in args.Credits:
        split_pair = pair.split("_")
        creds += float(split_pair[0])
        summed_gpa += float(split_pair[0]) * float(split_pair[1])

    gpa = round(summed_gpa / creds, 3)

    print(f"Your current GPA is {gpa}.")

    if args.Goal_GPA != -1:
        req_creds = calculate_required_credits(gpa, args.Goal_GPA, creds, args.New_GPA)
        goal_GPA = round(args.Goal_GPA, 3)
        new_GPA = round(args.New_GPA, 3)
        if req_creds == 0:
            print("You've already reached the goal!")
        elif req_creds == -1:
            print("Your goal is unreachable!")
        else:
            print(f"You would need a {new_GPA} in {req_creds} credits to get to a {goal_GPA} GPA overall.")
            if req_creds > 120:
                print(f"This is equivalent to about {round(req_creds / 120, 3)} bachelor's degrees.")
