#!/usr/bin/env python

import os
from datetime import datetime

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkslb.request.v20140515 import UploadServerCertificateRequest
from retrying import retry

@retry(stop_max_attempt_number=7, wait_fixed=2000)
def upload(domain, fullchain_path, privkey_path):
    client = AcsClient(
        os.environ['ALI_SLB_ACCESS_KEY_ID'],
        os.environ['ALI_SLB_ACCESS_KEY_SECRET'],
        'cn-beijing'
    )

    request = UploadServerCertificateRequest.UploadServerCertificateRequest()
    request.set_ServerCertificate(open(fullchain_path).read().rstrip())
    request.set_PrivateKey(open(privkey_path).read().rstrip())
    request.set_ServerCertificateName(datetime.now().strftime('%Y.%m.%d-%H.%M.%S'))

    client.do_action_with_exception(request)
    print('successfully upload server certificate of %s to ali slb...' % domain)

def deploy():
    live_cert_directory = os.path.dirname(os.environ['RENEWED_LINEAGE'])

    for domain in os.environ['RENEWED_DOMAINS'].split(' '):
        domain = domain.lstrip('*.') # strip *. to support wildcard domain

        fullchain_path = os.path.join(live_cert_directory, domain, 'fullchain.pem')
        privkey_path = os.path.join(live_cert_directory, domain, 'privkey.pem')

        upload(domain, fullchain_path, privkey_path)

deploy()
