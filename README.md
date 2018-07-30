# certbot-hooks-aliyun
certbot-hooks-aliyun automates letsencrypt creation/renewal for dns managed on aliyun



## Prerequisites

* [certbot](https://certbot.eff.org/docs/install.html)
* python 2.7.x
* pip
* Configure the following environment variables
  * ALI_DNS_ACCESS_KEY_ID, ALI_DNS_ACCESS_KEY_SECRET (Create TXT record in ali dns for dns-01 challenge)
  * ALI_SLB_ACCESS_KEY_ID, ALI_SLB_ACCESS_KEY_SECRET (Upload certs to ali slb)



## Installation



```sh
$ pip install -r requirements.txt
```



## How to use

```sh
# create certs
# NOTE: you can omit --deploy-hook if you do not want to upload certs to ali slb
$ certbot certonly \
	--server https://acme-v02.api.letsencrypt.org/directory \
	--preferred-challenges dns-01 \
	-d *.example.com \
	-d a.example.com \
	-d b.example.com \
	--email you@email.com \
	--eff-email --agree-tos --manual-public-ip-logging-ok \
	--manual \
	--manual-auth-hook ./auth-hook.py \
	--manual-cleanup-hook ./cleanup-hook.py \
	--deploy-hook ./deploy.py

# renew
$ certbot renew
```
