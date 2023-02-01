import configparser

from TM1py.Objects import Dimension, Element, ElementAttribute, Hierarchy
from TM1py.Services import TM1Service

config = configparser.ConfigParser()
# storing the credentials in a file is not recommended for purposes other than testing.
# it's better to setup CAM with SSO or use keyring to store credentials in the windows credential manager. Sample:
# Samples/credentials_best_practice.py
config.read(r'../.config/config.ini')

name = 'TM1py Region'

# Connection to TM1. Needs IP, Port, Credentials, and SSL
# with TM1Service(**config['DEFAULT']) as tm1:
with TM1Service(address='192.168.224.1', port=44312, user='admin', password='', ssl=False) as tm1:
    # create elements objects
    elements = [Element(name='Europe', element_type='Consolidated'),
                Element(name='CH', element_type='Numeric'),
                Element(name='UK', element_type='Numeric'),
                Element(name='BE', element_type='Numeric')]

    # create edge object
    edges = {('Europe', 'CH'): 1,
             ('Europe', 'UK'): 1,
             ('Europe', 'BE'): 1}

    # create the element_attributes
    element_attributes = [ElementAttribute(name='Name Long', attribute_type='Alias'),
                          ElementAttribute(name='Name Short', attribute_type='Alias'),
                          ElementAttribute(name='Currency', attribute_type='String')]

    # create hierarchy object
    hierarchy = Hierarchy(name=name, dimension_name=name, elements=elements, element_attributes=element_attributes,
                          edges=edges)

    # create dimension object
    d = Dimension(name=name, hierarchies=[hierarchy])

    # create dimension in TM1 !
    tm1.dimensions.create(d)