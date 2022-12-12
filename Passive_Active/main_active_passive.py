# *** NOT FINISHED YET ***
# in this file I will use inputs to calculate active and passive pressure.

from input import input_values


def main_active_passive(input_values):
    product_id = input_values.get("product_id")
    user_id = input_values.get("user_id")
    unit_system = input_values.get("information").get("unit")
    title = input_values.get("information").get("title")
    jobNo = input_values.get("information").get("jobNo")
    designer = input_values.get("information").get("designer")
    checker = input_values.get("information").get("checker")
    company = input_values.get("information").get("company")
    client = input_values.get("information").get("client")
    date = input_values.get("information").get("date")
    comment = input_values.get("information").get("comment")
    other = input_values.get("information").get("other")
    number_soil_layer_active = input_values.get("data").get("Active Side").get("Number of Soil Layer").get("value")
    h_active = []
    h_passive = []

    space = " "
    for i in range(number_soil_layer_active):
        h = input_values.get("data").get("Active Side").get("H" + i * space).get("value")
        delta_h = input_values.get("data").get("Active Side").get("Δh" + i * space).get("value")













