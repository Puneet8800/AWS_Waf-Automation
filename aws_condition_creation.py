import boto3
import json
import requests

dreampay = boto3.client('waf',
	aws_access_key_id='AKIA6NIPWQYHUNP6WWQ6',
    aws_secret_access_key='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')

def sql():
	s = input("Enter Sql Injection Condition Name: ")
	response = dreampay.get_change_token()
	response1 = dreampay.create_sql_injection_match_set(Name=s, ChangeToken=response['ChangeToken'])
	response2 = dreampay.list_sql_injection_match_sets(Limit=5,)
	for i in response2['SqlInjectionMatchSets']:
		if i['Name'] == s:
			match_id = i['SqlInjectionMatchSetId']
			print(match_id)
	ct = dreampay.get_change_token()
	sql = dreampay.update_sql_injection_match_set(
    SqlInjectionMatchSetId=match_id,
    ChangeToken=ct['ChangeToken'],
    Updates=[
        {
            'Action': 'INSERT',
            'SqlInjectionMatchTuple': {
                'FieldToMatch': {
                    'Type': 'URI',
                },
                'TextTransformation': 'URL_DECODE'
            }
        },
    ]
)
	ct = dreampay.get_change_token()
	sql = dreampay.update_sql_injection_match_set(
    SqlInjectionMatchSetId=match_id,
    ChangeToken=ct['ChangeToken'],
    Updates=[
        {
            'Action': 'INSERT',
            'SqlInjectionMatchTuple': {
                'FieldToMatch': {
                    'Type': 'URI',
                },
                'TextTransformation': 'HTML_ENTITY_DECODE'
            }
        },
    ]
)
	ct = dreampay.get_change_token()
	sql = dreampay.update_sql_injection_match_set(
    SqlInjectionMatchSetId=match_id,
    ChangeToken=ct['ChangeToken'],
    Updates=[
        {
            'Action': 'INSERT',
            'SqlInjectionMatchTuple': {
                'FieldToMatch': {
                    'Type': 'HEADER',
                    'Data': 'cookie'
                },
                'TextTransformation': 'URL_DECODE'
            }
        },
    ]
)
	ct = dreampay.get_change_token()
	sql = dreampay.update_sql_injection_match_set(
    SqlInjectionMatchSetId=match_id,
    ChangeToken=ct['ChangeToken'],
    Updates=[
        {
            'Action': 'INSERT',
            'SqlInjectionMatchTuple': {
                'FieldToMatch': {
                    'Type': 'HEADER',
                    'Data': 'cookie'
                },
                'TextTransformation': 'HTML_ENTITY_DECODE'
            }
        },
    ]
)
	ct = dreampay.get_change_token()
	sql = dreampay.update_sql_injection_match_set(
    SqlInjectionMatchSetId=match_id,
    ChangeToken=ct['ChangeToken'],
    Updates=[
        {
            'Action': 'INSERT',
            'SqlInjectionMatchTuple': {
                'FieldToMatch': {
                    'Type': 'HEADER',
                    'Data':'user-agent'
                },
                'TextTransformation': 'URL_DECODE'
            }
        },
    ]
)
	ct = dreampay.get_change_token()
	sql = dreampay.update_sql_injection_match_set(
    SqlInjectionMatchSetId=match_id,
    ChangeToken=ct['ChangeToken'],
    Updates=[
        {
            'Action': 'INSERT',
            'SqlInjectionMatchTuple': {
                'FieldToMatch': {
                    'Type': 'HEADER',
                    'Data': 'user-agent'
                },
                'TextTransformation': 'HTML_ENTITY_DECODE'
            }
        },
    ]
)
	ct = dreampay.get_change_token()
	sql = dreampay.update_sql_injection_match_set(
    SqlInjectionMatchSetId=match_id,
    ChangeToken=ct['ChangeToken'],
    Updates=[
        {
            'Action': 'INSERT',
            'SqlInjectionMatchTuple': {
                'FieldToMatch': {
                    'Type': 'BODY',
                },
                'TextTransformation': 'URL_DECODE'
            }
        },
    ]
)
	ct = dreampay.get_change_token()
	sql = dreampay.update_sql_injection_match_set(
    SqlInjectionMatchSetId=match_id,
    ChangeToken=ct['ChangeToken'],
    Updates=[
        {
            'Action': 'INSERT',
            'SqlInjectionMatchTuple': {
                'FieldToMatch': {
                    'Type': 'BODY',
                },
                'TextTransformation': 'HTML_ENTITY_DECODE'
            }
        },
    ]
)
	ct = dreampay.get_change_token()
	sql = dreampay.update_sql_injection_match_set(
    SqlInjectionMatchSetId=match_id,
    ChangeToken=ct['ChangeToken'],
    Updates=[
        {
            'Action': 'INSERT',
            'SqlInjectionMatchTuple': {
                'FieldToMatch': {
                    'Type': 'QUERY_STRING',
                },
                'TextTransformation': 'URL_DECODE'
            }
        },
    ]
)
	ct = dreampay.get_change_token()
	sql = dreampay.update_sql_injection_match_set(
    SqlInjectionMatchSetId=match_id,
    ChangeToken=ct['ChangeToken'],
    Updates=[
        {
            'Action': 'INSERT',
            'SqlInjectionMatchTuple': {
                'FieldToMatch': {
                    'Type': 'QUERY_STRING',
                },
                'TextTransformation': 'HTML_ENTITY_DECODE'
            }
        },
    ]
)

