## ssh into instance, while exposing remote port for remote VS Code
```
ssh -i {path-to-keyfile}.pem -R 52698:localhost:52698 {Username}@{instance-ip}
```
