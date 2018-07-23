#!/usr/bin/env python

import os
import json
from time import sleep

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkalidns.request.v20150109 import AddDomainRecordRequest

client = AcsClient(
    os.environ['ALI_DNS_ACCESS_KEY_ID'],
    os.environ['ALI_DNS_ACCESS_KEY_SECRET'],
    'cn-beijing'
)

certbot_domain = os.environ['CERTBOT_DOMAIN']
parts = certbot_domain.split('.')
top_domain = '.'.join(parts[-2:])
rr = '.'.join(['_acme-challenge'] + ([] if len(parts) < 3 else parts[:-2]))

request = AddDomainRecordRequest.AddDomainRecordRequest()
request.set_DomainName(top_domain)
request.set_Type('TXT')
request.set_RR(rr)
request.set_Value(os.environ['CERTBOT_VALIDATION'])

response = client.do_action_with_exception(request)
print('successfully added txt record for challenge validation...')
print(response)

with open('/tmp/ali-dns-record-id', 'w') as f:
    f.write(json.loads(response)['RecordId'])

sleep(60)
