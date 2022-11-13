from input import input_values
from surchargeLoad import surcharge

import numpy as np

h = input_values.get("general information").get("h")
delta_h = input_values.get("general information").get("delta h")
surchargeInstance = surcharge(h, delta_h)
solution = []

# pl --> point load
pl_num = input_values.get("point load").get("number")
pl_q = []
pl_l = []
pl_teta = []
solution_pl = []
for i in range(pl_num):
    spaceNum = " "
    pl_q.append(input_values.get("point load").get("q" + i * spaceNum))
    pl_l.append(input_values.get("point load").get("l" + i * spaceNum))
    pl_teta.append(input_values.get("point load").get("teta" + i * spaceNum))
    solution_pl.append(surchargeInstance.point_load(pl_q[i], pl_l[i], pl_teta[i]))

# ll --> line load
ll_num = input_values.get("line load").get("number")
ll_q = []
ll_l = []
solution_ll = []
for i in range(ll_num):
    spaceNum = " "
    ll_q.append(input_values.get("line load").get("q" + i * spaceNum))
    ll_l.append(input_values.get("line load").get("l" + i * spaceNum))
    solution_ll.append(surchargeInstance.line_load(ll_q[i], ll_l[i]))

# sl --> strip load
sl_num = input_values.get("strip load").get("number")
sl_q = []
sl_l1 = []
sl_l2 = []
solution_sl = []
for i in range(sl_num):
    spaceNum = " "
    sl_q.append(input_values.get("strip load").get("q" + i * spaceNum))
    sl_l1.append(input_values.get("strip load").get("l1" + i * spaceNum))
    sl_l2.append(input_values.get("strip load").get("l2" + i * spaceNum))
    solution_sl.append(surchargeInstance.strip_load(sl_q[i], sl_l1[i], sl_l2[i]))

solution.append(solution_pl)
solution.append(solution_ll)
solution.append(solution_sl)
lateral_pressure = 0
lateral_multiple_centroid = 0
# sigmah_pl = [0 for i in solution_pl]
# sigmah_ll = [0 for i in solution_ll]
# sigmah_sl = [0 for i in solution_sl]
for item in solution:
    for solve in item:
        if solve[3][0] == "No error":
            lateral_pressure += solve[0]
            lateral_multiple_centroid += solve[0] * solve[1]

centroid = lateral_multiple_centroid / lateral_pressure
print(lateral_pressure)
print(centroid)
# surchargeInstance.plotter(lateral_pressure, centroid)
