import Node
import KruskalFunction
import math

num_inf = math.inf
num_ninf = -math.inf

def Kruskal (ListMentor, MAX, traffic_matric, w_kk, DeBug):
        
    for ListPosition in ListMentor:

        NumNode = len(ListPosition)

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

                    check_circle = KruskalFunction.check_circle_node(ListPosition[i], ListPosition[j], ListPosition)

                    if(link_cost[i][j] == link_cost_member and check_circle):

                        if DeBug:
                            print("")

                        ListPosition[i].set_connect(ListPosition[j].get_name() )
                        ListPosition[j].set_connect(ListPosition[i].get_name() )

        Node.matplot_krukal(ListPosition, MAX)
        Node.plt.show()

    return ListMentor


        