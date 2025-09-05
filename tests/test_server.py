"""
Tests básicos para el servidor MCP Haiku
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from haiku_mcp.tools.haiku import generate_haiku_prompt, generate_haiku


def test_haiku_prompt_generation():
    """Prueba la generación de prompts para diferentes idiomas."""
    print("Testing haiku prompt generation...")

    # Test español
    prompt_es = generate_haiku_prompt("es", "naturaleza")
    assert "español" in prompt_es
    assert "naturaleza" in prompt_es
    print("✓ Prompt en español generado correctamente")

    # Test inglés
    prompt_en = generate_haiku_prompt("en", "ocean")
    assert "English" in prompt_en
    assert "ocean" in prompt_en
    print("✓ Prompt en inglés generado correctamente")

    # Test idioma por defecto
    prompt_default = generate_haiku_prompt("unknown", "test")
    assert "English" in prompt_default
    print("✓ Prompt por defecto generado correctamente")


def test_server_import():
    """Prueba que el servidor se puede importar correctamente."""
    print("Testing server import...")

    try:
        from haiku_mcp.server import mcp
        print("✓ Servidor importado correctamente")
        return True
    except ImportError as e:
        print(f"✗ Error importando servidor: {e}")
        return False


def run_tests():
    """Ejecuta todos los tests."""
    print("=== Ejecutando Tests del Servidor MCP Haiku ===\n")

    tests_passed = 0
    total_tests = 0

    # Test 1: Import del servidor
    total_tests += 1
    if test_server_import():
        tests_passed += 1

    print()

    # Test 2: Generación de prompts
    total_tests += 1
    try:
        test_haiku_prompt_generation()
        tests_passed += 1
    except Exception as e:
        print(f"✗ Error en test de prompts: {e}")

    print(f"\n=== Resultados: {tests_passed}/{total_tests} tests pasaron ===")

    if tests_passed == total_tests:
        print("🎉 Todos los tests pasaron exitosamente!")
        return True
    else:
        print("❌ Algunos tests fallaron")
        return False


if __name__ == "__main__":
    run_tests()
