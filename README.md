# Deep Learning

## Configurar

1. Clonar repositorio.
    ```bash
    git clone https://github.com/gonblas/deep-learning-unlp
    ```

2. Crear un entorno virtual.
    ```bash
    python -m venv env
    ```
3. Activar entorno virtual
   - En Linux/Mac:
     ```bash
     source env/bin/activate
     ```
   - En Windows (CMD):
     ```cmd
     .\env\Scripts\activate
     ```
   - En Windows (PowerShell):
     ```powershell
     .\env\Scripts\Activate.ps1
     ```
1. Instalar dependencias.
    ```bash
      pip install -r requirements.txt
      python setup.py sdist bdist_wheel
      pip install .
    ```