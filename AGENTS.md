# AGENTS.md

Instrucciones permanentes para agentes que trabajan en este repositorio con
OpenCode.

## Propósito del proyecto

El Proyecto 0 busca configurar un ambiente reproducible en Python, obtener
información real del computador e implementar y probar una multiplicación de
matrices sencilla.

## Reglas generales

- Mantener el código sencillo y fácil de explicar.
- No inventar mediciones del computador: todos los datos del sistema deben
  obtenerse ejecutando los scripts, nunca escribirlos a mano.
- Conservar los datos originales generados por los scripts.
- No crear matrices de tamaño que puedan agotar la memoria.
- No subir credenciales, archivos `.env` ni el ambiente virtual (`.venv/`).
- No ejecutar comandos destructivos de Git, como `git reset --hard`.
- No hacer `git commit` ni `git push` sin autorización explícita del usuario.
- Antes de confirmar cambios, mostrar al usuario los cambios realizados.

## Flujo de trabajo

1. Ejecutar `git status` antes de modificar archivos.
2. Revisar la estructura actual del repositorio.
3. Proponer un plan breve antes de implementar.
4. Después de modificar código, ejecutar `pytest` para verificar.
5. Explicar los cambios realizados y mostrar el resultado de `git diff`.
