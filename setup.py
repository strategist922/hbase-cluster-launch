

import setuptools

setuptools.setup(
    name="hbase-cluster-launch",
    entry_points={
                 "console_scripts": [
                     "hbase_cluster_launch = hbase_cluster_launcher.nova_launcher:main",
                     "generate_descriptor = hbase_cluster_launcher.descriptor:main"
                 ]
    }
)
