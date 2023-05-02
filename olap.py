"""
https://www.cdata.com/kb/tech/azureanalysisservices-python-pandas.rst#:~:text=Python%20Connector%20Libraries%20for%20Azure%20Analysis%20Services%20Data,visualize%20live%20Azure%20Analysis%20Services%20data%20in%20Python.
https://learn.microsoft.com/en-us/answers/questions/274512/connecting-to-azure-analysis-services-using-python.html
https://learn.microsoft.com/en-us/answers/questions/233745/can-adomd-net-core-connect-to-an-ssas-endpoint-fro.html
https://stackoverflow.com/questions/33725862/connecting-to-microsoft-sql-server-using-python/33727190#33727190
https://allentseng92.medium.com/querying-a-ssas-tabular-model-using-r-or-python-1edf46b25c63
https://pypi.org/project/pyadomd/
"""

# Import packages
import config
import pandas as pd
from sys import path

path.append('\\Program Files\\Microsoft.NET\\ADOMD.NET\\130')

from pyadomd import Pyadomd
from azure.identity import ClientSecretCredential

"""
scope = 'https://northeurope.asazure.windows.net/.default'
tenant_id = input('Tenant id: ')
client_id = input('Client id: ')
client_secret = input('Client secret: ')
authority = f'https://login.microsoftonline.com/'

credential = ClientSecretCredential(tenant_id, client_id, client_secret, authority=authority)
token = credential.get_token(scope)
"""

# Build connection string
# conn_str = 'Provider=MSOLAP; Data Source=<YourServerNameHere>; Catalog=<YourCubeNameHere>;'
conn_str = config.rcr_conn_str_test

# Enter DAX or MDX query
dax_query = """Your DAX or MDX query here"""

# Output results as pandas dataframe
with Pyadomd(conn_str) as conn:
    with conn.cursor().execute(dax_query) as cur:
        df = pd.DataFrame(cur.fetchone(),
        columns=[i.name for i in cur.description])

# Rename Columns
df.rename(
    columns={
        "OriginalColumnName1": "NewColumnName1",
        "OriginalColumnName2": "NewColumnName2",
        "OriginalColumnName3": "NewColumnName3"
    },
    inplace = True)

print(df.head())

