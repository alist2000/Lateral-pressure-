# functions of active passive pressure calculator.

# all angels must be degree

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


def pressure_calculator(unit_system, number_of_layer, theory, state, water, h, gama, phi, beta, delta=None, omega=None):
    """attention : h gama theory and state must be a list with length equal number of layer.
    water is also a list for every layer. if layer number one ( index 0 ) was yes or true it means all
    layers are in water. completely every index was yes all next index ( soil layer ) are in water. and
    we should consider all of them as one saturate layer.
    layers are ordered from top to bottom."""

    # control for water layers. if any layer has water all after that has too.
    i = 0
    for waterlayer in water:
        if waterlayer == "Yes":
            for j in range(i, len(water)):
                water[j] = "Yes"
        i += 1

    # state = "active" or "passive"
    total_h = sum(h)
    k = []
    pressure = []
    water_pressure = []
    number_of_coulomb = 0
    for i in range(number_of_layer):
        # if state = active , k --> ka and if state = passive , k --> kp
        if theory == "Rankine":
            K = rankine(phi[i], beta[i], state[i])
            k.append(K)
        elif theory == "Coulomb":
            K = coulomb(phi[i], beta[i], delta[number_of_coulomb], omega[number_of_coulomb], state[i])
            # k must transform in horizontal --> Kh = k * cos(delta)
            delta = np.pi * delta[number_of_coulomb] / 180
            Kh = K * cos(delta)
            k.append(Kh)
            number_of_coulomb += 1

        # control gama
        if water[i] == "Yes":
            gama[i] = gama[i] - gama_w[unit_system]  # gama prime
        sigma_h = []
        if i == 0:  # layer number one
            sigma_h.append(0)
        else:
            '''pressure is a list and every index is a list with two index --> 
               index 0 is pressure in top of layer and index 1 is pressure in bottom of layer
               if divide this by k[i - 1] it will equal to gama h. now we can multiply it to k[i]'''

            sigma_zero = pressure[i - 1][1] * k[i] / k[i - 1]
            sigma_h.append(sigma_zero)

        # append index = 1 ( second value )
        sigma = sigma_h[0] + k[i] * h[i] * gama[i]
        sigma_h.append(sigma)

        pressure.append(sigma_h)
    return pressure


# a = pressure_calculator(number_of_layer=1, h=[10], gama=[120], phi=[34], theory="Rankine", state=["active"],
#                         water=["No"], unit_system="us", beta=[0])
# b = pressure_calculator(number_of_layer=1, h=[23], gama=[125], phi=[36], theory="Coulomb", state=["active"],
#                         water=["No"], unit_system="us", beta=[0], omega=[0], delta=[24])
d = pressure_calculator(number_of_layer=1, h=[23], gama=[125], phi=[36], theory= "Coulomb", state=["passive"],
                        water=["No"], unit_system="us", beta=[-32], omega=[0], delta=[24])
# c = pressure_calculator(number_of_layer=2, h=[10, 23], gama=[120, 125], phi=[34, 36], theory="Rankine",
#                         state=["active", "active"], water=["No", "No"],
#                         unit_system="us", beta=[0, 0], omega=[0], delta=[24])
# print(a)
