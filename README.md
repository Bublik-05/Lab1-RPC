# Lab 1 – RPC Implementation on EC2

## Description
This project implements a simple RPC (Remote Procedure Call) system using Python sockets.
A client sends JSON-based RPC requests to a server running on a separate EC2 instance.
The client supports timeout and retry logic to demonstrate failure handling.

## Files
- `server.py` – RPC server implementation
- `client.py` – RPC client implementation
- `requirements.txt` – Python dependencies (standard library only)

## Requirements
- Python 3.x
- Two EC2 instances in the same VPC
- Port 5000 open in the EC2 security group

## How to Run

### 1. Start the server (on node-B)
```bash
python3 server.py
