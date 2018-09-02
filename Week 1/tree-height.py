# python3

import sys
sys.setrecursionlimit(10**7) # max depth of recursion
  # new thread will get stack of such size

def TreeHeight(num_nodes,parents_list):
    for i in range(0,num_nodes):
        if parents_list[i] == -1:
            parent_node = i
        else :
            index = parents_list[i]
            children_dict[index].append(i)
    return height(parent_node)+1

def height(node):
    if children_dict[node]==[]:
        return 0
    list_children = children_dict[node]
    max = -1
    for i in list_children:
        if height(i)+1>max:
            max = height(i)+1
    return max

import time
start_time = time.time()
num_nodes = int(input())
children_dict = [[] for i in range(0,num_nodes)]
parents_list = input()
print(TreeHeight(num_nodes,list(map(int, parents_list.split()))))
print("--- %s seconds ---" % (time.time() - start_time))