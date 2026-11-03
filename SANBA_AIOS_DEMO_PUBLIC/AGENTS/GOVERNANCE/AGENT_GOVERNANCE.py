"""
S.A.N.B.A. v5.0 - AGENT GOVERNANCE
Audits agent requests. Command requests are checked by the sandbox guard
allowlist; requests that carry no command are denied (deny by default).
"""

from AGENTS.GOVERNANCE.AGENT_SANDBOX_GUARD import SandboxGuardAgent


class AgentGovernance:
    def __init__(self):
        self.guard = SandboxGuardAgent()
        print("[AGENT GOVERNANCE] Initialized. Requests are checked against the command allowlist.")

    def audit_agent_request(self, agent_name: str, action: str, parameters: dict) -> bool:
        print(f"[AGENT GOVERNANCE] Auditing action '{action}' from agent '{agent_name}'...")
        return self.guard.validate_action(agent_name, action, parameters)
