"""
- Create a subset
- Query and manipulate it
- Push it back to TM1
- Delete it
"""
import configparser
import uuid

from TM1py.Objects import Subset
from TM1py.Services import TM1Service

config = configparser.ConfigParser()
# storing the credentials in a file is not recommended for purposes other than testing.
# it's better to setup CAM with SSO or use keyring to store credentials in the windows credential manager. Sample:
# Samples/credentials_best_practice.py
config.read(r'..\config.ini')

with TM1Service(**config['tm1srv01']) as tm1:
    # get a random string that we can use a subset name
    subset_name = str(uuid.uuid4())

    # create subset
    s = Subset(dimension_name='Plan_Department', subset_name=subset_name, alias='', elements=['200', '405', '410'])
    tm1.dimensions.subsets.create(s, True)

    # get it and print out the elements
    s = tm1.dimensions.subsets.get(dimension_name='Plan_Department', subset_name=subset_name, private=True)
    print(s.elements)

    # update it
    s.add_elements(['105', '115'])
    tm1.dimensions.subsets.update(s, True)

    # get it and print out the elements
    s = tm1.dimensions.subsets.get(dimension_name='Plan_Department', subset_name=subset_name, private=True)
    print(s.elements)

    # delete it
    tm1.dimensions.subsets.delete(dimension_name='Plan_Department', subset_name=subset_name, private=True)