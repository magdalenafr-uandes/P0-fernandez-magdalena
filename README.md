# P0-fernandez-magdalena

Proyecto 0 MCOC

## Propósito general

El Proyecto 0 busca poner en práctica los conceptos básicos del curso de
Métodos Computacionales (MCOC) mediante un proyecto incremental. En la
primera entrega (P0E1) se configura el ambiente de trabajo y se construyen
herramientas sencillas para obtener información del sistema y realizar
multiplicación de matrices.

## Entorno

- Sistema operativo: Windows
- Python 3.11.13

## Configuración del ambiente

Crear el ambiente virtual:

```powershell
python -m venv .venv
```

Activar el ambiente virtual:

```powershell
.\.venv\Scripts\Activate.ps1
```

Instalar las dependencias:

```powershell
pip install -r requirements.txt
```

## Ejecutar el proyecto

Obtener la información del computador:

```powershell
python src/system_info.py
```

Ejecutar las pruebas:

```powershell
python -m pytest
```

## Estado actual

- Ambiente virtual configurado y dependencias instaladas.
- `src/system_info.py` implementado; `data/system_info.json` generado con
  datos reales del computador.
- `src/mimatmul.py` implementado con dos pruebas iniciales aprobadas.
