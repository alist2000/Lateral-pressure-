from input import input_values
from surchargeLoad import surcharge
import scipy.integrate as spi
from plot import plotter2
from output import output, output_noSolution

import numpy as np
import json

max_load_number = 4  # In site I will define a specific number of load. it can be changed.


def surcharge_calculator(input_values):
    product_id = input_values.get("product_id")
    user_id = input_values.get("user_id")
    unit_system = input_values.get("information").get("unit")
    h = input_values.get("data").get("Load Properties").get("H").get("value")
    delta_h = input_values.get("data").get("Load Properties").get("Δh").get("value")
    surchargeInstance = surcharge(unit_system, h, delta_h)
    depth_list = surchargeInstance.depth_list
    depth_array = np.array(depth_list)
    solution = []
    load_type = []
    plots = []

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
        load_type_dict = json.loads(
            input_values.get("data").get("Load Properties").get("Load Type" + i * spaceNum).get("value")).get("item")
        load_type.append(load_type_dict)
        if load_type[i] == "Point Load":
            pl_q.append(
                abs(float(input_values.get("data").get("Load Properties").get("q" + i * spaceNum).get("value"))))
            if pl_q[i_pl] != 0:
                pl_l.append(input_values.get("data").get("Load Properties").get("L1" + i * spaceNum).get("value"))
                pl_teta.append(input_values.get("data").get("Load Properties").get("Ɵ" + i * spaceNum).get("value"))
                point_load = surchargeInstance.point_load(pl_q[i_pl], pl_l[i_pl], pl_teta[i_pl])
                plots.append(point_load[3])  # plot index = 3
                solution_pl.append(point_load)
                i_pl += 1
            else:  # it's like there is no load!
                del pl_q[i_pl]
        elif load_type[i] == "Line Load":
            ll_q.append(
                abs(float(input_values.get("data").get("Load Properties").get("q" + i * spaceNum).get("value"))))
            if ll_q[i_ll] != 0:
                ll_l.append(input_values.get("data").get("Load Properties").get("L1" + i * spaceNum).get("value"))
                line_load = surchargeInstance.line_load(ll_q[i_ll], ll_l[i_ll])
                plots.append(line_load[3])  # plot index = 3
                solution_ll.append(line_load)
                i_ll += 1
            else:  # it's like there is no load!
                del ll_q[i_ll]
        elif load_type[i] == "Strip Load":
            sl_q.append(
                abs(float(input_values.get("data").get("Load Properties").get("q" + i * spaceNum).get("value"))))
            if sl_q[i_sl] != 0:
                sl_l1.append(input_values.get("data").get("Load Properties").get("L1" + i * spaceNum).get("value"))
                sl_l2.append(input_values.get("data").get("Load Properties").get("L2" + i * spaceNum).get("value"))
                strip_load = surchargeInstance.strip_load(sl_q[i_sl], sl_l1[i_sl], sl_l2[i_sl])
                plots.append(strip_load[3])  # plot index = 3
                solution_sl.append(strip_load)
                i_sl += 1
            else:
                del sl_q[i_sl]
        else:
            pass  # no load

    solution.append(solution_pl)
    solution.append(solution_ll)
    solution.append(solution_sl)

    # Check for errors
    for load_type in solution:
        for load in load_type:
            for status in load[4]:
                if status != "No error":
                    Output = output_noSolution(product_id, user_id, load[4])
                    return Output

    """ to drawing final sigma h - z plot we should sum all sigma h array of every load.
        for this result I create an array with length equal to length of sigma h array
         of every solution ( index number 2 of every solution ( solution pl or ll or sl )
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
    # surchargeInstance.total_plotter(lateral_pressure, centroid, sum_sigma_h)
    result_plot = plotter2(unit_system, h, sum_sigma_h, depth_list, lateral_pressure, centroid)
    plots.append(result_plot)
    Output = output(product_id, user_id, solution, sum_sigma_h, depth_array, lateral_pressure, centroid, unit_system,
                    plots)
    return Output


final_output = surcharge_calculator(input_values)
print(final_output)
