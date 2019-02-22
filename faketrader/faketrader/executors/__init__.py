from .node import *

"""
The module `faketrader.executors` provides resources to distribute vector tracking
  and trade execution over a number of nodes.

node.py:
    - Node
    - WorkerNode: receives vector assignment, "executes trade"
    - MasterNode: manages all vector assignments
    - NodeFactory: generates, scales nodes

tests/
    testNodeFactory.py
    testNodes.py
"""

__all__ =  ['WorkerNode', 
            'MasterNode', 
            'NodeFactory']