choice = "y"

# This while loop keeps the program running as long as the user enters "y",
# allowing marks for multiple students to be entered one after another (Iteration)
while choice == "y":

    # Ask the user to enter each of the three quiz marks, converting the
    # text typed in by the user into a decimal number (float) so maths can be done on it
    quiz_1 = float ( input ( "Enter Quiz 1 mark: " ) )
    quiz_2 = float ( input ( "Enter Quiz 2 mark: " ) )
    quiz_3 = float ( input ( "Enter Quiz 3 mark: " ) )

    # Add the three marks together and divide by 3 to get the average,
    # then display the result to the user
    average = ( quiz_1 + quiz_2 + quiz_3 ) / 3
    print ( "Average mark:", average )

    # Check whether the average is a pass (50 or above) or a fail (Selection)
    if average >= 50:
        print ( "Result: PASS" )
    else:
        print ( "Result: FAIL" )

    # Ask the user if they want to enter marks for another student.
    # If they type anything other than "y", the while loop will stop
    choice = input ( "Continue? Select Y/N: " )

print ( "Program Ended" )