def xss():
	s = input("Enter XSS Condition Name: ")
	response = dreampay.get_change_token()
	response1 = dreampay.create_xss_match_set(Name=s, ChangeToken=response['ChangeToken'])
	response2 = dreampay.list_xss_match_sets(Limit=5,)
	for i in response2['XssMatchSets']:
		if i['Name'] == s:
			match_id = i['XssMatchSetId']
			print(match_id)
	ct = dreampay.get_change_token()
	xss = dreampay.update_xss_match_set(
    XssMatchSetId=match_id,
    ChangeToken=ct['ChangeToken'],
    Updates=[
        {
            'Action': 'INSERT',
            'XssMatchTuple': {
                'FieldToMatch': {
                    'Type': 'URI',
                },	
                'TextTransformation': 'URL_DECODE'
            }
        },
    ]

)
	ct = dreampay.get_change_token()
	xss = dreampay.update_xss_match_set(
    XssMatchSetId=match_id,
    ChangeToken=ct['ChangeToken'],
    Updates=[
        {
            'Action': 'INSERT',
            'XssMatchTuple': {
                'FieldToMatch': {
                    'Type': 'URI',
                },
                'TextTransformation': 'HTML_ENTITY_DECODE'
            }
        },
    ]
)
	ct = dreampay.get_change_token()
	xss = dreampay.update_xss_match_set(
    XssMatchSetId=match_id,
    ChangeToken=ct['ChangeToken'],
    Updates=[
        {
            'Action': 'INSERT',
            'XssMatchTuple': {
                'FieldToMatch': {
                    'Type': 'BODY',
                },
                'TextTransformation': 'URL_DECODE'
            }
        },
    ]
)
	ct = dreampay.get_change_token()
	xss = dreampay.update_xss_match_set(
    XssMatchSetId=match_id,
    ChangeToken=ct['ChangeToken'],
    Updates=[
        {
            'Action': 'INSERT',
            'XssMatchTuple': {
                'FieldToMatch': {
                    'Type': 'BODY',
                },
                'TextTransformation': 'HTML_ENTITY_DECODE'
            }
        },
    ]
)
	ct = dreampay.get_change_token()
	xss = dreampay.update_xss_match_set(
    XssMatchSetId=match_id,
    ChangeToken=ct['ChangeToken'],
    Updates=[
        {
            'Action': 'INSERT',
            'XssMatchTuple': {
                'FieldToMatch': {
                    'Type': 'QUERY_STRING',
                },
                'TextTransformation': 'URL_DECODE'
            }
        },
    ]
)
	ct = dreampay.get_change_token()
	xss = dreampay.update_xss_match_set(
    XssMatchSetId=match_id,
    ChangeToken=ct['ChangeToken'],
    Updates=[
        {
            'Action': 'INSERT',
            'XssMatchTuple': {
                'FieldToMatch': {
                    'Type': 'QUERY_STRING',
                },
                'TextTransformation': 'HTML_ENTITY_DECODE'
            }
        },
    ]
)
	ct = dreampay.get_change_token()
	xss = dreampay.update_xss_match_set(
    XssMatchSetId=match_id,
    ChangeToken=ct['ChangeToken'],
    Updates=[
        {
            'Action': 'INSERT',
            'XssMatchTuple': {
                'FieldToMatch': {
                    'Type': 'HEADER',
                    'Data': 'cookie'
                },
                'TextTransformation': 'URL_DECODE'
            }
        },
    ]
)
	ct = dreampay.get_change_token()
	xss = dreampay.update_xss_match_set(
    XssMatchSetId=match_id,
    ChangeToken=ct['ChangeToken'],
    Updates=[
        {
            'Action': 'INSERT',
            'XssMatchTuple': {
                'FieldToMatch': {
                    'Type': 'HEADER',
                    'Data': 'cookie'
                },
                'TextTransformation': 'HTML_ENTITY_DECODE'
            }
        },
    ]
)
	ct = dreampay.get_change_token()
	xss = dreampay.update_xss_match_set(
    XssMatchSetId=match_id,
    ChangeToken=ct['ChangeToken'],
    Updates=[
        {
            'Action': 'INSERT',
            'XssMatchTuple': {
                'FieldToMatch': {
                    'Type': 'HEADER',
                    'Data': 'user-agent'
                },
                'TextTransformation': 'URL_DECODE'
            }
        },
    ]
)
	ct = dreampay.get_change_token()
	xss = dreampay.update_xss_match_set(
    XssMatchSetId=match_id,
    ChangeToken=ct['ChangeToken'],
    Updates=[
        {
            'Action': 'INSERT',
            'XssMatchTuple': {
                'FieldToMatch': {
                    'Type': 'HEADER',
                    'Data': 'user-agent'
                },
                'TextTransformation': 'HTML_ENTITY_DECODE'
            }
        },
    ]
)


