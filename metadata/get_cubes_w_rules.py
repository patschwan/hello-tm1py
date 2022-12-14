"""
Get last_change for all cubes with rules
"""
from TM1py.Services import TM1Service

cubes_changes = dict()

with TM1Service(address='192.168.80.1', port=52670, user='admin', password='apple', ssl=False) as tm1:

    cubes_w_rux = tm1.cubes.get_all_names_with_rules()
    for c_w_rux in cubes_w_rux:
        dims_c_w_rux = tm1.cubes.get_dimension_names(c_w_rux)
        last_chg_c_w_rux = tm1.cubes.get_last_data_update(c_w_rux)
        cubes_changes[c_w_rux] = last_chg_c_w_rux           
    
    print(cubes_changes)