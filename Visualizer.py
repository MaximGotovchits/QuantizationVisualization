import matplotlib.pyplot as plt
import numpy as np
%matplotlib inline

with open("output_data.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

height = []

left_boards = []
right_boards = []

for current_row in content:
    row_data = current_row.split()
    left_board = float(row_data[0])
    threshold = float(row_data[1])
    right_board = float(row_data[2] )
    left_mean = float(row_data[3])
    right_mean = float(row_data[4])
    
    left_boards.append(left_board)
    left_boards.append(threshold)
    left_boards = list(set(left_boards))
    left_boards.sort()
    
    right_boards.append(threshold)
    right_boards.append(right_board)
    right_boards = list(set(right_boards))
    right_boards.sort()
    if height != []:
        height.remove(max(height))
    height.append(left_mean)
    height.append(right_mean)
    plt.ylabel('Mean value');
    plt.xlabel('Threashold');
    curr_bins += 1
bar_list = plt.bar(left_boards, height=height, width=[y - x for x, y in zip(left_boards, right_boards)])

for curr_num in range(len(left_boards)):
        bar_list[curr_num].set_color(str(left_boards[curr_num] / 255.0))
