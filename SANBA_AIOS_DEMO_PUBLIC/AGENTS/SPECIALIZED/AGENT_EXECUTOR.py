"""
MIKE-CORE AI-OS FUSION 5.0 - SANBA
Module: AGENT_EXECUTOR (Specialized Execution Agent)
Location: AGENTS/SPECIALIZED/AGENT_EXECUTOR.py

Runs a command WITHOUT a shell. The executor does not decide what is allowed:
callers must validate the command first (see AGENT_SANDBOX_GUARD).
"""

import shlex
import subprocess
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("AgentExecutor")


class ExecutorAgent:
    def __init__(self, name="AGENT_EXECUTOR"):
        self.name = name

    def execute_task(self, command: str) -> dict:
        """Executes an already-approved command (no shell, 10 second timeout)."""
        logger.info(f"[{self.name}] Executing command: {command}")
        try:
            args = shlex.split(command)
            if not args:
                return {"exit_code": -1, "error": "empty command"}
            result = subprocess.run(
                args, shell=False, capture_output=True, text=True, timeout=10
            )
            return {
                "exit_code": result.returncode,
                "stdout": result.stdout.strip(),
                "stderr": result.stderr.strip()
            }
        except Exception as e:
            logger.error(f"[{self.name}] Execution error: {str(e)}")
            return {"exit_code": -1, "error": str(e)}


if __name__ == "__main__":
    executor = ExecutorAgent()
    res = executor.execute_task("echo 'Executor online'")
    print("Executor test response:", res)
