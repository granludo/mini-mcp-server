# Product Requirements Document (PRD): Haiku MCP Server

## Visión General

Este documento describe los requisitos para el desarrollo de un servidor MCP (Model Context Protocol) llamado `haiku_mcp` que genera haikus usando inteligencia artificial.

## Objetivos

Crear un servidor MCP que proporcione una herramienta para generar haikus personalizados basados en temas específicos y en diferentes idiomas, utilizando modelos de lenguaje avanzados.

## Requisitos Técnicos

### 1. Plataforma y Lenguaje

- **Lenguaje de Programación**: Python
- **Arquitectura**: MCP Server implementado sobre stdio
- **Nombre del Proyecto**: `haiku_mcp`

### 2. Funcionalidades Principales

#### Herramienta "haiku"

- **Nombre**: `haiku`
- **Parámetros**:
  - `idioma` (string): Idioma en el que se generará el haiku
  - `tema` (string): Tema sobre el cual se creará el haiku
- **Funcionalidad**: Generar un haiku original basado en el tema especificado en el idioma solicitado

### 3. Integración con IA

- **Modelo LLM**: GPT-4.1-mini (OpenAI)
- **Configuración**: La clave API de OpenAI se almacenará en la variable de entorno `OPENAI_API_KEY`
- **Archivo de Configuración**: `.env`

### 4. Arquitectura MCP

- **Protocolo**: Model Context Protocol (MCP)
- **Transporte**: stdio (standard input/output)
- **Compatibilidad**: Debe ser compatible con clientes MCP

## Requisitos Funcionales

### Generación de Haikus

1. El servidor debe aceptar solicitudes con parámetros `idioma` y `tema`
2. Debe generar haikus que sigan la estructura tradicional:
   - Tres líneas (5-7-5 sílabas)
   - Tema consistente con el parámetro proporcionado
   - Idioma correspondiente al parámetro especificado
3. La generación debe ser realizada por GPT-4.1-mini
4. El haiku generado debe ser devuelto como respuesta

### Manejo de Errores

- Validación de parámetros requeridos
- Manejo de errores de conexión con OpenAI API
- Manejo de errores de configuración (falta de API key)

## Requisitos No Funcionales

### Seguridad

- La clave API de OpenAI debe almacenarse de forma segura en variables de entorno
- No debe exponer la clave API en logs o respuestas

### Rendimiento

- Tiempo de respuesta razonable para generación de haikus (< 30 segundos)
- Manejo eficiente de recursos

### Mantenibilidad

- Código bien estructurado y documentado
- Uso de mejores prácticas de Python
- Dependencias mínimas y bien documentadas

## Dependencias

### Requeridas

- `openai` - Para integración con OpenAI API
- `python-dotenv` - Para manejo de variables de entorno
- Librerías MCP (por determinar según especificaciones oficiales, mcp.server.fastmcp 



## Estructura del Proyecto

```bash
/Users/granludo/Code/mini-mcp-server/
├── haiku_mcp/
│   ├── __init__.py
│   ├── server.py
│   └── tools/
│       └── haiku.py
├── tests/
├── .env
├── requirements.txt
├── PRD.md
└── README.md
```

## Criterios de Aceptación

1. ✅ El servidor se inicia correctamente por stdio
2. ✅ Implementa la herramienta `haiku` con parámetros `idioma` y `tema`
3. ✅ Genera haikus válidos usando GPT-4.1-mini
4. ✅ Lee la clave API desde variable de entorno `OPENAI_API_KEY`
5. ✅ Maneja errores de forma apropiada
6. ✅ Código está bien documentado y estructurado

## Próximos Pasos

1-> crear el esqueleto de la aplicacion con una herramienta (tool) de test
2-> crear el generador de haikus y hacer un mini programa de testing desde la linea de comandos
3-> integrar las dos cosas y terminar el proyecto