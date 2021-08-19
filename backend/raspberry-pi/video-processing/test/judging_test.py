from random import *


def make_random_input_dict():
    for boolKey in input_dict:
        input_dict[boolKey] = int(randint(0, 100)/80)

    return input_dict


def judging_continous(CONTINOUS_VALUE, detected_result_dict, continous_info):

    for i in range(len(continous_info)):
        if detected_result_dict[i] == 0:
            continous_info[i] += 1
            if continous_info[i] < CONTINOUS_VALUE:
                detected_result_dict[i] = 1
            elif continous_info[i] > CONTINOUS_VALUE*2:  # 스택오버플로우 방지
                continous_info[i] = CONTINOUS_VALUE
        else:
            continous_info[i] = 0

    return detected_result_dict


CONTINOUS_VALUE = 3
parking_slot_number = 8

continous_info = [CONTINOUS_VALUE+1 for i in range(parking_slot_number)]
print(continous_info)
input_dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}


for k in range(25):
    input_dict = make_random_input_dict()

    output_dict = judging_continous(
        CONTINOUS_VALUE, input_dict, continous_info)

    print(f"final function : {output_dict}")
