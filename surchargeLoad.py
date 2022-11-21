import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt
from math import *

from plot import plotter2


class surcharge:
    def __init__(self, unit_system, h, delta_h=0.01):
        self.unit_system = unit_system
        self.h = h
        self.delta_h = delta_h

        if h > 0 and delta_h <= h:
            error = ["No error"]  # default value
        else:
            error = []
        if delta_h > h:
            error.append("Delta h can't be larger than h! Change your input!")
        if h <= 0:
            error.append("h can't be <= 0!")
        depth_list = []

        # for more accuracy and better output delta h can not be a large number
        # delta h large --> decrease length of depth list
        if delta_h > 0.1:
            delta_h = 0.1  # minimum allowable delta h

        # count number of decimals
        delta_h_decimal = str(delta_h)[::-1].find('.')
        if delta_h_decimal == -1:
            delta_h_decimal = 0
        sigma_h = []
        n = []
        depth_list = [i / pow(10, delta_h_decimal) if i / pow(10, delta_h_decimal) <= h else h
                      for i in
                      range(0, int((h + delta_h) * pow(10, delta_h_decimal)),
                            int(delta_h * pow(10, delta_h_decimal)))]
        for depth in depth_list:
            n.append(depth / h)

        self.error = error
        self.delta_h_decimal = delta_h_decimal
        self.sigma_h = sigma_h
        self.n = n
        self.depth_list = depth_list

    # plotter for every surcharge load
    def plotter(self, lateral_pressure, centroid):
        h = self.h
        sigma_h = self.sigma_h
        depth_list = self.depth_list
        print(depth_list)
        # add end point just for looking better
        depth_list.append(h)
        depth_array = np.array(depth_list)
        sigma_h.append(0)
        sigma_h_array = np.array(sigma_h)

        plt.plot(sigma_h_array, depth_array)
        plt.gca().invert_yaxis()
        plt.gca().xaxis.tick_top()
        plt.fill(sigma_h_array, depth_array, color="lightsteelblue")
        plt.arrow(x=max(sigma_h_array), y=centroid, dx=-max(sigma_h_array) + 0.7, dy=0, width=.15,
                  facecolor='firebrick', edgecolor='none')
        del sigma_h[-1]
        del depth_list[-1]
        plt.show()

    def total_plotter(self, lateral_pressure, centroid, sigma_h_array):
        h = self.h
        depth_list = self.depth_list
        # add end point just for looking better
        depth_list.append(h)
        depth_array = np.array(depth_list)
        sigma_h_array = np.append(sigma_h_array, 0)

        plt.plot(sigma_h_array, depth_array)
        plt.gca().invert_yaxis()
        plt.gca().xaxis.tick_top()
        plt.fill(sigma_h_array, depth_array, color="lightsteelblue")
        plt.arrow(x=max(sigma_h_array), y=centroid, dx=-max(sigma_h_array) + 0.7, dy=0, width=.15,
                  facecolor='firebrick', edgecolor='none')
        # del sigma_h[-1]
        # del depth_list[-1]
        plt.show()

    # point load
    def point_load(self, q, l, teta=0.):
        if self.error[0] == "No error":
            h = self.h
            sigma_h = self.sigma_h
            n = self.n
            depth_list = self.depth_list
            # convert teta from degree to radian
            teta = float(teta) * np.pi / 180

            m = l / h
            i = 0
            for depth in depth_list:
                if m <= 0.4:
                    sigma_h_i = 0.28 * q * pow(n[i], 2) / (pow(h, 2) * pow(0.16 + pow(n[i], 2), 3))
                else:
                    sigma_h_i = 1.77 * q * pow(n[i], 2) * pow(m, 2) / (pow(h, 2) * pow(pow(m, 2) + pow(n[i], 2), 3))
                if teta == 0:
                    sigma_h.append(sigma_h_i)
                else:
                    sigma_h.append(sigma_h_i * pow(cos(1.1 * teta), 2))
                i += 1
            depth_array = np.array(depth_list)
            sigma_h_array = np.array(sigma_h)
            # print(sigma_h_array)
            lateral_pressure = spi.simpson(sigma_h_array, depth_array)
            centroid = spi.simpson(sigma_h_array * depth_array, depth_array) / lateral_pressure
            # self.plotter(lateral_pressure, centroid)
            plotter2(self.unit_system, h, sigma_h, depth_list, lateral_pressure, centroid)
            sigma_h.clear()
            return lateral_pressure, centroid, sigma_h_array, self.error
        else:
            return [], [], [], self.error

    def line_load(self, q, l):
        if self.error[0] == "No error":
            h = self.h
            sigma_h = self.sigma_h
            n = self.n
            depth_list = self.depth_list

            i = 0
            m = l / h
            for depth in depth_list:
                if m <= 0.4:
                    sigma_h_i = 0.2 * q * n[i] / (h * pow(0.16 + pow(n[i], 2), 2))
                else:
                    sigma_h_i = 1.28 * q * n[i] * pow(m, 2) / (h * pow(pow(m, 2) + pow(n[i], 2), 2))
                sigma_h.append(sigma_h_i)
                i += 1
            depth_array = np.array(depth_list)
            sigma_h_array = np.array(sigma_h)
            # print(sigma_h_array)
            lateral_pressure = spi.simpson(sigma_h_array, depth_array)
            centroid = spi.simpson(sigma_h_array * depth_array, depth_array) / lateral_pressure
            plotter2(self.unit_system, h, sigma_h, depth_list, lateral_pressure, centroid)
            # self.plotter(lateral_pressure, centroid)
            sigma_h.clear()
            return lateral_pressure, centroid, sigma_h_array, self.error
        else:
            return [], [], [], self.error

    def strip_load(self, q, l1, l2):
        h = self.h
        a = l2 - l1
        if self.error[0] == "No error":
            sigma_h = self.sigma_h
            depth_list = self.depth_list

            i = 0
            alpha = []
            beta = []
            for depth in depth_list:
                try:
                    alpha.append(atan((l1 + a / 2) / depth))  # radian
                    teta1 = atan(l1 / depth)
                    teta2 = atan(l2 / depth)
                    beta.append(teta2 - teta1)
                    sigma_h.append(2 * q * (beta[i] - sin(beta[i]) * cos(2 * alpha[i])) / np.pi)
                    i += 1
                except:
                    sigma_h.append(0)
            depth_array = np.array(depth_list)
            sigma_h_array = np.array(sigma_h)
            # print(sigma_h_array)
            lateral_pressure = spi.simpson(sigma_h_array, depth_array)
            centroid = spi.simpson(sigma_h_array * depth_array, depth_array) / lateral_pressure
            plotter2(self.unit_system, h, sigma_h, depth_list, lateral_pressure, centroid)
            # self.plotter(lateral_pressure, centroid)
            sigma_h.clear()
            return lateral_pressure, centroid, sigma_h_array, self.error
        else:
            return [], [], [], self.error


example = surcharge(unit_system="us", h=10, delta_h=2)
# print(example.point_load(q=16000, l=6, teta=66.8))
# print(example.point_load(q=16000, l=6, teta=0))
# print(example.point_load(q=4000, l=6, teta=66.8))
# print(example.point_load(q=16000, l=12, teta=49.4))
# print(example.point_load(q=16000, l=12, teta=0))
# print(example.point_load(q=4000, l=12, teta=49.4))
# print(example.line_load(q=400, l=12))
# print(example.line_load(q=4000, l=10))
