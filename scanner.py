from tld import get_tld
import os
import urllib.request
import io

def get_domain_name(url):
	domain_name = get_tld(url)
	return domain_name

def get_ip(domain_url):
	command = "host " + domain_url
	process = os.popen(command)
	data = str(process.read())
	ip = data[len(domain_url)+13:].splitlines()[0]
	return ip

def nmap_output(domain_url):
	command = "nmap " + domain_url
	process = os.popen(command)
	data = str(process.read())
	return data

def robots_txt_downloader(url):
	if url.endswith('/'):
		path = url
	else:
		path = url + '/'

	req = urllib.request.urlopen(path + "robots.txt",data = None)
	data = io.TextIOWrapper(req,encoding = 'utf-8')
	return data.read()

def whois(url):
	command = "whois " + url
	process = os.popen(command)
	data = str(process.read())
	return data
