import check_non_exist

def updateTerminalNode(_ListPosition, _ListMentor, _centerNode, DEBUG_UpdateTerminalNode, RM, Limit):

        if DEBUG_UpdateTerminalNode:
            print("Enter Update Terminal Node Function! ")
            print("Node backbone", _centerNode.get_name())

        # Kiểm tra khoảng cách các node so với node backbone
        ListBackbone = []
        ListBackbone.append(_centerNode)

        #Node.printList(_ListPosition)
        for i in _ListPosition:
            # set_distance tinh khoang cach nut i den nut center
            i.set_distance(_centerNode)
            if DEBUG_UpdateTerminalNode:
                print("Check Distance Node", i.get_name(), " : ", i.get_distance())
            if check_non_exist.check_non_exist(i.get_name(),ListBackbone,_ListMentor, DEBUG_UpdateTerminalNode):
                if i.get_distance() <= RM:
                    if DEBUG_UpdateTerminalNode:
                        print("Node", i.get_name(), "is terminal node of Node center", _centerNode.get_name())
                    ListBackbone.append(i)

        # Xử lý giới hạn số nút đầu cuối của nút backbone

        def sort_by_distance_to_backbone(m):
            return  m.get_distance()

        ListBackbone.sort(key=sort_by_distance_to_backbone)

        if Limit > 0:
            if DEBUG_UpdateTerminalNode:
                for i in ListBackbone:
                    print(i.get_name(),end =' ')
                print()
            if len(ListBackbone)-1 > Limit:
                ListBackbone = ListBackbone[0:Limit+1]
            if DEBUG_UpdateTerminalNode:
                for i in ListBackbone:
                    print(i.get_name(),end =' ')
                print()



        _ListMentor.append(ListBackbone)

        for i in ListBackbone:
            for j in _ListPosition:
                if i.get_name() == j.get_name():
                    _ListPosition.remove(j)

        if DEBUG_UpdateTerminalNode:
            print("Exit Update Terminal Node Function! ")