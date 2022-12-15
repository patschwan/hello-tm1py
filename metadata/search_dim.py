"""
List all cubes that contain dimension - search via exact dimension name
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

    cubes = tm1.cubes.search_for_dimension('organization')

    print(cubes)