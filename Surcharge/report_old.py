import datetime
import xlsxwriter


def report(project_type, product_id, user_id, inputs, output):
    variables = []
    html_temp_list = []
    file_name_list = []
    title = inputs["title"]
    jobNo = inputs["jobNo"]
    designer = inputs["designer"]
    checker = inputs["checker"]
    company = inputs["company"]
    client = inputs["client"]
    date = inputs["date"]
    if date == None:
        date = datetime.datetime.now()
        date = date.strftime("%Y/%m/%d")
    comment = inputs["comment"]
    if comment == None:
        comment = "-"
    other = inputs["other"]
    load_types = inputs["load_type"]
    h = inputs["h"]
    delta_h = inputs["delta_h"]
    q = inputs["q"]
    l1 = inputs["l1"]
    l2 = inputs["l2"]
    teta = inputs["teta"]
    html_temp = {1: "Rep_surcharge_point_load.html",
                 2: "Rep_surcharge_line_load.html",
                 3: "Rep_surcharge_strip_load.html",
                 4: "Rep_surcharge_result.html"}
    i = 0

    report_values = {"project_title": title, "designer": designer, "job_title": jobNo, "checker": checker,
                     "company": company, "analysis_date": date, "comments": comment}
    if project_type == "single":
        #  for loads
        if len(load_types) > 1:
            for load in load_types:
                if load == "Point Load":
                    html_temp_root = "/report/" + html_temp[1]
                    # inputs:
                    report_values["H"] = h
                    report_values["delta_h"] = delta_h
                    report_values["Load_Type"] = load
                    report_values["q"] = q[i]
                    report_values["L1"] = l1[i]
                    report_values["teta"] = teta[i]
                    # outputs
                    report_values["Pr"] = output[4][i][0]
                    report_values["Zr"] = output[4][i][1]
                    report_values["excel_name"] = "http://civision.balafan.com:8010/report/Surchage/excel/excel" + str(
                        i + 1)
                    report_values["plot_address"] = "../plot/output" + str(i + 1) + ".png"
                    variables.append(report_values)
                    html_temp_list.append(html_temp_root)
                elif load == "Line Load":
                    html_temp_root = "/report/" + html_temp[2]
                    # inputs:
                    report_values["H"] = h
                    report_values["delta_h"] = delta_h
                    report_values["Load_Type"] = load
                    report_values["q"] = q[i]
                    report_values["L1"] = l1[i]
                    # outputs
                    report_values["Pr"] = output[4][i][0]
                    report_values["Zr"] = output[4][i][1]
                    report_values["excel_name"] = "http://civision.balafan.com:8010/report/Surchage/excel/excel" + str(
                        i + 1)
                    report_values["plot_address"] = "../plot/output" + str(i + 1) + ".html"

                    variables.append(report_values)
                    html_temp_list.append(html_temp_root)
                elif load == "Strip Load":
                    html_temp_root = "/report/" + html_temp[3]
                    # inputs:
                    report_values["H"] = h
                    report_values["delta_h"] = delta_h
                    report_values["Load_Type"] = load
                    report_values["q"] = q[i]
                    report_values["L1"] = l1[i]
                    report_values["L2"] = l2[i]
                    # outputs
                    report_values["Pr"] = output[4][i][0]
                    report_values["Zr"] = output[4][i][1]
                    report_values["excel_name"] = "http://civision.balafan.com:8010/report/Surchage/excel/excel" + str(
                        i + 1)
                    report_values["plot_address"] = "../plot/output" + str(i + 1) + ".html"
                    variables.append(report_values)
                    print(report_values)
                    html_temp_list.append(html_temp_root)
        file_name = "p" + str(product_id) + "u" + str(user_id) + "_" + "Solution" + str(
            i + 1) + "_SurchargeLoad_Report.pdf"
        file_name_list.append(file_name)
        i += 1

        # for result
        html_temp_root = "/report/" + html_temp[4]
        # inputs:
        report_values["H"] = h,
        report_values["load_number"] = len(output[4]) - 1,
        # outputs
        report_values["Pr"] = output[4][-1][0],
        report_values["Zr"] = output[4][-1][1],
        report_values["excel_name"] = "http://civision.balafan.com:8010/report/Surchage/excel/excel" + str(i + 1)
        report_values["plot_address"] = "../plot/output" + str(i + 1) + ".html"
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

from weasyprint import HTML
from jinja2 import Environment, FileSystemLoader


####################################################

# Loading and filling the template

def create_pdf_report(html_temp_file, template_vars, pdf_name):
    env = Environment(loader=FileSystemLoader('..'))
    template = env.get_template(html_temp_file)
    html_filled = template.render(template_vars)
    HTML(string=html_filled, base_url=__file__).write_pdf(pdf_name)


####################################################


# creating excel
def create_excel(depth, sigma, excel_name):
    file = xlsxwriter.Workbook("/app/app/Surcharge/report/excel/" + excel_name + ".csv")
    worksheet = file.add_worksheet()
    row = 0
    for z in depth:
        worksheet.write(row, 0, z)
        row += 1
    row = 0
    for sigmah in sigma:
        worksheet.write(row, 1, sigmah)
    file.close()
    return None


def item_receiver(variable, html_temp_list, file_name_list, depth, sigma):
    global variables
    global html_temp_lists
    global file_name_lists
    global depth_list
    global sigma_list
    variables = variable
    html_temp_lists = html_temp_list
    file_name_lists = file_name_list
    file_name_lists = file_name_list
    depth_list = depth
    sigma_list = sigma
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


def choose_excel(product_number: 1, pdf_number):
    pdf_number = int(pdf_number)
    product_number = int(product_number)
    pdf_number -= 1
    product_number -= 1
    create_excel(depth_list,
                 sigma_list[pdf_number],
                 "excel" + str(pdf_number))
    return None
