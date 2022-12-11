import copy
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
        for load in load_types:
            if load == "Point Load":
                html_temp_root = "/report/template/" + html_temp[1]
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
                report_values["excel_name"] = "http://civision.balafan.com:8010/report/Surcharge/excel/excel" + str(
                    i + 1)
                report_values["plot_address"] = "http://civision.balafan.com:8010/report/Surcharge/plot/output" + str(
                    i + 1)

            elif load == "Line Load":
                html_temp_root = "/report/template/" + html_temp[2]
                # inputs:
                report_values["H"] = h
                report_values["delta_h"] = delta_h
                report_values["Load_Type"] = load
                report_values["q"] = q[i]
                report_values["L1"] = l1[i]
                # outputs
                report_values["Pr"] = output[4][i][0]
                report_values["Zr"] = output[4][i][1]
                report_values["excel_name"] = "http://civision.balafan.com:8010/report/Surcharge/excel/excel" + str(
                    i + 1)
                report_values["plot_address"] = "http://civision.balafan.com:8010/report/Surcharge/plot/output" + str(
                    i + 1)


            elif load == "Strip Load":
                html_temp_root = "/report/template/" + html_temp[3]
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
                report_values["excel_name"] = "http://civision.balafan.com:8010/report/Surcharge/excel/excel" + str(
                    i + 1)
                report_values["plot_address"] = "http://civision.balafan.com:8010/report/Surcharge/plot/output" + str(
                    i + 1)
            myvalues = copy.deepcopy(report_values)
            variables.append(myvalues)
            html_temp_list.append(html_temp_root)
            file_name = "p" + str(product_id) + "u" + str(user_id) + "_" + "Solution" + str(
                i + 1) + "_SurchargeLoad_Report.pdf"
            file_name_list.append(file_name)
            i += 1
        if len(load_types) > 1:
            # for result
            html_temp_root = "/report/template/" + html_temp[4]
            # inputs:
            report_values["H"] = h
            report_values["load_number"] = len(output[4]) - 1
            # outputs
            report_values["Pr"] = output[4][-1][0]
            report_values["Zr"] = output[4][-1][1]
            report_values["excel_name"] = "http://civision.balafan.com:8010/report/Surcharge/excel/excel" + str(
                i + 1)
            report_values["plot_address"] = "http://civision.balafan.com:8010/report/Surcharge/plot/output" + str(
                i + 1)
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

def create_html_report(html_temp_files, template_vars, pdf_names):
    for i in range(len(html_temp_files)):
        html_temp_file = html_temp_files[i]
        template_var = template_vars[i]
        pdf_name = pdf_names[i]
        env = Environment(loader=FileSystemLoader('..'))
        template = env.get_template(html_temp_file)
        html_filled = template.render(template_var)
        file = open("report/" + pdf_name[:-4] + ".html", "w")
        file.write(html_filled)
        file.close()


####################################################

import pandas as pd
import pyarrow.feather as feather


# creating excel
def create_feather(depth, sigma, excel_name):
    print(len(depth))
    print(len(sigma))
    data = list(zip(depth, sigma))
    print(data)
    df = pd.DataFrame(data, columns=["Z", "Ϭh"])
    df.to_feather("report/excel/" + excel_name + ".feather")


def choose_and_create_pdf(file_name):
    file = open("report/" + file_name + ".html", "r")
    html_filled = file.read()
    # file_name is a name with .html suffix it must be replaced with .pdf
    pdf_name = file.name[:-5] + ".pdf"
    file.close()
    HTML(string=html_filled, base_url=__file__).write_pdf(pdf_name)


def choose_and_create_excel(file_name):
    # file name must be a string with style like this "excelname" + number of project
    data = pd.read_feather("report/excel/" + file_name + ".feather")
    data.to_csv("report/excel/" + file_name + ".csv")
    return None
