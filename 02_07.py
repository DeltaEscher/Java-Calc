# Coder: Skyler Grabowsky
# Date: 12/15/2015
# 02_07: Module Project

from math import *     # Import Math Functions


def calculator_setup():     # Choose Calculator Type
        print "\n"
	print "This calculator can use many functions"
	print "Type in how powerful you want your calculator to be"
	print "Choices are: Basic, Intermediate, Scientific"
	print "In order of choice: Type 1, 2, or 3"

        print "\n"
	global complexity_choice
	complexity_choice = input("Calculator type: ")
	if complexity_choice != 1:
		if complexity_choice != 2:
			if complexity_choice !=  3:
				print "Invalid Choice, restarting"
		
				calculator_setup()
				
                        else:
                                if complexity_choice == 1:
                                        calculator_idle()
			
                                elif complexity_choice == 2:
                                        calculator_idle()
			
                                elif complexity_choice == 3:
                                        calculator_idle()
			
                                else:
                                        print "\n"
                                        print "Unknown Error"
                                        print "Please Exit Program"
			
                                        limbo()

                else:
                                if complexity_choice == 1:
                                        calculator_idle()
			
                                elif complexity_choice == 2:
                                        calculator_idle()
			
                                elif complexity_choice == 3:
                                        calculator_idle()
			
                                else:
                                        print "\n"
                                        print "Unknown Error"
                                        print "Please Exit Program"
			
                                        limbo()

        else:
                                if complexity_choice == 1:
                                        calculator_idle()
			
                                elif complexity_choice == 2:
                                        calculator_idle()
			
                                elif complexity_choice == 3:
                                        calculator_idle()
			
                                else:
                                        print "\n"
                                        print "Unknown Error"
                                        print "Please Exit Program"
			
                                        limbo()

		
	

def calculator_idle():     # Choose to Take Tutorial of Calculator
        print "\n"
        
	calculator_tutorial = raw_input("Would you like an overview of the available functions? ").lower()
	
	if calculator_tutorial == 'yes' or 'y':
		calculator_function_overview()
		
	else:
		calculator_menu()

		
def calculator_function_overview():     # Gives Tutorial of Calculator
	if complexity_choice >= 1 :
                print "\n"
		print "Basic"
		
		print "\n"
		print "1. To figure the sum of numbers, type 'Sum'"
		print "2. To figure out the product of numbers, type 'Multiply'"
		print "3. To figure out the difference, type 'Difference'"
		print "4. To figure out division, type 'Divide'"
		print "5. To figure out powers, type 'Power'"
		
	if complexity_choice >= 2:
		print "\n"
		print "Intermediate"
		
		print "\n"
		print "1.  To figure out square roots, type 'Square Root'"
		print "2. To figure out cube roots, type 'Cube Root'"
		print "3. To figure out fourth roots, type 'Fourth Root'"
		print "4. To figure out a base 10 logarithm, type 'Logarithm'"
		print "5. To figure out the hypotenuse of a right triangle, type 'Hypotenuse'"
		
	if complexity_choice > 2:
                print "\n"
                print "Scientific"

                print "\n"
		print "1. To figure out the sine, cosine, or tangent of an angle, type 'Sin' 'Cos' or 'Tan'"
		print "2. To figure out the arcsine, arccosine, or arctangent, type 'ArcSin' 'ArcCos' or 'ArcTan'"
		
	print "\n"
	print "All Functions Logged"
	
	raw_input("Do Anything to Continue. ")
	
	if complexity_choice == 1:
		calculator_menu_basic()
		
	elif complexity_choice == 2:
		calculator_menu_intermediate()
		
	elif complexity_choice == 3:
		calculator_menu_scientific()
		
	else:
                print "\n"
		print "Unknown Error"
		print "Please Exit Program"
		
		limbo()
		

def calculator_menu_basic():     # Choose Function to Use
	print "\n" * 50
	
	function_select_calc = raw_input("").lower()
	
	if function_select_calc == "sum":
		calculate_sum()
		
	elif function_select_calc == "multiply":
		calculate_multiply()
		
	elif function_select_calc == "difference":
		calculate_difference()
		
	elif function_select_calc == "divide":
		calculate_division()
		
	elif function_select_calc == "power":
		calculate_powers()
		
	else:
		print "Non-Recognized Function"
		print "Restarting"
		
		raw_input("Press Enter to Continue. ")
		
		calculator_menu_basic()


