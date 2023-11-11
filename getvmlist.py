import requests
import certifi
import urllib3
http = urllib3.PoolManager(
    	cert_reqs='CERT_REQUIRED', 
    	ca_certs=certifi.where()
	# ca_certs='/Users/salmansiddiqui/anaconda3/lib/python3.11/site-packages/certifi/cacert.pem' # replace with your own 
)
import sys

from urllib3.exceptions import InsecureRequestWarning

'''Variable Initiation'''

ip_addr = 'vmrest.udp1024.com' 
machine_list = ['k8s-master','k8s-worker1','k8s-worker2','k8s-worker3']
authCode = 'c2FsbWFuOm1BbkEoZUQxdkVOdA=='

#resp = requests.get(url='https://' + ip_addr + '/api/vms', headers={'Accept': 'application/vnd.vmware.vmw.rest-v1+json', 'Authorization': 'Basic ' + authCode}, verify=False)

resp = requests.get(url='https://' + ip_addr + '/api/vms', headers={'Accept': 'application/vnd.vmware.vmw.rest-v1+json', 'Authorization': 'Basic ' + authCode})

if resp.status_code != 200:

    #something fell down

    print("Status Code " + resp.status_code + ": Something bad happened")

result_json = resp.json()

print(resp.text)
