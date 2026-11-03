"""
MIKE-CORE AI-OS FUSION 5.0 - SANBA
Module: AGENT_SANDBOX_GUARD (command allowlist)
Location: AGENTS/GOVERNANCE/AGENT_SANDBOX_GUARD.py

Approves a command only if it matches an explicit allowlist. Everything else
is refused (deny by default). This is a demo-level guard: it is not a
replacement for a real OS-level sandbox (containers, seccomp, separate user).
"""

import re
import shlex
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("SandboxGuard")

# Characters that allow chaining, redirection, substitution or subshells.
SHELL_METACHARACTERS = re.compile(r"[;&|`$<>(){}\\\n\r]")
MAX_COMMAND_LENGTH = 500


class SandboxGuardAgent:
    def __init__(self):
        # Program names allowed on their own.
        self.allowed_programs = {"status", "inspect", "echo"}
        # Programs allowed only with a fixed first argument.
        self.allowed_subcommands = {"systemctl": {"status"}}
        # Kept for backwards compatibility with the old attribute name.
        self.allowed_commands = sorted(self.allowed_programs) + ["systemctl status"]
        # Note: "python" and "podman" were removed from the old list because
        # they allow running arbitrary code.

    def _is_allowed(self, command) -> bool:
        if not isinstance(command, str):
            return False
        command = command.strip()
        if not command or len(command) > MAX_COMMAND_LENGTH:
            return False
        if SHELL_METACHARACTERS.search(command):
            return False
        try:
            tokens = shlex.split(command)
        except ValueError:
            return False
        if not tokens:
            return False
        program = tokens[0]
        if program in self.allowed_programs:
            return True
        if program in self.allowed_subcommands:
            return len(tokens) >= 2 and tokens[1] in self.allowed_subcommands[program]
        return False

    def validate_action(self, agent_id: str, action_type: str, payload: dict) -> bool:
        """Returns True only if the proposed command is on the allowlist."""
        logger.info(f"[SANDBOX GUARD] Inspecting action from agent '{agent_id}': {action_type}")
        command = (payload or {}).get("command", "")

        if not self._is_allowed(command):
            logger.error(f"[SANDBOX GUARD] BLOCKED: command not on allowlist ('{command}') from agent '{agent_id}'")
            return False

        logger.info("[SANDBOX GUARD] PASSED: command is on the allowlist.")
        return True


if __name__ == "__main__":
    guard = SandboxGuardAgent()
    assert guard.validate_action("AGENT_TEST", "EXEC", {"command": "echo 'SANBA Test'"}) is True
    assert guard.validate_action("AGENT_TEST", "EXEC", {"command": "rm -rf /"}) is False
    assert guard.validate_action("AGENT_TEST", "EXEC", {"command": "echo hi; rm -fr /"}) is False
    print("SandboxGuard self-test passed.")
