import requests

data = pd.read_csv("report1560963766641.csv",encoding='latin-1')
first3000data=data[:3000]
url = 'https://query.wikidata.org/sparql'
wikidata=[]
for index,grid_id in enumerate(first3000data['GRID Number']):
    if index%50==0:
        print(index)
    query = """
    SELECT ?me ?meLabel ?country ?countryLabel ?geo ?geo2 ?hq ?hqLabel ?street_dep ?post2 ?web ?industry ?industryLabel ?chief ?chiefLabel ?manager ?managerLabel ?annual ?children ?childrenLabel ?employee ?parent ?parentLabel ?post ?location ?locationLabel
    WHERE
    {
      ?me wdt:P2427 '"""+grid_id+"""' .
      optional {?me wdt:P17 ?country }
      optional {?me wdt:P625 ?geo }
      optional {?me wdt:P159 ?hq }
      optional {?hq wdt:P625 ?geo2}
      optional {?hq wdt:P969 ?street_dep}
      optional {?hq wdt:P281 ?post2}
      optional {?me wdt:P856 ?web }
      optional {?me wdt:P452 ?industry }
      optional {?me wdt:P169 ?chief }
      optional {?me wdt:P1037 ?manager }
      optional {?me wdt:P2139 ?annual }
      optional {?me wdt:P335 ?children }
      optional {?me wdt:P1128 ?employee }
      optional {?me wdt:P749 ?parent }
      optional {?me wdt:P281 ?post }
      optional {?me wdt:P131 ?location }
      SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
    }
    limit 1
    """
    try:
        r = requests.get(url, params = {'format': 'json', 'query': query})
        data = r.json()
        data=data['results']['bindings'][0]

    except:
        try:
            query = """
        SELECT ?me ?meLabel ?country ?countryLabel ?geo ?geo2 ?hq ?hqLabel ?street_dep ?post2 ?web ?industry ?industryLabel ?chief ?chiefLabel ?manager ?managerLabel ?annual ?children ?childrenLabel ?employee ?parent ?parentLabel ?post ?location ?locationLabel
        WHERE
        {
          ?me wdt:P2427 '"""+grid_id+"""' .
          optional {?me wdt:P17 ?country }
          optional {?me wdt:P625 ?geo }
          optional {?me wdt:P159 ?hq }
          optional {?hq wdt:P625 ?geo2}
          optional {?hq wdt:P969 ?street_dep}
          optional {?hq wdt:P281 ?post2}
          optional {?me wdt:P856 ?web }
          optional {?me wdt:P452 ?industry }
          optional {?me wdt:P169 ?chief }
          optional {?me wdt:P1037 ?manager }
          optional {?me wdt:P2139 ?annual }
          optional {?me wdt:P335 ?children }
          optional {?me wdt:P1128 ?employee }
          optional {?me wdt:P749 ?parent }
          optional {?me wdt:P281 ?post }
          optional {?me wdt:P131 ?location }

        }
        limit 1
        """
            r = requests.get(url, params = {'format': 'json', 'query': query})
            data = r.json()
            data=data['results']['bindings'][0]
        except:
            print(index,grid_id)
            data={}

    for i in ['me', 'meLabel', 'country', 'countryLabel', 'geo', 'geo2', 'hq', 'hqLabel', 'street_dep', 'post2' ,'web', 'industry' ,'industryLabel' ,'chief' ,'chiefLabel' ,'manager', 'managerLabel', 'annual', 'children', 'childrenLabel' ,'employee', 'parent', 'parentLabel', 'post', 'location','locationLabel']:
        if i not in data.keys():
            data[i]=[]
    wikidata.append(data)
    print(data)

wiki_df = pd.DataFrame(wikidata)
wiki_df.to_csv('wiki_df.csv')
# wiki_df=wiki_df[['me', 'meLabel', 'web', 'industry' ,'industryLabel','country', 'countryLabel', 'hq', 'hqLabel',
#  'street_dep', 'geo', 'geo2','post' ,'post2', 'location','locationLabel',
#  'chief' ,'chiefLabel' ,'manager', 'managerLabel', 'annual',
#  'children', 'childrenLabel' ,'employee', 'parent', 'parentLabel']]

# WikidataAPI_first3000 = pd.concat( [first3000data, wiki_df], axis=1)
# WikidataAPI_first3000.columns = [str(col) + '_wikidataAPI' for col in WikidataAPI_first3000.columns]
# WikidataAPI_first3000.to_csv('WikidataAPI_first3000.csv')  
