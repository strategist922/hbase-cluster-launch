#hbase_cluster-launcher is a tool for launching HBase clusters on
#Openstack clouds
#
#Copyright (C) 2013  NigelB
#
#This program is free software; you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation; either version 2 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License along
#with this program; if not, write to the Free Software Foundation, Inc.,
#51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

mime_types = {
    '#include' :        'text/x-include-url',
    '#!' :              'text/x-shellscript',
    '#cloud-config' :   'text/cloud-config',
    '#upstart-job' :    'text/upstart-job',
    '#part-handler' :   'text/part-handler',
    '#cloud-boothook' : 'text/cloud-boothook'
}

def find_mimetype(data, default=""):
    for key in mime_types:
        if data.startswith(key):
            return mime_types[key]
    return default

def encode(files, template_dictionary, boundary=None):
    msg = MIMEMultipart(boundary=boundary)
    files.sort()
    for fl in files:
        f = open(fl)
        data = f.read()
        f.close()
        mime_type = find_mimetype(data).split("/")
        data, filename = (data, fl)
        maintype, subtype =  mime_type
        entry = MIMEText(data, subtype)
        entry.add_header("Content-Disposition", "attachment", filename=os.path.basename(filename))
        msg.attach(entry)

    return msg.as_string(unixfrom=False)