def calculator_menu_intermediate():     # Choose Function to Use
	print "\n" * 50
	
	function_select_calc2 = raw_input("").lower()
	
	if function_select_calc2 == "sum":
		calculate_sum()
		
	elif function_select_calc2 == "multiply":
		calculate_multiply()
		
	elif function_select_calc2 == "difference":
		calculate_difference()
		
	elif function_select_calc2 == "divide":
		calculate_division()
		
	elif function_select_calc2 == "power":
		calculate_powers()
		
	elif function_select_calc2 == "square root":
		calculate_squareRoot()
		
	elif function_select_calc2 == "cube root":
		calculate_cubeRoot()
		
	elif function_select_calc2 == "fourth root":
		calculate_fourthRoot()
		
	elif function_select_calc2 == "logarithm":
		calculate_logarithm()
		
	elif function_select_calc2 == "hypotenuse":
		calculate_hypotenuse()
		
	else:
		print "Non-Recognized Function"
		print "Restarting"
		
		raw_input("Press Enter to Continue. ")
		
		calculator_menu_intermediate()


def calculator_menu_scientific():     # Choose Function to Use
	print "\n" * 50
	
	function_select_calc3 = raw_input(">>> ").lower()
	
	if function_select_calc3 == "sum":
		calculate_sum()
		
	elif function_select_calc3 == "multiply":
		calculate_multiply()
		
	elif function_select_calc3 == "difference":
		calculate_difference()
		
	elif function_select_calc3 == "divide":
		calculate_division()
		
	elif function_select_calc3 == "power":
		calculate_powers()
		
	elif function_select_calc3 == "square root":
		calculate_squareRoot()
		
	elif function_select_calc3 == "cube root":
		calculate_cubeRoot()
		
	elif function_select_calc3 == "fourth root":
		calculate_fourthRoot()
		
	elif function_select_calc3 == "logarithm":
		calculate_logarithm()
		
	elif function_select_calc3 == "hypotenuse":
		calculate_hypotenuse()
		
	elif function_select_calc3 == "sin":
		calculate_sine()
		
	elif function_select_calc3 == "cos":
		calculate_cosine()
		
	elif function_select_calc3 == "tan":
		calculate_tangent()
		
	elif function_select_calc3 == "arcsin":
		calculate_arcsine()
		
	elif function_select_calc3 == "arccos":
		calculate_arccosine()
		
	elif function_select_calc3 == "arctan":
		calculate_arctangent()
	
	else:
		print "Non-Recognized Function"
		print "Restarting"
		
		raw_input("Press Enter to Continue. ")
		
		calculator_menu_scientific()
	

def calculate_sum():     # Calculate a Number Sum
	print "\n"

	sum_continuity = True
	sum_total = 0
	numbers_in_sum = []
	
	amountOf_numbers_sum  = input("Amount of numbers being added: ")
		
	for x in range(0, amountOf_numbers_sum):
                print "\n"
		result_sum = input("Number to add: ")

                numbers_in_sum.append(str(result_sum))
		
	for item in numbers_in_sum:
		sum_total += int(item)
	
	print "\n"
	print "The sum of the numbers is " + "'" + str(sum_total) + "'"

	print "\n"
	raw_input("Press Enter to Continue. ")
	
	if complexity_choice == 1:
		calculator_menu_basic()
	
	elif complexity_choice == 2:
		calculator_menu_intermediate()
	
	elif complexity_choice == 3:
		calculator_menu_scientific()

	else:
		print "\n"
		print "Unknown Error Found"
		print "Please Exit Program"
		
		limbo()

