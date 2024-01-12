# Описание задачи в print с выводом результата

import random

def main():
    SIZE = 6
    MIN_RANGE = 1
    MAX_RANGE = 5
    
    
    arr_one = []
    arr_two = []
    
    
    # fill the array with random numbers
    for i in range(SIZE):
        random_num = random.randint(MIN_RANGE, MAX_RANGE)
        arr_one.append(random_num)
        
        random_num = random.randint(MIN_RANGE, MAX_RANGE)  
        arr_two.append(random_num)
    
    print(f"First array {arr_one}")
    print(f"Second array {arr_two}")

    # Сombine arrays
    arr_common = arr_one + arr_two
    print(f"Cформувати третій список, що містить елементи обох списків \n{arr_common}")
    
    
    
    # Create array without repeat numbers
    arr_not_repeat = []
    
    for i in arr_one:
        # Check number for repat in the (arr_not_repeat) array 
        if i not in arr_not_repeat:
            # If number no, add
            arr_not_repeat.append(i)
            
    for i in arr_two:
        if i not in arr_not_repeat:
            arr_not_repeat.append(i) 
    
    print(f"Cформувати третій список, що містить елементи обох списків без повторів \n{arr_not_repeat}")
      
      
            
    # Create array for common numbers
    arr_common_numbers = []
    
    for i in arr_one:
        # If there number in arr_common_numbers, continue next iteration
        if i in arr_common_numbers:
            continue
        
        # If number in the arr_one and arr_two, number is common
        elif i in arr_one and i in arr_two:
            arr_common_numbers.append(i)     
    
    print(f"Cформувати третій список, що містить елементи спільні для двох списків \n{arr_common_numbers}")
    
    
    
    arr_unique = []
    
    # For arr_one 
    for i in arr_one:
        count_repeat = 0
        
        for k in arr_one:
            if i == k :
                count_repeat += 1
                
        # If the number is repeated < 2, this number unique
        if count_repeat < 2:
            arr_unique.append(i)
            
    # For arr_two      
    for i in arr_two:
        count_repeat = 0
        
        for k in arr_two:
            if i == k :
                count_repeat += 1
        
        # If the number is repeated < 2, this number unique
        if count_repeat < 2:
            arr_unique.append(i)
        
    print(f"Cформувати третій список, що містить тільки унікальні елементи кожного зі списків \n{arr_unique}")
    
    
        
    arr_max_min = []
    
    #For numbers max and min in arr_one
    max = min = arr_one[0]
    for i in arr_one:
        if i > max:
            max = i
        elif i < min:
            min = i
            
    arr_max_min.append(max)
    arr_max_min.append(min)
    
    # For numbers max and min in arr_two
    max = min = arr_two[0]
    for i in arr_two:
        if i > max:
            max = i
        elif i < min:
            min = i
            
    arr_max_min.append(max)
    arr_max_min.append(min)
    
    print(f"Cформувати третій список, що містить тільки мінімальне та максимальне значення кожного зі списків \n{arr_max_min}")
        
        
        
main()