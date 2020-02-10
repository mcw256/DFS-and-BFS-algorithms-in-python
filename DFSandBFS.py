from collections import deque
from sys import exit, stdin

adjacency_dic = {}
"""
{a: [b,c,d,...],
b: [a,c,d,...],
...
}
a - given vertex
[] - its adjacency list
"""

def depth_first_search(start_vertex): #returns list containing traveling order
    def travel(start_v):
        stack.append(start_v)
        output.append(start_v)
        is_visited_dic[start_v] = True
        for adj in adjacency_dic[start_v]:
            if not is_visited_dic[adj]:
                travel(adj)
        stack.pop()

    global adjacency_dic
    is_visited_dic = dict.fromkeys(adjacency_dic.keys(), False)
    stack = deque()
    output = []

    if adjacency_dic[start_vertex] == None:
        return [start_vertex]

    travel(start_vertex)
    return output

def breadth_first_search(start_vertex): #returns list containing traveling order
    global adjacency_dic
    def travel(start_v):
        global adjacency_dic
        queue.popleft()
        for adj in adjacency_dic[start_v]:
            if not is_visited_dic[adj]:
                output.append(adj)


                queue.append(adj)
                is_visited_dic[adj] = True
        if(queue): #true if dequeue contains any element
            travel(queue[0])


    is_visited_dic = dict.fromkeys(adjacency_dic.keys(), False)
    queue = deque()
    output = []
    output.append(start_vertex)
    queue.append(start_vertex)
    is_visited_dic[start_vertex] = True

    if adjacency_dic[start_vertex] == None:
        return [start_vertex]

    travel(start_vertex)
    return output