def calculate_multiply():     # Calculates Multiplication
	print "\n"
	
	multiply_total = 1
	numbers_in_multiply = []
	
	amountOf_numbers_multiply = input("Amount of numbers being multiplied: ")
			
	for x in range(0, amountOf_numbers_multiply):
                print "\n"
		result_multiply  = input("Number to multiply: ")
		
		numbers_in_multiply.append(str(result_multiply))
		
	for item in numbers_in_multiply:
		multiply_total *= int(item)
		
	print "\n"
	print "The product of the numbers is " + "'" + str(multiply_total) + "'"

        print "\n"
	raw_input("Press Enter to Continue. ")
	
	if complexity_choice == 1:
		calculator_menu_basic()
	
	elif complexity_choice == 2:
		calculator_menu_intermediate()
	
	elif complexity_choice == 3:
		calculator_menu_scientific()

	else:
		print "\n"
		print "Unknown Error Found"
		print "Please Exit Program"
		
		limbo()
		

def calculate_difference():     # Calculates Subtraction
	print "\n"
	
	difference_total = 0
	numbers_in_difference = []
	
	difference_total = input("Number to start with: ")
	amountOf_numbers_difference = input("Amount of numbers in difference: ")
	
	for x in range(0, amountOf_numbers_difference):
                print "\n"
		result_difference = input("Number to subtract: ")

		numbers_in_difference.append(str(result_difference))
			
	for item in numbers_in_difference:
		difference_total -= int(item)
			
	print "\n"
	print "The difference of the numbers is " + "'" + str(difference_total) + "'"

	print "\n"
	raw_input("Press Enter to Continue. ")
		
	if complexity_choice == 1:
		calculator_menu_basic()
			
	elif complexity_choice == 2:
		calculator_menu_intermediate()
			
	elif complexity_choice == 3:
		calculator_menu_scientific()
			
	else:
		print "\n"
		print "Unknown Error Found"
		print "Please Exit Program"
			
		limbo()


def calculate_division():     # Calculates Division
	print "\n"
	
	division_total = 0
	numbers_in_division = []
	
	division_total = input("Number to start with: ")
	amountOf_numbers_divide = input("Amount of numbers in division: ")
	
	for x in range(0, amountOf_numbers_divide):
                print "\n"
		result_division = raw_input("Number to divide: ")
		
		numbers_in_division.append(str(result_division))
			
	for item in numbers_in_division:
			division_total /= float(item)
			
	print "\n"
	print "The result of the numbers is " + "'" + str(division_total) + "'"

	print "\n"
	raw_input("Press Enter to Continue. ")
		
	if complexity_choice == 1:
		calculator_menu_basic()
			
	elif complexity_choice == 2:
		calculator_menu_intermediate()
			
	elif complexity_choice == 3:
		calculator_menu_scientific()
			
	else:
		print "\n"
		print "Unknown Error Found"
		print "Please Exit Program"
			
		limbo()

def calculate_powers():     # Calculate Exponents
	print "\n"
	
	number_start_power = 0
	number_power_up = 0
	
	number_start_power = input("Beginning Number: ")
	number_power_up = input("To what power: ")
			
	power_total = pow(number_start_power, number_power_up)
		
	print "\n"
        print "The result of the numbers is " + "'" + str(power_total) + "'"

	print "\n"
	raw_input("Press Enter to Continue. ")
		
	if complexity_choice == 1:
		calculator_menu_basic()
			
	elif complexity_choice == 2:
		calculator_menu_intermediate()
			
	elif complexity_choice == 3:
		calculator_menu_scientific()
			
	else:
		print "\n"
		print "Unknown Error Found"
		print "Please Exit Program"
			
		limbo()


def calculate_squareRoot():     # Calculates Square Roots
	print "\n"
	
	number_root = 0
	
	number_root = input("Number to square: ")
	
	root_total = sqrt(number_root)
	
	print "\n"
	print "The result of the numbers is " + "'" + str(root_total) + "'"

	print "\n"
	raw_input("Press Enter to Continue. ")
	
	if complexity_choice == 1:
		calculator_menu_basic()
			
	elif complexity_choice == 2:
		calculator_menu_intermediate()
			
	elif complexity_choice == 3:
		calculator_menu_scientific()
			
	else:
		print "\n"
		print "Unknown Error Found"
		print "Please Exit Program"
			
		limbo()


