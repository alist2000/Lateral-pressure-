# functions of active passive pressure calculator.

gama_w = {"metric": 9.81, "us": 62.4}


def rankine(phi, state):
    if state == "active":
        Ka = ...
        return Ka
    else:  # passive
        Kp = ...
        return Kp


def coulomb(phi, state):
    if state == "active":
        Ka = ...
        return Ka
    else:  # passive
        Kp = ...
        return Kp


def pressure_calculator(number_of_layer, h, gama, phi, theory, state, water, unit_system):
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
    for i in range(number_of_layer):
        # if state = active , k --> ka and if state = passive , k --> kp
        if theory[i] == "Rankine":
            K = rankine(phi[i], state[i])
            k.append(K)
        elif theory[i] == "Coulomb":
            K = coulomb(phi[i], state[i])
            k.append(K)

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
