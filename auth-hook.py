#!/usr/bin/env python

import os
import json
from time import sleep
import tld

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkalidns.request.v20150109 import AddDomainRecordRequest
from retrying import retry

@retry(stop_max_attempt_number=7, wait_fixed=2000)
def auth():
    client = AcsClient(
        os.environ['ALI_DNS_ACCESS_KEY_ID'],
        os.environ['ALI_DNS_ACCESS_KEY_SECRET'],
        'cn-beijing'
    )

    certbot_domain = os.environ['CERTBOT_DOMAIN']
    domain = tld.get_tld(certbot_domain, as_object=True, fix_protocol=True)
    top_domain = domain.fld
    rr = '.'.join(['_acme-challenge'] + ([] if len(domain.subdomain) == 0 else [domain.subdomain]))

    request = AddDomainRecordRequest.AddDomainRecordRequest()
    request.set_DomainName(top_domain)
    request.set_Type('TXT')
    request.set_RR(rr)
    request.set_Value(os.environ['CERTBOT_VALIDATION'])

    response = client.do_action_with_exception(request)
    print('successfully added txt record for challenge validation...')
    print(response)

    with open('/tmp/ali-dns-record-id-%s' % certbot_domain, 'w') as f:
        f.write(json.loads(response)['RecordId'])

auth()
sleep(60)
