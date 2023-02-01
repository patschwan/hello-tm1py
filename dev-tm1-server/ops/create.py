import configparser

from TM1py.Objects import Dimension, Subset, Element, ElementAttribute, Hierarchy
from TM1py.Services import TM1Service

config = configparser.ConfigParser()
# storing the credentials in a file is not recommended for purposes other than testing.
# it's better to setup CAM with SSO or use keyring to store credentials in the windows credential manager. Sample:
# Samples/credentials_best_practice.py
config.read(r'../.config/config.ini')


def create_dimension(dim_name, elements, edges, element_attributes):
    """Neue Dimension erzeugen"""

    with TM1Service(address='192.168.224.1', port=44312, user='admin', password='', ssl=False) as tm1:
        dim_name
        hierarchy = Hierarchy(name=dim_name, dimension_name=dim_name, elements=elements, element_attributes=element_attributes,
                          edges=edges)
        dim = Dimension(name=dim_name, hierarchies=[hierarchy])

        # Create Dimension on TM1 Server
        tm1.dimensions.create(dim)

        # TODO: Standard Set an Subsets "All Elements", "All C-Elements", etc
        # tm1.subsets.create()
        # ein Beispiel, wie das funktionieren könnte 
        # https://github.com/cubewise-code/tm1py-samples/blob/master/Metadata/dim_hierarchy_subset_update.py

        # Create Default Subsets
        # TODO subset_definitionen, Name zu MDX und das MDX für get_elements
        subset_name = ['x.Sys_All_Elements']
        subset_elements = tm1.dimensions.get(dimension_name=dim_name)
        print(subset_elements) # TODO was liefert das zurück?

        # create subset
        s = Subset(dimension_name=dim_name, subset_name=subset_name, alias='', elements=subset_elements)
        tm1.dimensions.subsets.create(s, True)