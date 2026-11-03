import time
import threading
import json
import socket

print("==================================================================")
print(" S.A.N.B.A. AI-OS v5.0 - LOCAL TWO-NODE TCP DEMO")
print("==================================================================")

class SANBANode:
    def __init__(self, node_id, port, peer_port=None):
        self.node_id = node_id
        self.port = port
        self.peer_port = peer_port
        self.running = True

    def start_listener(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind(('127.0.0.1', self.port))
        server.listen(5)
        print(f"[{self.node_id}] 🌐 Node active on 127.0.0.1:{self.port} (plain Python TCP socket, Erlang bridge not used)")
        
        while self.running:
            try:
                server.settimeout(1.0)
                conn, addr = server.accept()
                data = conn.recv(1024).decode('utf-8')
                if data:
                    msg = json.loads(data)
                    print(f"\n[{self.node_id}] 📩 RECEIVED over TCP from [{msg['sender']}]:")
                    print(f" └─> Task/Payload: '{msg['payload']}'")
                    print(f" └─> Groundlaw audit: not implemented in this demo\n")
                conn.close()
            except socket.timeout:
                continue

    def send_mesh_message(self, target_port, payload):
        time.sleep(1.5)
        print(f"\n[{self.node_id}] 🚀 SENDING over TCP to node on port {target_port}...")
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect(('127.0.0.1', target_port))
            msg = {
                "sender": self.node_id,
                "payload": payload,
                "timestamp": time.time()
            }
            client.send(json.dumps(msg).encode('utf-8'))
            client.close()
            print(f"[{self.node_id}] ✅ Message sent.")
        except Exception as e:
            print(f"[{self.node_id}] ❌ Error sending: {e}")

# 1. Start Node Alpha (Instance 1)
node_alpha = SANBANode("NODE_ALPHA_CRONOS_01", 9001)
t1 = threading.Thread(target=node_alpha.start_listener, daemon=True)
t1.start()

# 2. Start Node Beta (Instance 2)
node_beta = SANBANode("NODE_BETA_CRONOS_02", 9002)
t2 = threading.Thread(target=node_beta.start_listener, daemon=True)
t2.start()

time.sleep(1)
print("\n[DEMO] 🔗 Two local TCP listeners are running (no clustering, no authentication).")

# 3. Simulate distributed task between the 2 nodes
node_alpha.send_mesh_message(9002, "EXECUTE_ORCHESTRATION_TASK: Run Macula Indexing Job")

time.sleep(2)
print("==================================================================")
print(" ✅ DEMO COMPLETE: one message was sent between two local TCP nodes.")
print("==================================================================")