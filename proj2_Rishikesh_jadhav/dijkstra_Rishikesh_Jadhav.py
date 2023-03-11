#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENPM 661
Project 2

@author: Rishikesh Jadhav
UID: 119256534
"""

from functions import *

map = create_map()

initialize()

start_node = getStartNode(map)
goal_node = getGoalNode(map)

nodes = Dijkstra(start_node, goal_node, map)
node_objects, path = GeneratePath(nodes, goal_node)

Animate(node_objects, path, map)

