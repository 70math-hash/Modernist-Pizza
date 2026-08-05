---
name: modernist-pizza
description: Motor técnico de pizza baseado no Modernist Pizza (Myhrvold & Migoya), volumes 1 e 2. Traz as 10 massas-mestre e ~30 sub-mestres com fórmula completa em percentual de padeiro, as 7 massas sem glúten, as 10 grades de variação (levain, second-chance, compleat wheat, grãos/nozes/sementes, country, grãos antigos, no-knead, daily pizza, purês de sabor, blend sem glúten), os tempos de mistura de cada massa em cada tipo de batedeira, o planejamento de produção (cronograma etapa por etapa, capacidade de forno, escala, antecedência), o cálculo de fórmula (percentual de padeiro, net contents, DDW, RCF), a física de forno (radiação, condução, emissividade, heat pipe, gum line), fermentação (bulk, dobras, prova fria/ambiente/quente, ponto, dough CPR), o sistema completo de levain, farinha (proteína, cinzas, W, granulometria), água, fermento, sal, gordura e melhoradores, molhos de tomate (consistência, correção de sabor, compra de enlatado) e não-tomate (béchamel, emulsões, caldos, purês), queijo (compra, ralado, antiaglomerante, conservação, congelar, vegano) e queijo caseiro (fior di latte, burrata, ricota, frankencheese), payload e preparo de coberturas, azeite, a pesquisa de campo em São Paulo e Buenos Aires, e diagnóstico de defeitos. Use SEMPRE que a conversa envolver massa de pizza, hidratação, percentual de padeiro, escalonar receita, glúten, autólise, poolish, levain/fermento natural, biga, fermentação a frio, dobras, ponto da massa, abrir/modelar massa, batedeira (espiral, planetária, garfo, diving arm, processador), tempo de batida, forno (a lenha, a gás, deck, esteira, combi, convecção, doméstico, portátil), aço ou pedra de forno, temperatura e tempo de assagem, leopardagem, cornicione, gum line, borda, miolo/alvéolo, escala de produção, quantas pizzas por serviço, pré-assar, pizza para muita gente, molho de tomate, San Marzano, lata de tomate, pesto, béchamel, molho branco, creme de leite na pizza, mussarela/fior di latte/burrata/ricota, queijo ralado, queijo vegano, Catupiry, gramagem de cobertura, azeite, pepperoni que encaracola, pizza romana, Pinsa, al taglio, tomato pie, bar pizza, a cena de pizza de São Paulo, fainá, canchera, fugazzeta, ou qualquer defeito de pizza ("massa não estica", "fundo queimado", "centro ensopado", "borda murcha", "queijo não derrete", "massa passou do ponto"). Dispara também para estilos: napolitana, AVPN, New York, New Haven/apizza, Quad Cities, artisan, al taglio, pala, Detroit, focaccia, sfincione, deep-dish, thin-crust, brasileira, NY square, Old Forge, al molde argentina, sem glúten, integral, centeio.
---

# Modernist Pizza

Base técnica extraída dos volumes **1 (History and Fundamentals)** e **2 (Techniques and
Ingredients)** de *Modernist Pizza*, de Nathan Myhrvold e Francisco Migoya. O volume 3
(receitas montadas) não está nesta base.

## Como usar

1. Responda com **números e mecanismo**, não com opinião. O livro inteiro é feito de
   experimentos controlados — quando houver um resultado experimental relevante, cite-o.
2. Antes de recomendar uma mudança, pergunte-se: **isso passa no teste de significância?**
   Há uma lista de coisas que o livro testou e concluiu que **não fazem diferença**
   (`references/10-diagnostico.md`, seção 8). Não mande ninguém trocar de batedeira, padronizar
   o ralo do queijo ou filtrar a água.
3. Distinga **preferência** de **defeito**. Crosta mole × crocante é preferência. Gum line,
   massa sub-salgada, crosta carbonizada e centro ensopado são defeito em qualquer estilo.
4. Quando a pergunta for um sintoma ("minha massa não estica"), vá direto ao
   `references/10-diagnostico.md`.
5. Percentual de padeiro sempre sobre **net contents** (a fórmula real, com a farinha e a
   água do pré-fermento contabilizadas). A coluna de percentual da lista de ingredientes **não
   é a fórmula** quando há poolish ou levain — ver `references/18-calculo-e-escalonamento.md`.
6. **Quando o livro se contradiz, a ficha de receita manda sobre o quadro geral.** As fichas
   trazem o valor testado para aquela massa; os quadros generalizam por família. Onde os dois
   divergem, este material publica o valor da ficha e registra a outra leitura.
7. Este cartão é resumo. **Para qualquer número que vá virar produção, abra a referência** —
   as faixas completas estão lá, e o cartão arredonda.

## Roteiro de referências

