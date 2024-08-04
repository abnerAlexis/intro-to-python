f = open('achievement-1/exercise-1.2/1.2-PracticeTask1/types.txt', 'r')
lines = f.readlines()
[principal, rate, time_period] = [x.strip('\n') for x in lines]
f.close

print('principal : ', principal)    # principal :  1000
print('rate : ', rate)              # rate :  0.145
print('time_period: ', time_period)   # time_period:  3

print('\nType Casting')
print('principal : ', float(principal))    # principal :  1000.0
print('rate : ', float(rate))              # rate :  0.145
print('time_period: ', float(time_period))   # time_period:  3.0