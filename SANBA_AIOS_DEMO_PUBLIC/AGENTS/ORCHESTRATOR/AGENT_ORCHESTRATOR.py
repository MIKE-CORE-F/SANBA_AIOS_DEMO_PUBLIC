"""
MIKE-CORE AI-OS FUSION 5.0 - SANBA
Module: AGENT_ORCHESTRATOR (Samba Orchestration Engine with Telemetry)
Location: AGENTS/ORCHESTRATOR/AGENT_ORCHESTRATOR.py
"""

import logging
from AGENTS.GOVERNANCE.AGENT_SANDBOX_GUARD import SandboxGuardAgent
from AGENTS.ROUTER.AGENT_MCP_ROUTER import MCPRouterAgent
from AGENTS.SPECIALIZED.AGENT_EXECUTOR import ExecutorAgent
from AGENTS.TELEMETRY.AGENT_TELEMETRY import TelemetryAgent

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")
logger = logging.getLogger("Orchestrator")

class SambaOrchestrator:
    def __init__(self):
        self.guard = SandboxGuardAgent()
        self.router = MCPRouterAgent()
        self.executor = ExecutorAgent()
        self.telemetry = TelemetryAgent()
        
        # Register the executor on the MCP Router bus
        self.router.register_agent("EXECUTOR", lambda envelope: self._handle_executor_task(envelope))

    def dispatch_user_request(self, user_prompt: str, target_command: str):
        """Processes a request through the secure Samba pipeline and logs everything."""
        logger.info(f"[ORCHESTRATOR] Received request: '{user_prompt}'")
        self.telemetry.log_event("USER_REQUEST_RECEIVED", {"prompt": user_prompt, "target": target_command})

        # 1. Security check via Sandbox Guard
        payload = {"command": target_command}
        if not self.guard.validate_action("ORCHESTRATOR", "EXEC", payload):
            logger.warning(f"[ORCHESTRATOR] Action blocked by Sandbox Guard.")
            self.telemetry.log_event("SECURITY_BLOCKED", {"command": target_command})
            return {"status": "BLOCKED", "reason": "Security policy violated"}

        # 2. Route via the MCP bus to the Executor
        mcp_res = self.router.send_mcp_message(
            sender="ORCHESTRATOR",
            recipient="EXECUTOR",
            action="RUN_COMMAND",
            data={"command": target_command}
        )

        self.telemetry.log_event("TASK_EXECUTED", mcp_res)
        return mcp_res

    def _handle_executor_task(self, envelope: dict) -> dict:
        cmd = envelope["params"].get("command", "")
        return self.executor.execute_task(cmd)

if __name__ == "__main__":
    orchestrator = SambaOrchestrator()
    
    print("\n--- TEST 1: Safe Command with Telemetry ---")
    res1 = orchestrator.dispatch_user_request("Status check", "echo 'Samba Pipeline + Telemetry Active'")
    print("Result:", res1)

    print("\n--- TEST 2: Unsafe Command with Block Logging ---")
    res2 = orchestrator.dispatch_user_request("Destructive action", "rm -rf /")
    print("Result:", res2)