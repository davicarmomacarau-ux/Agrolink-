# ============================================
# AgroLink - frontend.py
# ============================================

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="refresh" content="5">
    <title>AgroLink Dashboard</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Segoe UI', system-ui, sans-serif; }
        body { background-color: #0f172a; color: #f8fafc; padding: 20px; display: flex; justify-content: center; }
        .dashboard { width: 100%; max-width: 900px; display: flex; flex-direction: column; gap: 20px; }
        .header { background-color: #1e293b; padding: 24px; border-radius: 12px; border: 1px solid #334155; text-align: center; }
        .header h1 { color: #22c55e; font-size: 28px; margin-bottom: 6px; }
        .header p { color: #94a3b8; font-size: 14px; }
        
        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 16px; }
        .card { background-color: #1e293b; padding: 20px; border-radius: 12px; border: 1px solid #334155; }
        .card h3 { color: #38bdf8; font-size: 16px; margin-bottom: 12px; border-bottom: 1px solid #334155; padding-bottom: 8px; }
        
        .device-item { display: flex; justify-content: space-between; align-items: center; padding: 8px 0; border-bottom: 1px solid #334155; font-size: 14px; }
        .device-item:last-child { border-bottom: none; }
        .badge { padding: 4px 10px; border-radius: 12px; font-size: 12px; font-weight: bold; background-color: rgba(34, 197, 94, 0.2); color: #4ade80; border: 1px solid #22c55e; }
        
        table { width: 100%; border-collapse: collapse; margin-top: 8px; font-size: 14px; }
        th, td { text-align: left; padding: 10px; border-bottom: 1px solid #334155; }
        th { color: #94a3b8; font-weight: 600; }
        tr:hover { background-color: #0f172a; }
    </style>
</head>
<body>
    <div class="dashboard">
        <div class="header">
            <h1>🌱 AgroLink</h1>
            <p>Plataforma de Telemetria e Monitoramento Agrícola</p>
        </div>

        <div class="grid">
            <div class="card">
                <h3>Sensores Conectados</h3>
                {% for dev in devices %}
                <div class="device-item">
                    <span>{{ dev[1] }} ({{ dev[2] }})</span>
                    <span class="badge">{{ dev[3] }}</span>
                </div>
                {% endfor %}
            </div>

            <div class="card">
                <h3>Resumo do Sistema</h3>
                <div class="device-item">
                    <span>Status do Servidor</span>
                    <span class="badge">Online</span>
                </div>
                <div class="device-item">
                    <span>Ciclos de Leitura</span>
                    <strong>#{{ cycle }}</strong>
                </div>
            </div>
        </div>

        <div class="card">
            <h3>Últimas Leituras de Campo</h3>
            <table>
                <thead>
                    <tr>
                        <th>Sensor</th>
                        <th>Temperatura</th>
                        <th>Umidade</th>
                        <th>Horário</th>
                    </tr>
                </thead>
                <tbody>
                    {% for row in readings %}
                    <tr>
                        <td>{{ row[1] }}</td>
                        <td>{{ "%.1f"|format(row[2]) }} °C</td>
                        <td>{{ "%.1f"|format(row[3]) }} %</td>
                        <td>{{ row[4] }}</td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
    </div>
</body>
</html>
"""