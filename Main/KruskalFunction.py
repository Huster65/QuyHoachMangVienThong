import Node

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

def check_circle_node(node1, node2):
    list_connect_node1 = node1.get_list_connect()
    list_connect_node2 = node2.get_list_connect()
    for i in range(len(list_connect_node1)):
        for j in range(len(list_connect_node2)):
            if(list_connect_node1[i] == list_connect_node2[j]):
                return False
    return True