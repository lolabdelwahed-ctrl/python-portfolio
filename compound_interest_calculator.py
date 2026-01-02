# 2025-12-29
# Purpose: This project connects my interest in coding with my passion of finance
# Compound interest calculator

principle = 0
rate = 0
time = 0
compounding_frequency = 0

while principle <= 0:
    principle = float(input('Enter the principle amount:'))
    if principle <= 0:
        print ('Invalid principle amount we do not accept <= 0')
    
while rate <= 0:
    rate = float(input('Enter the interest rate:'))
    if rate <= 0:
        print ('Invalid interest rate we do not accept <= 0')
               
while time <= 0:
    time = float(input('Enter the time in years:'))
    if time <= 0:
        print ('Invalid time frame we do not accept <= 0')

while compounding_frequency <= 0:
    compounding_frequency = int(input('Enter the amount of times interest is compounded per year:'))
    if compounding_frequency <= 0:
        print ('Invalid frequency we do not accept <= 0')

print (principle)
print (rate)
print (time)
print (compounding_frequency)
# to check if everything ran smoothly

total = principle * (1+(rate/100)/compounding_frequency) ** (time)

print (round(total,2))