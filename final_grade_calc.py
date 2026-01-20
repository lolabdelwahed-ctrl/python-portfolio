# 2025-01-15
# Purpose: This project was created to help me understand what went into calculating my final grade every time i calculated it when stressing over exams
# Final grade calculator

current = 0
target = 0
final_weight = 0

current = float(input('Your current grade is (numbers only please): '))
target = float(input('You want at least (numbers only please): '))
final_weight = float(input('Your final is worth (numbers only please): '))

print (current)
print (target)
print (final_weight)
# to check if everything ran smoothly
final_weight = final_weight/100


final_score_req = (target-(current*(1-final_weight)))/final_weight

print (f'you need at least a {final_score_req:.2f} in order to achieve your target grade')

