import numpy as np

sample_set = np.random.choice(90000, 100000, replace=True)
sample_set_solved = []
duplicate_list = {}
highest_possible = len(sample_set)-1
lowest_possible = 0

print(f"Unorganized: {sample_set} \n")


for i in range(lowest_possible, len(sample_set)):

    list_position = highest_possible - sample_set[i]
    duplicate_list.setdefault(list_position,[])
    duplicate_list[list_position].append(sample_set[i])

for i in range(lowest_possible, len(sample_set)):
    try:
        sample_set_solved.append(duplicate_list[i])
    except:
       continue


print(f"Organized: {sample_set_solved} \n")
