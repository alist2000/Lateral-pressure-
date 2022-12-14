# *** NOT FINISHED YET ***
# in this file I will use inputs to calculate active and passive pressure.

from input import input_values

# def main_active_passive(input_values):
#     product_id = input_values.get("product_id")
#     user_id = input_values.get("user_id")
#     unit_system = input_values.get("information").get("unit")
#     title = input_values.get("information").get("title")
#     jobNo = input_values.get("information").get("jobNo")
#     designer = input_values.get("information").get("designer")
#     checker = input_values.get("information").get("checker")
#     company = input_values.get("information").get("company")
#     client = input_values.get("information").get("client")
#     date = input_values.get("information").get("date")
#     comment = input_values.get("information").get("comment")
#     other = input_values.get("information").get("other")
#     number_soil_layer_active = input_values.get("data").get("Active Side").get("Number of Soil Layer").get("value")
#     h_active = []
#     h_passive = []
#
#     space = " "
#     for i in range(number_soil_layer_active):
#         h = input_values.get("data").get("Active Side").get("H" + i * space).get("value")
#         delta_h = input_values.get("data").get("Active Side").get("Δh" + i * space).get("value")


from sympy import symbols, substitution
from active_passive import active_passive

x = symbols("x")
h = [10, x]
main = active_passive([10, x], ["No", "No"])
soil, water = main.pressure_calculator(number_of_layer=2, gama=[120, 125], phi=[34, 36], theory="Coulomb",
                                       state="active",
                                       unit_system="us", beta=[0, 0], omega=[0, 0], delta=[0, 24])
print(soil, water)

force_soil = main.force_final(soil)
force_water = main.force_final(water, "water")
print(force_soil)
print(force_water)
# force_list = []
# i = 0
# for pressure in soil:
#     force_list.append(force_calculator(pressure, h[i]))
#     i += 1
# water_force = force_calculator(water[1], water[0])
# print(force_list)
# print(water_force)
# test_symbol = pressure_calculator(number_of_layer=1, h=[x], gama=[120], phi=[34], theory="Rankine", state="active",
#                                   water=["No"], unit_system="us", beta=[0])
# print(test_symbol)

# test = pressure_calculator(number_of_layer=3, h=[4, 6, 20], gama=[130, 102.4, 102.4], phi=[37, 30, 30],
#                            theory="Rankine",
#                            state="active", water=["No", "No", "Yes"],
#                            unit_system="us", beta=[0, 0, 0])
# print(test)
#  a = pressure_calculator(number_of_layer=1, h=[10], gama=[120], phi=[34], theory="Rankine", state="active",
#                         water=["No"], unit_system="us", beta=[0])
# b = pressure_calculator(number_of_layer=1, h=[23], gama=[125], phi=[36], theory="Coulomb", state="active",
#                         water=["No"], unit_system="us", beta=[0], omega=[0], delta=[24])
# d = pressure_calculator(number_of_layer=1, h=[23], gama=[125], phi=[36], theory="Coulomb", state="passive",
#                         water=["No"], unit_system="us", beta=[-32], omega=[0], delta=[24])
# c = pressure_calculator(number_of_layer=2, h=[10, 23], gama=[120, 125], phi=[34, 36], theory="Rankine",
#                         state="active", water=["No", "No"],
#                         unit_system="us", beta=[0, 0], omega=[0], delta=[24])
# print(a)
