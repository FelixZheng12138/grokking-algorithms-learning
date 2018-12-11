#!/usr/bin/python
# -*- coding: UTF-8 -*-
#《算法图解》(原书《grokking algorithms》)
# 广度优先搜索
from collections import deque
def person_is_seller(name):
    return name[-1] == 'm'
def createGraph():
    graph = {}
    graph["you"] = ["alice", "bob", "claire"]
    graph["bob"] = ["anuj", "peggy"]
    graph["alice"] = ["peggy"]
    graph["claire"] = ["thom", "jonny"]
    graph["anuj"] = []
    graph["peggy"] = []
    graph["thom"] = []
    graph["jonny"] = []
    return graph
def BFS(graph):
    search_queue = deque()
    search_queue += graph["you"]
    while search_queue:
        person = search_queue.popleft()
        if person_is_seller(person) is True:
            print('now we found the mango seller : %s' % person)
            return True
        else:
            search_queue += graph[person]
            print('add %s to search_queue' % person)
    return False
def main():
    graph =  createGraph()
    BFS(graph)
if __name__ == "__main__":
    main()
