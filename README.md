# certbot-hooks
certbot-hooks is created for letsencrypt automation



## Prerequisites

* [certbot](https://certbot.eff.org/docs/install.html)
* python 2.7.x
* pip

* Ali dns/slb full permission is needed for the script, configure the following environment variables
  * ALI_DNS_ACCESS_KEY_ID
  * ALI_DNS_ACCESS_KEY_SECRET
  * ALI_SLB_ACCESS_KEY_ID
  * ALI_SLB_ACCESS_KEY_SECRET



## Installation



```sh
$ pip install -r requirements.txt
```



## How to use

```sh
# create a cert
$ certbot --server https://acme-v02.api.letsencrypt.org/directory -d *.example.com --manual --preferred-challenges dns-01 --email you@email.com --eff-email --agree-tos --manual-public-ip-logging-ok --manual-auth-hook ./auth-hook.py --manual-cleanup-hook ./cleanup-hook.py --deploy-hook ./deploy.py certonly

# renew
$ certbot renew
```

