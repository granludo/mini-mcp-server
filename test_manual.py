#!/usr/bin/env python3
"""
Script de prueba manual para el servidor MCP Haiku
"""

import sys
import os

# Agregar el directorio raíz al path
sys.path.insert(0, os.path.dirname(__file__))

from haiku_mcp.tools.haiku import generate_haiku, test_haiku_generation


def test_server_tools():
    """Prueba las herramientas del servidor MCP."""
    print("=== Probando Herramientas del Servidor MCP ===\n")

    # Importar el servidor
    from haiku_mcp.server import mcp, test_tool, haiku

    # Probar herramienta de test
    print("1. Probando herramienta de test:")
    result = test_tool("hola mundo")
    print(f"Resultado: {result}\n")

    # Probar herramienta de haiku (sin API key real para evitar costos)
    print("2. Probando herramienta de haiku:")
    result = haiku("es", "naturaleza")
    print(f"Resultado:\n{result}\n")


def test_individual_haiku():
    """Prueba la generación individual de haikus."""
    print("=== Probando Generación Individual de Haikus ===\n")

    # Probar con diferentes idiomas y temas
    test_cases = [
        ("es", "montaña"),
        ("en", "sunset"),
        ("fr", "printemps")
    ]

    for idioma, tema in test_cases:
        print(f"Generando haiku en {idioma} sobre '{tema}':")
        result = generate_haiku(idioma, tema)
        print(result)
        print("-" * 50)


def main():
    """Función principal de pruebas."""
    print("🚀 Iniciando pruebas del Servidor MCP Haiku\n")

    # Verificar que tenemos API key
    if not os.getenv("OPENAI_API_KEY"):
        print("⚠️  Advertencia: OPENAI_API_KEY no encontrada. Las pruebas con IA fallarán.\n")
    else:
        print("✅ OPENAI_API_KEY encontrada\n")

    # Ejecutar pruebas
    test_server_tools()
    test_individual_haiku()

    print("✅ Pruebas completadas!")


if __name__ == "__main__":
    main()