def calculate_cubeRoot():     # Calculates Cube Roots
	print "\n"
	
	number_cube = 0
	
	number_cube = input("Number to cube: ")
	
	cube_total = pow(number_cube, 1.0/3.0)
	
	print "\n"
        print "The result of the numbers is " + "'" + str(cube_total) + "'"

        print "\n"
	raw_input("Press Enter to Continue. ")
	
	if complexity_choice == 1:
		calculator_menu_basic()
			
	elif complexity_choice == 2:
		calculator_menu_intermediate()
			
	elif complexity_choice == 3:
		calculator_menu_scientific()
			
	else:
		print "\n"
		print "Unknown Error Found"
		print "Please Exit Program"
			
		limbo()


def calculate_fourthRoot():     # Calculates Fourth Roots
	print "\n"
	
	number_fourth = 0
	
	number_fourth = input("Number to fourth: ")
	
	fourth_total = pow(number_fourth, 1.0/4.0)
	
	print "\n"
	print "The result of the numbers is " + "'" + str(fourth_total) + "'"
	
	print "\n"
	raw_input("Press Enter to Continue. ")
	
	if complexity_choice == 1:
		calculator_menu_basic()
			
	elif complexity_choice == 2:
		calculator_menu_intermediate()
			
	elif complexity_choice == 3:
		calculator_menu_scientific()
			
	else:
		print "\n"
		print "Unknown Error Found"
		print "Please Exit Program"
			
		limbo()

def calculate_logarithm():     # Calculates Base 10 Logarithms
	print "\n"
	
	number_log = 0
	
	number_log = input("Number to log 10: ")

	log_total = log10(number_log)
	
	print "\n"
	print "The result of the numbers is " + "'" + str(log_total) + "'"
	
	print "\n"
	raw_input("Press Enter to Continue. ")
	
	if complexity_choice == 1:
		calculator_menu_basic()
			
	elif complexity_choice == 2:
		calculator_menu_intermediate()
			
	elif complexity_choice == 3:
		calculator_menu_scientific()
			
	else:
		print "\n"
		print "Unknown Error Found"
		print "Please Exit Program"
			
		limbo()


def calculate_hypotenuse():     # Calculates a Right Triangle Hypotenuse
	print "\n"
	
	equate_hypotenuse = 0
	first_num_hypo = 0
	second_num_hypo = 0
	hypotenuse = 0
	
	first_num_hypo = input("What is the first side's length: ")
	print "\n"
	second_num_hypo = input ("What is the second side's length: ")
	
	equate_hypotenuse = pow(first_num_hypo, 2) + pow(second_num_hypo, 2)
	hypotenuse = sqrt(equate_hypotenuse)
	
	print "\n"
	print "The result of the numbers is " + "'" + str(hypotenuse) + "'"
	
	raw_input("\n Press Enter to Continue. ")
	
	if complexity_choice == 1:
		calculator_menu_basic()
			
	elif complexity_choice == 2:
		calculator_menu_intermediate()
			
	elif complexity_choice == 3:
		calculator_menu_scientific()
			
	else:
		print "\n"
		print "Unknown Error Found"
		print "Please Exit Program"
			
		limbo()


def calculate_sine():     # Calculates Sine
	print "\n"
	print "Note: Calc does not accept 'pi' yet"
	print "\n"
	
	sine_angle = 0
	sine_total = 0
	
	sine_angle = input("Radian to sine: ")
	
	sine_total = sin(sine_angle)
	
	print "\n"
	print "The result of the numbers is " + "'" + str(sine_total) + "'"

	print "\n"
	raw_input("Press Enter to Continue. ")
	
	if complexity_choice == 1:
		calculator_menu_basic()
			
	elif complexity_choice == 2:
		calculator_menu_intermediate()
			
	elif complexity_choice == 3:
		calculator_menu_scientific()
			
	else:
		print "\n"
		print "Unknown Error Found"
		print "Please Exit Program"
			
		limbo()


