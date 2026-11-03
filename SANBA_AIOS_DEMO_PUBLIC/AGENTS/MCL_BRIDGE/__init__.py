"""
S.A.N.B.A. AI-OS v5.0 - MCL Integration Bridge for Agents & Kernel
"""
import sys
import os

# Voeg de map zelf toe aan path zodat submodules direct bereikbaar zijn
sys.path.append(os.path.dirname(__file__))

try:
    from .mcl_om import *
except ImportError:
    # Fallback voor lichte demo baseline als mcl_om als platte structuur draait
    pass
