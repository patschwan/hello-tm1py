"""
List all cubes that contain dimension - search via Substring
"""
from TM1py.Services import TM1Service

cubes_changes = dict()

with TM1Service(address='192.168.80.1', port=52670, user='admin', password='apple', ssl=False) as tm1:

    cubes = tm1.cubes.search_for_dimension_substring('orga')

    # Dict = keys/cube names : values/dimension_substr_search_result
    print(cubes.values())