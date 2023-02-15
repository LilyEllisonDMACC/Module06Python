"""
Program: validate_input_in_functions.py
Author: Lily Ellison
Last date modified: 02/15/2023

The purpose of this program is to write a function, score_input(),
that takes parameters test_name (mandatory), test_score (optional, default is negative,
validation required), and invalid_message (optional, default is 'Invalid test score!'),
validates the test_score, and returns a string. String will be either test name and score
if validation passes, or test_name and invalid_message.
"""
def score_input(test_name, test_score=-1, invalid_message='Invalid Test Score!'):
#try to cast test_score as int
    try:
        test_score_as_int = int(test_score)
        # validate if test_score btwn 1 to 100 inclusive
        if test_score_as_int < 0 or test_score_as_int > 100:
            # throw exception
            raise ValueError('Bad Input')
        # return string with test_name and test_score (Test 1: 70)
        else:
            return test_name + ": " + str(test_score)
    except:
        # return string with test_name and invalid_message (Test 2: Invalid Test Score!)
        return test_name + ": " + invalid_message

#call function from main
if __name__ == '__main__':
    #Call function with valid input:
    display_results01 = score_input("Test 1", 90)
    print(display_results01)

    #call function with score too low:
    display_results02 = score_input("Test 2", -5)
    print(display_results02)

    #call function with score too high:
    display_results03 = score_input("Test 3", 500)
    print(display_results03)

    #call function with non-numeric input
    display_results04 = score_input("Test 4", "ninety")
    print(display_results04)

    #call function without score input
    display_results05 = score_input("Test 5")
    print(display_results05)

"""
Test results:
Test 1: 90
Test 2: Invalid Test Score!
Test 3: Invalid Test Score!
Test 4: Invalid Test Score!
Test 5: Invalid Test Score!
"""






