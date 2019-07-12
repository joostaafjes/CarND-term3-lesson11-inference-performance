from graph_utils import load_graph

sess, base_ops = load_graph('base_graph.pb')
print(len(base_ops)) # 2165
sess, frozen_ops = load_graph('frozen_graph.pb')
print(len(frozen_ops)) # 245
sess, optimized_ops = load_graph('optimized_graph.pb')
print(len(optimized_ops)) # 200
sess, eightbit_ops = load_graph('eightbit_graph.pb')
print(len(eightbit_ops)) # 425
