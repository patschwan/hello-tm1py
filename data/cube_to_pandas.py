"""
- Query data from a cube view into a Pandas Dataframe.
http://pandas.pydata.org/

- Calculate statistical measures on dataset (mean, median, std)
"""
import configparser

from TM1py.Services import TM1Service
from TM1py.Utils import Utils

## siehe tm1py samples Original - wegen configparser
# config = configparser.ConfigParser()
# storing the credentials in a file is not recommended for purposes other than testing.
# it's better to setup CAM with SSO or use keyring to store credentials in the windows credential manager. Sample:
# Samples/credentials_best_practice.py
# config.read(r'..\config.ini')

# with TM1Service(**config['tm1srv01']) as tm1:

with TM1Service(address='192.168.80.1', port=52670, user='admin', password='apple', ssl=False) as tm1:
    # define MDX Query
    # basiert auf 24retail SAMPLE TM1 Modell und Cube: Revenue Reporting View: Variance Analysis
    mdx = "SELECT {[product].[Product Total],[product].[Phones],[product].[PCs],[product].[Tablets]} on ROWS, " \
          "{[Version].[Budget],[Version].[Actual],[Version].[Volume Variance]} on COLUMNS  " \
          "FROM [Revenue Reporting] " \
          "WHERE ([organization].[Total Company],[Year].[2020],[Month].[Jun], " \
          "[Revenue].[Gross Revenue],[Channel].[Retail]) "

    # Get data from P&L cube through MDX
    pnl_data = tm1.cubes.cells.execute_mdx(mdx)

    # Build pandas DataFrame fram raw cellset data
    df = Utils.build_pandas_dataframe_from_cellset(pnl_data)

    print(df)

    # Calculate Statistical measures for dataframe
    print(df.describe())