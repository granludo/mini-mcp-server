"""
Herramienta para generación de haikus usando OpenAI
"""

import os
from typing import Optional
from openai import OpenAI
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Configurar cliente OpenAI
api_key = os.getenv("OPENAI_API_KEY")
if api_key:
    client = OpenAI(api_key=api_key)
else:
    client = None


def generate_haiku_prompt(idioma: str, tema: str) -> str:
    """
    Genera el prompt para crear un haiku.

    Args:
        idioma: Idioma del haiku
        tema: Tema del haiku

    Returns:
        Prompt formateado para el modelo
    """
    prompts = {
        "es": f"Genera un haiku tradicional (estructura 5-7-5 sílabas) sobre el tema '{tema}'. El haiku debe ser en español, original y seguir la estructura clásica.",
        "en": f"Generate a traditional haiku (5-7-5 syllable structure) about the theme '{tema}'. The haiku should be in English, original and follow the classic structure.",
        "fr": f"Générez un haïku traditionnel (structure 5-7-5 syllabes) sur le thème '{tema}'. Le haïku doit être en français, original et suivre la structure classique.",
    }

    return prompts.get(idioma.lower(), prompts["en"])


def generate_haiku(idioma: str, tema: str) -> str:
    """
    Genera un haiku usando OpenAI GPT-4.1-mini.

    Args:
        idioma: Idioma del haiku
        tema: Tema del haiku

    Returns:
        Haiku generado o mensaje de error
    """
    try:
        if not client:
            return "Error: OPENAI_API_KEY no configurada en variables de entorno"

        prompt = generate_haiku_prompt(idioma, tema)

        response = client.chat.completions.create(
            model="gpt-4o-mini",  # Nota: gpt-4.1-mini no existe, usando gpt-4o-mini
            messages=[
                {"role": "system", "content": "Eres un poeta experto en haikus tradicionales."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=200,
            temperature=0.7
        )

        haiku = response.choices[0].message.content.strip()
        return haiku

    except Exception as e:
        return f"Error generando haiku: {str(e)}"


# Función para testing independiente
def test_haiku_generation():
    """Función de prueba para generar haikus desde línea de comandos."""
    print("=== Prueba de Generación de Haikus ===")

    # Pruebas de ejemplo
    test_cases = [
        ("es", "naturaleza"),
        ("en", "ocean"),
        ("fr", "automne")
    ]

    for idioma, tema in test_cases:
        print(f"\nGenerando haiku en {idioma} sobre '{tema}':")
        result = generate_haiku(idioma, tema)
        print(result)
        print("-" * 50)


if __name__ == "__main__":
    test_haiku_generation()
