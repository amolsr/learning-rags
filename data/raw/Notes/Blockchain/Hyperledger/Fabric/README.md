### Setup For 3 Nodes two Channels 
https://medium.com/@kctheservant/demo-of-three-node-two-channel-setup-in-hyperledger-fabric-54ba8a9c461f

### Adding a Node to network
https://medium.com/@kctheservant/add-a-new-organization-on-existing-hyperledger-fabric-network-2c9e303955b2

### Removing a Node from network
https://medium.com/@kctheservant/remove-an-organization-from-a-running-fabric-network-55f52cd0a012


### Create Cryptological Artifacts

```
 ../bin/cryptogen generate --config=./crypto-config.yaml 
 ../bin/configtxgen -profile TwoOrgsOrdererGenesis -outputBlock ./channel-artifacts/genesis.block 
 ../bin/configtxgen -profile Channel -outputCreateChannelTx ./channel-artifacts/channel.tx -channelID channel12 
 
 ```
 
### Inspecting a Certificate

```
 openssl x509 -noout -text -in crypto-config/peerOrganizations/org1.example.com/users/Admin@org1.example.com/msp/signcerts/Admin@org1.example.com-cert.pem
 ```
 
### Compose Docker Images

```
 cd deployment/  
 docker-compose -f docker-compose-orderer.yml up -d 
 docker-compose -f docker-compose-node1.yml up -d 
 docker-compose -f docker-compose-node2.yml up -d 
 ```
 
### Create Channel

```
 docker exec -e "CORE_PEER_MSPCONFIGPATH=/var/hyperledger/users/Admin@org1.example.com/msp" peer0.org1.example.com peer channel create -o orderer.example.com:7050 -c channel12 -f /var/hyperledger/configs/channel.tx 
 docker cp peer0.org1.example.com:channel12.block . 
 docker cp channel12.block peer0.org2.example.com:/channel12.block 
 ```
 
### Join Channel

```
 docker exec -e "CORE_PEER_MSPCONFIGPATH=/var/hyperledger/users/Admin@org2.example.com/msp" peer0.org2.example.com peer channel join -b channel12.block 
 docker exec -e "CORE_PEER_MSPCONFIGPATH=/var/hyperledger/users/Admin@org1.example.com/msp" peer0.org1.example.com peer channel join -b channel12.block  
 ```

### Install Chaincode

```
 docker exec -it cli-org1 peer chaincode install -n mycc -p github.com/chaincode/ATA -v v0 
 docker exec -it cli-org2 peer chaincode install -n mycc -p github.com/chaincode/ATA -v v0 
```

### Instantiate Chaincode

```
 docker exec -it cli-org1 peer chaincode instantiate -o orderer.example.com:7050 -C channel12 -n mycc github.com/chaincode/ATA -v v0 -c '{"Args": []}' -P "OR('Org1MSP.member', 'Org2MSP.member')" 
```

### Testing Purpose

```
docker exec -it cli-org1 peer chaincode invoke -o orderer.example.com:7050 -C channel12 -n mycc -c '{"Args":["assign","abcd","Org2MSP"]}'
docker exec -it cli-org1 peer chaincode query -C channel12 -n mycc -c '{"Args":["read","abcd"]}' 
docker exec -it cli-org1 peer chaincode invoke -o orderer.example.com:7050 -C channel12 -n mycc -c '{"Args":["transfer","abcd","Org1MSP"]}' 
docker exec -it cli-org1 peer chaincode query -C channel12 -n mycc -c '{"Args":["read","abcd"]}'
docker exec -it cli-org2 peer chaincode query -C channel12 -n mycc -c '{"Args":["read","admin"]}'
  ```
  
  
   // only Admin can set value
 x509, _ := cid.GetX509Certificate(stub)
 if x509.Subject.CommonName != "Admin@org1.example.com" {
  return "", fmt.Errorf("Only Admin can set new value.")
 }
