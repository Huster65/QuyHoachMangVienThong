import Node
import KruskalFunction
import math
import EsauWiliamFunction

num_inf = math.inf
num_ninf = -math.inf

def Kruskal (ListMentor, MAX, traffic_matric, w_kk,Limit, DeBug):
        
    for ListPosition in ListMentor:
        backbone = ListPosition[0]

        NumNode = len(ListPosition)
        weightGroup = []
        if DeBug:
            print("Xây dựng ma trận giá thành liên kết giữa các nút:\n")

        link_cost = [[num_inf] * NumNode for i in range(NumNode)]

        if DeBug:
            print("Ma trận link cost")
            print(link_cost)

        KruskalFunction.link_cost_by_distance(ListPosition, link_cost)

        flat_sorted_link_cost = sorted([
            cost
            for row in link_cost
            for cost in row
            if cost != num_inf and cost != 0
        ])

        unique_sorted_cost = []
        previous = None

        for cost in flat_sorted_link_cost:
            if cost != previous:
                unique_sorted_cost.append(cost)
                previous = cost

        if DeBug:
            print("Ma trận sắp xếp giá liên kết ")
            print(flat_sorted_link_cost)

        for link_cost_member in unique_sorted_cost:

            for i in range(NumNode):

                for j in range(NumNode):

                    ListPosition[0].set_weight_of_group(0)

                    check_circle = KruskalFunction.check_circle_node(ListPosition[i], ListPosition[j], ListPosition, w_kk)
                    check_limit_weight = KruskalFunction.check_limit_weight(ListPosition[i], ListPosition[j], ListPosition, w_kk)
                    print("check_limit_weight", check_limit_weight)
                    if(link_cost[i][j] == link_cost_member):
                        if(check_circle):
                            if KruskalFunction.check_limit_size(ListPosition[i].get_name(), ListPosition[j].get_name(), Limit, ListPosition):
                                if KruskalFunction.check_limit_weight(ListPosition[i].get_name(), ListPosition[j].get_name(), ListPosition, w_kk):
                                    
                                    ListPosition[i].set_connect(ListPosition[j].get_name() )
                                    ListPosition[j].set_connect(ListPosition[i].get_name() )
                                    KruskalFunction.updateWG(ListPosition[i].get_name(),ListPosition[j].get_name(), ListPosition, weightGroup, DeBug)
        print("kruskal", ListPosition)
        Node.matplot_krukal(ListPosition, MAX)
        Node.plt.show()

    return ListMentor


        