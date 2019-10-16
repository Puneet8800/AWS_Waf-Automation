import boto3
import json
import requests

dreampay = boto3.client('waf',
	aws_access_key_id='AKIA6NIPWQYHUNP6WWQ6',
    aws_secret_access_key='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')

def webacl():
	s = input("Enter Web ACL Name: ")
	response = dreampay.get_change_token()
	response1 = dreampay.create_web_acl(
    ChangeToken=response['ChangeToken'],
    DefaultAction={
        'Type': 'ALLOW',
    },
    MetricName=s,
    Name=s,
)
	response2 = dreampay.list_web_acls(Limit=50,)

	for i in response2['WebACLs']:
		if i['Name'] == s:
			match_id = i['WebACLId']
			print(match_id)
	j=1		
	for i in l.readlines():
		ct = dreampay.get_change_token()
		acl = dreampay.update_web_acl(
	    WebACLId=match_id,
	    ChangeToken=ct['ChangeToken'],
	    Updates=[
	        {
	            'Action': 'INSERT',
	            'ActivatedRule': {
	                'Priority':j,
	                'RuleId':i ,
	                'Action': {
	                    'Type': 'BLOCK'
	                },
	                'OverrideAction': {
	                    'Type': 'NONE'
	                },
	                'Type': 'REGULAR',
	                
	            }
	        },
	    ],
	    DefaultAction={
	        'Type': 'ALLOW'
	    }
	)
		j+=1



webacl()

