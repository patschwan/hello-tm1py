from ops import create as cr
from TM1py.Objects import Dimension, Element, ElementAttribute, Hierarchy

# Definition of Dimesion Region
name='RegionPerFunctionMitSubset'
elements = [Element(name='Europe', element_type='Consolidated'),
            Element(name='CH', element_type='Numeric'),
            Element(name='UK', element_type='Numeric'),
            Element(name='BE', element_type='Numeric')]

edges = {('Europe', 'CH'): 1,
        ('Europe', 'UK'): 1,
        ('Europe', 'BE'): 1}

element_attributes = [ElementAttribute(name='Name Long', attribute_type='Alias'),
                        ElementAttribute(name='Name Short', attribute_type='Alias'),
                        ElementAttribute(name='Currency', attribute_type='String')]

cr.create_dimension(dim_name=name, elements=elements, edges=edges, element_attributes=element_attributes)