def calculate_cosine():     # Calculates Cosine
	print "\n"
	print "Note: Calc does not accept 'pi' yet"
	print "\n"
	
	cosine_angle = 0
	cosine_total = 0
	
	cosine_angle = input("Radian to cosine: ")
	
	cosine_total = cos(cosine_angle)
	
	print "\n"
	print "The result of the numbers is " + "'" + str(cosine_total) + "'"
	
	print "\n"
	raw_input("Press Enter to Continue")
	
	if complexity_choice == 1:
		calculator_menu_basic()
			
	elif complexity_choice == 2:
		calculator_menu_intermediate()
			
	elif complexity_choice == 3:
		calculator_menu_scientific()
			
	else:
		print "\n"
		print "Unknown Error Found"
		print "Please Exit Program"
			
		limbo()


def calculate_tangent():     # Calculates Tangent
	print "\n"
	print "Note: Calc does not accept 'pi' yet"
	print "\n"
	
	tangent_angle = 0
	tangent_total = 0
	
	tangent_angle = input("Radian to tangent: ")
	
	tangent_total = tan(tangent_angle)
	
	print "\n"
	print "The result of the numbers is " + "'" + str(tangent_total) + "'"
	
	print "\n"
	raw_input("Press Enter to Continue")
	
	if complexity_choice == 1:
		calculator_menu_basic()
			
	elif complexity_choice == 2:
		calculator_menu_intermediate()
			
	elif complexity_choice == 3:
		calculator_menu_scientific()
			
	else:
		print "\n"
		print "Unknown Error Found"
		print "Please Exit Program"
			
		limbo()


def calculate_arcsine():     # Calculates Arcsine
	print "\n"
	print "Note: Calc does not accept 'pi' yet"
	print "Math Reminder: arcsin/arccos/arctan can only accept numbers from -1 to 1"
	print "\n"
	
	arcsine_angle = 0
	arcsine_total = 0
	
	arcsine_angle = input("Radian to arcsine: ")
			
	arcsine_total = asin(arcsine_angle)
	
	print "\n"
	print "The result of the numbers is " + "'" + str(arcsine_total) + "'"

	print "\n"
	raw_input("Press Enter to Continue")
	
	if complexity_choice == 1:
		calculator_menu_basic()
			
	elif complexity_choice == 2:
		calculator_menu_intermediate()
			
	elif complexity_choice == 3:
		calculator_menu_scientific()
			
	else:
		print "\n"
		print "Unknown Error Found"
		print "Please Exit Program"
			
		limbo()


def calculate_arccosine():     # Calculates Arccosine
	print "\n"
	print "Note: Calc does not accept 'pi' yet"
	print "Math Reminder: arcsin/arccos/arctan can only accept numbers from -1 to 1"
	print "\n"
	
	arccosine_angle = 0
	arccosine_total = 0
		
	arccosine_angle =input("Radian to arccosine: ")
	
	arccosine_total = acos(arccosine_angle)
	
	print "\n"
	print "The result of the numbers is " + "'" + str(arccosine_total) + "'"
	
	print "\n"
	raw_input("Press Enter to Continue")
	
	if complexity_choice == 1:
		calculator_menu_basic()
			
	elif complexity_choice == 2:
		calculator_menu_intermediate()
			
	elif complexity_choice == 3:
		calculator_menu_scientific()
			
	else:
		print "\n"
		print "Unknown Error Found"
		print "Please Exit Program"
			
		limbo()


def calculate_arctangent():     # Calculates Arctangent
	print "\n"
	print "Note: Calc does not accept 'pi' yet"
	print "Math Reminder: arcsin/arccos/arctan can only accept numbers from -1 to 1"
	print "\n"
	
	arctangent_angle = 0
	arctangent_total = 0
	
	arctangent_angle = input("Radian to arctangent: ")
	
	arctangent_total = atan(arctangent_angle)
	
	print "\n"
	print "The result of the numbers is " + "'" + str(arctangent_total) + "'"

	print "\n"
	raw_input("Press Enter to Continue")
	
	if complexity_choice == 1:
		calculator_menu_basic()
			
	elif complexity_choice == 2:
		calculator_menu_intermediate()
			
	elif complexity_choice == 3:
		calculator_menu_scientific()
			
	else:
		print "\n"
		print "Unknown Error Found"
		print "Please Exit Program"
			
		limbo()

		
def limbo():     # Freezes Program for Errors
	print "\n"
	
	
calculator_setup()     # Begin Setup
