import random
import math
import matplotlib.pyplot as plt
import Node
import updateTerminalNode

num_inf = math.inf
num_ninf = -math.inf


def MenTor(ListPosition,MAX,C,w,RadiusRatio,Limit,DeBug):
    ListMentor = []
    '''

    Bước 2: Tìm Nút Backbone và phân cây truy nhập dựa trên thuật toán MENTOR

    '''
    print("{:*<100}".format(''))
    print("Bước 2: Tìm Nút Backbone và phân cây truy nhập dựa trên thuật toán MENTOR")
    print("{:*<100}".format(''))

    ListBackboneType1 = []

    for i in ListPosition:
        if i.get_traffic() / C > w:
            # i.print()
            ListBackboneType1.append(i)
            ListPosition.remove(i)

    if DeBug:
        print("2.1. List Backbone do lưu lượng chuẩn hóa lớn hơn ngưỡng")
        Node.printMentorList(ListBackboneType1)


    # Tìm MaxCost
    if DeBug:
        print("Tìm MaxCost và R*MaxCost")
    MaxCost = 0
    for i in range(len(ListPosition)):
        for j in range(i + 1, len(ListPosition)):
            dc = math.sqrt((ListPosition[i].get_position_x() - ListPosition[j].get_position_x()) ** 2 + (
                    ListPosition[i].get_position_y() - ListPosition[j].get_position_y()) ** 2)
            if dc > MaxCost:
                #print(ListPosition[i].get_name(), ListPosition[j].get_name(), dc)
                MaxCost = dc

    RM = RadiusRatio * MaxCost
    if DeBug:
        print('MaxCost = {:<8} & R*MaxCost = {:<8}'.format(round(MaxCost,3), round(RM,3)))

    # Dựng hàm cập nhật các nút đầu cuối cho các nút backbone

    DEBUG_UpdateTerminalNode = 0

    
    for i in ListBackboneType1:
        updateTerminalNode.updateTerminalNode(ListPosition, ListMentor, i, DEBUG_UpdateTerminalNode, RM, Limit)

    del ListBackboneType1
    if DeBug:
        print("-----------Danh sách các nút Backbone và cây truy nhập đi kèm sau khi tìm Backbone dựa trên ngưỡng lưu lượng -----------")

        Node.printList2D(ListMentor)

        print("-----------Dach sách các nút còn lại chưa được phân cây truy nhập-----------")

        Node.printMentorList(ListPosition)


    '''

    Bước 3: Đối với các nút còn lại, tiến hành tìm nút backbone dựa trên giá trị thưởng, sau đó cập nhật các nút đầu cuối

    '''
    if DeBug:
        print()
        print(
        "2.2. Đối với các nút còn lại, tiến hành tìm nút Backbone dựa trên giá trị thưởng, sau đó cập nhật cây truy nhập tương ứng với nút Backbone mới")
        
    center = Node.Node()
    iloop = 1
    while len(ListPosition) > 0:
        if DeBug:
            print("Vòng lặp tìm giá trị thưởng lần", iloop)
        iloop = iloop + 1
        # Tìm trung tâm trọng lực
        sumx = 0
        sumy = 0
        sumw = 0
        xtt = 0
        ytt = 0
        maxw = 1
        maxdc = 1
        maxaward = 0
        indexBB = 0

        for i in ListPosition:
            sumx = sumx + (i.get_position_x()) * i.get_traffic()
            sumy = sumy + (i.get_position_y()) * i.get_traffic()
            sumw = sumw + i.get_traffic()
            if i.get_traffic() > maxw:
                maxw = i.get_traffic()
        xtt = sumx / sumw
        ytt = sumy / sumw

        center.set_position(xtt, ytt)

        if DeBug:
            center.printCenterPress()

        for i in ListPosition:
            i.set_distance(center)
            if i.get_distance() > maxdc:
                maxdc = i.get_distance()
        if DeBug:
            print("MaxDistance = {:<6} & Max Weight: {:<3}".format(round(maxdc,2), maxw))
        for i in ListPosition:
            i.set_award((0.5 * (maxdc - i.get_distance() / maxdc)) + (0.5 * i.get_traffic() / maxw))
            if i.get_award() > maxaward:
                maxaward = i.get_award()

        for i in ListPosition:
            if i.get_award() >= maxaward:
                e = Node.Node()
                e.copyNode(i)
                if DeBug:
                    print("Nút Thưởng được chọn làm backbone: {:<3}".format(e.get_name()))
                ListPosition.remove(i)
                if DeBug:
                    print("--- Danh sách các nút còn lại sau khi bỏ nút backbone ---")
                    Node.printMentorList(ListPosition)
                if DeBug:
                    print("---------------------")
                if DeBug:
                    print("Cập nhật cây truy nhập cho nút backbone mới")
                updateTerminalNode.updateTerminalNode(ListPosition, ListMentor, e, DEBUG_UpdateTerminalNode, RM, Limit)
                if DeBug:
                    print("---------------------")
                    print("--- Danh sách các nút còn lại sau khi cập nhật cây truy nhập cho nút backbone mới ---")
                    Node.printMentorList(ListPosition)
                    print("---------------------")
                break

    '''

    Kết thúc thuật toán, hiển thị kết quả

    '''

    if DeBug:
        print("-------Kết quả thuật toán Mentor-------")

        for i in ListMentor:
            for j in i:
                print(j.get_name(), end=' ')
            print()

    Node.matplot_mentor(ListMentor,MAX)
    Node.plt.show()
    return ListMentor