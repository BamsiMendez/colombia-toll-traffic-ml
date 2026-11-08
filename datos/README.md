# Datos

`peajes_2019_2022.csv` conserva exactamente los bytes del CSV procesado recibido. Contiene 26.986 filas, 16 variables analíticas y una columna `Unnamed: 0` de exportación, que se retira al leer. La huella SHA-256 está en `../resultados/auditoria_datos.json`.

El póster menciona Kaggle. Los notebooks leen copias mediante Dropbox, pero no incluyen una ficha inequívoca del dataset original, su autor ni licencia. No se afirma que Dropbox sea la fuente original ni que el archivo tenga una licencia abierta particular. La preparación desde datos brutos queda documentada en los notebooks originales del ZIP, pero el archivo bruto no está incluido. Antes de reutilizar o redistribuir el conjunto fuera del contexto del trabajo, debe recuperarse su ficha de procedencia.

| Campo | Significado y unidad |
|---|---|
| `IdPeaje` | Identificador de estación |
| `Peaje` | Nombre de estación; 119 valores distintos |
| `IdCategoriaTarifa` | Categoría I–VII seleccionada en el trabajo |
| `FechaDesde`, `FechaHasta` | Extremos del intervalo registrado |
| `ValorTarifa` | Tarifa nominal, COP |
| `Trafico` | Conteo de vehículos del registro |
| `TraficoEvasores` | Conteo registrado de evasores; definición de origen pendiente de verificar |
| `TraficoExentos787` | Conteo de exentos bajo el campo de la fuente |
| `Lat` | **Contiene longitud**, aproximadamente -77,41 a -72,09 |
| `Lon` | **Contiene latitud**, aproximadamente 1,09 a 11,44 |
| `DuracionPeriodo(DIAS)` | FechaHasta menos FechaDesde, sin sumar uno; 1–30 días |
| `TraficoPromedioDiario` | Trafico / duración, vehículos/día |
| `IngresoTotal` | ValorTarifa × Trafico, COP; ingreso calculado |
| `IngresoPromedioDiario` | IngresoTotal / duración, COP/día |
| `TipoVehiculo` | Etiqueta recodificada en el notebook a partir de categoría |
| `Unnamed: 0` | Índice de exportación sin uso analítico |

No se verificó que la recodificación de vehículos sea uniforme entre concesiones. No hay nulos ni duplicados completos después de retirar el índice, pero estas comprobaciones no garantizan calidad integral o cobertura completa del sistema de peajes. El conjunto bruto tenía nulos y el notebook inicial ejecutó `dropna`.

Los campos derivados conservan las definiciones históricas. Si los extremos del intervalo son inclusivos, la duración requeriría otra convención y cambiarían las respuestas diarias. El ingreso calculado no debe denominarse recaudo neto medido.
