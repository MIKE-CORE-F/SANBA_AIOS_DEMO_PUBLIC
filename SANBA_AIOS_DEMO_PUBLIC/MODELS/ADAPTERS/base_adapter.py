"""
S.A.N.B.A. AI-OS v5.0 - Abstract Base Adapter Interface (Public Demo Spec)
Defines the standard protocol for routing model signals and memory streams.
"""

from abc import ABC, abstractmethod
from typing import Dict, Any

class BaseModelAdapter(ABC):
    """Abstract interface for external model and memory integration adapters."""
    
    @abstractmethod
    def initialize(self, config: Dict[str, Any]) -> bool:
        """Initialize the model binding with specified configuration parameters."""
        pass

    @abstractmethod
    def process_telemetry(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Process incoming telemetry data and return transformed model context."""
        pass
