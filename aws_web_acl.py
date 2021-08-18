import boto3
import json
import requests

waf = boto3.client('waf',
	aws_access_key_id='******',
    aws_secret_access_key='******')

def webacl():
	s = input("Enter Web ACL Name: ")
	response = waf.get_change_token()
	response1 = waf.create_web_acl(
    ChangeToken=response['ChangeToken'],
    DefaultAction={
        'Type': 'ALLOW',
    },
    MetricName=s,
    Name=s,
)
	response2 = waf.list_web_acls(Limit=50,)

	for i in response2['WebACLs']:
		if i['Name'] == s:
			match_id = i['WebACLId']
			print(match_id)
	j=1		
	for i in l.readlines():
		ct = waf.get_change_token()
		acl = waf.update_web_acl(
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
