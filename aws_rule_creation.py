import boto3
import json
import requests

dreampay = boto3.client('waf',
	aws_access_key_id='******',
    aws_secret_access_key='******')


def sqlrule():
	s = input("Enter Sql Rule Name: ")
	response = dreampay.get_change_token()
	response1 = dreampay.create_rule(Name=s,MetricName=s,ChangeToken=response['ChangeToken'])
	response2 = dreampay.list_rules(Limit=50,)

	for i in response2['Rules']:
		if i['Name'] == s:
			match_id = i['RuleId']
			print(match_id)

	ct = dreampay.get_change_token()
	sql = dreampay.update_rule(
    RuleId=match_id,
    ChangeToken=ct['ChangeToken'],
    Updates=[
        {
            'Action': 'INSERT',
            'Predicate': {
                'Negated': False,
                'Type': 'SqlInjectionMatch',
                'DataId': '79e5091c-469b-47ec-b0f7-0ca8b3c2db7d'
            }
        },
    ]
)

def xssrule():
	s = input("Enter XSS Rule Name: ")
	response = dreampay.get_change_token()
	response1 = dreampay.create_rule(Name=s,MetricName=s,ChangeToken=response['ChangeToken'])
	response2 = dreampay.list_rules(Limit=50,)

	for i in response2['Rules']:
		if i['Name'] == s:
			match_id = i['RuleId']
			print(match_id)

	ct = dreampay.get_change_token()
	sql = dreampay.update_rule(
    RuleId=match_id,
    ChangeToken=ct['ChangeToken'],
    Updates=[
        {
            'Action': 'INSERT',
            'Predicate': {
                'Negated': False,
                'Type': 'XssMatch',
                'DataId': '91b63ce2-5925-4f96-a2f2-a268455abd9c'
            }
        },
    ]
)

def sqlsleep():
	s = input("Enter SQL Sleep Rule Name: ")
	response = dreampay.get_change_token()
	response1 = dreampay.create_rule(Name=s,MetricName=s,ChangeToken=response['ChangeToken'])
	response2 = dreampay.list_rules(Limit=50,)

	for i in response2['Rules']:
		if i['Name'] == s:
			match_id = i['RuleId']
			print(match_id)

	ct = dreampay.get_change_token()
	sql = dreampay.update_rule(
    RuleId=match_id,
    ChangeToken=ct['ChangeToken'],
    Updates=[
        {
            'Action': 'INSERT',
            'Predicate': {
                'Negated': False,
                'Type': 'ByteMatch',
                'DataId': 'b49667eb-44dd-4f9a-aa48-f1ce79a0ae57'
            }
        },
    ]
)

def sqlnull():
	s = input("Enter SQL Null Rule Name: ")
	response = dreampay.get_change_token()
	response1 = dreampay.create_rule(Name=s,MetricName=s,ChangeToken=response['ChangeToken'])
	response2 = dreampay.list_rules(Limit=50,)

	for i in response2['Rules']:
		if i['Name'] == s:
			match_id = i['RuleId']
			print(match_id)

	ct = dreampay.get_change_token()
	sql = dreampay.update_rule(
    RuleId=match_id,
    ChangeToken=ct['ChangeToken'],
    Updates=[
        {
            'Action': 'INSERT',
            'Predicate': {
                'Negated': False,
                'Type': 'ByteMatch',
                'DataId': '277293a9-ef7c-4049-bcf2-79d295939da2'
            }
        },
    ]
)

def xforwarded():
	s = input("Enter xforwarded Rule Name: ")
	response = dreampay.get_change_token()
	response1 = dreampay.create_rule(Name=s,MetricName=s,ChangeToken=response['ChangeToken'])
	response2 = dreampay.list_rules(Limit=50,)

	for i in response2['Rules']:
		if i['Name'] == s:
			match_id = i['RuleId']
			print(match_id)

	ct = dreampay.get_change_token()
	sql = dreampay.update_rule(
    RuleId=match_id,
    ChangeToken=ct['ChangeToken'],
    Updates=[
        {
            'Action': 'INSERT',
            'Predicate': {
                'Negated': False,
                'Type': 'RegexMatch',
                'DataId': 'e64c5ccb-4188-40a7-aed6-d78000176afc'
            }
        },
    ]
)

def Geo():
	s = input("Enter Geo Rule Name: ")
	response = dreampay.get_change_token()
	response1 = dreampay.create_rule(Name=s,MetricName=s,ChangeToken=response['ChangeToken'])
	response2 = dreampay.list_rules(Limit=50,)

	for i in response2['Rules']:
		if i['Name'] == s:
			match_id = i['RuleId']
			print(match_id)

	ct = dreampay.get_change_token()
	sql = dreampay.update_rule(
    RuleId=match_id,
    ChangeToken=ct['ChangeToken'],
    Updates=[
        {
            'Action': 'INSERT',
            'Predicate': {
                'Negated': False,
                'Type': 'GeoMatch',
                'DataId': '' #Enter the Geo location ID
            }
        },
    ]
)

def Ip_Match():
	s = input("Enter IP Match Rule Name: ")
	response = dreampay.get_change_token()
	response1 = dreampay.create_rule(Name=s,MetricName=s,ChangeToken=response['ChangeToken'])
	response2 = dreampay.list_rules(Limit=50,)

	for i in response2['Rules']:
		if i['Name'] == s:
			match_id = i['RuleId']
			print(match_id)

	ct = dreampay.get_change_token()
	sql = dreampay.update_rule(
    RuleId=match_id,
    ChangeToken=ct['ChangeToken'],
    Updates=[
        {
            'Action': 'INSERT',
            'Predicate': {
                'Negated': False,
                'Type': 'IPMatch',
                'DataId': '663ddf47-c6a3-4fea-8344-bc3c76702380' 
            }
        },
    ]
)

Ip_Match()
