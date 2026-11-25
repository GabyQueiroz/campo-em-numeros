# Campo em Números

Página com os resultados de duas pesquisas sobre a produção animal no Paraná, escrita para produtores e para quem trabalha com eles.

Site: https://gabyqueiroz.github.io/campo-em-numeros/

## O que tem na página

**Leite nos 399 municípios** (repositório [CITREN_leite](https://github.com/GabyQueiroz/CITREN_leite))

- Produção anual de leite do Paraná, de 2006 a 2019.
- Busca por município: histórico, previsão do modelo para 2017–2019 e anos com queda de 10% ou mais.
- Principais achados: a produção do ano anterior é o que mais explica a previsão, e repetir o número do ano anterior errou menos que os modelos testados.

**Peso de suínos por foto** (repositório [PesoSuinosDL](https://github.com/GabyQueiroz/PesoSuinosDL))

- Ideia, exemplo de imagem com o fundo removido e comparação de tamanho e rapidez dos modelos.
- Marcado como teste piloto: os erros de peso ainda não são válidos, porque a amostra usada leu o número da foto no lugar do peso real.

## Arquivos

```text
index.html                    página (HTML, CSS e JavaScript, sem dependências)
dados/leite.json              dados por município usados nos gráficos
imagens/suino-segmentacao.png exemplo da base pública PIGRGB-Weight
scripts/preparar_dados_leite.py  gera dados/leite.json a partir do CITREN_leite
```

Para gerar os dados de novo:

```bash
python scripts/preparar_dados_leite.py caminho/para/CITREN_leite dados/leite.json
```

## Fontes

- IBGE, Pesquisa da Pecuária Municipal, SIDRA tabela 74 (produção de leite).
- INMET, estação automática A819, Castro/PR (clima).
- PIGRGB-Weight, base pública de imagens de suínos.

Departamento de Informática, Universidade Estadual de Ponta Grossa (UEPG).
