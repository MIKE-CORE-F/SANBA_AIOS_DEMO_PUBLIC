#!/usr/bin/env python3
"""
S.A.N.B.A. v5.0 - DEMO BOOTLOADER
Imports and instantiates the demo components and reports what actually
happened. Most components are placeholders (stubs), and the output says so.
Location: AIOS_BOOT.py
"""

import os
import shutil
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"


def _loaded(note):
    print(f" {GREEN}[LOADED]{RESET} {note}")
    return True


def _failed(what, err):
    print(f" {RED}[FAILED]{RESET} {what}: {err}")
    return False


def integral_system_boot():
    print(f"{CYAN}=================================================================={RESET}")
    print(f"{CYAN} SANBA AI-OS v5.0 - DEMO BOOT (components are simulated stubs){RESET}")
    print(f"{CYAN}=================================================================={RESET}")

    results = []

    # 1. GOVERNANCE
    print("\n[1/6] Governance...")
    try:
        from GOVERNANCE.GROUNDLAWS.GROUNDLAWS import GroundlawsEngine
        from GOVERNANCE.DRIFT_WATCHDOG_LAYER.DRIFT_WATCHDOG import DriftWatchdogLayer
        from GOVERNANCE.FINANCIAL_GOVERNOR.FINANCIAL_GOVERNOR import AutonomousFinancialGovernor

        laws = GroundlawsEngine().verify_and_heal()
        drift = DriftWatchdogLayer().check_drift()
        AutonomousFinancialGovernor()
        print(f" {YELLOW}[STUB]{RESET} Groundlaws verification implemented: {laws['implemented']}")
        print(f" {YELLOW}[STUB]{RESET} Drift watchdog implemented: {drift['implemented']}")
        results.append(_loaded("Governance modules imported (financial governor has real limit logic)."))
    except Exception as e:
        results.append(_failed("Governance", e))

    # 2. KERNEL & SCHEDULER
    print("\n[2/6] Core kernel & task scheduler...")
    try:
        from CORE.KERNEL.SCHEDULER.TASK_SCHEDULER import TaskScheduler
        from CORE.AI_CPU_KERNEL.ai_cpu_kernel import AICPUKernel

        TaskScheduler()
        AICPUKernel()
        results.append(_loaded("Scheduler and kernel classes created (no worker threads started)."))
    except Exception as e:
        results.append(_failed("Kernel", e))

    # 3. VPU MESH
    print("\n[3/6] VPU mesh router...")
    try:
        from CORE.VPU_MESH.MESH_ROUTER import MeshRouter

        MeshRouter()
        results.append(_loaded("Mesh router class created (simulated, no network)."))
    except Exception as e:
        results.append(_failed("VPU mesh", e))

    # 4. MODEL BRIDGE
    print("\n[4/6] Model bridge...")
    try:
        from MODELS.MODEL_BRIDGE.MODEL_BRIDGE import ModelBridge

        bridge = ModelBridge()
        results.append(_loaded(f"Model bridge created (mock model: {bridge.active_model})."))
    except Exception as e:
        results.append(_failed("Model bridge", e))

    # 5. AGENTS
    print("\n[5/6] Agents...")
    try:
        from AGENTS.COCKPIT.AGENT_COCKPIT import AgentCockpit
        from AGENTS.TELEMETRY.AGENT_TELEMETRY import TelemetryAgent
        from AGENTS.ORCHESTRATOR.AGENT_ORCHESTRATOR import SambaOrchestrator

        AgentCockpit()
        TelemetryAgent()
        SambaOrchestrator()
        results.append(_loaded("Cockpit, telemetry and orchestrator created."))
    except Exception as e:
        results.append(_failed("Agents", e))

    # 6. EVOLUTION
    print("\n[6/6] Evolution & growth engine...")
    try:
        from EVOLUTION.EVOLUTION_ENGINE import EvolutionEngine
        from CORE.AI_CPU_KERNEL.autonomous_growth_engine import AutonomousGrowthEngine

        EvolutionEngine()
        AutonomousGrowthEngine()
        results.append(_loaded("Evolution and growth engine classes created (stubs)."))
    except Exception as e:
        results.append(_failed("Evolution", e))

    # Erlang bridge: report facts only
    print("\n[Info] Erlang MCL bridge...")
    has_erl = shutil.which("erl") is not None
    print(f" {YELLOW}[NOT STARTED]{RESET} Erlang sources are present in AGENTS/MCL_BRIDGE/ but this demo does not start them "
          f"(Erlang/OTP found: {has_erl}; the sources also need the 'macula', 'cowboy' and 'jsx' dependencies).")

    ok = sum(results)
    print(f"\n{CYAN}=================================================================={RESET}")
    colour = GREEN if ok == len(results) else RED
    print(f"{colour} {ok}/{len(results)} demo component groups loaded.{RESET}")
    print(" Note: most components are placeholders. No real governance, mesh or model checks were performed.")
    print(f"{CYAN}=================================================================={RESET}")
    return ok == len(results)


if __name__ == "__main__":
    sys.exit(0 if integral_system_boot() else 1)
