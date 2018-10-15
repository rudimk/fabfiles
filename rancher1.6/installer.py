from fabric import Connection
import os

def connectSSH():
    return Connection(host=os.getenv('FAB_HOST'), user=os.getenv('FAB_USER'))

def updatePackages():
    conn = connectSSH()
    result = conn.run('apt-get update')