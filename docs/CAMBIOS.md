# Criterios editoriales

- Póster: se eligió el PDF con referencias. El PDF alternativo y el JPG de casi 20 MB no aportan una versión principal adicional; se generó una vista previa ligera.
- Notebooks: se consolidó la versión de 74 celdas, retirando mapas redundantes, una gráfica temporal duplicada, celdas vacías y salidas pesadas. La versión de 46 celdas aportó las métricas numéricas históricas; se exportaron a CSV. El notebook inicial documentó limpieza y variables derivadas para el informe.
- Código: lectura local del CSV; actualización de `sparse=False` a `sparse_output=False`; corrección del orden de coordenadas en el mapa conservado; corrección del mensaje que imprimía métricas antiguas en la variante de mayor learning rate; imágenes nuevas a `resultados/` y menor resolución de exportación.
- Metodología: la fuga de la cascada y el preprocesamiento neuronal previo a la división se documentan y permanecen identificados como decisiones históricas. No se inventaron métricas faltantes ni se reconstruyó una tabla de ingresos sin respaldo.
- Datos y figuras: se conservan bytes originales del CSV y de los PNG seleccionados; el nombre con `&` se sustituyó por `y` para facilitar rutas.
- Entregables nuevos: informe, README, diccionario, evaluación de referencia separada, auditoría, configuración Git y guía de publicación.

La selección completa, tamaños y SHA-256 de los originales están en `seleccion_archivos.json`. El ZIP original permanece en la carpeta de trabajo y no debe añadirse al repositorio preparado.
