import os
import argparse
import urllib.request
import sys

#DNSSEC Check
def Checkdnssec(domain):
	val=os.popen(f"dig {domain} +dnssec|egrep -w '^flags|ad'|wc -l")
	val=val.read()
	if int(val) == 0:
		return "DNSSEC Not Exist"
	else:
		return "DNSSEC OK"

#TLS Check
def CheckTls(domain):
	sys.stderr = open("/dev/null")
	result = sys.stderr= urllib.request.urlopen(f"http://www.{domain}").getcode()
	if result:
		return "HTTPS OK"
	else:
		return "HTTPS Not Exist"

#Number NS for domain
def CheckNs(domain):
	result = os.popen(f"dig {domain} |egrep -w 'NS'|wc -l")
	result = result.read().replace('\n',';')
	if result != 0:
		return result
	else:
    		return 0

#Number MX for Domain
def CheckMX(domain):
	result = os.popen(f"dig {domain} MX +short|wc -l")
	result = result.read().replace('\n',';')
	if result != 0:
		return result
	else:
    		return 0

#IPV6 Adresse for domain
def CheckIpv6(domain):
	result=os.popen(f"dig {domain} AAAA +short")
	result=result.read().replace('\n',';')
	if result != " ":
		    return result
	else:
            return "Aucun"
  
#Number ns IPV6 for domain
def CheckNsIpv6(domain):
	result = os.popen(f"dig {domain}|grep -w AAAA|wc -l")
	result = result.read().replace('\n',';')
	if result != 0:
		return result
	else:
		return 0
  
def Checktest(domain):
    result = os.popen(f"{domain}")
    result = result.read().replace('\n',';')
    
    if result != 0:
	    return result

"""Checkdnssec(domain)
CheckTls(domain)
CheckNs(domain)
CheckMX(domain)
CheckIpv6(domain)
CheckNsIpv6(domain)"""

