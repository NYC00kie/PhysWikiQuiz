#TODO: slow down print out process
#TODO: print out ALL retrieved variables

import module0_formula_and_identifier_retrieval as module0
import module1_identifier_unit_retrieval as module1
import module2_formula_rearrangement as module2
import module3_identifier_value_generation as module3
import module4_question_text_generation as module4
import module5_solution_value_and_unit_check as module5

##############################################
# Module 0: Formula and Identifier Retrieval #
##############################################

# INSTRUCTOR INPUT

# Module 0.0: Input formula question QID
qid = input('Input formula question QID:')
# Example
#qid = 'Q11376'
print('\nInput formula question QID: ',qid)

# Get item from QID
print('\nRetrieving Wikidata item...\n')
item = module0.get_Wikidata_item(qid)

# Module 0.1: Get concept name from item
concept_name = module0.get_concept_name(item)
print(f'Retrieving formula concept name: >>{concept_name}<<\n')
# Example
#concept_name = 'acceleration'

# System output for processing question
print(f'Generating physics formula question for >>{concept_name}<<...\n')
# Example
#print('Generating physics formula question for >>acceleration<<...')

# Module 0.2: Get defining formula
defining_formula = module0.get_defining_formula(item)
print(f'Retrieving defining formula: >>{defining_formula}<<\n')
# Example
# 'defining formula' (P2534) = 'a = dv/dt'
#defining_formula = '\\boldsymbol{a} = \\frac{\\mathrm{d} \\boldsymbol{v}}{\\mathrm{d} t}'

# Module 0.3: Get formula identifier (symbol, name) tuples
print('Retrieving formula identifier symbols and names...\n')
formula_identifiers = module0.get_formula_identifiers(item)
# Example
#formula_identifiers = [('a', 'acceleration'), ('v', 'velocity'), ('t', 'duration')]
# a: 'acceleration' (Q11376)
# v: 'velocity' (Q11465)
# t: 'duration' (Q2199864)

#######################################
# Module 1: Identifier Unit Retrieval #
#######################################

print('Retrieving formula identifier units...\n')
formula_unit_dimensions = module1.get_formula_unit_dimensions(item)
#identifier_unit_dimensions = module1.get_identifier_unit_dimensions(defining_formula,formula_identifiers,formula_unit_dimensions)
# Example
# 'ISQ dimension' property (P4020) = 'LT^-2
#formula_unit_dimensions = '\mathsf{L} \mathsf{T}^{-2}'
identifier_unit_dimensions = ['m/s^2', 'm/s', 's']

###################################
# Module 2: Formula Rearrangement #
###################################

print('Generating formula rearrangements...\n')
# Get formula rearrangements using Computer Algebra Systems (CAS), maybe SymPy
#formula_rearrangements = module2.get_random_formula_rearrangements(defining_formula)
# Example
formula_rearrangements = ['a = v/t', 'v = a t','t = v/a']

#########################################
# Module 3: Identifier Value Generation #
#########################################

print('Generating random identifier values...\n')
#identifier_values = module3.get_random_identifier_values(formula_rearrangements)
# (randomize)
# Example
identifier_values = (3,6,2)#, [(6,3,2), (2,6,3)] # (a,v,t)

######################################
# Module 4: Question Text Generation #
######################################

print('Generating formula question text...\n')
question_text = module4.get_question_text(formula_identifiers,identifier_values,identifier_unit_dimensions)
# Example
#question_text = 'What is the acceleration a, given velocity v = 6 m/s and time t = 2 s ?' # a = v/t = 3 m/s^2
# a) 'What is the force F, given mass m = 2 kg and acceleration a = 3 m/s^2 ?'
# b) 'What is the mass m, given force F = 6 N and acceleration a = 3 m/s^2 ?'
# c) 'What is the acceleration a, given Force F = 6 N and mass m = 2 kg ?'
# (randomize)
print(question_text)

#############

# STUDENT INPUT

print('Get student answer input...\n')
identifier_name, identifier_symbol = module5.get_lhs_identifier_properties(formula_rearrangements,formula_identifiers)
answer_input = input(f'{identifier_name} {identifier_symbol} = ?')
answer_value,answer_unit = module5.get_answer_value_and_unit(answer_input)
print('\nParse answer input...\n')
print(f'Answer value: {answer_value}')
print(f'Answer unit: {answer_unit}\n')
# Example
# a = 3 m/s^2

###########################################
# Module 5: Solution Value and Unit Check #
###########################################

print('Check answer value and unit...\n')
# check solution value
#value_correct = module5.check_value(formula_rearrangements,answer_value)
value_correct = True
if value_correct:
    print('Value correct!')
else:
    print('Value incorrect!')
# 'correct'
# check solution unit
#unit_correct = module5.check_unit(formula_rearrangements,answer_value)
unit_correct = True
if unit_correct:
    print('Unit correct!')
else:
    print('Unit incorrect!')
# 'correct'

print('\nEnd of system workflow.')