| Arquivo | Quando abrir |
|---|---|
| `references/01-formulas-massas.md` | Fórmulas das 10 mestres, pesos por tamanho, cross-crusting, famílias de variação, aditivos |
| `references/02-mistura-e-gluten.md` | Percentual de padeiro, estágios de glúten, DDT, autólise, dupla hidratação, ferramentas |
| `references/03-fermentacao.md` | Bulk, dobras, prova (fria/ambiente/quente), temperar, chamar o ponto, dough CPR, poolish, tipos e conversões de fermento |
| `references/04-divisao-modelagem.md` | Bancada, farinha de bancada, dividir, pré-modelar (bola, bâtard, wonton), massa molhada, transferir com pá/tela/papel |
| `references/05-fornos-e-cocao.md` | Física do assar, tipos de forno, temperaturas e tempos, rotação, pré-aquecimento, aço/pedra, gum line, leopardagem, pré-assar e par-assar, problemas |
| `references/06-ingredientes.md` | Farinha (proteína, cinzas, W, partícula, marcas), água, sal, açúcar, gordura, relaxantes, melhoradores |
| `references/07-molhos.md` | Visão geral de molho: o que faz, consistência por estilo, gramagem, quando aplicar, problemas, tomate e San Marzano |
| `references/08-queijos-e-coberturas.md` | Física do derretimento, gramagem de queijo por estilo e tamanho, preparo por categoria |
| `references/09-estilos.md` | O que define um estilo, atributos universais de qualidade, teste triangular, as 10 famílias, e **os nomes que confundem** (pizza romana, Pinsa, al taglio, tomato pie, bar pizza) |
| `references/10-diagnostico.md` | **Sintoma → causa → correção.** Comece por aqui em pergunta de problema |
| `references/11-submasters-e-variacoes.md` | Os ~30 sub-mestres com fórmula fechada: AVPN, napolitana de alta hidratação e de centeio, apizza (New Haven), Quad Cities, sfincione, pala, Old Forge, al molde argentina, Detroit modernista, deep-dish enriquecida, versões emergency/direct/poolish |
| `references/12-tabelas-de-variacao.md` | As 10 grades de variação sobre **qualquer** mestre, com fórmula completa por estilo: levain, second-chance, compleat wheat, grãos/nozes/sementes, country, grãos antigos, no-knead, daily pizza, purês de sabor, blend sem glúten |
| `references/13-levain.md` | Construir do zero, alimentar, estágios, guardar a 13 °C, hidratação reduzida, desidratar, congelar, second-chance, problemas |
| `references/14-preparo-de-coberturas.md` | Cru ou cozido (tabela de ~24 itens) e as receitas de cobertura: rösti, frico, linguiça, confit, caramelizar sob pressão, assar legume e assar fruta |
| `references/15-molhos-brancos-e-queijos-caseiros.md` | Espessantes e dispersão, teste de consistência, e o **mapa** das famílias de molho não-tomate e de queijo caseiro |
| `references/16-planejamento-e-producao.md` | **Quando e quanto produzir.** Cronograma etapa por etapa das 10 mestres, checagem de pré-produção, capacidade de forno como gargalo, **bolear em ondas** (a bola tem prazo, o bulk não), que massa escolher por situação, FIFO e descanso de bancada, antecedência, janela de serviço (napolitana × New York), proofer × geladeira, pizza para muita gente e evento |
| `references/17-batedeiras-e-tempos-de-mistura.md` | **Quantos minutos em cada velocidade, massa a massa e batedeira a batedeira.** Carga mínima e máxima da bacia, multiplicador da receita, qual mestre cada sub-mestre herda, onde entra cada ingrediente, operação e segurança da máquina, mistura à mão |
| `references/18-calculo-e-escalonamento.md` | Escalonar receita, DDW, RCF, as duas notações de porcentagem, fechar o net contents com pré-fermento, manteiga 81/19, peso de bola por tamanho, batelada mínima |
| `references/19-molho-de-tomate-avancado.md` | Medir e ajustar consistência, engrossar com xantana, **correção de sabor do molho** (acidez, umami, doçura em %), as receitas fechadas (New York/artisan, amatriciana, fermentado, slow-roasted, cru), compra de enlatado e tamanhos de lata, pesto paramétrico |
| `references/20-molhos-brancos-cremes-e-emulsoes.md` | Creme de leite como molho, lácteos de prateleira, béchamel e sopas **sem roux** com gelana, molho de queijo, adaptar sopa/purê/caldo/curry para pizza, holandesa, aioli, maionese, barbecue, bolognese, carbonara, cacio e pepe, molhos de vegetal |
| `references/21-queijo-compra-e-operacao.md` | Comprar queijo, ralado × fatiado, antiaglomerante, baixa umidade em napolitana, rendimento leite→queijo, listas de blend seguro e de quando cada queijo entra, congelar, conservação com CO₂, Catupiry, veganos |
| `references/22-mussarela-e-queijos-caseiros.md` | **Idade ótima da mussarela**, esticar, fior di latte em forno de deck, e as receitas fechadas: receita-mãe, bulk stretched, SHMP, cultivada/cabra/buttermilk, burrata, mais gordura, infundidas, frankencheeses, ricotas |
| `references/23-coberturas-tecnicas-e-payload.md` | **Payload por tamanho** com o peso que entra no forno, quando aplicar cada categoria, biteability, refogar/fritar/vapor/escalfar/sous vide/char com números, fatiar carne e frios, pepperoni na compra, óleos aromatizados, azeite |
| `references/24-massas-sem-gluten.md` | As **7 massas sem glúten** fechadas, os padrões comuns, por que cada componente do blend está lá, a troca por Caputo Fiore Glut, psyllium e leopardagem |
| `references/25-pesquisa-de-campo.md` | **São Paulo e Buenos Aires vistos de fora**: as 16 casas paulistanas visitadas e o que cada uma ensina, os números do mercado, preço, Catupiry, molho golf, caixa redonda, eucalipto; canchera e fainá; e como ler lista de "melhor pizza" |

