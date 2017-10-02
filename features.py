from pandas import DataFrame

def feature_extraction(json_data):
    columns = ['id','name','lat','lon','coordinates','address','city','seller_id','price', 'accessible', 'valet', 'security', 'restrooms', 'printed_pass', 'reentry_allowed']
    frame = DataFrame(columns=columns)

    for i, event in enumerate(json_data):
        try:
            dict0={}
            dict0['id'] = event['_embedded']['pw:location']['id']
            dict0['name'] = event['_embedded']['pw:location']['name']
            dict0['lat'] = float(event['_embedded']['pw:location']['entrances'][0]['coordinates'][0])
            dict0['lon'] = float(event['_embedded']['pw:location']['entrances'][0]['coordinates'][1])
            dict0['coordinates'] = event['_embedded']['pw:location']['entrances'][0]['coordinates']
            dict0['address'] = event['_embedded']['pw:location']['address1']
            dict0['city'] = event['_embedded']['pw:location']['city']
            dict0['seller_id'] = event['seller_id']
            dict0['price'] = float(event['purchase_options'][0]['price']['USD'])

            amenities = event['purchase_options'][0]['amenities']
            for item in amenities:
                if item['name'] == 'Accessible':
                    dict0['accessible'] = item['enabled']
                if item['name'] == 'Valet':
                    dict0['valet'] = item['enabled']
                if item['name'] == 'Security':
                    dict0['security'] = item['enabled']
                if item['name'] == 'Restrooms':
                    dict0['restrooms'] = item['enabled']
                if item['name'] == 'Printed Pass':
                    dict0['printed_pass'] = item['enabled']
                if item['name'] == 'Reentry Allowed':
                    dict0['reentry_allowed'] = item['enabled']
            # Checks if it is accessible, if there is valet, security, restrooms, printed pass, re-entry allowed
            for key in dict0:
                frame.loc[i,key] = dict0[key]
        except Exception:
            pass
    return frame