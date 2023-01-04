# functions of active passive pressure calculator.

# all angels must be degree
import copy

import numpy as np
from math import sin, cos, tan, atan, acos, asin, sqrt

gama_w = {"metric": 9.81, "us": 62.4}


def rankine(phi, beta, state):
    if state == "active":
        phi = np.pi * phi / 180
        beta = np.pi * beta / 180
        Ka = cos(beta) * ((cos(beta) - sqrt(cos(beta) ** 2 - cos(phi) ** 2)) / (
                cos(beta) + sqrt(cos(beta) ** 2 - cos(phi) ** 2)))
        return Ka
    else:  # passive
        Kp = Ka = cos(beta) * ((cos(beta) + sqrt(cos(beta) ** 2 - cos(phi) ** 2)) / (
                cos(beta) - sqrt(cos(beta) ** 2 - cos(phi) ** 2)))
        return Kp


def coulomb(phi, beta, delta, omega, state):
    phi = np.pi * phi / 180
    beta = np.pi * beta / 180
    delta = np.pi * delta / 180
    omega = np.pi * omega / 180
    if state == "active":
        Ka = cos(phi - omega) ** 2 / ((cos(omega) ** 2) * (cos(delta + omega)) * (1 + sqrt(
            (sin(delta + phi) * sin(phi - beta)) / cos(delta + omega) * cos(omega - beta))) ** 2)
        return Ka
    else:  # passive
        Kp = cos(phi + omega) ** 2 / ((cos(omega) ** 2) * (cos(delta - omega)) * (1 - sqrt(
            (sin(delta + phi) * sin(phi + beta)) / cos(delta - omega) * cos(beta - omega))) ** 2)
        return Kp


# force function
def force_calculator(pressure_list, depth):
    rectangle_force = pressure_list[0] * depth
    triangle_force = (pressure_list[1] - pressure_list[0]) * depth / 2
    force = [rectangle_force, triangle_force]
    # unit --> force / length

    place_rec = depth / 2
    place_tri = depth / 3
    place = [place_rec, place_tri]  # list for place of force from bottom
    return force, place


class active_passive:
    def __init__(self, h, water, delta_h=0.1):
        if delta_h > 0.1:
            delta_h = 0.1
        if delta_h < 0.001:
            delta_h = 0.001
        self.delta_h = delta_h
        self.h = h
        self.water = water
        # ATTENTION : this part should be in input file and calculate h water and water list.
        # here we just use this value. ( for later h water will receive directly and water list don't need edition )
        # control for water layers. if any layer has water all after that has too.
        i = 0
        h_water = 0
        water_pressure = 0
        for waterlayer in water:
            if waterlayer == "Yes":
                for j in range(i, len(water)):
                    water[j] = "Yes"

                    # calculate h of water
                    h_water += h[j]
                break

            i += 1

        # *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** ***
        self.h_water = h_water

        # depth list :
        depth = []
        depth_list = []
        i = 0
        for height in h:
            depth.append(0)
            depth.append(depth[0] + height)
            depth_copy = copy.deepcopy(depth)
            depth_list.append(depth_copy)
            depth.clear()
            i += 1
        self.depth_list = depth_list

    def pressure_calculator(self, unit_system, number_of_layer, theory, state, gama, phi, beta, delta=None,
                            omega=None):
        """attention : h gama theory and state must be a list with length equal number of layer.
        water is also a list for every layer. if layer number one ( index 0 ) was yes or true it means all
        layers are in water. completely every index was yes all next index ( soil layer ) are in water. and
        we should consider all of them as one saturate layer.
        layers are ordered from top to bottom."""
        h = self.h
        h_water = self.h_water
        water = self.water

        # calculate water pressure
        water_pressure = h_water * gama_w[unit_system]

        # state = "active" or "passive"
        total_h = sum(h)
        k = []
        pressure = []
        number_of_coulomb = 0
        for i in range(number_of_layer):
            # if state = active , k --> ka and if state = passive , k --> kp
            if theory == "Rankine":
                K = rankine(phi[i], beta[i], state)
                try:
                    # k must transform in horizontal --> Kh = k * cos(delta)
                    delta[number_of_coulomb] = np.pi * delta[number_of_coulomb] / 180
                    Kh = K * cos(delta[number_of_coulomb])
                    k.append(Kh)
                    number_of_coulomb += 1
                except:
                    k.append(K)
            elif theory == "Coulomb":
                K = coulomb(phi[i], beta[i], delta[number_of_coulomb], omega[number_of_coulomb], state)
                # k must transform in horizontal --> Kh = k * cos(delta)
                delta[number_of_coulomb] = np.pi * delta[number_of_coulomb] / 180
                Kh = K * cos(delta[number_of_coulomb])
                k.append(Kh)
                number_of_coulomb += 1
            elif theory == "User Defined":
                # here there is no K we have just EFP = gama * K. we assumed K = 1 and gama = EFP
                K = 1
                k.append(K)

            # control gama
            if water[i] == "Yes":
                gama[i] = gama[i] - gama_w[unit_system]  # gama prime

                # calculate water pressure
            sigma_h = []
            if i == 0:  # layer number one
                sigma_h.append(0)
            else:
                '''pressure is a list and every index is a list with two index --> 
                   index 0 is pressure in top of layer and index 1 is pressure in bottom of layer
                   if divide this by k[i - 1] it will equal to gama h. now we can multiply it to k[i]
                   (it will work when k and gama were declared separately)'''

                sigma_zero = pressure[i - 1][1] * k[i] / k[i - 1]
                sigma_h.append(sigma_zero)

            # append index = 1 ( second value )
            sigma = sigma_h[0] + k[i] * h[i] * gama[i]
            sigma_h.append(sigma)

            pressure.append(sigma_h)
        return pressure, [[0, water_pressure]], self.depth_list, self.h_water, k

    def force_final(self, pressure, type_pressure="soil"):
        # if pressure was for water user send us water word
        h = self.h
        if type_pressure == "water":
            h = [self.h_water]
        force_list = []
        arm_list = []
        for i in range(len(pressure)):
            arms = []
            force, place = force_calculator(pressure[i], h[i])
            force_list.append(force)
            # place is centroid just in that layer. we should calculate arm from bottom of pile.
            for load in range(len(force)):
                try:  # if we have more than one layer
                    arm = sum(h[i + 1:]) + place[load]
                except:
                    arm = place[load]
                arms.append(arm)
            arms_copy = copy.deepcopy(arms)
            arm_list.append(arms_copy)
        return force_list, arm_list
