#!/bin/bash
# ==================================================================
# S.A.N.B.A. AI-OS v5.0 - DEMO BOOT SCRIPT
# Location: /boot.sh
# ==================================================================

echo "=================================================================="
echo " 🚀 S.A.N.B.A. AI-OS v5.0 - STARTING LOCAL DEMO BASELINE"
echo "=================================================================="

# Check if python3 is available
if ! command -v python3 &> /dev/null; then
    echo "[ERROR] python3 could not be found. Please install Python 3."
    exit 1
fi

if [ "$1" == "--with-mesh" ]; then
    echo "[MESH] Starting the local two-node TCP demo (127.0.0.1)..."
    if [ -f "DEMO_MULTI_NODE_MESH.py" ]; then
        python3 DEMO_MULTI_NODE_MESH.py
    else
        echo "[ERROR] DEMO_MULTI_NODE_MESH.py not found in root directory!"
        exit 1
    fi
else
    echo "[INFO] Running the local demo boot (no cloud calls, components are stubs)."
    if [ -f "AIOS_BOOT.py" ]; then
        python3 AIOS_BOOT.py
    else
        echo "[ERROR] AIOS_BOOT.py not found in root directory!"
        exit 1
    fi
fi
