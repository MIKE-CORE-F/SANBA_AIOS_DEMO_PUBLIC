"""
S.A.N.B.A. v5.0 - AGENT KERNEL (demo stub)
Records directives; it does not forward them to a kernel.
"""


class AgentKernel:
    def __init__(self):
        self.directives = []
        print("[AGENT KERNEL] Demo stub: no kernel attached.")

    def execute_kernel_directive(self, directive: str, data: dict) -> bool:
        self.directives.append({"directive": directive, "data": data})
        print(f"[AGENT KERNEL] Directive '{directive}' recorded (demo stub, not executed).")
        return True
