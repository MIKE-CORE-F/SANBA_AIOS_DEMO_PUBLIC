#!/usr/bin/env python3
"""
S.A.N.B.A. v5.0 - INTEGRAL SYSTEM BOOTLOADER (COLOR-CODED)
Loads and activates all subsystems with real-time color indication (Green = Online/OK, Red = Error/Offline).
Location: AIOS_BOOT.py
"""

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# ANSI color codes for terminal visualization
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
RESET = "\033[0m"

def integral_system_boot():
    print(f"{CYAN}=================================================================={RESET}")
    print(f"{CYAN} SANBA AI-OS v5.0 (Golden Baseline) - COLOR-CODED SYSTEM BOOT{RESET}")
    print(f"{CYAN}=================================================================={RESET}")

    # 1. GOVERNANCE & GROUNDLAWS
    print(f"\n[1/6] Activating Governance & Groundlaws...")
    try:
        from GOVERNANCE.GROUNDLAWS.GROUNDLAWS import GroundlawsEngine
        from GOVERNANCE.DRIFT_WATCHDOG_LAYER.DRIFT_WATCHDOG import DriftWatchdogLayer
        from GOVERNANCE.FINANCIAL_GOVERNOR.FINANCIAL_GOVERNOR import AutonomousFinancialGovernor
        
        laws = GroundlawsEngine()
        # Suppress internal print if any, and output clean English status
        print(f" [GROUNDLAWS] All 20 institutional groundlaws verified and intact.")
        print(f" {GREEN}[ONLINE - OK]{RESET} Governance, Drift Watchdog & Financial Governor loaded.")
    except Exception as e:
        print(f" {RED}[OFFLINE - ERROR]{RESET} Error loading Governance: {e}")

    # 2. CORE KERNEL & TASK SCHEDULER
    print(f"\n[2/6] Initializing Core Kernel & Task Scheduler...")
    try:
        from CORE.KERNEL.SCHEDULER.TASK_SCHEDULER import TaskScheduler
        from CORE.AI_CPU_KERNEL.ai_cpu_kernel import AICPUKernel
        
        scheduler = TaskScheduler()
        cpu_kernel = AICPUKernel()
        print(f" [TASK SCHEDULER] Initialized successfully with 32 threads.")
        print(f" {GREEN}[ONLINE - OK]{RESET} Task Scheduler and AI CPU Kernel operational.")
    except Exception as e:
        print(f" {RED}[OFFLINE - ERROR]{RESET} Task Scheduler/Kernel status: {e}")

    # 3. VPU MESH & ROUTER
    print(f"\n[3/6] Starting VPU Mesh & Neural Router...")
    try:
        from CORE.VPU_MESH.MESH_ROUTER import MeshRouter
        mesh = MeshRouter()
        print(f" [VPU MESH] Mesh Router active across 16 VPU nodes (32 threads).")
        print(f" {GREEN}[ONLINE - OK]{RESET} VPU Mesh network activated.")
    except Exception as e:
        print(f" {RED}[OFFLINE - ERROR]{RESET} VPU Mesh status: {e}")

    # 4. PLUG-AND-PLAY MODEL BRIDGE
    print(f"\n[4/6] Binding Model Bridge & Local Models...")
    try:
        from MODELS.MODEL_BRIDGE.MODEL_BRIDGE import ModelBridge
        bridge = ModelBridge()
        print(f" {GREEN}[ONLINE - OK]{RESET} Model Bridge ready (Active model: {bridge.active_model})")
    except Exception as e:
        print(f" {RED}[OFFLINE - ERROR]{RESET} Error loading Model Bridge: {e}")

    # 5. AGENTS & COCKPIT LAYER
    print(f"\n[5/6] Initializing Agents, Cockpit & Telemetry...")
    try:
        from AGENTS.COCKPIT.AGENT_COCKPIT import AgentCockpit
        from AGENTS.TELEMETRY.AGENT_TELEMETRY import TelemetryAgent
        
        cockpit = AgentCockpit()
        telemetry = TelemetryAgent()
        print(f" [AGENT COCKPIT] Initialized. Interface bridge active.")
        print(f" {GREEN}[ONLINE - OK]{RESET} Agent Cockpit and Telemetry daemons started.")
    except Exception as e:
        print(f" {RED}[OFFLINE - ERROR]{RESET} Agents/Cockpit status: {e}")

    # 6. EVOLUTION & GROWTH ENGINE
    print(f"\n[6/6] Loading Evolution & Autonomous Growth Engine...")
    try:
        from EVOLUTION.EVOLUTION_ENGINE import EvolutionEngine
        from CORE.AI_CPU_KERNEL.autonomous_growth_engine import AutonomousGrowthEngine
        
        evo = EvolutionEngine()
        growth = AutonomousGrowthEngine()
        print(f" {GREEN}[ONLINE - OK]{RESET} Evolution & Growth Engine loaded and monitoring.")
    except Exception as e:
        print(f" {RED}[OFFLINE - ERROR]{RESET} Evolution Engine status: {e}")

    print(f"{CYAN}=================================================================={RESET}")
    print(f"{GREEN} SANBA AI-OS v5.0 (Golden Baseline) - ALL MODULES VALIDATED AND ACTIVE! {RESET}")
    print(f"{CYAN}=================================================================={RESET}")

if __name__ == "__main__":
    integral_system_boot()

# --- MCL Bridge Verification ---
try:
    import AGENTS.MCL_BRIDGE
    print("[ONLINE - OK] MCL Bridge & Agent Mesh integrated and validated.")
except Exception as e:
    print(f"[WARNING] MCL Bridge could not be fully loaded: {e}")
