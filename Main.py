# -*- coding: utf-8 -*-
import Node
import InitialTopo
import MENTOR
import EsauWilliam
import sys
sys.stdout.reconfigure(encoding='utf-8')

#MAX = 1200 # MAX là thông số độ dài cạnh của mặt phẳng hình vuông kích thước MAX*MAX, nơi các nút được đặt lên.
MAX = 1000
#NumNode = 100 # Số lượng nút trong mạng
NumNode = 80
#RadiusRatio = 0.35
RadiusRatio = 0.3 # Tỉ lệ dùng để tính bán kính quét mạng truy nhập của thuật toán MENTOR
C = 12 # Dung lượng 1 liên kết
w = 2  # Trọng số lưu lượng chuẩn hóa dùng để xét nút backbone của thuật toán MENTOR
w_ew = 8 # Trọng số ngưỡng của các nhóm trong cây truy nhập của thuật toán Esau Williams
debug = False

ListPosition = InitialTopo.Global_Init_Topo(MAX, NumNode, debug)
#ListPosition = InitialTopo.Global_Init_Topo_Fix_Position(MAX,NumNode,False)
# False/ True: Nếu chọn True, toàn bộ các bước trong tạo topology mạng sẽ được giám sát và hiển thị

ListMentor = MENTOR.MenTor(ListPosition,MAX,C,w,RadiusRatio,0, debug)
# 5: Là số giới hạn nút đầu cuối của thuật toán MENTOR.
# Khi một nút Backbone tìm thấy số lượng nút đầu cuối đạt của một mạng truy nhập tới giới hạn. Nó ngừng việc quét tìm nút đầu cuối. Nếu cài đặt giá trị này bằng 0 thì xem như không có giới hạn số lượng nút đầu cuối.
# False/ True: Bật tắt giám sát thuật toán

ListFinish = EsauWilliam.Esau_William(ListMentor,w_ew,MAX,5, debug)
# False/ True: Bật tắt giám sát thuật toán
# 5: Giới hạn số nút trên cây truy nhập. Nếu đặt bằng 0 thì không giới hạn.

Node.printList2D(ListFinish)
Node.matplot_total(ListFinish,MAX)
Node.plt.show()
