"""
Get a Cube from TM1
"""
from TM1py.Services import TM1Service

with TM1Service(address='192.168.80.1', port=52670, user='admin', password='apple', ssl=False) as tm1:

    cubes_w_rux = tm1.cubes.get_all_names_with_rules()
    for c_w_rux in cubes_w_rux:
        print(c_w_rux)