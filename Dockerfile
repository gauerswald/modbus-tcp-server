FROM python:3.9-slim

# Arbeitsverzeichnis setzen
WORKDIR /app

# Abhängigkeiten installieren
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Quellcode in das Container-Image kopieren
COPY modbus_server.py /app/

# Command, um den Modbus Server zu starten
CMD ["python", "modbus_server.py"]
