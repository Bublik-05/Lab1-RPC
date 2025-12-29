# Lab 1 – RPC Implementation on EC2

## Description
This project implements a simple RPC (Remote Procedure Call) system using Python sockets.
A client sends JSON-based RPC requests to a server running on a separate EC2 instance.
The client supports timeout and retry logic to demonstrate failure handling.

## Files
- `rpc_server.py` – RPC server implementation
- `rpc_client.py` – RPC client implementation

## Requirements
- Python 3.x
- Two EC2 instances in the same VPC
- Port 5000 open in the EC2 security group

## How to Run

### 0. Prerequisites
- Two EC2 instances in the same VPC:
  - node-B (server)
  - node-A (client)
- TCP port 5000 is allowed in the Security Group
- Python 3 is installed on both instances

### 1. Start the server (on node-B)
Connect to the server EC2 instance and run:

You should see: RPC Server ready on port 5000

### 2. Get the server private IP (on node-B)
Run: hostname -I


Copy the private IP address (for example: 172.31.x.x).

### 3. Configure the client (on node-A)
Open `rpc_client.py` and set the server private IP address: SERVER_IP = "172.31.x.x"


### 4. Run the client (on node-A)
Connect to the client EC2 instance and run:


### Expected Output
Successful RPC calls return responses with status OK.

Failure demonstration shows timeout and retry behavior:

TIMEOUT -> retry
FAILED after retries

