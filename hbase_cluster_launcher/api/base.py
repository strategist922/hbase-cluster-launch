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

class VMLaunch:
    def launch_vm(self, config):
        raise Exception("Not Implemented")

    def description(self):
        return None

    def initialize_parser(self, parser):
        parser.set_defaults(vm=self)
        parser.add_argument("descriptor", help="The file containing the cluster descriptor.", type=file)

    def parse(self, args):
        print ""
        print "This VM API has not implemented a command line parser."
        print ""
        raise Exception("Not Implemented")


