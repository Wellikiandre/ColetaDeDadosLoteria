# %%
import requests
import pandas as pd 

# %%
url = 'https://servicebus2.caixa.gov.br/portaldeloterias/api/resultados?modalidade=Lotof%C3%A1cil'
r = requests.get(url, verify=False)
bronze  = r.text
# %%
prata = bronze.replace('''{\r\n  "html": "''','')
prata = prata.replace('''"\r\n}''','')
prata = prata.replace('''\\r\\n''','')
prata = pd.read_html(prata)

# %%
prata_1 = prata[0]
# %%
df_ouro = prata_1[prata_1['Bola1'].notnull()]
# %%
df_ouro