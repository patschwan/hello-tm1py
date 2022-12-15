"""
Get last_change for all cubes with rules
"""
import configparser
from TM1py.Services import TM1Service

# storing the credentials in a file is not recommended for purposes other than testing.
# it's better to setup CAM with SSO or use keyring to store credentials in the windows credential manager. Sample:
# Samples/credentials_best_practice.py
config = configparser.ConfigParser()
config.read(r'../.config/config.ini')

cubes_changes = dict()

with TM1Service(**config['24retail']) as tm1:

    cubes_w_rux = tm1.cubes.get_all_names_with_rules()
    for c_w_rux in cubes_w_rux:
        dims_c_w_rux = tm1.cubes.get_dimension_names(c_w_rux)
        last_chg_c_w_rux = tm1.cubes.get_last_data_update(c_w_rux)
        cubes_changes[c_w_rux] = last_chg_c_w_rux           
    
    print(cubes_changes)