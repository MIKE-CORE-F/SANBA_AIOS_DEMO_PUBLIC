# S.A.N.B.A. AI-OS v5.0 – Public Demo Baseline

**Local multi-agent architecture demo (control plane, governance layer, model bridge)**

This repository is a **public architecture demonstration**. It shows the intended folder layout and interfaces of the S.A.N.B.A. AI-OS and contains a few working parts. **Most components are placeholders (stubs)**; the boot and demo scripts report this explicitly. See [Status of the components](#status-of-the-components).

## Quick start

Requires Python 3.10 or newer. No third-party Python packages are needed.

```bash
git clone https://github.com/MIKE-CORE-F/SANBA_AIOS_DEMO_PUBLIC.git
cd SANBA_AIOS_DEMO_PUBLIC

./boot.sh                      # demo boot: loads the components, reports what is a stub
./boot.sh --with-mesh          # local two-node TCP example (127.0.0.1, no authentication)
python3 -m AGENTS.ORCHESTRATOR.AGENT_ORCHESTRATOR   # guarded command pipeline
python3 test_smoke.py          # 10 smoke tests
```

## Structure

| Folder | Purpose |
|---|---|
| `AGENTS/` | Orchestrator, in-process message router, sandbox guard, executor, telemetry, cockpit, snapshots |
| `AGENTS/MCL_BRIDGE/` | Erlang sources (see [Third-party code](#third-party-code)); not started by the demo |
| `CORE/` | Kernel, scheduler, AI-CPU kernel and mesh router (stubs) |
| `GOVERNANCE/` | Financial governor, groundlaws engine and drift watchdog |
| `MODELS/` | Model bridge (mock) and the abstract adapter interface |
| `EVOLUTION/`, `CORE/EVOLUTION/` | Evolution engine stub (the two copies are identical) |

## Status of the components

| Component | Status |
|---|---|
| Sandbox guard (`AGENT_SANDBOX_GUARD.py`) | **Working.** Allowlist (`echo`, `status`, `inspect`, `systemctl status`); everything else is refused, and shell metacharacters (`; & \| $ > <` …) are refused. Not a replacement for an OS-level sandbox. |
| Executor (`AGENT_EXECUTOR.py`) | **Working.** Runs a command without a shell, 10 second timeout. It does not decide what is allowed; callers must use the guard. |
| Orchestrator, MCP router | **Working.** Guard → router → executor, with telemetry logging. |
| Financial governor | **Working.** Amount limits (allow / revise / block) and an audit log with a hash chain. The chain is kept in memory and restarts on every run. `trustScore` is read from the context and must come from a trusted source. |
| Snapshots (`AGENT_PRESERVATION.py`) | **Working, in memory only.** |
| Groundlaws engine, drift watchdog | **Stub.** 20 laws are declared; nothing is verified or monitored. |
| Kernel, scheduler, mesh router, AI-CPU kernel, growth/evolution engines | **Stub.** They print or record calls; no threads, no network, no optimisation. |
| Model bridge | **Mock.** Returns a fixed reply; no request is sent to any model. |
| Telemetry metrics | **Simulated** values. |
| `MCL_BRIDGE/` (Erlang) | **Not started.** Needs Erlang/OTP and dependencies that are not included (`macula`, `cowboy`, `jsx`). |
| `DEMO_MULTI_NODE_MESH.py` | Local example with two TCP listeners on `127.0.0.1`. No clustering, no authentication, no encryption. |

`VPU_CONFIG.TOML` lists `mesh_protocol = "mTLS"` as a planned setting; mTLS is **not implemented**.

## Third-party code

`AGENTS/MCL_BRIDGE/` contains Erlang sources. Their `mcl_om.app.src` declares the license `Apache-2.0`. They are not part of the Python demo and are not covered by the license in `LICENSE`. Origin and attribution still need to be documented by the maintainer.

## License

See [`LICENSE`](LICENSE): non-commercial, source-available.
