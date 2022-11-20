def output(product_id, user_id, solution, sum_sigma_h, depth, lateral_pressure, centroid, unit_system):
    otitle = ["lateral pressure calculator - Output Summary",
              "Final Solution Alternatives"]
    header1 = [2, "lateral pressure"]
    if unit_system == "us":
        length_unit = "ft"
        pressure_unit = "psf"
    else:
        length_unit = "m"
        pressure_unit = "Pa"
    units = [length_unit, pressure_unit]
    values = []
    if len(solution[0]) + len(solution[1]) + len(solution[2]) != 1:
        # it means that we have more than one load
        i = 0
        for load_type in solution:
            for load in load_type:
                load_solution = [load[0], load[1]]  # lateral pressure , centroid
                values.append(load_solution)
                i += 1

    # add final solution
    values.append([lateral_pressure, centroid])

    header2 = ["P", "Z"]
    # values = [["load 1"], ["load 2 "]]
    file_name = []
    for i in range(len(values)):
        filename_summary = "p" + str(product_id) + "u" + str(user_id) + "_" + "Solution" + str(
            i + 1) + "_Surcharge_Summary_Report"
        filename_detail = "p" + str(product_id) + "u" + str(user_id) + "_" + "Solution" + str(
            i + 1) + "_Surcharge_Detailed_Report"
        file_name.append(filename_summary)
        file_name.append(filename_detail)

    output = []
    output.append(otitle)
    output.append(header1)
    output.append(header2)
    output.append(units)
    output.append(values)
    output.append(file_name)
    return output
