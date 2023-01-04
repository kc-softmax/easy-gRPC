# easy-gRPC
You can easily run the gRPC example.
1. [basic gRPC (Unary, Server streaming)](#1-basic-grpc)
- server : python
- client : python, node
2. [gRPC all service (Unary, Server streaming, Client streaming, Bidirectional streaming)](#2-grpc-all-service)
- server : python
- client : python
3. [gRPC-web (Unary, Server streaming)](#3-grpc-web)
- server : python
- proxy : envoy
- client(browser) : node
---
## Guide
### Requirements
#### [Install the protobuf compiler](https://grpc.io/docs/protoc-installation/)
&nbsp;
&nbsp;
### 1. basic gRPC
#### go to directory
```sh
cd python_basic
```
#### Dependencies
```sh
pip3 install -r requirements.txt
```
#### Compile `helloworld.proto`
```
python3 -m grpc.tools.protoc -I=. \
    --python_out=. --grpc_python_out=. helloworld.proto \
    --mypy_out=readable_stubs:.
```

You should see `helloworld_pb2_grpc.py, helloworld_pb2.py, helloworld_pb2.pyi`
#### Run the server
```sh
python3 python_server.py
```
#### Run the python client
```sh
python3 python_client.py
```
```sh
# client
Greeter client received: hi test, python!

# server
Greeter server received: python
```
#### Run the node client(No Codegen)
```sh
cd node_basic

npm install
node node_client.js
```
> #### Note : [Check Node Version for Grpc PKG](https://github.com/grpc/grpc-node/blob/master/PACKAGE-COMPARISON.md)
```sh
# client
Greeting: hi test, node!

# server
Greeter server received: node
```
## 2. gRPC all service
---
#### Go to directory
```sh
cd python_route_guide
```
#### Dependencies
```sh
pip3 install -r requirements.txt
```
#### compile `route_guide.proto`
```
python3 -m grpc.tools.protoc -I=. \
    --python_out=. \
    --grpc_python_out=. route_guide.proto \
    --mypy_out=readable_stubs:.
```
You should see `route_guide_pb2_grpc.py, route_guide_pb2.py, route_guide_pb2.pyi`
#### Run the server
```sh
python3 route_guide_server.py
```
#### Run the python client
```sh
python3 route_guide_client.py
```
>```sh
># client
>-------------- GetFeature --------------
>Feature called Berkshire Valley Management Area Trail, Jefferson, NJ, USA at latitude: 409146138
>longitude: -746188906
>
>Found no feature at
>-------------- ListFeatures --------------
>...
>```
>Unary(`GetFeature`), Server streaming(`ListFeatures`), Client streaming(`RecordRoute`), Bidirectional streaming(`RouteChat`)

## 3. gRPC-web
---
#### Go to directory
```sh
cd grpc-web
```
#### Run the server
[basic-grpc/run the server](#run-the-server)

#### Run the Envoy(Proxy server)
```sh
# if docker installed and running
docker run -d -v "$(pwd)"/envoy.yaml:/etc/envoy/envoy.yaml:ro \
    -p 8080:8080 -p 9901:9901 envoyproxy/envoy:v1.22.0
```
#### Compile `helloworld.proto`
```sh
protoc -I=. ./helloworld.proto \
  --js_out=import_style=commonjs:. \
  --grpc-web_out=import_style=commonjs,mode=grpcwebtext:.
```
> #### Note : [js compile error(protoc-gen-js' is not recognized as an internal or external command)](https://github.com/protocolbuffers/protobuf-javascript/issues/127)

you should see `helloworld_grpc_web_pb.js, helloworld_pb.js`

#### Install pkg and run the webpack
```sh
npm install
npx webpack client.js
```
you shuld see `dist/main.js`
#### Run the client
```sh
python3 -m http.server 8081 &
```

#### Open a browser and navigate to
```text
localhost:8081
```

#### You should see the following printed out in developer console
```text
hi Sayhello, World!
hi SayReapeatHello, World!
hi SayReapeatHello2, World!
```

---
---
## References
#### [basic gRPC](https://github.com/grpc/grpc/tree/master/examples/python/helloworld)
#### [gRPC all service](https://github.com/grpc/grpc/tree/master/examples/python/route_guide)
#### [gRPC-web](https://github.com/grpc/grpc-web/tree/master/net/grpc/gateway/examples/helloworld)
