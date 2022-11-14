from input import input_values
from surchargeLoad import surcharge
import scipy.integrate as spi

import numpy as np

h = input_values.get("general information").get("h")
delta_h = input_values.get("general information").get("delta h")
surchargeInstance = surcharge(h, delta_h)
depth_list = surchargeInstance.depth_list
depth_array = np.array(depth_list)
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

""" for plot final sigma h - h plot we should sum all sigma h array of every load.
    for this result I create an array with length equal to length of sigma h array
     of every solution ( index number 3 of every solution ( solution pl or ll or sl )
      is sigma_h_array and all of them have same shape. ).
    and 0 value.then I write a loop to sum sigma h array of every load with first 
    sigma_h_array ( sum_sigma_h that has 0 value ).
    now we can plot our final result and calculate centroid."""
for i in solution:
    try:
        sum_sigma_h = np.array([0. for i in range(len(i[0][2]))])
        break
    except:
        continue

for load_type in range(len(solution)):
    for load in range(len(solution[load_type])):
        sum_sigma_h += solution[load_type][load][2]


# calculate total centroid. there are two method.

# number one
# lateral_pressure1 = 0
# lateral_multiple_centroid = 0
# for item in solution:
#     for solve in item:
#         if solve[3][0] == "No error":
#             lateral_pressure1 += solve[0]
#             lateral_multiple_centroid += solve[0] * solve[1]
# centroid1 = lateral_multiple_centroid / lateral_pressure1
# print(lateral_pressure1)
# print(centroid1)

# number two
lateral_pressure = spi.simpson(sum_sigma_h, depth_array)
centroid = spi.simpson(sum_sigma_h * depth_array, depth_array) / lateral_pressure
print(lateral_pressure)
print(sum_sigma_h)
print(centroid)
surchargeInstance.total_plotter(lateral_pressure, centroid, sum_sigma_h)
