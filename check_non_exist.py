def check_non_exist(index,listbackbone,listmentor, DEBUG_UpdateTerminalNode):
            if DEBUG_UpdateTerminalNode:
                for i in listbackbone:
                    print(i.get_name(),end =' ')
                print()
                for i in listmentor:
                    for j in i:
                        print(j.get_name(), end=' ')
                print()
            for i in listbackbone:
                if i.get_name() == index:
                    if DEBUG_UpdateTerminalNode:
                        print("in list backbone. no check any more")
                    return False
            for i in listmentor:
                for j in i:
                    if j.get_name() == index:
                        if DEBUG_UpdateTerminalNode:
                            print("in list mentor. no check any more")
                        return False
            return True