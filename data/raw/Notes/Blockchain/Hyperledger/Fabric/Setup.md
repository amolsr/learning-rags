```
sudo apt-get install curl
sudo apt install golang-go
export GOPATH=$HOME/go
export PATH=$PATH:$GOPATH/bin
sudo apt-get install nodejs
sudo apt-get install npm
sudo apt-get install python
sudo apt install docker.io
sudo apt-get update
apt-cache policy docker-ce
sudo apt-get install -y docker-ce
sudo apt-get install docker-compose
sudo apt-get upgrade

curl -sSL http://bit.ly/2ysbOFE | bash -s -- 1.4.6 1.4.6 0.4.18
sudo chmod 777 -R fabric-samples
cd fabric-samples/first-network
./byfn.sh generate
./byfn.sh up
./byfn.sh down
```
