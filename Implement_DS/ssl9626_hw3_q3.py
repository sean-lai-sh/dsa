def find_duplicates(lst):
    if not isinstance(lst, list):
        raise TypeError("Invalid Type. Please use List objects for function")
    poss_num = [i for i in range(1, len(lst))]  # from 1 -> n-1 0(N)
    return_lst = []
    for i in range(len(lst)): # 0(n)
        num_val = int(lst[i])
        if num_val == poss_num[num_val - 1]:
            poss_num[num_val - 1] = None  # Make it such that a copy has been here
        elif poss_num[num_val - 1] is None:
            return_lst.append(num_val)
            poss_num[num_val - 1] = "STOP" #Prevent further repeats
    return return_lst
