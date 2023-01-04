import scipy.integrate as spi
import numpy as np

"""result function for use all inputs and calculate 
sum of all surcharges.this function used for soldier pile
 but can be used in main surcharge function also.
"""


def result_surcharge(surchargeInstance, load_type, q, l1, l2, teta, k=1):
    """load type, q, l1, l2, teta are list"""
    depth_list = surchargeInstance.depth_list
    depth_array = np.array(depth_list)

    solution = []
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
    i_pl = 0
    i_ll = 0
    i_sl = 0

    # un --> uniform load
    un_q = []
    solution_un = []
    i_un = 0

    for i in range(len(load_type)):
        if load_type[i] == "Point Load":
            q_new = k * q[i]
            pl_q.append(q_new)
            if q[i] != 0:
                pl_l.append(l1[i])
                pl_teta.append(teta[i])
                point_load = surchargeInstance.point_load(pl_q[i_pl], pl_l[i_pl], pl_teta[i_pl])
                plots.append(point_load[3])  # plot index = 3
                solution_pl.append(point_load)
                i_pl += 1


            else:  # it's like there is no load!
                del pl_q[i_pl]
        elif load_type[i] == "Line Load":
            q_new = k * q[i]
            ll_q.append(q_new)
            if q[i] != 0:
                ll_l.append(l1[i])
                line_load = surchargeInstance.line_load(ll_q[i_ll], ll_l[i_ll])
                plots.append(line_load[3])  # plot index = 3
                solution_ll.append(line_load)
                i_ll += 1

            else:  # it's like there is no load!
                del ll_q[i_ll]
        elif load_type[i] == "Strip Load":
            q_new = k * q[i]
            sl_q.append(q_new)
            if sl_q[i_sl] != 0:
                sl_l1.append(l1[i])
                sl_l2.append(l2[i])
                strip_load = surchargeInstance.strip_load(sl_q[i_sl], sl_l1[i_sl], sl_l2[i_sl])
                plots.append(strip_load[3])  # plot index = 3
                solution_sl.append(strip_load)
                i_sl += 1

            else:
                del sl_q[i_sl]
        elif load_type[i] == "Uniform":  # uniform
            q_new = k * q[i]
            un_q.append(q_new)
            uniform_load = surchargeInstance.uniform(un_q[i_sl])
            plots.append(uniform_load[3])  # plot index = 3
            solution_un.append(uniform_load)
            i_un += 1


        else:
            pass  # no load!

    solution.append(solution_pl)
    solution.append(solution_ll)
    solution.append(solution_sl)
    solution.append(solution_un)
    for i in solution:
        try:
            sum_sigma_h = np.array([0. for i in range(len(i[0][2]))])
            break
        except:
            continue
    for Load_type in range(len(solution)):
        for load in range(len(solution[Load_type])):
            sum_sigma_h += solution[Load_type][load][2]

    lateral_pressure = spi.simpson(sum_sigma_h, depth_array)
    centroid = spi.simpson(sum_sigma_h * depth_array, depth_array) / lateral_pressure

    return lateral_pressure, centroid, sum_sigma_h
