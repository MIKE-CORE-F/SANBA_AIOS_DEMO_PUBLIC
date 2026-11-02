# S.A.N.B.A. AI-OS v5.0 - System Documentation (Public Baseline)

## 1. Executive Summary
S.A.N.B.A. AI-OS v5.0 is a sovereign, local-first artificial intelligence operating system engineered for autonomous task execution, zero-latency multi-agent orchestration, and deterministic governance.

The baseline architecture combines a high-performance Python Single-Kernel Engine with an optional, fault-tolerant Erlang OTP Actor Mesh (`AGENTS/MCL_BRIDGE/`). This public baseline represents a sanitized configuration, stripped of private credentials, proprietary business logic, and persistent user histories to demonstrate maximum security, zero cloud dependency, and sovereign execution.

---

## 2. Architectural Core Structure
The system is partitioned into modular, highly-decoupled functional layers:

* **`CORE/`**: Houses the AI-CPU Kernel (`ai_cpu_kernel.py`), Autonomous Growth Engine, Task Scheduler, and VPU Mesh Router (`MESH_ROUTER.py`) for thread-level execution and load balancing.
* **`GOVERNANCE/`**: Enforces strict operational boundaries via the 20 Groundlaws (`GROUNDLAWS.py`), the Financial Governor, and real-time Drift Watchdogs (`DRIFT_WATCHDOG.py`).
* **`AGENTS/`**: Manages agent lifecycle binding, routing, telemetry, sandbox guards, and the Erlang OTP actor bridge (`MCL_BRIDGE/`) for optional P2P node mesh networking.
* **`MODELS/`**: Contains the unified model bridge (`MODEL_BRIDGE.py`) and dynamic adapters, abstracting model execution from natural language context.
* **`STORAGE/`**: Isolated state and logging directories (`STORAGE/LOGS/`) sanitized for public demonstration.

---

## 3. Security, Sovereignty & Governance
* **Sovereign Execution:** The core OS operates 100% locally on host hardware without external cloud or network dependencies.
* **Groundlaw Verification:** All subsystem routines undergo validation against institutional groundlaws during initialization (`AIOS_BOOT.py`).
* **Zero-Trust Isolation:** Agents execute within guarded sandboxes (`AGENT_SANDBOX_GUARD.py`) monitored by financial and drift governors to prevent unauthorized deviations.

---

## 4. Operational Boot Sequence & CLI Execution
Navigate to the project root directory in WSL / Linux:

```bash
cd /path/to/SANBA_AIOS_DEMO_PUBLIC