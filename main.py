# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 12:24:53 2022

@author: janpe
"""

import os

file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)
from optimizer import topological_opti

from fancy_classes import Graph, State
# import config_concurrence as confi
from state import state1 as sst
import theseus as th
import help_functions as hf
import sys
import saver
import json


config = 'configs/conc_4-3'#sys.argv[1] #conc_4-3 'ghz_346' #
with open(config + ".json") as data:
    cnfg = json.load(data)

sys.setrecursionlimit(1000000000)

if cnfg['loss_func'] == 'ent':
    # concurrence optimization
    # define local dimensions
    dimensions = [int(ii) for ii in str(cnfg['dim'])]
    if len(dimensions) % 2 != 0:
        dimensions.append(1)
    target_state = None
    sys_dict = hf.get_sysdict(dimensions, bipar_for_opti=cnfg['K'],
                              imaginary = cnfg['imaginary'])
else:
    # target state optimization
    sys_dict = None
    # add ancillas
    term_list = [term + cnfg['num_anc'] * '0' for term in cnfg['target_state']]
    if 'amplitudes' in cnfg:
        target_state = State(term_list,amplitudes=cnfg['amplitudes'])
    else:
        target_state = State(term_list)
    target_kets = target_state.kets
    # define local dimensions
    dimensions = th.stateDimensions(target_kets)

# build starting graph
edge_list = th.buildAllEdges(dimensions, imaginary=cnfg['imaginary'])
edge_list = hf.prepEdgeList(edge_list, cnfg)

print(f'start graph has {len(edge_list)} edges.')
start_graph = Graph(edge_list)

# topological optimization
sv = saver.saver(config=cnfg)
for i in range(cnfg['samples']):
    optimizer = topological_opti(start_graph, ent_dic=sys_dict, target_state=target_state, config=cnfg)
    graph_res = optimizer.topologicalOptimization()
    sv.save_graph(optimizer)
#%%
graph_res.getState()
print(f'finished with graph with {len(graph_res.edges)} edges.')
print(graph_res.state.state)

ancillas = dimensions.count(1)
if ancillas != 0:
    end_res = dict()
    for kets,ampl in graph_res.state.state.items():
        end_res[kets[:-ancillas]] = ampl
else: end_res = graph_res.state.state
result = sst(end_res)
result.info()






