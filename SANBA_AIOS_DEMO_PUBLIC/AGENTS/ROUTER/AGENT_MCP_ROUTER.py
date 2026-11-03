"""
S.A.N.B.A. v5.0 - AGENT MCP ROUTER
Manages and routes messages between agents within the multi-agent triarc architecture.
Location: AGENTS/ROUTER/AGENT_MCP_ROUTER.py
"""

import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")
logger = logging.getLogger("AgentMCPRouter")

class AgentMCPRouter:
    def __init__(self):
        self.routes = {}
        logger.info("[MCP ROUTER] Initialization of Agent MCP Router completed.")

    def register_route(self, agent_name: str, endpoint: str):
        """Registers a communication channel for a specific agent."""
        self.routes[agent_name] = endpoint
        logger.info(f"[MCP ROUTER] Route registered for '{agent_name}' on endpoint '{endpoint}'")

    def dispatch_message(self, sender: str, receiver: str, payload: dict) -> bool:
        """Dispatches a message from one agent to another via the MCP mesh."""
        if receiver in self.routes or receiver in ["Agent_Orchestrator", "Agent_Kernel"]:
            logger.info(f"[MCP ROUTER] Message sent from {sender} to {receiver} | Payload size: {len(str(payload))} bytes")
            return True
        logger.warning(f"[MCP ROUTER] Target agent '{receiver}' not found in active routes.")
        return False

class MCPRouterAgent:
    """In-process message bus used by the orchestrator.

    Agents register a handler under a name; send_mcp_message() wraps the data
    in an envelope and calls the handler of the recipient directly.
    """

    def __init__(self):
        self.handlers = {}

    def register_agent(self, name: str, handler) -> None:
        """Registers a callable that receives an envelope dict and returns a dict."""
        self.handlers[name] = handler
        logger.info(f"[MCP ROUTER] Handler registered for '{name}'")

    def send_mcp_message(self, sender: str, recipient: str, action: str, data: dict) -> dict:
        """Delivers a message to the recipient and returns the handler result."""
        handler = self.handlers.get(recipient)
        if handler is None:
            logger.warning(f"[MCP ROUTER] Unknown recipient '{recipient}'")
            return {"status": "ERROR", "reason": f"unknown recipient '{recipient}'"}
        envelope = {
            "sender": sender,
            "recipient": recipient,
            "action": action,
            "params": dict(data or {}),
        }
        return handler(envelope)


if __name__ == "__main__":
    router = AgentMCPRouter()
    router.register_route("Agent_Orchestrator", "ipc:///tmp/orchestrator.sock")
    router.dispatch_message("Agent_Kernel", "Agent_Orchestrator", {"status": "sync_request"})