import pytest
from unittest.mock import patch
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def test_model_not_found():
    from api import app  # esto debería fallar si el modelo no existe, pero lo parcheamos antes de importar
    # Parchear os.path.exists para que retorne False
    with patch('os.path.exists', return_value=False):
        with pytest.raises(RuntimeError, match="Modelo no encontrado en"):
            # Forzar la recarga del módulo api (para que evalúe la condición)
            import importlib
            import api
            importlib.reload(api)
