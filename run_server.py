#!/usr/bin/env python3
"""
Script para ejecutar el servidor MCP Haiku en modo stdio
"""

import sys
import os

# Agregar el directorio raíz al path
sys.path.insert(0, os.path.dirname(__file__))

from haiku_mcp.server import mcp

if __name__ == "__main__":
    # Ejecutar el servidor directamente
    mcp.run(transport='stdio')