def string_match_sql_null():
	s = input("Enter Sql Null String Match Condition Name: ")
	response = dreampay.get_change_token()
	response1 = dreampay.create_byte_match_set(Name=s, ChangeToken=response['ChangeToken'])
	response2 = dreampay.list_byte_match_sets(Limit=5,)
	for i in response2['ByteMatchSets']:
		if i['Name'] == s:
			match_id = i['ByteMatchSetId']
			print(match_id)
	ct = dreampay.get_change_token()
	string_match = dreampay.update_byte_match_set(
    ByteMatchSetId=match_id,
    ChangeToken=ct['ChangeToken'],
    Updates=[
        {
            'Action': 'INSERT',
            'ByteMatchTuple': {
                'FieldToMatch': {
                    'Type': 'URI',
                    
                },
                'TargetString': b'select ifnull',
                'TextTransformation': 'LOWERCASE',
                'PositionalConstraint': 'CONTAINS'
            }
        },
    ]
)
	ct = dreampay.get_change_token()
	string_match = dreampay.update_byte_match_set(
    ByteMatchSetId=match_id,
    ChangeToken=ct['ChangeToken'],
    Updates=[
        {
            'Action': 'INSERT',
            'ByteMatchTuple': {
                'FieldToMatch': {
                    'Type': 'HEADER',
                    'Data': 'cookie'
                    
                },
                'TargetString': b'select ifnull',
                'TextTransformation': 'LOWERCASE',
                'PositionalConstraint': 'CONTAINS'
            }
        },
    ]
)
	ct = dreampay.get_change_token()
	string_match = dreampay.update_byte_match_set(
    ByteMatchSetId=match_id,
    ChangeToken=ct['ChangeToken'],
    Updates=[
        {
            'Action': 'INSERT',
            'ByteMatchTuple': {
                'FieldToMatch': {
                    'Type': 'HEADER',
                    'Data': 'referer'
                    
                },
                'TargetString': b'select ifnull',
                'TextTransformation': 'LOWERCASE',
                'PositionalConstraint': 'CONTAINS'
            }
        },
    ]
)
	ct = dreampay.get_change_token()
	string_match = dreampay.update_byte_match_set(
    ByteMatchSetId=match_id,
    ChangeToken=ct['ChangeToken'],
    Updates=[
        {
            'Action': 'INSERT',
            'ByteMatchTuple': {
                'FieldToMatch': {
                    'Type': 'HEADER',
                    "Data": 'user-agent'
                },
                'TargetString': b'select ifnull',
                'TextTransformation': 'LOWERCASE',
                'PositionalConstraint': 'CONTAINS'
            }
        },
    ]
)
	ct = dreampay.get_change_token()
	string_match = dreampay.update_byte_match_set(
    ByteMatchSetId=match_id,
    ChangeToken=ct['ChangeToken'],
    Updates=[
        {
            'Action': 'INSERT',
            'ByteMatchTuple': {
                'FieldToMatch': {
                    'Type': 'BODY',
                    
                },
                'TargetString': b'select ifnull',
                'TextTransformation': 'LOWERCASE',
                'PositionalConstraint': 'CONTAINS'
            }
        },
    ]
)
	ct = dreampay.get_change_token()
	string_match = dreampay.update_byte_match_set(
    ByteMatchSetId=match_id,
    ChangeToken=ct['ChangeToken'],
    Updates=[
        {
            'Action': 'INSERT',
            'ByteMatchTuple': {
                'FieldToMatch': {
                    'Type': 'QUERY_STRING',
                    
                },
                'TargetString': b'select ifnull',
                'TextTransformation': 'LOWERCASE',
                'PositionalConstraint': 'CONTAINS'
            }
        },
    ]
)

