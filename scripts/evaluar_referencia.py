"""Evaluación adicional de RF y del ingreso tarifa*tráfico; no reescribe resultados de 2025."""
from pathlib import Path
import argparse
import json
import platform
import numpy as np
import pandas as pd
import sklearn
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

ROOT = Path(__file__).resolve().parents[1]

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--division', choices=['aleatoria', 'temporal'], default='aleatoria')
    args = p.parse_args()
    df = pd.read_csv(ROOT / 'datos/peajes_2019_2022.csv')
    features = ['ValorTarifa', 'TipoVehiculo', 'Peaje', 'DuracionPeriodo(DIAS)']
    if args.division == 'aleatoria':
        train, test = train_test_split(np.arange(len(df)), test_size=.2, random_state=42)
        criterio = '80/20 de filas; semilla 42; no mide generalización a peajes nuevos'
    else:
        # Separación estricta por intervalos: ninguno del entrenamiento alcanza 2021.
        start = pd.to_datetime(df.FechaDesde)
        end = pd.to_datetime(df.FechaHasta)
        train = np.flatnonzero(end < pd.Timestamp('2021-01-01'))
        test = np.flatnonzero(start >= pd.Timestamp('2021-01-01'))
        criterio = 'entrenamiento: FechaHasta<2021-01-01; prueba: FechaDesde>=2021-01-01'
    assert set(train).isdisjoint(test) and len(train) and len(test)
    prep = ColumnTransformer([
        ('num', StandardScaler(), ['ValorTarifa']),
        ('cat', OneHotEncoder(drop='first', handle_unknown='ignore', sparse_output=False),
         ['TipoVehiculo', 'Peaje', 'DuracionPeriodo(DIAS)'])])
    model = Pipeline([('prep', prep), ('rf', RandomForestRegressor(n_estimators=100,
                                                        random_state=42, n_jobs=2))])
    model.fit(df.iloc[train][features], df.iloc[train].TraficoPromedioDiario)
    pred = model.predict(df.iloc[test][features])
    truth = df.iloc[test]
    def metrics(y, yhat):
        return {'RMSE':float(np.sqrt(mean_squared_error(y, yhat))),
                'MAE':float(mean_absolute_error(y, yhat)), 'R2':float(r2_score(y, yhat))}
    result = {'estado':'evaluacion adicional de 2026; no es la cascada historica',
              'division':args.division, 'criterio':criterio,
              'n_train':len(train),'n_test':len(test),'n_excluidas':len(df)-len(train)-len(test),
              'python':platform.python_version(),'sklearn':sklearn.__version__,
              'numpy':np.__version__,'pandas':pd.__version__,
              'trafico_rf':metrics(truth.TraficoPromedioDiario,pred),
              'ingreso_tarifa_por_trafico_rf':metrics(truth.IngresoPromedioDiario,
                                                     truth.ValorTarifa.to_numpy()*pred)}
    dest=ROOT / f'resultados/referencia_{args.division}.json'
    dest.write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(result,ensure_ascii=False,indent=2))

if __name__=='__main__':
    main()
