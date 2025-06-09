import math

def print_linkcostmatrix(_link_cost):
    for i in range(len(_link_cost)):
        for j in range(len(_link_cost[i])):
            print("{:<8}".format(_link_cost[i][j]), end='\t')
        print()


def set_linkcost(_link, i, j, c):
    _link[i][j] = c
    _link[j][i] = c

# Xây dựng hàm cập nhật giá theo distance (cost = distance)

def calc_distance_2Dpoint(a, b):
    return round(math.sqrt(
        (a.get_position_x() - b.get_position_x()) ** 2 + (a.get_position_y() - b.get_position_y()) ** 2), 4)

def link_cost_by_distance(_list, _link_cost):
    for i in range(len(_list)):
        for j in range(i + 1, (len(_list))):
            set_linkcost(_link_cost, i, j, calc_distance_2Dpoint(_list[i], _list[j]))

# Định nghĩa hàm tìm index của node khi biết tên node
def find_index_node(m, ListPosition):
    for i in range(0, len(ListPosition)):
        if ListPosition[i].get_name() == m:
            return i
    return 0

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

def check_limit_weight(next_connect, oneself, ListPosition):
    node_next_connect = ListPosition[find_index_node(next_connect, ListPosition)]
    node_oneself = ListPosition[find_index_node(oneself, ListPosition)]
    sum = node_next_connect.get_weight_of_group() + node_oneself.get_weight_of_group()
    return sum

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
        
# Định nghĩa hàm cập nhật thỏa hiệp
def cap_nhat_thoa_hiep(_list, _link_cost, weightGroup, num_inf, ListPosition):
    def find_list(m_child,m_check):
        for i in weightGroup:
            for j in i:
                if j == m_child:
                    for k in i:
                        if k == m_check:
                            return True
                    return False

    for i in range(1, len(_list)):
        if _list[i].get_thoahiep() < 0:
            min_th = num_inf
            for j in range(1, len(_list)):
                if find_list(_list[i].get_name(),_list[j].get_name()):
                    continue

                subt = round(_link_cost[j][i] - _list[i].get_cost_to_center(), 4)
                if subt < min_th:
                    min_th = subt
                    _list[i].set_next_connect(ListPosition[j].get_name())
            _list[i].set_thoahiep(min_th)

# Định nghĩa hàm kiểm tra thỏa hiệp âm
def check_neg_thoa_hiep(_list):
    for i in range(1, len(_list)):
        if _list[i].get_thoahiep() < 0:
            return True
    return False