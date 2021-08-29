from random import *

CONTINOUS_VALUE = 100

continous_info = [CONTINOUS_VALUE+1 for i in range(8)]
print(continous_info)
boolResult = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}


for k in range(25):
    for boolKey in boolResult:
        boolResult[boolKey] = int(randint(0, 100)/80)

    # print(f"before function : {boolResult}")

    for i in range(len(continous_info)):
        if boolResult[i] == 0:
            continous_info[i] += 1
            if continous_info[i] < CONTINOUS_VALUE:
                boolResult[i] = 1
            elif continous_info[i] > 200:
                continous_info[i] = CONTINOUS_VALUE
        else:
            continous_info[i] = 0
    print(f"after function : {boolResult}\n")

    # print(f"{k}번째 시행 결과 : {continous_info}")

# print(f"final function : {boolResult}\n")
