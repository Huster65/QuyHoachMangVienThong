# -*- coding: utf-8 -*-
import Node
import InitialTopo
import MENTOR
import EsauWilliam
import Kruskal
import KruskalFunction
import sys
sys.stdout.reconfigure(encoding='utf-8')

MAX = 1000

NumNode = 80

RadiusRatio = 0.3 
C = 12 
w = 2 
w_ew = 12 
w_kk = 12
debug = False

traffic_matric = KruskalFunction.initMatricTraffic()

ListPosition = InitialTopo.Global_Init_Topo(MAX, NumNode, debug)

ListMentor = MENTOR.MenTor(ListPosition,MAX,C,w,RadiusRatio,0, debug)

ListFinish = EsauWilliam.Esau_William(ListMentor,w_ew,MAX,0, debug)

#ListFinish = Kruskal.Kruskal(ListMentor, MAX, traffic_matric, w_kk, debug)

# print("mentor list")
# Node.printMentorList(ListFinish)

Node.printList2D(ListFinish)
Node.matplot_total(ListFinish,MAX)
Node.plt.show()
