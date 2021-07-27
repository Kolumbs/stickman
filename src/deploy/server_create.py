'''Script installs Apache server and deploys it on the system it is run'''
import os
import sys

def status(p):
	r = p.close()
	if r:
		return os.waitstatus_to_exitcode(p.close())
	else:
		return 0

if 'openbsd6' == sys.platform:
	ps = os.popen("pkg_info -e 'apache-httpd->=2.1'")
	if status(ps) == 1:
		print('No Apache server installed')
		sys.exit()
	ps = os.popen("rcctl ls on")
	service = False
	for line in ps.readlines():
		if 'apache2' in line:
			service = True
	if not service:
		if not os.access('/etc/rc.conf.local', os.R_OK):
			print('File /etc/rc.conf.local is not readable or does not exist')
			sys.exit()
		with open('/etc/rc.conf.local') as conf_file:
			conf = False
			for line in conf_file:
				if 'apache2_flags' in line:
					conf = True
		if not conf:
			print('File /etc/rc.conf.local is missing apache2_flags for configuration file')
			sys.exit()
		print('Please enable apache2 server with: rcctl enable apache2')
else:
	print('Platform "' + sys.platform + '" not supported yet')

