"""
List all Dimensions of all Cubes
"""

import configparser
from TM1py.Services import TM1Service

# storing the credentials in a file is not recommended for purposes other than testing.
# it's better to setup CAM with SSO or use keyring to store credentials in the windows credential manager. Sample:
# Samples/credentials_best_practice.py
config = configparser.ConfigParser()
config.read(r'../.config/config.ini')

RESULT_FILE = r'/home/psw/code/hello-tm1py/output/cube_all_dimensios.txt'
log_lines = []

with TM1Service(**config['24retail']) as tm1:
    cubes = tm1.cubes.get_all()

    # for cube in cubes:
    #     log_lines.append("All dimensions for " + str(cube) + ":")
    #     dims = tm1.cubes.get_dimension_names
    #     log_lines.append(dims)

with open(RESULT_FILE, 'w', encoding='utf-8') as file:
    file.write("\n".join(str(cube) for cube in cubes))
    file.close()

    # liefert
    # {"Name": "Asset Life", 
    # "Dimensions@odata.bind": [
    #   "Dimensions('Asset Types')",
    #   "Dimensions('Version')",
    #   "Dimensions('Asset Life')"
    # ],
    # "Rules": "#Region System\nFEEDSTRINGS;\nSKIPCHECK;\nUNDEFVALS;\n#EndRegion\n\nFEEDERS;"}