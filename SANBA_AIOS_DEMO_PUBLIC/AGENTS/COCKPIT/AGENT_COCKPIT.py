"""
S.A.N.B.A. v5.0 - AGENT COCKPIT (demo stub)
Prints status data. No UI is attached in this baseline.
"""


class AgentCockpit:
    def __init__(self):
        print("[AGENT COCKPIT] Demo stub: no UI attached.")

    def render_system_status(self, status_data: dict) -> bool:
        print(f"[AGENT COCKPIT] Status (console only): {status_data}")
        return True