---

## Cartão de consulta rápida

### As 10 massas-mestre (net contents)

| Massa | Hidr. | Sal | IDY | Gordura | Farinha |
|---|---|---|---|---|---|
| Brasileira | 50,41% | 2,0% | 0,49% | 9,76% azeite | 60% bolo + 40% pão |
| Deep-dish | 60% | 2,11% | 0,82% | 8,68% banha+manteiga | pão 11,5–12% |
| Napolitana | 62,3% | 1,99% | **0,04%** | — | 00 ou pão 11,5–12,5% |
| New York | 69,49% | 2,46% | 0,48% | 3,39% azeite | alta força 13,5–15% |
| Detroit | 70,43% | 2,0% | **0,9%** | — | pão + 15% semolina |
| Thin-crust | 71,43% | 2,18% | 0,82% | 0 | pão 11,5–12% |
| Artisan | 72% | 2,0% | 0,43% | 3,2% azeite | alta força 13–14% |
| NY square | 74,68% | 2,0% | 0,49% | 3,8% azeite | alta força 13,5–15% |
| Al taglio | 79,73% | 2,5% | 0,5% | 4,02% azeite | pão 11,5–12% ou 00 |
| Focaccia | 87,27% | 2,02% | 0,25% | 4,04% azeite | alta força 13,5–15% |

### Temperatura e tempo

| Estilo | Temperatura | Tempo |
|---|---|---|
| Napolitana | **425–480 °C** | **1–1½ min** |
| New York | **315 °C** · ou 285 °C | **4–5 min** · ou 5–6 min |
| Al taglio | 315 °C | 11 min |
| Thin-crust · brasileira | 285 °C | 5 min |
| Artisan | 285 °C | 6–7 min |
| NY square | 285 °C | 27 min (pré-assada) |
| Detroit | 275 °C | 15 min |
| Deep-dish | 250 °C | 27 min |
| Focaccia | 245 °C | 12–15 min |

> Os pares de temperatura e tempo andam juntos: **285 °C com 5–6 min** OU **315 °C com
> 4–5 min** — nunca o intervalo cruzado. Fora da napolitana, o livro generaliza
> **245–285 °C** no texto; a tabela acima vem das fichas de receita e prevalece.
> A napolitana aparece como 425–480 °C no capítulo de assagem e **450–480 °C** no de massas.

### Prova

**Frio 4 °C**: thin-crust 24 h · brasileira 24 h · deep-dish 24 h · napolitana c/ poolish 48 h ·
New York 48 h · artisan 48 h. New York e artisan aceitam **rebolear no 2º dia e voltar por até
mais 3 — 5 dias no total**.
**Ambiente 21 °C**: thin-crust **2–3 h** · brasileira 1½ h · deep-dish **1½ h** ·
**napolitana 20–24 h (bulk em bloco) + 3–4 h (bolas depois de bolear)** · focaccia 3 h ·
NY square 3 h · al taglio 3 h · Detroit 3 h.
**Quente 27 °C / 65% UR**: focaccia 2 h · NY square 2 h · al taglio 2 h · Detroit 2½ h.

> Thin-crust e deep-dish: os valores acima são **das fichas**. O quadro geral da p. 75 dá 2 h e
> 2–4 h, e o quadro da p. 25 dá 1½–2 h para as duas. Trabalhe pela ficha.
> **Prova fria não serve para massa de forma** — dá menos volume.

Temperar massa fria: **1½–2 h** antes de abrir, ou até a massa chegar a **13 °C / 55 °F**
internos. **Thin-crust abre com rolo direto do frio, sem temperar.**
Tolerância de tempo de prova: **±15%**.

