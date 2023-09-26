import os
from pathlib import Path

# Construir la ruta al directorio base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# ... (resto del archivo settings.py)

TEMPLATES = [
    {
        # ...
        'DIRS': [BASE_DIR / 'totalmarketing_entrega/templates'],
        # ...
    },
]
