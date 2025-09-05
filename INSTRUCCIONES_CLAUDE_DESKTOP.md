# 🚀 Configuración para Claude Desktop

## Archivo de Configuración

Para usar este servidor MCP con Claude Desktop, debes agregar la siguiente configuración al archivo de configuración de Claude Desktop.

### Ubicación del archivo de configuración:
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

## Opción 1: Configuración Simple (usando run_server.py)

```json
{
  "mcpServers": {
    "haiku-mcp": {
      "command": "/opt/homebrew/Caskroom/mambaforge/base/bin/uv",
      "args": ["run", "run_server.py"],
      "cwd": "/Users/granludo/Code/mini-mcp-server"
    }
  }
}
```

## Opción 2: Configuración Directa (usando el módulo Python)

```json
{
  "mcpServers": {
    "haiku-mcp": {
      "command": "/opt/homebrew/Caskroom/mambaforge/base/bin/uv",
      "args": ["run", "python", "-m", "haiku_mcp.server"],
      "cwd": "/Users/granludo/Code/mini-mcp-server"
    }
  }
}
```

## Opción 3: Si tienes múltiples servidores MCP

Si ya tienes otros servidores MCP configurados, agrega esta entrada a tu configuración existente:

```json
{
  "mcpServers": {
    "otro-servidor": {
      // ... configuración existente ...
    },
    "haiku-mcp": {
      "command": "/opt/homebrew/Caskroom/mambaforge/base/bin/uv",
      "args": ["run", "run_server.py"],
      "cwd": "/Users/granludo/Code/mini-mcp-server"
    }
  }
}
```

## 📝 Pasos para Configurar

1. **Abre el archivo de configuración**:
   ```bash
   # En macOS
   open ~/Library/Application\ Support/Claude/
   # O edita directamente
   nano ~/Library/Application\ Support/Claude/claude_desktop_config.json
   ```

2. **Copia una de las configuraciones anteriores** y pégala en el archivo

3. **Guarda el archivo** y **reinicia Claude Desktop**

4. **Verifica la conexión**:
   - En Claude Desktop, deberías ver "haiku-mcp" en la lista de servidores MCP conectados
   - Prueba escribiendo: "Genera un haiku sobre la naturaleza en español"

## 🔧 Troubleshooting

### Si el servidor no se conecta:

1. **Verifica que uv esté instalado y funcione**:
   ```bash
   /opt/homebrew/Caskroom/mambaforge/base/bin/uv --version
   ```

2. **Verifica que el servidor funcione manualmente**:
   ```bash
   cd /Users/granludo/Code/mini-mcp-server
   /opt/homebrew/Caskroom/mambaforge/base/bin/uv run run_server.py
   ```

3. **Verifica los logs de Claude Desktop**:
   - En macOS: `~/Library/Logs/Claude/`

4. **Asegúrate de que el archivo .env existe** con tu API key:
   ```bash
   cat /Users/granludo/Code/mini-mcp-server/.env
   # Debe mostrar: OPENAI_API_KEY=tu_clave_aqui
   ```

## ✨ Herramientas Disponibles

Una vez configurado, tendrás acceso a estas herramientas en Claude Desktop:

- **test_tool(message)**: Herramienta de prueba que convierte texto a mayúsculas
- **haiku(idioma, tema)**: Genera haikus usando GPT-4o-mini en el idioma especificado

### Ejemplos de uso en Claude Desktop:

```
"Usa la herramienta test_tool con el mensaje 'hola mundo'"
"Genera un haiku en francés sobre el otoño"
"Crea un haiku en inglés sobre el océano"
```

¡Listo! Tu servidor MCP de haikus está configurado para Claude Desktop 🎉
