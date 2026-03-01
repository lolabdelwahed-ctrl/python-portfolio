# 2025-01-15
# Purpose: This project was created to help me understand what went into calculating my final grade every time i calculated it when stressing over exams
# Final grade calculator


def fin_grade(current,target,final_weight):
  final_weight = user_final_weight/100
  final_score_req = (target-(current*(1-final_weight)))/final_weight
  return final_score_req

user_current = float(input('Your current grade is (numbers only please): '))
user_target = float(input('You want at least (numbers only please): '))
user_final_weight = float(input('Your final is worth (numbers only please): '))

You_ok = fin_grade(user_current,user_target,user_final_weight)
print (f'you need at least a {You_ok:.2f} in order to achieve your target grade')

