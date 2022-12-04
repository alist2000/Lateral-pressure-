def report(project_type, product_id, user_id, inputs, output):
    variables = []
    html_temp_list = []
    file_name_list = []
    load_types = inputs[1]
    h = inputs[0]
    q = inputs[2]
    l1 = inputs[3]
    l2 = inputs[4]
    teta = inputs[5]
    html_temp = {1: "Rep_surcharge_point_load.html",
                 2: "Rep_surcharge_line_load.html",
                 3: "Rep_surcharge_strip_load.html",
                 4: "Rep_surcharge_result.html"}
    i = 0
    if project_type == "single":
        #  for loads
        if len(load_types) > 1:
            for load in load_types:
                if load == "Point Load":
                    html_temp_root = "/report/" + html_temp[1]
                    report_values = {
                        # inputs:
                        "H": h,
                        "q": q[i],
                        "L1": l1[i],
                        "&#xc6;&#x9f;": teta[i],
                        # outputs
                        "Pr": output[4][i][0],
                        "Zr": output[4][i][1],
                        "excel_name": "name of excel that I should  create.",
                        "plot_address": "../plot/output" + str(i+1) + ".html"

                    }
                    variables.append(report_values)
                    html_temp_list.append(html_temp_root)
                elif load == "Line Load":
                    html_temp_root = "/report/" + html_temp[2]
                    report_values = {
                        # inputs:
                        "H": h,
                        "q": q[i],
                        "L1": l1[i],
                        # outputs
                        "Pr": output[4][i][0],
                        "Zr": output[4][i][1],
                        "excel_name": "name of excel that I should  create.",
                        "plot_address": "../plot/output" + str(i + 1) + ".html"

                    }
                    variables.append(report_values)
                    html_temp_list.append(html_temp_root)
                elif load == "Strip Load":
                    html_temp_root = "/report/" + html_temp[3]
                    report_values = {
                        # inputs:
                        "H": h,
                        "q": q[i],
                        "L1": l1[i],
                        "L2": l2[i],
                        # outputs
                        "Pr": output[4][i][0],
                        "Zr": output[4][i][1],
                        "excel_name": "name of excel that I should  create.",
                        "plot_address": "../plot/output" + str(i + 1) + ".html"
                    }
                    variables.append(report_values)
                    html_temp_list.append(html_temp_root)
                file_name = "p" + str(product_id) + "u" + str(user_id) + "_" + "Solution" + str(
                    i + 1) + "_SurchargeLoad_Report.pdf"
                file_name_list.append(file_name)
                i += 1

            # for result
            html_temp_root = "/report/" + html_temp[4]
            report_values = {
                # inputs:
                "H": h,
                "load_number": len(output[4]) - 1,
                # outputs
                "Pr": output[4][-1][0],
                "Zr": output[4][-1][1],
                "excel_name": "name of excel that I should  create.",
                "plot_address": "../plot/output" + str(i + 1) + ".html"
            }
            variables.append(report_values)
            html_temp_list.append(html_temp_root)
            file_name = "p" + str(product_id) + "u" + str(user_id) + "_" + "Solution" + str(
                i + 1) + "_SurchargeLoad_Report.pdf"
            file_name_list.append(file_name)
            # create_pdf_report(html_temp_root, report_values, file_name)
        else:
            pass  # must be developed for multi project

        return variables, html_temp_list, file_name_list


"""
A HTML page is generated from a template and rendered as a local PDF file.
"""

# from weasyprint import HTML
from jinja2 import Environment, FileSystemLoader


####################################################

# Loading and filling the template

def create_pdf_report(html_temp_file, template_vars, pdf_name):
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template(html_temp_file)
    html_filled = template.render(template_vars)
    HTML(string=html_filled, base_url=__file__).write_pdf(pdf_name)


####################################################

def item_receiver(variable, html_temp_list, file_name_list):
    global variables
    global html_temp_lists
    global file_name_lists
    variables = variable
    html_temp_lists = html_temp_list
    file_name_lists = file_name_list
    return None


def choose_pdf_item_surcharge(product_number: 1, pdf_number):
    pdf_number = int(pdf_number)
    product_number = int(product_number)
    pdf_number -= 1
    product_number -= 1
    create_pdf_report(html_temp_lists[pdf_number],
                      variables[pdf_number],
                      file_name_lists[pdf_number])
    return None
