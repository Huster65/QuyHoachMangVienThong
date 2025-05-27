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

def check_circle_node(node1, node2, ListPosition, w_kk=None):
    
    visited = set()

    def dfs(node):
        if node.get_name() in visited:
            return
        visited.add(node.get_name())
        for neighbor_name in node.get_list_connect():
            neighbor = next(n for n in ListPosition if n.get_name() == neighbor_name)
            dfs(neighbor)

    # DFS từ node1
    dfs(node1)

    # Nếu node2 đã nằm trong visited → tạo vòng
    if node2.get_name() in visited:
        return False

    return True  # hợp lệ để nối
def find_index_node(m, ListPosition):
    for i in range(0, len(ListPosition)):
        if ListPosition[i].get_name() == m:
            return i
    return 0

def total_weight(ListWeight):
    sum = 0 
    for i in len(ListWeight):
        sum += ListWeight.get_traffic()
    return sum


def check_limit_weight(next_connect, oneself, ListPosition, w_kk):
    if(next_connect == ListPosition[0].get_name() or oneself == ListPosition[0].get_name()):
        return True
    node_next_connect = ListPosition[find_index_node(next_connect, ListPosition)]
    node_oneself = ListPosition[find_index_node(oneself, ListPosition)]
    sum = node_next_connect.get_weight_of_group() + node_oneself.get_weight_of_group()
    if(sum <= w_kk):
        return True
    return False

# def check_limit_weight(next_connect, oneself, ListPosition, w_kk, check_weight_arr):
    
#     check_together = True
#     check_node1_in_weight_arr = False
#     check_node2_in_weight_arr = False
#     total_weight = next_connect.get_traffic() + oneself.get_traffic()
#     for i in check_weight_arr:
#         for j in len(i):
#             print("vao day roi nhe")
#             if(j == next_connect.get_name() or j == oneself.get_name()):
#                 check_together = False
#                 break
#     print("check_together", check_together)
#     print("total_weight", total_weight)
#     if(check_together == False and total_weight < w_kk):
#         check_weight_arr.append([next_connect.get_name()])
#         print("check_weight_arr", check_weight_arr[0])
#         for i in check_weight_arr:
#             for j in len(i):
#                 if(j == next_connect.get_name()):
#                     check_weight_arr[i].append(oneself.get_name())
#     for i in check_weight_arr:
#         for j in len(i):
#             if(j == next_connect.get_name()):
#                 check_node1_in_weight_arr = True
#             elif(j == oneself.get_name()):
#                 check_node2_in_weight_arr = True
#     if( check_node1_in_weight_arr and check_node2_in_weight_arr):
#         index_arr_1 = 0
#         index_arr_2 = 0
#         for i in check_weight_arr:
#             for j in check_weight_arr:
#                 if(j == next_connect.get_name()):
#                     index_arr_1 = i
#                 elif(j == oneself.get_name()):
#                     index_arr_2 = i
#         total_weight = total_weight(check_weight_arr[index_arr_1]) + total_weight(check_weight_arr[index_arr_2])
#         if(total_weight <= w_kk):
#             check_weight_arr.extend(check_weight_arr[index_arr_1], check_weight_arr[index_arr_2])
#             return True
#     if ( check_node1_in_weight_arr == True and check_node2_in_weight_arr == False):
#         index_arr_1 = 0
#         for i in check_weight_arr:
#             for j in check_weight_arr:
#                 if(j == next_connect.get_name()):
#                     index_arr_1 = i
#         total_weight = total_weight(check_weight_arr[index_arr_1]) + oneself.get_traffic()
#         if(total_weight <= w_kk):
#             check_weight_arr[index_arr_1].append(oneself.get_name())
#             return True
#     elif( check_node1_in_weight_arr == False and check_node2_in_weight_arr == True):
#         index_arr_2 = 0
#         for i in check_weight_arr:
#             for j in check_weight_arr:
#                 if(j == oneself.get_name()):
#                     index_arr_2 = i
#         total_weight = total_weight(check_weight_arr[index_arr_2]) + next_connect.get_traffic()
#         if(total_weight <= w_kk):
#             check_weight_arr[index_arr_2].append(next_connect.get_name())
#             return True
#     return False    
    
        


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

def updateWG(des, src, ListPosition, weightGroup, DeBug):
    index_des = find_index_node(des, ListPosition)
    index_src = find_index_node(src, ListPosition)
    node_des = ListPosition[index_des]
    node_src = ListPosition[index_src]
    sum_w = node_des.get_weight_of_group() + node_src.get_weight_of_group()
    sum_size = node_des.get_group_size() + node_src.get_group_size()
    node_des.set_weight_of_group(sum_w)
    node_des.set_group_size(sum_size)

    def check_node_exist(father):
        for i in weightGroup:
            for j in range(0, len(i)):
                if i[j] == father:
                    return True
        return False

    def del_node(m_father,m_child):
        for i in weightGroup:
            tmp_a = False
            tmp_b = False
            for j in i:
                if j == m_child:
                    tmp_a = True
                if j == m_father:
                    tmp_b = True
            if tmp_a and (not tmp_b):
                weightGroup.remove(i)
    # Thêm group source vào group des

    def update_node(m_father, m_child):
        index_m_child = find_index_node(m_child, ListPosition)
        index_m_father = find_index_node(m_father, ListPosition)

        #if DeBug:
            #print('Check destination group exist: ', m_father, check_node_exist(m_father))
            #print('Check source group exist: ', m_child, check_node_exist(m_child))
        if check_node_exist(m_father) == False:
            weightGroup.append([m_father])
            update_node(m_father, m_child)
        elif check_node_exist(m_child) == False:
            weightGroup.append([m_child])
            update_node(m_father, m_child)
        else:
            k = []

            for i in weightGroup:
                for j in range(0, len(i)):
                    # Thêm nút vào group mới
                    if i[j] == m_child:
                        k = i
            for i in weightGroup:
                for j in range(0, len(i)):
                    # Thêm nút vào group mới
                    if i[j] == m_father:
                        i.extend(k)
                        for a in i:
                            ListPosition[find_index_node(a, ListPosition)].set_weight_of_group(sum_w)
                            ListPosition[find_index_node(a, ListPosition)].set_group_size(sum_size)
                            ListPosition[find_index_node(a, ListPosition)].set_cost_to_center(node_des.get_cost_to_center())
                            ListPosition[find_index_node(a, ListPosition)].set_group_node_to_center(node_des.get_group_node_to_center())

    update_node(des, src)
    del_node(des,src)
    if DeBug:
        for i in weightGroup:
            for j in range(0, len(i)):
                print(i[j], end=' ')
            print()
            
def check_limit_size(next_connect,oneself, Limit, ListPosition):
    if Limit == 0:
        return True
    else:
        node_next_connect = ListPosition[find_index_node(next_connect, ListPosition)]
        node_oneself = ListPosition[find_index_node(oneself, ListPosition)]
        sum = node_next_connect.get_group_size()+node_oneself.get_group_size()
        if sum <= Limit:
            return True
        else:
            return False