# Modernist Pizza

Skill do Claude Code com a base técnica dos volumes **1 (History and Fundamentals)** e
**2 (Techniques and Ingredients)** de *Modernist Pizza*, de Nathan Myhrvold e Francisco Migoya.

O volume 3 (receitas montadas) não faz parte desta base — é o livro de receitas, e as
referências no formato `3:xx` que aparecem no texto original apontam para ele.

## Instalação

Copie a pasta da skill para onde o Claude Code procura skills:

```bash
cp -r .claude/skills/modernist-pizza ~/.claude/skills/
```

Ou deixe no repositório e trabalhe a partir daqui — o Claude Code carrega
`.claude/skills/` do diretório do projeto.

## O que tem dentro

```
.claude/skills/modernist-pizza/
├── SKILL.md                          roteador + cartão de consulta rápida
├── references/
│   ├── 01-formulas-massas.md         as 10 mestres, pesos, cross-crusting, variações
│   ├── 02-mistura-e-gluten.md        % de padeiro, glúten, DDT, autólise, batedeiras
│   ├── 03-fermentacao.md             bulk, dobras, prova, ponto, dough CPR, poolish, levain
│   ├── 04-divisao-modelagem.md       bancada, dividir, pré-modelar, transferir
│   ├── 05-fornos-e-cocao.md          física do assar, fornos, temperaturas, gum line
│   ├── 06-ingredientes.md            farinha, água, sal, açúcar, gordura, melhoradores
│   ├── 07-molhos.md                  consistência, gramagem, tomates, receita paramétrica
│   ├── 08-queijos-e-coberturas.md    derretimento, gramagem, payload
│   ├── 09-estilos.md                 o que define estilo, qualidade, teste triangular
│   ├── 10-diagnostico.md             sintoma → causa → correção
│   ├── 11-submasters-e-variacoes.md  os ~30 sub-mestres com fórmula fechada
│   ├── 12-tabelas-de-variacao.md     as 10 tabelas de variação sobre qualquer mestre
│   ├── 13-levain.md                  construir, alimentar, guardar, desidratar, ressuscitar
│   ├── 14-preparo-de-coberturas.md   cru ou cozido, assar, confitar, caramelizar sob pressão
│   └── 15-molhos-brancos-e-...md     molhos não-tomate, emulsões, queijos caseiros
└── scripts/
    ├── massa.py                      calculadora (escalona, converte, monta poolish)
    └── massas.json                   as 10 fórmulas + gramagens de molho e queijo
```

## Calculadora

```bash
python3 .claude/skills/modernist-pizza/scripts/massa.py listar
python3 .../massa.py ver napolitana
python3 .../massa.py calcular napolitana --pizzas 24
python3 .../massa.py calcular artisan --pizzas 12 --tamanho "40 cm"
python3 .../massa.py calcular focaccia --total 8kg
python3 .../massa.py fermento --de fresco --para instantaneo --peso 30
python3 .../massa.py poolish --farinha 500 --pronto 12-16h
python3 .../massa.py hidratacao
```

O comando `calcular` já devolve pré-fermento, massa, total, folga de bancada, processo,
temperatura e tempo de forno, gramagem de molho e queijo para o lote inteiro, e um aviso de
capacidade de batedeira.

## As 10 massas-mestre (net contents)

| Massa | Hidratação | Sal | Fermento (IDY) | Gordura |
|---|---|---|---|---|
| Brasileira | 50,41% | 2,00% | 0,49% | 9,76% |
| Deep-dish | 60,00% | 2,11% | 0,82% | 8,68% |
| Napolitana | 62,30% | 1,99% | 0,04% | 0 |
| New York | 69,49% | 2,46% | 0,48% | 3,39% |
| Detroit | 70,43% | 2,00% | 0,90% | 0 |
| Thin-crust | 71,43% | 2,18% | 0,82% | 0 |
| Artisan | 72,00% | 2,00% | 0,43% | 3,20% |
| New York square | 74,68% | 2,00% | 0,49% | 3,80% |
| Al taglio | 79,73% | 2,50% | 0,50% | 4,02% |
| Focaccia | 87,27% | 2,02% | 0,25% | 4,04% |

Cada mestre tem sub-mestres (direct, poolish, emergency, high-hydration) e as variações
regionais fiéis — AVPN, apizza de New Haven, Quad Cities, sfincione, pala, Old Forge, al molde
argentina. Todas em `references/11-submasters-e-variacoes.md`, com fórmula fechada.

## Confiabilidade dos números

O volume 2 foi extraído do texto digital do PDF: os números são fiéis. O volume 1 é um PDF
escaneado e passou por OCR, então as tabelas numéricas vindas dele (especificação de farinhas,
gramagens por estilo das tabelas de variação) têm risco de dígito trocado. As regras e os
percentuais são a parte confiável — se um número parecer fora de escala, recalcule pelo
percentual.

## O que não está aqui

O capítulo de história (vol. 1, cap. 1), o panorama mundial em profundidade (vol. 1, cap. 2),
o capítulo de pesquisa de campo (vol. 1, cap. 3, que inclui São Paulo e Buenos Aires), as 8
receitas individuais de massa sem glúten — o blend e as regras estão em
`12-tabelas-de-variacao.md` — e o volume 3 inteiro.