def string_match_sql_sleep():
	s = input("Enter Sql Sleep String Match Condition Name: ")
	response = dreampay.get_change_token()
	response1 = dreampay.create_byte_match_set(Name=s, ChangeToken=response['ChangeToken'])
	response2 = dreampay.list_byte_match_sets(Limit=5,)
	for i in response2['ByteMatchSets']:
		if i['Name'] == s:
			match_id = i['ByteMatchSetId']
			print(match_id)
	ct = dreampay.get_change_token()
	string_match = dreampay.update_byte_match_set(
    ByteMatchSetId=match_id,
    ChangeToken=ct['ChangeToken'],
    Updates=[
        {
            'Action': 'INSERT',
            'ByteMatchTuple': {
                'FieldToMatch': {
                    'Type': 'URI',
                    
                },
                'TargetString': b'sleep',
                'TextTransformation': 'LOWERCASE',
                'PositionalConstraint': 'CONTAINS'
            }
        },
    ]
)
	ct = dreampay.get_change_token()
	string_match = dreampay.update_byte_match_set(
    ByteMatchSetId=match_id,
    ChangeToken=ct['ChangeToken'],
    Updates=[
        {
            'Action': 'INSERT',
            'ByteMatchTuple': {
                'FieldToMatch': {
                    'Type': 'HEADER',
                    'Data': 'cookie'
                    
                },
                'TargetString': b'sleep',
                'TextTransformation': 'LOWERCASE',
                'PositionalConstraint': 'CONTAINS'
            }
        },
    ]
)
	ct = dreampay.get_change_token()
	string_match = dreampay.update_byte_match_set(
    ByteMatchSetId=match_id,
    ChangeToken=ct['ChangeToken'],
    Updates=[
        {
            'Action': 'INSERT',
            'ByteMatchTuple': {
                'FieldToMatch': {
                    'Type': 'HEADER',
                    'Data': 'referer'
                    
                },
                'TargetString': b'sleep',
                'TextTransformation': 'LOWERCASE',
                'PositionalConstraint': 'CONTAINS'
            }
        },
    ]
)
	ct = dreampay.get_change_token()
	string_match = dreampay.update_byte_match_set(
    ByteMatchSetId=match_id,
    ChangeToken=ct['ChangeToken'],
    Updates=[
        {
            'Action': 'INSERT',
            'ByteMatchTuple': {
                'FieldToMatch': {
                    'Type': 'HEADER',
                    "Data": 'user-agent'
                },
                'TargetString': b'sleep',
                'TextTransformation': 'LOWERCASE',
                'PositionalConstraint': 'CONTAINS'
            }
        },
    ]
)
	ct = dreampay.get_change_token()
	string_match = dreampay.update_byte_match_set(
    ByteMatchSetId=match_id,
    ChangeToken=ct['ChangeToken'],
    Updates=[
        {
            'Action': 'INSERT',
            'ByteMatchTuple': {
                'FieldToMatch': {
                    'Type': 'BODY',
                    
                },
                'TargetString': b'sleep',
                'TextTransformation': 'LOWERCASE',
                'PositionalConstraint': 'CONTAINS'
            }
        },
    ]
)
	ct = dreampay.get_change_token()
	string_match = dreampay.update_byte_match_set(
    ByteMatchSetId=match_id,
    ChangeToken=ct['ChangeToken'],
    Updates=[
        {
            'Action': 'INSERT',
            'ByteMatchTuple': {
                'FieldToMatch': {
                    'Type': 'QUERY_STRING',
                    
                },
                'TargetString': b'sleep',
                'TextTransformation': 'LOWERCASE',
                'PositionalConstraint': 'CONTAINS'
            }
        },
    ]
)

