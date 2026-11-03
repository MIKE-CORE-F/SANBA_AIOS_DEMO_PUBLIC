"""
S.A.N.B.A. v5.0 - AGENT PRESERVATION
Keeps in-memory snapshots of a state dict. Snapshots are lost when the
process ends (no disk persistence in this baseline).
"""

import copy


class AgentPreservation:
    def __init__(self):
        self.snapshots = {}
        print("[AGENT PRESERVATION] In-memory snapshots available (not persisted).")

    def create_snapshot(self, snapshot_name: str, state: dict = None) -> bool:
        self.snapshots[snapshot_name] = copy.deepcopy(state or {})
        print(f"[AGENT PRESERVATION] Snapshot '{snapshot_name}' stored in memory.")
        return True

    def restore_snapshot(self, snapshot_name: str):
        """Returns a copy of the stored state, or None if the snapshot does not exist."""
        if snapshot_name not in self.snapshots:
            print(f"[AGENT PRESERVATION] Snapshot '{snapshot_name}' not found.")
            return None
        print(f"[AGENT PRESERVATION] Snapshot '{snapshot_name}' returned.")
        return copy.deepcopy(self.snapshots[snapshot_name])
