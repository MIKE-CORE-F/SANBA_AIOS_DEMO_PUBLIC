from typing import Optional


class StatusMonitor:
    """Prints and aggregates the states it is given. It does not probe anything."""

    def __init__(self):
        self.GREEN = "\033[92m"
        self.RED = "\033[91m"
        self.RESET = "\033[0m"

    def check_status(self, component_name: str, is_online: bool) -> bool:
        if is_online:
            status_str = f"{self.GREEN}[ONLINE]{self.RESET}"
        else:
            status_str = f"{self.RED}[OFFLINE]{self.RESET}"
        print(f"[STATUS MONITOR] Subsystem '{component_name}': {status_str}")
        return is_online

    def verify_all_systems(self, systems: Optional[dict] = None) -> bool:
        """systems maps a component name to its measured state (True/False)."""
        if not systems:
            print("[STATUS MONITOR] No subsystem states supplied, nothing to verify.")
            return False
        all_green = True
        for sys_name, status in systems.items():
            if not self.check_status(sys_name, bool(status)):
                all_green = False
        return all_green