def regex():
	s = input("Enter Pattern Set Condition Name: ")

	response = dreampay.get_change_token()
	response1 = dreampay.create_regex_pattern_set(Name=s, ChangeToken=response['ChangeToken'])
	response2 = dreampay.list_regex_pattern_sets(Limit=5,)
	for i in response2['RegexPatternSets']:
		if i['Name'] == s:
			pid = i['RegexPatternSetId']	
			print(pid)
	ct = dreampay.get_change_token()
	pattern = dreampay.update_regex_pattern_set(
    RegexPatternSetId=pid,
    Updates=[
        {
            'Action': 'INSERT',
            'RegexPatternString': '.+?'
        },
    ],
    ChangeToken=ct['ChangeToken']
)
	s = input("Enter Regex Set Condition Name: ")

	response = dreampay.get_change_token()
	response1 = dreampay.create_regex_match_set(Name=s, ChangeToken=response['ChangeToken'])
	response2 = dreampay.list_regex_match_sets(Limit=5,)
	for i in response2['RegexMatchSets']:
		if i['Name'] == s:
			match_id = i['RegexMatchSetId']	
			print(match_id)
	ct = dreampay.get_change_token()
	response = dreampay.update_regex_match_set(
    RegexMatchSetId=match_id,
    Updates=[
        {
            'Action': 'INSERT',
            'RegexMatchTuple': {
                'FieldToMatch': {
                    'Type': 'HEADER',
                    'Data': 'x-forwarded-host'
                },
                'TextTransformation': 'LOWERCASE',
                'RegexPatternSetId': pid
            }
        },
    ],
    ChangeToken=ct['ChangeToken']
)

def ip_allowed():
	s = input("Enter IP Allowed Condition Name: ")

	response = dreampay.get_change_token()
	response1 = dreampay.create_ip_set(Name=s, ChangeToken=response['ChangeToken'])
	response2 = dreampay.list_ip_sets(Limit=5,)
	for i in response2['IPSets']:
		if i['Name'] == s:
			match_id = i['IPSetId']	
			print(match_id)
	ct = dreampay.get_change_token()		

	Updateset=[{'Action': 'INSERT','IPSetDescriptor': {'Type': 'IPV4','Value': '1.1.1.1/32'}},]
	response = dreampay.update_ip_set(IPSetId=match_id,ChangeToken=ct['ChangeToken'],Updates=Updateset)


def geo_block():
	s = input("Enter Geo Block Condition Name: ")

	response = dreampay.get_change_token()
	response1 = dreampay.create_geo_match_set(Name=s, ChangeToken=response['ChangeToken'])
	response2 = dreampay.list_geo_match_sets(Limit=5,)
	for i in response2['GeoMatchSets']:
		if i['Name'] == s:
			match_id = i['GeoMatchSetId']	
			print(match_id)
	ct = dreampay.get_change_token()
	response = dreampay.update_geo_match_set(
    GeoMatchSetId=match_id,
    ChangeToken=ct['ChangeToken'],
    Updates=[
        {
            'Action': 'INSERT',
            'GeoMatchConstraint': {
                'Type': 'Country',
                'Value': 'AF'
            }
        },
    ]
)




sql()
xss()
string_match_sql_null()
string_match_sql_sleep()
regex()
ip_allowed()
geo_block()

