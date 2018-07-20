#!/usr/bin/env python

import os

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkalidns.request.v20150109 import DeleteDomainRecordRequest

client = AcsClient(
    os.environ['ALI_DNS_ACCESS_KEY_ID'],
    os.environ['ALI_DNS_ACCESS_KEY_SECRET'],
    'cn-beijing'
)

request = DeleteDomainRecordRequest.DeleteDomainRecordRequest()
request.set_RecordId(open('/tmp/ali-dns-record-id', 'r').read().rstrip())

response = client.do_action_with_exception(request)
print(response)
