# if the order of all node is in a circle
from random import shuffle

def dist_of_2D(nodes, squ_siz = -1) :
    len_n = len(nodes)
    
    shuffle(nodes)
    order = [-sum(x) if x[0] > x[1] else sum(x) for x in nodes]
    order.sort()
    print("all_kind",order)

    if squ_siz != -1 :
        # if all nodes are on a square sized "squ_siz"
        squ_len = squ_siz*4
        order = [-sum(x)+squ_len if x[0] > x[1] else sum(x) for x in nodes]
        order.sort()
        print("squ",order)

    if squ_siz != -1 :
        # form a recursion circle
        cycle_len = squ_len
        order += [n+cycle_len for n in order]
        print("recur",order)

        # check whether in a cycle, a point is used twice
        start_i = 2
        final_node_i = 7
        if final_node_i - len_n <= start_i :
            print("didn't use the same node")
        else :
            print("use the same node, usually means invalid")
    

dist_of_2D([[0,2],[2,0],[2,2],[0,0]], 2)
dist_of_2D([[0,0],[0,1],[0,2],[1,2],[2,2],[2,1],[2,0],[1,0]], 2)
dist_of_2D([[0,50],[66,36],[0,9],[5,0],[46,66],[66,23],[0,36]], 66)