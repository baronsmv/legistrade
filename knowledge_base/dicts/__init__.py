import importlib
import os

knowledge_base = {}

current_dir = os.path.dirname(__file__)

for filename in os.listdir(current_dir):
    if filename.endswith(".py") and filename != "__init__.py":
        module_name = filename[:-3]
        module = importlib.import_module(f".{module_name}", package=__name__)

        if hasattr(module, module_name):
            obj = getattr(module, module_name)
            globals()[module_name] = obj  # Agrega al espacio de nombres del paquete
            knowledge_base[module_name] = obj

if __name__ == "__main__":
    from pprint import pprint

    pprint(knowledge_base)
