#!/usr/bin/env python

import os
from datetime import datetime

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkslb.request.v20140515 import UploadServerCertificateRequest
from retrying import retry

@retry(stop_max_attempt_number=7, wait_fixed=2000)
def deploy():
    client = AcsClient(
        os.environ['ALI_SLB_ACCESS_KEY_ID'],
        os.environ['ALI_SLB_ACCESS_KEY_SECRET'],
        'cn-beijing'
    )

    request = UploadServerCertificateRequest.UploadServerCertificateRequest()
    request.set_ServerCertificate(open('%s/fullchain.pem' % os.environ['RENEWED_LINEAGE']).read().rstrip())
    request.set_PrivateKey(open('%s/privkey.pem' % os.environ['RENEWED_LINEAGE']).read().rstrip())
    request.set_ServerCertificateName(datetime.now().strftime('%Y.%m.%d-%H.%M.%S'))

    client.do_action_with_exception(request)
    print('successfully upload server certificate to ali slb...')

deploy()
