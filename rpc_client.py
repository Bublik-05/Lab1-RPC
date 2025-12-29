import socket, json, uuid, time

SERVER_IP = "172.31.17.16"   # <-- вставь сюда private IP node-B
PORT = 5000

TIMEOUT_SECONDS = 2
MAX_RETRIES = 3

def rpc_call(method, params, simulate_delay_seconds=None):
    request_id = str(uuid.uuid4())
    req = {
        "request_id": request_id,
        "method": method,
        "params": params
    }
    if simulate_delay_seconds is not None:
        req["simulate_delay_seconds"] = simulate_delay_seconds

    payload = json.dumps(req).encode("utf-8")

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            print(f"[CLIENT] attempt {attempt} request_id={request_id}")
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(TIMEOUT_SECONDS)
            s.connect((SERVER_IP, PORT))
            s.sendall(payload)

            resp_raw = s.recv(4096).decode("utf-8")
            s.close()

            resp = json.loads(resp_raw)
            print("[CLIENT] response:", resp)
            return resp

        except socket.timeout:
            print("[CLIENT] TIMEOUT -> retry")
        except Exception as e:
            print("[CLIENT] ERROR:", e)

        time.sleep(0.5)

    print("[CLIENT] FAILED after retries")
    return None

if __name__ == "__main__":
    # 1) успешный вызов
    rpc_call("add", {"a": 10, "b": 5})

    # 2) успешный вызов
    rpc_call("reverse_string", {"s": "hello"})

    # 3) демонстрация сбоя: сервер “тормозит” 5 сек, клиент timeout+retries
    rpc_call("add", {"a": 1, "b": 2}, simulate_delay_seconds=5)
