import math
import matplotlib.pyplot as plt
import Node
import EsauWiliamFunction

num_inf = math.inf
num_ninf = -math.inf

def Esau_William(ListMentor,w_ew,MAX,Limit,DeBug):

    print("{:*<100}".format(''))
    print("Bước 3: Thuật toán Esau William tìm cây truy nhập")
    if DeBug:
        print("Giới hạn trọng số W = {:<3}".format(w_ew))
        print("{:*<100}".format(''))

    for ListPosition in ListMentor:
        if DeBug:
            print("\nTìm cây truy nhập cho nút Backbone {:<3}\n".format(ListPosition[0].get_name()))

        NumNode = len(ListPosition)
        if DeBug:
            print("Số nút đầu cuối: {:<3}\n".format(NumNode-1))
            for i in ListPosition:
                print(i.get_name(), end=' ')
            print()

        # Xây dựng ma trận giá
        if DeBug:
            print("Xây dựng ma trận giá thành liên kết giữa các nút:\n")
        link_cost = [[num_inf] * NumNode for i in range(NumNode)]

        EsauWiliamFunction.link_cost_by_distance(ListPosition, link_cost)

        # Cập nhật giá về nút trung tâm ban đầu
        for i in range(1, len(ListPosition)):
            ListPosition[i].set_cost_to_center(link_cost[0][i])

        # Dựng ma trận quản lý trọng số
        weightGroup = []

        # Khởi tạo weightGroup
        if DeBug:
            for i in weightGroup:
                for j in range(0, len(i)):
                    print(i[j], end=' ')
                print()

        # Cập nhật hàm thỏa hiệp lần đầu
        for i in range(1, len(ListPosition)):
            ListPosition[i].set_connect(ListPosition[0].get_name())
            ListPosition[0].set_connect(ListPosition[i].get_name())

        if DeBug:
            print("Node list to backbone:", ListPosition[0].get_list_connect())

        EsauWiliamFunction.cap_nhat_thoa_hiep(ListPosition, link_cost, weightGroup, num_inf, ListPosition)

        if DeBug:
            print("{:-<100}".format(''))

            print("Cập nhật thỏa hiệp lần đầu")

        '''

                Vòng lặp cập nhật thỏa hiệp

        '''

        if DeBug:
            print(ListPosition[0].get_list_connect())

            print("------ Vào vòng lặp cập nhật thỏa hiệp ----------")

        ew_loop = 1
        while EsauWiliamFunction.check_neg_thoa_hiep(ListPosition):
            if DeBug:
                print("Vòng lặp lần", ew_loop)
            ew_loop = ew_loop + 1
            # Tìm thỏa hiệp âm nhất
            min_thoa_hiep_index = 0
            min_thoa_hiep = 0
            for i in range(1, len(ListPosition)):
                if ListPosition[i].get_thoahiep() < min_thoa_hiep:
                    min_thoa_hiep = ListPosition[i].get_thoahiep()
                    min_thoa_hiep_index = i

            minthoahiep_node = ListPosition[min_thoa_hiep_index]
            minthoahiep_next_connect_index = EsauWiliamFunction.find_index_node(minthoahiep_node.get_next_connect(), ListPosition)
            minthoahiep_next_connect_node = ListPosition[minthoahiep_next_connect_index]

            if DeBug:
                print("Thỏa hiệp âm nhất tại nút", minthoahiep_node.get_name(), "bằng",
                    minthoahiep_node.get_thoahiep())

            # Kiểm tra điều kiện tổng trọng số

            if EsauWiliamFunction.check_limit_size(minthoahiep_next_connect_node.get_name(), minthoahiep_node.get_name(), Limit, ListPosition):

                if EsauWiliamFunction.check_limit_weight(minthoahiep_next_connect_node.get_name(), minthoahiep_node.get_name(), ListPosition) <= w_ew:
                    if DeBug:
                        print("Thỏa hiệp tại nút", minthoahiep_node.get_name(), "chấp nhận được. Ghép liên kết",
                          minthoahiep_node.get_name(),
                          minthoahiep_next_connect_node.get_name())

                    # Cập nhật tổng trọng số của nhánh và node nối trung tâm của nhánh
                    ListPosition[EsauWiliamFunction.find_index_node(minthoahiep_node.get_group_node_to_center(), ListPosition)].remove_connect(ListPosition[0].get_name())

                    minthoahiep_node.set_connect(minthoahiep_next_connect_node.get_name())
                    minthoahiep_next_connect_node.set_connect(minthoahiep_node.get_name())

                    EsauWiliamFunction.updateWG(minthoahiep_next_connect_node.get_name(),minthoahiep_node.get_name(), ListPosition, weightGroup, DeBug)

                else:
                    if DeBug:
                        print("Thỏa hiệp tại nút", minthoahiep_node.get_name(), "không chấp nhận được.",
                              EsauWiliamFunction.check_limit_weight(minthoahiep_next_connect_node.get_name(), minthoahiep_node.get_name(), ListPosition),
                              ">", w_ew,
                              "Bỏ liên kết",
                              minthoahiep_node.get_name(),
                              minthoahiep_next_connect_node.get_name())
                    EsauWiliamFunction.set_linkcost(link_cost, EsauWiliamFunction.find_index_node(minthoahiep_node.get_name(), ListPosition),
                                 EsauWiliamFunction.find_index_node(minthoahiep_next_connect_node.get_name(), ListPosition), num_inf)

            else:
                if DeBug:
                    print("Thỏa hiệp tại nút", minthoahiep_node.get_name(), "không chấp nhận được. Điều kiện giới hạn số nút trên cây không được thỏa mãn")
                EsauWiliamFunction.set_linkcost(link_cost,EsauWiliamFunction.find_index_node(minthoahiep_node.get_name(), ListPosition),EsauWiliamFunction.find_index_node(minthoahiep_next_connect_node.get_name(), ListPosition),num_inf)

            # Cập nhật thỏa hiệp
            if DeBug:
                print("Cập nhật thỏa hiệp")
            EsauWiliamFunction.cap_nhat_thoa_hiep(ListPosition, link_cost, weightGroup, num_inf, ListPosition)
            if DeBug:
                Node.printEWList(ListPosition)
            if DeBug:
                for i in weightGroup:
                    for j in i:
                        print(j, end=' ')
                    print()
        print("Các cây của nút backbone",ListPosition[0].get_name()," :")
        for i in weightGroup:
            print(i)
        Node.matplot_esau_william(ListPosition, MAX)
        Node.plt.show()

    return ListMentor

