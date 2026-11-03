"""
S.A.N.B.A. v5.0 - Autonomous Financial Governor & Self-Evolving Ledger
Applies amount limits (ALLOW / REVISE / BLOCK) and writes a hash-chained audit log.

Limitations of this demo:
- The hash chain lives in memory and restarts from zeros on every start; the
  log file is not verified when it is read back, so it is tamper-evident only
  while the process runs.
- "trustScore" is read from the context. It must come from a trusted source,
  never from the caller whose transaction is being judged.
"""

import os
import time
import hashlib
import json

class AutonomousFinancialGovernor:
    def __init__(self):
        self.legal_framework_version = "SANBA-LEGAL-FIN-v5.0-AUTONOMOUS"
        self.max_transaction_limit = 500.0  
        self.circuit_breaker_threshold = 2000.0 
        self.previous_hash = "0000000000000000000000000000000000000000000000000000000000000000"
        self.adaptation_log = []

    def verify_transaction(self, context: dict, amount: float) -> dict:
        legal_basis = "Art. 4.2 Autonomous Financial Execution"
        
        # Autonomous policy adaptation based on historical risk in context
        self._autonomous_policy_adaptation(context)

        # 1. Legal Circuit Breaker (BLOCK)
        if amount > self.circuit_breaker_threshold:
            decision = {
                "status": "BLOCK",
                "reason": "ERR_CIRCUIT_BREAKER_BREACH",
                "legal_basis": legal_basis,
                "flags": ["requires-audit", "security-alert"]
            }
        # 2. Asynchronous CFO Gateway (REVISE)
        elif amount > self.max_transaction_limit:
            token = hashlib.sha256(f"{context.get('workflowId', 'WF')}-{amount}-{time.time()}".encode("utf-8")).hexdigest()
            decision = {
                "status": "REVISE",
                "reason": "EXCEEDS_DYNAMIC_LIMIT_CFO_GATEWAY",
                "legal_basis": legal_basis,
                "crypto_token": token,
                "flags": ["human-in-the-loop", "cfo-approval-required"]
            }
        # 3. Nominal Framework (ALLOW)
        else:
            decision = {
                "status": "ALLOW",
                "reason": "WITHIN_DYNAMIC_NOMINAL_FRAMEWORK",
                "legal_basis": legal_basis,
                "flags": []
            }

        self._log_and_return(context, amount, decision)
        return decision

    def _autonomous_policy_adaptation(self, context: dict):
        """
        Self-adapting algorithm: adjusts limits based on trust score or risk profile.
        """
        trust_score = context.get("trustScore", 1.0)
        if trust_score > 1.2 and self.max_transaction_limit < 1000.0:
            old_limit = self.max_transaction_limit
            self.max_transaction_limit *= 1.1  # Autonomous scaling upon proven stability
            adjustment_note = f"[SELF-EVOLUTION] Max limit dynamically shifted from {old_limit} to {self.max_transaction_limit}"
            self.adaptation_log.append(adjustment_note)
            print(f"[FINANCIAL GOVERNOR] {adjustment_note}")

    def _log_and_return(self, context: dict, amount: float, decision: dict):
        log_entry = {
            "workflowId": context.get("workflowId", "UNKNOWN"),
            "amount": amount,
            "decisionType": decision["status"],
            "reason": decision["reason"],
            "timestamp": time.time(),
            "previous_hash": self.previous_hash
        }
        
        serialized = json.dumps(log_entry, sort_keys=True)
        entry_hash = hashlib.sha256(serialized.encode("utf-8")).hexdigest()
        log_entry["entry_hash"] = entry_hash
        self.previous_hash = entry_hash

        log_path = "STORAGE/LOGS/SYSTEM_AUDIT.LOG"
        os.makedirs(os.path.dirname(log_path), exist_ok=True)
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(f"[FINANCIAL GOVERNOR AUDIT] {json.dumps(log_entry)}\n")
            
        print(f"[FINANCIAL GOVERNOR] Transaction €{amount} evaluated -> Status: {decision['status']}")