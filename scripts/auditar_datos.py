"""Regenera la auditoría y las estadísticas del CSV recibido, sin modificarlo."""
from pathlib import Path
import hashlib
import json
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]

def main():
    path = ROOT / 'datos/peajes_2019_2022.csv'
    d = pd.read_csv(path).drop(columns=['Unnamed: 0'], errors='ignore')
    stats = {
        'filas': len(d), 'columnas_analiticas': len(d.columns),
        'peajes': d.Peaje.nunique(),
        'fecha_desde_min': d.FechaDesde.min(), 'fecha_hasta_max': d.FechaHasta.max(),
        'nulos': int(d.isna().sum().sum()),
        'duplicados_sin_indice': int(d.duplicated().sum()),
        'sha256_csv': hashlib.sha256(path.read_bytes()).hexdigest(),
        'identidad_ingreso_max_error_abs': float(
            (d.IngresoPromedioDiario - d.ValorTarifa*d.TraficoPromedioDiario).abs().max())
    }
    result = ROOT / 'resultados'
    result.mkdir(exist_ok=True)
    (result/'auditoria_datos.json').write_text(
        json.dumps(stats, ensure_ascii=False, indent=2), encoding='utf-8')
    d[['ValorTarifa', 'TraficoPromedioDiario', 'IngresoPromedioDiario']].describe().to_csv(
        result/'estadisticas_descriptivas.csv')
    print(json.dumps(stats, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
