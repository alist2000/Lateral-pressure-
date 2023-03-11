# CIV Base Application
# This application is generated for soldier pile design
# Soldier Piles can be either cantilevered or Restrained
# The application calculates:
# Required Embedment Depth
# Shear and Moment Diagrams
# Maximum Shear and Moment values
# Required section
# Maximum soldier pile deflection

from .HTML.sp_front import generate_html_response2, generate_html_response3, generate_html_response
from .HTML.FTAO_front import generate_html_response4
from .HTML.BFP_front import generate_html_response_BFP, generate_html_response_BFP_multi, \
    generate_html_response_BFP_no_solution, generate_html_response_BFP_multi_no_solution
from .HTML.Surcharge_front import generate_html_response_surcharge, generate_html_response_surcharge_no_solution
from .FTAO.multi_Shear_Wall_main import multi_shear_wall
from .FTAO.Shear_Wall_main import shear_wall
from .sp.msp import multi_soldier_pile
from .sp.sp import soldier_pile  # just for here actual import isn't this
# from .bfp.BFP_main_local import BFP_main
from .bfp.BFP_main import BFP_main
from .bfp.pdf_report import choose_pdf_item_sum, choose_pdf_item_rep
# from .bfp.bfp_multi_project import bfp_multi_project
from .section_level.section_main import Section_main

# shoring
from .Surcharge.main_surcharge import surcharge_calculator
from .Surcharge.report import choose_pdf_item_surcharge, choose_excel
from email import header
from itertools import count
import os
import re
import sys
from fastapi import Request, FastAPI
from fastapi.responses import FileResponse
from fastapi.responses import HTMLResponse

import sympy as sym
import math
import numpy as np

app = FastAPI()

# sys.path.insert(1,'/root/cvision/Base-v2/app/sp')

# from .sp.sp import single_soldier_pile

path = "/app/app/reports"
path1 = "/app/app/"


# Get json and call corresponding function
@app.post("/base")
async def get_body(request: Request):
    items = await request.json()

    print(items)

    product_id = items.get("product_id")
    user_id = items.get("user_id")
    data = items.get("data")
    process_type = items.get("type")
    num_of_projects = items.get("number_of_projects")

    if (product_id == 8):
        if (process_type == 1):
            output = soldier_pile(data, product_id,
                                  user_id)  # this is not true. line below is actual code but this folder and sp file is not upgrade.
            # output = single_soldier_pile(data,product_id,user_id)
            response = generate_html_response2(output)
        else:
            output = multi_soldier_pile(
                data, product_id, user_id, num_of_projects)
            response = generate_html_response3(output)
    elif (product_id == 11):
        if (process_type == 1):
            output = shear_wall(items)
            response = generate_html_response4(output)
        else:
            output = multi_shear_wall(items)
            response = generate_html_response3(output)

    elif (product_id == 2):
        output, status = BFP_main(num_of_projects, items)
        if (process_type == 1):
            if status == "solved":
                response = generate_html_response_BFP(output)
            else:
                response = generate_html_response_BFP_no_solution(output)
        else:
            response = generate_html_response_BFP_multi(output)
        # output = bfp_multi_project(num_of_projects, items)
        # response = generate_html_response_BFP(output)

    elif product_id == 13:
        output = Section_main(items)
        response = "hello friend"

    elif product_id == 25:
        inputs, output = surcharge_calculator(items)
        if inputs == "No Solution":
            response = generate_html_response_surcharge_no_solution(output)

        else:
            response = generate_html_response_surcharge(inputs, output)

    return HTMLResponse(content=response, status_code=200)


# Send pdf reports
@app.get("/report/{file_name}")
async def send_report(file_name):
    file_path = os.path.join(path, file_name + ".pdf")

    if os.path.exists(file_path):
        return FileResponse(file_path)
    return {"error": " !"}


path = "/app/app/reports"
path2 = "/app/app/reports/FTAO"
path3 = "/app/app/reports/BFP"
path4 = "/app/app/reports/Surcharge"
path5 = "/app/app/Surcharge/report/excel"


# Show pdf download images
@app.get("/icon/{file_name}")
async def send_report(file_name):
    file_path = os.path.join(path1, file_name + ".png")

    if os.path.exists(file_path):
        return FileResponse(file_path)
    return {"error": " !"}


# _________________________for test generating summary html page_______________________


@app.get("/report/FTAO/{file_name}")
def html_response_summary(file_name):
    file_path = os.path.join(path2, file_name + ".txt")
    if os.path.exists(file_path):
        file = open(file_path)
        content = file.read()
        return HTMLResponse(content=content, status_code=200)
    return {"error": " !"}


@app.get("/report/BFP/{file_name}")
async def send_report(file_name):
    file_path = os.path.join(path3, file_name + ".pdf")
    if "Detailed" in file_path:
        # based on file path number of solution for detail file is index number 25 from the end. or 8 index after "solution"
        solution = file_path.rindex("Solution")
        product_number = file_path.rindex("_")
        choose_pdf_item_rep(file_path[product_number + 1], file_path[solution + 8])

    else:
        # based on file path number of solution for summary file is index number 24 from the end.or 8 index after "solution"
        solution = file_path.rindex("Solution")
        product_number = file_path.rindex("_")
        choose_pdf_item_sum(file_path[product_number + 1], file_path[solution + 8])
    file_path = file_path[:product_number] + file_path[
                                             product_number + 2:]  # file name till  "_ + product number"  +  ".pdf"
    if os.path.exists(file_path):
        return FileResponse(file_path)
    return {"error": " !"}


@app.get("/report/Surcharge/{file_name}")
async def send_report(file_name):
    file_path = os.path.join(path4, file_name + ".pdf")
    # based on file path number of solution for detail file is index number 25 from the end. or 8 index after "solution"
    solution = file_path.rindex("Solution")
    product_number = file_path.rindex("_")
    print(file_path)
    print(file_path[product_number + 1], file_path[solution + 8])
    choose_pdf_item_surcharge(file_path[product_number + 1], file_path[solution + 8])

    file_path = file_path[:product_number] + file_path[
                                             product_number + 2:]  # file name till  "_ + product number"  +  ".pdf"
    print(file_path)
    if os.path.exists(file_path):
        return FileResponse(file_path)
    return {"error": " !"}


@app.get("/report/Surcahrge/excel/{file_name}")
async def excel_surcharge(file_name):
    # file name = excel + number --> for find number of file --> file name [5:]
    i = int(file_name[5:])
    choose_excel(i)
    file_path = os.path.join(path5, file_name + ".csv")

    if os.path.exists(file_path):
        return FileResponse(file_path)
    return {"error": " !"}
