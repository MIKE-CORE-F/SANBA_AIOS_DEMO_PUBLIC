# S.A.N.B.A. AI-OS v5.0 - System Documentation (Public Baseline)

## 1. Summary
S.A.N.B.A. AI-OS v5.0 is a local-first multi-agent architecture demo. It shows the intended layering (kernel, governance, agents, model abstraction) and includes a small number of working parts: a command allowlist guard, a shell-free executor, an orchestrator pipeline, a financial limit governor with an audit log, and in-memory snapshots. The other components are placeholders.

The demo runs on the local machine and makes no cloud calls. An optional Erlang OTP bridge (`AGENTS/MCL_BRIDGE/`) is included as source but is not started by the demo.

## 2. Structure

* **`CORE/`**: AI-CPU kernel, growth engine, task scheduler and VPU mesh router (all stubs).
* **`GOVERNANCE/`**: financial governor (working), groundlaws engine and drift watchdog (stubs).
* **`AGENTS/`**: orchestrator, MCP router, sandbox guard, executor, telemetry, cockpit, preservation (snapshots), kernel and binding layers. `MCL_BRIDGE/` holds Erlang sources.
* **`MODELS/`**: model bridge (mock) and the abstract adapter interface.
* **`STORAGE/`**: runtime logs (created on demand, excluded from git).

## 3. Execution pipeline and security notes

`SambaOrchestrator.dispatch_user_request(prompt, command)`:

1. The sandbox guard checks the command against an **allowlist**. It refuses anything that is not listed, and refuses shell metacharacters.
2. If approved, the message goes through the MCP router to the executor.
3. The executor runs the command **without a shell** (10 second timeout).
4. Each step is written to `STORAGE/LOGS/SYSTEM_AUDIT.LOG`.

What this does **not** provide: process isolation, resource limits, authentication of callers or protection against a compromised host. Use a container or separate OS user for real isolation. The allowlist deliberately excludes `python` and `podman`, because they permit arbitrary code.

Financial governor: limits are 500 (revise) and 2000 (block). The audit hash chain is in memory and restarts on each run, so it is tamper-evident only within a process. `trustScore` in the context raises the limit; it must come from a trusted source.

## 4. Running

```bash
cd /path/to/SANBA_AIOS_DEMO_PUBLIC
./boot.sh                 # demo boot
./boot.sh --with-mesh     # local two-node TCP example
python3 test_smoke.py     # smoke tests
```

## 5. Known limitations

* Groundlaws verification, drift monitoring, scheduling, mesh routing and the model bridge are placeholders.
* The mesh demo uses plain TCP on localhost without authentication or encryption.
* `mTLS` in `VPU_CONFIG.TOML` is a planned setting, not an implemented feature.
* `AGENTS/MCL_BRIDGE/` is third-party Erlang code (Apache-2.0 declared); attribution is still to be documented.
