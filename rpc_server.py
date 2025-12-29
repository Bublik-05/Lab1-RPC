import socket, json, time

HOST = "0.0.0.0"
PORT = 5000

def add(a, b):
    return a + b

def reverse_string(s):
    return s[::-1]

METHODS = {
    "add": add,
    "reverse_string": reverse_string,
}

def handle_request(raw: str) -> str:
    try:
        req = json.loads(raw)
        request_id = req.get("request_id")
        method = req.get("method")
        params = req.get("params", {})

        # для демонстрации сбоя (задержка)
        if req.get("simulate_delay_seconds"):
            time.sleep(req["simulate_delay_seconds"])

        if method not in METHODS:
            return json.dumps({
                "request_id": request_id,
                "status": "ERROR",
                "error": f"Unknown method: {method}"
            })

        if method == "add":
            result = add(params["a"], params["b"])
        elif method == "reverse_string":
            result = reverse_string(params["s"])

        return json.dumps({
            "request_id": request_id,
            "status": "OK",
            "result": result
        })

    except Exception as e:
        return json.dumps({
            "request_id": None,
            "status": "ERROR",
            "error": str(e)
        })

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(5)
    print(f"RPC Server ready on port {PORT}")

    while True:
        conn, addr = s.accept()
        data = conn.recv(4096).decode("utf-8")
        print(f"[SERVER] from {addr}: {data}")
        resp = handle_request(data)
        conn.sendall(resp.encode("utf-8"))
        conn.close()

if __name__ == "__main__":
    main()
