import Node
import KruskalFunction

def Kruskal (ListMentor, MAX, traffic_matric, w_kk):
    
    list_connect_weigh = []

    for tree in ListMentor:
        list_connect_weigh = []
        for i in range(len(tree)):
            for j in range(i + 1, len(tree)):
                node_i = tree[i].get_name() - 1
                node_j = tree[j].get_name() - 1
                connect_weight = traffic_matric[node_i][node_j]
                list_connect_weigh.append(connect_weight)
        list_connect_weigh = sorted(set(
            w for w in list_connect_weigh if w != 0
        ))
        
        for i in range(len(tree)):
            if(len(list_connect_weigh) > 0 ):
                current_traffic_weight = list_connect_weigh[0]
                for j in range(i+1, len(tree)):
                    
                    node_i = tree[i].get_name() - 1
                    node_j = tree[j].get_name() - 1
                    connect_weight = traffic_matric[node_i][node_j]
                    current_weight_total = tree[i].get_weight_kk() + tree[j].get_weight_kk() 
                    print("current_weight_total", current_weight_total)

                    if (connect_weight == 0 & current_weight_total > w_kk):
                        continue
                    elif (connect_weight == current_traffic_weight):
                        check1 = tree[i].check_connect(tree[j].get_name())
                        check2 = KruskalFunction.check_circle_node(tree[i], tree[j])
                        if(check1 == False & check2 == True):
                            print("ok")
                            add_node_1 = tree[j].get_name() 
                            add_node_2 = tree[i].get_name()
                            tree[i].set_connect(add_node_1)
                            tree[j].set_connect(add_node_2)
                    current_traffic_weight = current_traffic_weight + 1
                    if(current_traffic_weight > 38):
                        break
        Node.matplot_esau_william(tree, MAX)
        Node.plt.show()
    return ListMentor


        