### Marcos de temperatura interna
50–60 °C levedura morre · 55–65 °C amido incha · 60–80 °C gelatinização + coagulação (fim do
oven spring) · ~85 °C amido "cozido" · 91–93 °C miolo estruturado · **130 °C na superfície:
Maillard**.

### Conversão de fermento e substituições rápidas

**Fermento**: instantâneo → seco ativo **×1,33** · instantâneo → fresco **×3** · seco ativo →
fresco **×2,28**. **Poolish** (IDY sobre a farinha do poolish): 3 h = 0,4–0,5% · 8 h =
0,23–0,33% · 12–16 h = 0,1–0,2%.

**Variações sobre qualquer mestre** (fórmula completa em `12-tabelas-de-variacao.md`):
levain **24,3–47,5%** sobre a farinha · second-chance **0,43–1,5%** de IDY · compleat wheat
(farelo ≈14% da farinha + gérmen ≈2,5% + água de molho ≈13–20%) · grãos/nozes/sementes
**20–25%**, com pedaço de no máximo **3 mm** · country **30%** (15 integral + 15 centeio) ·
grãos antigos **40%** em três combinações por família de estilo · no-knead IDY **0,27%** com
bulk 12–18 h · daily pizza IDY 0,27% + ácido ascórbico 0,22%.

### Carga de batedeira (detalhe e tempos em `17-batedeiras-e-tempos-de-mistura.md`)

Bancada 4,5 qt **1–1,25 kg** · bancada 8 qt **1,5–1,75 kg** · planetária 12 qt **4–6 kg** ·
planetária 20 qt **6–8 kg** · diving arm 6 qt **3 kg** · processador **1–1,2 kg** · espiral e
garfo, mínimo recomendado **8 kg**. **Batelada mínima de batedeira de bancada: 800 g** — a bola
de New York de 35 cm pesa 400 g, abaixo do que a máquina bate direito.

### Cinco coisas que quase sempre são a resposta

1. **Não é o peso do molho que impede o centro de subir** — é o calor latente de vaporização.
2. **A gum line só se resolve pré-assando.** Todo o resto é mitigação.
3. **A chama não assa; o que assa é a radiação das paredes** (e as brasas, num forno a lenha).
4. **Massa mais molhada não dá mais volume**, e fermentação mais longa não dá crosta mais
   saborosa. A napolitana fica abaixo de 70% e tem miolo aberto.
5. **Para controlar a fermentação, mexa no fermento ou na temperatura — nunca no sal.**

---

## Notas de escopo

- Tudo aqui é dos volumes 1 e 2. Referências no formato `3:xx` no texto original apontam para
  o volume 3 (receitas montadas, montagem e assagem pizza a pizza), **que não está nesta base**.
  Se a pergunta for sobre a montagem específica de uma receita icônica, diga que essa parte
  está no volume 3.
- Nomes de farinha são marcas norte-americanas e italianas testadas pelos autores. Para uso no
  Brasil, traduza pelo **alvo numérico** (proteína, cinzas, W) em `references/06-ingredientes.md`,
  não pela marca. A única farinha brasileira do livro é a **Anaconda Tipo 1**
  (22,7 glúten úmido · 7,8 seco · W 268 · 0,45% cinzas), que os autores replicam com
  **60% farinha de bolo + 40% farinha de pão**. As marcas de queijo vegano testadas também são
  americanas — ali o livro manda testar as marcas locais, e a lista de modos de falha em
  `references/21-queijo-compra-e-operacao.md` é o que serve para conduzir o teste.
- Temperaturas estão em °C com o °F original entre barras quando o livro dá os dois.
- **Confiabilidade dos números.** O volume 2 foi extraído do texto digital do PDF — os números
  são fiéis, e é dele que vêm as fórmulas, os tempos de mistura, as gramagens e as grades de
  variação. O volume 1 é um PDF escaneado e passou por **OCR**, então tabelas numéricas dele
  (a especificação de farinhas em `06-ingredientes.md`, a conversão de fermento em
  `03-fermentacao.md`, a física de forno em `05-fornos-e-cocao.md`) têm risco de dígito trocado.
  Se um número do volume 1 parecer fora de escala, recalcule pelo percentual em vez de repetir
  a grama.
- **O que ainda não está nesta base**: o **capítulo de história** (vol. 1, cap. 1 — deixado de
  fora por decisão de escopo, não por falta de acesso), as **outras cidades** do capítulo de
  pesquisa de campo (Nápoles, Roma, Norte da Itália, Tóquio, Nova York, New Haven, Chicago,
  Detroit, Portland, São Francisco — só os quadros de números delas entraram no
  `25-pesquisa-de-campo.md`) e o **volume 3** inteiro.
