
import requests
import pandas as pd
from collections import OrderedDict
import matplotlib.pyplot as plt

# E.g. read in key figures (gdp, average age, population, ...) of all countries.
# only EU countries: ?country wdt:P463 wd:Q458

url = 'https://query.wikidata.org/sparql'
query = """
SELECT
  ?countryLabel ?population ?area ?medianIncome ?age ?nominalGDP
WHERE {
  ?country wdt:P463 wd:Q458
  OPTIONAL { ?country wdt:P1082 ?population }
  OPTIONAL { ?country wdt:P2046 ?area }
  OPTIONAL { ?country wdt:P3529 ?medianIncome }
  OPTIONAL { ?country wdt:P571 ?inception.
    BIND(year(now()) - year(?inception) AS ?age)
  }
  OPTIONAL { ?country wdt:P2131 ?nominalGDP}
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
}
"""

r = requests.get(url, params={'format': 'json', 'query': query})
data = r.json()

countries = []
for item in data['results']['bindings']:
    countries.append(OrderedDict({
        'country': item['countryLabel']['value'],
        'population': item['population']['value'],
        'area': item['area']['value']
            if 'area' in item else None,
        'medianIncome': item['medianIncome']['value']
            if 'medianIncome' in item else None,
        'age': item['age']['value']
            if 'age' in item else None,
        'nominalGDP': item['nominalGDP']['value']
            if 'nominalGDP' in item else None}))

df=pd.DataFrame(countries)
df.set_index('country', inplace=True)
df=df.astype({'population': float, 'area': float, 'medianIncome': float, 'age': float, 'nominalGDP': float})
print(df)