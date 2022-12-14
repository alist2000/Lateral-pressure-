def force_calculator(pressure_list, depth, width):
    rectangle_force = pressure_list[0] * depth * width
    triangle_force = (pressure_list[1] - pressure_list[0]) * depth * width / 2
    force = [rectangle_force, triangle_force]

    place_rec = depth / 2
    place_tri = depth / 3
    place = [place_rec, place_tri]  # list for place of force from bottom
    return force, place


def moment_calculator(force, arm, width):
    total_moment = 0
    for layer in range(len(force)):
        for item in range(len(force[layer])):
            print(force[layer][item])
            print(arm[layer][item])
            print(arm[layer][item] * force[layer][item])
            total_moment += force[layer][item] * width * arm[layer][item]
    return total_moment
