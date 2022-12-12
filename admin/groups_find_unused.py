"""
Find all security groups, that are not used
"""
# import configparser

from TM1py.Services import TM1Service

## siehe tm1py samples Original - wegen configparser
# config = configparser.ConfigParser()
# storing the credentials in a file is not recommended for purposes other than testing.
# it's better to setup CAM with SSO or use keyring to store credentials in the windows credential manager. Sample:
# Samples/credentials_best_practice.py
# config.read(r'..\config.ini')

# with TM1Service(**config['tm1srv01']) as tm1:
    # Get all groups

with TM1Service(address='192.168.80.1', port=52670, user='admin', password='apple', ssl=False) as tm1:
    all_groups = tm1.security.get_all_groups()

    # Determine the used groups from }ClientGroups Cube
    mdx = "SELECT " \
          "NON EMPTY {TM1SUBSETALL( [}Clients] )} on ROWS, " \
          "NON EMPTY {TM1SUBSETALL( [}Groups] )} ON COLUMNS " \
          "FROM [}ClientGroups]"
    cube_content = tm1.cubes.cells.execute_mdx(mdx, ['Value'])

    used_groups = {cell['Value'] for cell in cube_content.values() if cell['Value'] != ''}

    # Determine the unused groups
    unused_groups = set(all_groups) - used_groups

    # Print out the unused groups
    print(unused_groups)