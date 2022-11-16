from input import input_values
from surchargeLoad import surcharge
import scipy.integrate as spi

import numpy as np

max_load_number = 9  # In site I will define a specific number of load. it can be changed.


def surcharge_calculator(input_values):
    unit_system = input_values.get("unit system")
    h = input_values.get("general information").get("h")
    delta_h = input_values.get("general information").get("delta h")
    surchargeInstance = surcharge(h, delta_h)
    depth_list = surchargeInstance.depth_list
    depth_array = np.array(depth_list)
    solution = []
    load_type = []

    # pl --> point load
    pl_q = []
    pl_l = []
    pl_teta = []
    solution_pl = []
    # ll --> line load
    ll_q = []
    ll_l = []
    solution_ll = []
    # sl --> strip load
    sl_q = []
    sl_l1 = []
    sl_l2 = []
    solution_sl = []
    spaceNum = " "
    i_pl = 0
    i_ll = 0
    i_sl = 0
    for i in range(max_load_number):
        load_type.append(input_values.get("general information").get("Load Type" + i * spaceNum))
        if load_type[i] == "Point Load":
            pl_q.append(input_values.get("general information").get("q" + i * spaceNum))
            pl_l.append(input_values.get("general information").get("l1" + i * spaceNum))
            pl_teta.append(input_values.get("general information").get("teta" + i * spaceNum))
            solution_pl.append(surchargeInstance.point_load(pl_q[i_pl], pl_l[i_pl], pl_teta[i_pl]))
            i_pl += 1
        elif load_type[i] == "Line Load":
            ll_q.append(input_values.get("general information").get("q" + i * spaceNum))
            ll_l.append(input_values.get("general information").get("l1" + i * spaceNum))
            print(ll_q)
            print(ll_l)
            solution_ll.append(surchargeInstance.line_load(ll_q[i_ll], ll_l[i_ll]))
            i_ll += 1
        elif load_type[i] == "Strip Load":
            sl_q.append(input_values.get("general information").get("q" + i * spaceNum))
            sl_l1.append(input_values.get("general information").get("l1" + i * spaceNum))
            sl_l2.append(input_values.get("general information").get("l2" + i * spaceNum))
            solution_sl.append(surchargeInstance.strip_load(sl_q[i_sl], sl_l1[i_sl], sl_l2[i_sl]))
            i_sl += 1
            i_sl

        else:
            pass  # no load

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
    otitle = ["lateral pressure calculator - Output Summary",
              "Final Solution Alternatives"]
    header1 = [4, "lateral pressure"]
    if unit_system == "us":
        length_unit = "ft"
        pressure_unit = "psf"
    else:
        length_unit = "m"
        pressure_unit = "Pa"
    units = [length_unit, pressure_unit]

    header2 = ["Z", "Ϭh", "Z bar", "P"]
    values = [["load 1"], ["load 2 "]]


    output = []
    return output

output = surcharge_calculator(input_values)
