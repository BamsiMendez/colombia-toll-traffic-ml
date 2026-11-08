# Validación de la preparación

Comprobaciones efectuadas el 8 de noviembre de 2026:

- CSV inspeccionado: dimensiones, fechas, categorías, peajes, nulos, duplicados completos, duraciones e identidad algebraica de ingreso.
- CSV y figuras contrastados por SHA-256 contra sus originales. El CSV no se reescribió.
- Código de las celdas del notebook consolidado validado mediante `ast.parse`; salidas y metadatos innecesarios retirados. No se ejecutó el notebook neuronal completo ni se afirma recuperación del entorno de 2025.
- `scripts/evaluar_referencia.py` ejecutado con ambas divisiones. Entorno: Python 3.11.13, scikit-learn 1.8.0, NumPy 1.26.4 y pandas 2.2.3. Métricas y tamaños guardados en los JSON de resultados.
- El RF aleatorio reproduce RMSE 718,596845, MAE 204,994041 y R² 0,883271, coincidentes con las salidas históricas hasta su precisión disponible.
- La evaluación temporal devuelve RMSE 1169,650029 y R² 0,790748 para tráfico. El codificador advierte categorías desconocidas en prueba; el comportamiento es esperado y está documentado.
- El script adicional evita ajustar transformaciones o bosque con prueba y calcula ingresos por identidad. No implementa la segunda etapa histórica ni validación fuera de pliegue para una cascada aprendida.
- Informe compilado desde LaTeX: 12 páginas, sin advertencias de cajas desbordadas. Se renderizaron y revisaron visualmente todas las páginas; se comprobaron también los enlaces relativos del README.

Los rangos de `requirements*.txt` son una propuesta de entorno moderno; no todos los paquetes opcionales se instalaron y probaron durante esta preparación. Las métricas neuronales históricas se respaldan por salidas guardadas, no por nuevos entrenamientos.
