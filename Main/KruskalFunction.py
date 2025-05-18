import Node
import math

def initMatricTraffic():
    NumNode = 80
    TrafficMatrix = [[0] * NumNode for i in range(NumNode)]
    def set_traffic(m, n, value):
        TrafficMatrix[m - 1][n - 1] = value
        TrafficMatrix[n - 1][m - 1] = value

    # Đưa thông tin về mối quan hệ
    def set_traffic0(m, n, value):
        TrafficMatrix[m][n] = value
        TrafficMatrix[n][m] = value

    for i in range(NumNode):

        if i + 14 < NumNode:
            set_traffic0(i, i + 14, 1)
        if i + 78 < NumNode:
            set_traffic0(i, i + 78, 2)
        if i + 38 < NumNode:
            set_traffic0(i, i + 38, 1)
        if i + 56 < NumNode:
            set_traffic0(i, i + 56, 1)

    set_traffic(10, 28, 38)
    set_traffic(32, 58, 36)
    set_traffic(58, 62, 4)
    set_traffic(48, 66, 3)
    set_traffic(18, 32, 1)
    
    return TrafficMatrix

def check_exits_connect():
    return True

# def check_circle_node(node1, node2):
#     list_connect_node1 = node1.get_list_connect()
#     list_connect_node2 = node2.get_list_connect()
#     for i in range(len(list_connect_node1)):
#         for j in range(len(list_connect_node2)):
#             if(list_connect_node1[i] == list_connect_node2[j]):
#                 return False
#     return True

def check_circle_node(node1, node2, tree, w_kk=None):
    visited = set()

    def dfs(node):
        if node.get_name() in visited:
            return
        visited.add(node.get_name())
        for neighbor_name in node.get_list_connect():
            neighbor = next(n for n in tree if n.get_name() == neighbor_name)
            dfs(neighbor)

    # DFS từ node1
    dfs(node1)

    # Nếu node2 đã nằm trong visited → tạo vòng
    if node2.get_name() in visited:
        return False

    # Nếu có ngưỡng w_kk, kiểm tra tổng traffic của nhánh node1 và node2
    if w_kk is not None:
        traffic_total = sum(
            n.get_traffic() for n in tree if n.get_name() in visited
        )
        traffic_total += node2.get_traffic()  # nếu nối vào node2

        if traffic_total > w_kk:
            return False  # không nối nếu vượt quá traffic giới hạn

    return True  # hợp lệ để nối



def calc_distance_2Dpoint(a, b):
    return round(math.sqrt(
        (a.get_position_x() - b.get_position_x()) ** 2 + (a.get_position_y() - b.get_position_y()) ** 2), 4)

def link_cost_by_distance(_list, _link_cost):
    for i in range(len(_list)):
        for j in range(i + 1, (len(_list))):
            set_linkcost(_link_cost, i, j, calc_distance_2Dpoint(_list[i], _list[j]))

def set_linkcost(_link, i, j, c):
    _link[i][j] = c
    _link[j][i] = c

def check_sum_weight_node(node1, node2, w_kk):
    weight_node_1 = node1.get_traffic()
    weight_node_2 = node2.get_traffic()
    list_connect_1 = node1.get_list_connect()
    list_connect_2 = node2.get_list_connect()
    sum1 = 0
    sum2 = 0
    for i in list_connect_1:
        sum1 = sum1 + i.get_traffic()
    for i in list_connect_2:
        sum2 = sum2 + i.get_traffic()
    sum = sum1 + sum2 + weight_node_1 + weight_node_2
    if(sum > w_kk):
        return False
    return True