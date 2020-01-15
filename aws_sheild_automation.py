import boto3
import json
shield = boto3.client('shield',region_name='us-east-1',aws_access_key_id='xxxxxx',aws_secret_access_key='xxxx')
shield_paginator  = shield.get_paginator('list_protections')
shield_protected_cf_list = []
shield_page_iterator = shield_paginator.paginate()
print(shield_page_iterator)
for page in shield_page_iterator:
    for cf in page['Protections']:
        shield_protected_cf_list.append(cf['ResourceArn'])
cf = boto3.client('cloudfront')
cf_paginator = cf.get_paginator('list_distributions')
cf_page_iterator = cf_paginator.paginate()

for page in cf_page_iterator:
    if page['DistributionList']['Quantity'] > 0:
        for i in page['DistributionList']['Items']:
            if i['ARN'] not in shield_protected_cf_list:
                print(i['ARN'],i['Id'],)

