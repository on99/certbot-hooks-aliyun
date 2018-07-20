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

request = AddDomainRecordRequest.AddDomainRecordRequest()
request.set_DomainName(os.environ['CERTBOT_DOMAIN'])
request.set_Type('TXT')
request.set_RR('_acme-challenge')
request.set_Value(os.environ['CERTBOT_VALIDATION'])

response = client.do_action_with_exception(request)
print(response)

with open('/tmp/ali-dns-record-id', 'w') as f:
    f.write(json.loads(response)['RecordId'])

sleep(60)
