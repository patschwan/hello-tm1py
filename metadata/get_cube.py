"""
Get a Cube from TM1
"""
from TM1py.Services import TM1Service

with TM1Service(address='192.168.80.1', port=52670, user='admin', password='apple', ssl=False) as tm1:
    cubes = tm1.cubes.get_all()
    for cube in cubes:
        cube_dims = tm1.cubes.get_dimension_names(cube_name=cube.name)
        print("Cube: " + str(cube.name) + " hat die Dimensionen: "+ str(cube_dims))

        # Liefert:
        # Cube: Revenue hat die Dimensionen: ['organization', 'Channel', 'product', 'Month', 'Year', 'Version', 'Revenue']
        # Cube: Revenue Assumptions hat die Dimensionen: ['product', 'Channel', 'Month', 'Year', 'Version', 'RevenueAsmpt']
        # Cube: Revenue Reporting hat die Dimensionen: ['organization', 'Channel', 'product', 'Month', 'Year', 'Revenue', 'Version']
        # Cube: Social Media hat die Dimensionen: ['product', 'SM Entries', 'SM Reviews']

