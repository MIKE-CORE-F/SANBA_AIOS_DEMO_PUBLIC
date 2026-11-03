"""
S.A.N.B.A. AI-OS v5.0 - Model Bridge Router (Public Demo Baseline)
Mock only: no request is sent to any model backend.
"""

from typing import Dict, Any


class ModelBridge:
    def __init__(self, endpoint: str = "http://localhost:11434"):
        self.endpoint = endpoint  # reserved for a real backend (e.g. Ollama)
        self.status = "MOCK"
        self.active_model = "mock-demo-model-v5"

    def dispatch_prompt(self, agent_id: str, prompt_payload: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "status": "MOCK",
            "agent_id": agent_id,
            "response": f"[DEMO_OUTPUT] Mock reply for agent '{agent_id}'. No request was sent to {self.endpoint}."
        }
