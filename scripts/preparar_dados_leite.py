# Gera dados/leite.json a partir do repositório CITREN_leite.
# Uso: python scripts/preparar_dados_leite.py caminho/para/CITREN_leite dados/leite.json
import pandas as pd, json, sys
r = sys.argv[1]; out = sys.argv[2]
b = pd.read_csv(f'{r}/data/base_integrada_leite_agroclima.csv')
p = pd.read_csv(f'{r}/results/tables/predicciones_prueba.csv')
q = pd.read_csv(f'{r}/results/decline_risk/tables/predicoes_alerta_queda.csv')
anos = list(range(2006, 2020))
mun = []
for cod, g in b.groupby('codigo_municipio'):
    g = g.set_index('ano')
    prod = [None if pd.isna(g.producao_leite_mil_litros.get(a)) else int(round(g.producao_leite_mil_litros.get(a))) for a in anos]
    pr = p[p.codigo_municipio == cod]
    def serie(m):
        s = pr[pr.modelo == m].set_index('ano').predicao_mil_litros
        return [int(round(s.get(a))) if a in s.index else None for a in (2017, 2018, 2019)]
    qq = q[(q.codigo_municipio == cod) & (q.modelo == 'Random Forest')].set_index('ano')
    mun.append({'n': g.municipio.iloc[0], 'p': prod, 'rf': serie('Random Forest'), 'xg': serie('XGBoost'), 'lag': serie('Persistencia lag-1'),
                'qd': [int(qq.queda_10_pct.get(a)) if a in qq.index else None for a in (2017, 2018, 2019)],
                'qp': [round(float(qq.probabilidade_queda.get(a)), 2) if a in qq.index else None for a in (2017, 2018, 2019)]})
mun.sort(key=lambda m: -(m['p'][-1] or 0))
clima = pd.read_csv(f'{r}/data/clima_castro_a819_anual.csv')
total = b.groupby('ano').producao_leite_mil_litros.sum().round().astype(int).tolist()
d = {'anos': anos, 'total': total, 'mun': mun}
s = json.dumps(d, allow_nan=False, ensure_ascii=False, separators=(',', ':'))
open(out, 'w', encoding='utf-8').write(s)
print(len(s), clima.columns.tolist())


