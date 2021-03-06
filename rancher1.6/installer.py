from fabric import Connection
import os

def connectSSH():
    return Connection(host=os.getenv('FAB_HOST'), user=os.getenv('FAB_USER'))

def updatePackages(conn):
    updateResult = conn.run('sudo apt-get update')

def installHelperPackages(conn):
    helperPackagesResult = conn.run('sudo apt-get install -y apt-transport-https ca-certificates curl software-properties-common')

def addDockerRepo(conn):
    keyResult = conn.run('curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -')
    addRepoResult = conn.run('sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"')

def installDocker(conn):
    installResult = conn.run('sudo apt-get update && sudo apt-get install -y docker-ce')
    gpasswdResult = conn.run('sudo gpasswd -a $USER docker')
    serviceResult = conn.run('sudo systemctl restart docker.service')


if __name__ == '__main__':
    conn = connectSSH()
    updatePackages(conn)
    installHelperPackages(conn)
    addDockerRepo(conn)
    installDocker(conn)