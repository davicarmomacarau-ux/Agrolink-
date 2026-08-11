# ============================================
# AgroLink - app.py
# ============================================

from flask import Flask, render_template_string
from rich.console import Console
import threading
import random
import time
import sys
import os

from database import Database
from frontend import HTML_TEMPLATE

console = Console()
app = Flask(__name__)

# Estado global do sistema
system_state = {
    "cycle": 0
}

def telemetry_worker():
    """Thread em segundo plano para simular a coleta periódica de sensores."""
    console.print("[bold green][INFO] AgroLink Telemetry Worker iniciado.[/bold green]")
    
    cycle = 1
    while True:
        try:
            # Cria a instância do banco dentro do ciclo para conexões isoladas
            db = Database()
            devices = db.get_devices()
            
            for dev in devices:
                device_id = dev[0]
                # Simula leituras de temperatura e umidade
                temp = round(random.uniform(22.0, 35.0), 2)
                humidity = round(random.uniform(40.0, 85.0), 2)
                
                db.add_telemetry(device_id, temp, humidity)
            
            system_state["cycle"] = cycle
            console.print(f"[cyan][AgroLink][/cyan] Coleta realizada - Ciclo #{cycle}")
            cycle += 1
            
        except Exception as e:
            console.print(f"[bold red][ERRO][/bold red] Falha na coleta de telemetria: {e}")
            
        time.sleep(10)  # Intervalo de 10 segundos entre cada coleta


@app.route('/')
def index():
    """Rota principal do Dashboard."""
    try:
        db = Database()
        devices = db.get_devices()
        readings = db.get_latest_telemetry(limit=10)
    except Exception as e:
        console.print(f"[bold red][ERRO][/bold red] Falha ao carregar dados do dashboard: {e}")
        devices, readings = [], []
    
    return render_template_string(
        HTML_TEMPLATE, 
        devices=devices, 
        readings=readings, 
        cycle=system_state["cycle"]
    )


if __name__ == "__main__":
    # Garante a inicialização das tabelas antes de subir as threads
    try:
        init_db = Database()
    except Exception as e:
        console.print(f"[bold red][ERRO][/bold red] Falha ao inicializar o banco: {e}")

    # Inicia a thread de telemetria em segundo plano
    worker_thread = threading.Thread(target=telemetry_worker, daemon=True)
    worker_thread.start()

    # Define a porta (10000 como padrão ou a do Render)
    port = int(os.environ.get("PORT", 10000))
    
    try:
        app.run(host="0.0.0.0", port=port)
    except (KeyboardInterrupt, SystemExit):
        console.print("[yellow]Encerrando o serviço AgroLink...[/yellow]")
        sys.exit(0)