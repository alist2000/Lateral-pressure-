def output(product_id, user_id, inputs, solution, sum_sigma_h, depth, lateral_pressure, centroid, unit_system, plots):
    # control inputs
    h = inputs[0]
    load_type_all = inputs[1]
    q_all = inputs[2]
    l1_all = inputs[3]
    l2_all = inputs[4]
    teta = inputs[5]
    title_input = ["H = ", "q = ", "L1 = ", "L2 = ", "Ɵ = "]

    input_values = []
    j = 0
    for i in load_type_all:
        if i == "Point Load":
            input_values.append(
                [title_input[0] + str(h), title_input[1] + str(q_all[j]), title_input[2] + str(l1_all[j]),
                 title_input[4] + str(teta[j])])
            j += 1
        if i == "Line Load":
            input_values.append(
                [title_input[0] + str(h), title_input[1] + str(q_all[j]), title_input[2] + str(l1_all[j])])
            j += 1
        if i == "Strip Load":
            input_values.append(
                [title_input[0] + str(h), title_input[1] + str(q_all[j]), title_input[2] + str(l1_all[j]),
                 title_input[3] + str(l2_all[j])])
            j += 1

    # control results
    otitle = ["lateral pressure calculator - Output Summary",
              "Final Solution Alternatives"]
    header1 = [3, "lateral pressure"]
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
                load_solution = [round(load[0], 2), round(load[1], 2)]  # lateral pressure , centroid
                values.append(load_solution)
                i += 1

    # add final solution
    values.append([round(lateral_pressure, 2), round(centroid, 2)])

    header2 = ["Inputs", f"Pr ({pressure_unit})", f"Zr ({length_unit})"]
    # values = [["load 1"], ["load 2 "]]
    file_name = []
    for i in range(len(values)):
        filename_summary = "p" + str(product_id) + "u" + str(user_id) + "_" + "Solution" + str(
            i + 1) + "_SurchargeLoad_Report"
        filename_detail = "p" + str(product_id) + "u" + str(user_id) + "_" + "Solution" + str(
            i + 1) + "_SurchargeLoad_Report"
        file_name.append(filename_summary)
        file_name.append(filename_detail)

    output = []
    output.append(otitle)
    output.append(header1)
    output.append(header2)
    output.append(units)
    output.append(values)
    output.append(file_name)

    i = 1
    for plot in plots:
        plot.write_html(f"plot/output{i}.html",
                        full_html=False,
                        include_plotlyjs='cdn')
        # plot.write_image(f"plot/output{i}.png")
        i += 1
    return input_values, output


def output_noSolution(product_id, user_id, error):
    otitle = ["lateral pressure calculator - Output Summary",
              "Final Solution Alternatives"]
    header1 = [len(error) + 1, "Error!"]  # +1 --> number of errors

    """header 2 : titles --> number of errors , description"""
    header2 = ["Number of errors", "Description"]
    solution = [len(error)]
    for i in error:
        solution.append(i)
    values = [solution]
    unit = []

    Output = [otitle, header1, header2, unit, values]
    return Output
