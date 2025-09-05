#!/usr/bin/env python3
"""
Servidor MCP para generación de haikus
"""

import os
import sys
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
from .tools.haiku import generate_haiku

# Cargar variables de entorno
load_dotenv()

# Inicializar el servidor MCP
mcp = FastMCP("haiku_mcp")


@mcp.tool()
def test_tool(message: str) -> str:
    """
    Herramienta de prueba para verificar el funcionamiento básico del servidor.

    Args:
        message: Mensaje de prueba a procesar

    Returns:
        Respuesta de prueba con el mensaje procesado
    """
    return f"Test tool response: {message.upper()}"


@mcp.tool()
def haiku(idioma: str, tema: str) -> str:
    """
    Genera un haiku basado en el tema especificado en el idioma solicitado.

    Args:
        idioma: Idioma en el que se generará el haiku
        tema: Tema sobre el cual se creará el haiku

    Returns:
        Haiku generado en el formato tradicional (5-7-5 sílabas)
    """
    return generate_haiku(idioma, tema)


if __name__ == "__main__":
    # Ejecutar el servidor directamente
    mcp.run(transport='stdio')
