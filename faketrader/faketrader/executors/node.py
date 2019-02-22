class Node:
    test = True
    def __init__(self):
        print("Node created.")

class MasterNode(Node):
    test = True

class WorkerNode(Node):
    test = True


class NodeFactory:
    test = True