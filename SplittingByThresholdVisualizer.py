import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
import math
%matplotlib inline

with open("output_data.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

left_boards = []
right_boards = []

current_row_number = 2*len(content)
g = nx.Graph()
g.add_nodes_from(range(2*len(content) + 1))
pos = {0:(0,0)}
nx.set_node_attributes(g, 'pos', pos)
boards_to_pos = {str([0,255]):(0,0)}

labels = {0:str([0,255])}

step = 1. #math.pow(2, current_row_number - 1)
pos_x = 0
pos_y = 0
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
    
    for current_board_to_pos in boards_to_pos:
        if eval(current_board_to_pos)[0] == left_board:
            pos_y = boards_to_pos[current_board_to_pos][1] - 1
            pos_x = boards_to_pos[current_board_to_pos][0] - step / -pos_y
            del boards_to_pos[current_board_to_pos]
            curr_labels_size = len(labels)
            break    
    
    pos[current_row_number] = (pos_x, pos_y)
    pos[current_row_number - 1] = (pos_x + 2 * (step / -pos_y), pos_y)
    boards_to_pos[str([left_board, threshold])] = (pos_x, pos_y)
    boards_to_pos[str([threshold, right_board])] = (pos_x + 2 * (step / -pos_y), pos_y)
    
    labels[current_row_number] = str([left_board, threshold])
    labels[current_row_number - 1] = str([threshold, right_board])
    step /= 2
    current_row_number -= 2
    
plt.figure(figsize=(10,10))
nx.draw(G=g, pos=pos, node_size=200, font_size=5, with_labels=False)
nx.draw_networkx_labels(G=g,pos=pos,labels=labels,font_size=8)
plt.savefig("SplittingByThresholdVisualizer.png", format="PNG")
