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




import os, sys

def add_argument(argParse, param, env_param, **kwargs):
    if env_param in os.environ:
        kwargs["default"]= os.environ[env_param]
    if "help" not in kwargs:
        kwargs["help"] = "Defaults to env[%s]."%env_param
    argParse.add_argument(param, **kwargs)

def initialize_parser(parser):
    add_argument(parser, '--os-username', "OS_USERNAME", metavar="<auth-user-name>", dest="auth_user_name", action="store")
    add_argument(parser, '--os-password', "OS_PASSWORD", metavar="<auth-password>", dest="auth_password", action="store")
    add_argument(parser, '--os-tenant-name', "OS_TENANT_NAME", metavar="<auth-tenant-name>", dest="auth_tenant_name", action="store")
    add_argument(parser, '--os-auth-url', "OS_AUTH_URL", metavar="<auth-url>", dest="auth_url", action="store")

def ensure_params(parser):
    if parser.auth_user_name is None:
        print 'Either "--os-username <auth-user-name>" is required or the environment variable "OS_USERNAME" must be set.'
        sys.exit(1)
