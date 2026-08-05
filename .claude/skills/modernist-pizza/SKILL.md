---
name: modernist-pizza
description: Motor técnico de pizza baseado no Modernist Pizza (Myhrvold & Migoya), volumes 1 e 2. Traz as 10 massas-mestre com fórmula completa em percentual de padeiro, a física de forno (radiação, condução, emissividade, heat pipe, gum line), fermentação (bulk, dobras, prova fria/ambiente/quente, ponto, dough CPR), farinha (proteína, cinzas, W, granulometria), água, fermento, sal, gordura e melhoradores, molhos, queijos, coberturas e diagnóstico de defeitos. Use SEMPRE que a conversa envolver massa de pizza, hidratação, percentual de padeiro, glúten, autólise, poolish, levain, biga, fermentação a frio, dobras, ponto da massa, abrir/modelar massa, forno (a lenha, a gás, deck, esteira, combi, convecção, doméstico, portátil), aço ou pedra de forno, temperatura e tempo de assagem, leopardagem, cornicione, gum line, borda, miolo/alvéolo, molho de tomate, San Marzano, mussarela/fior di latte/burrata, gramagem de cobertura, ou qualquer defeito de pizza ("massa não estica", "fundo queimado", "centro ensopado", "borda murcha", "queijo não derrete", "massa passou do ponto"). Dispara também para estilos: napolitana, New York, artisan, al taglio, Detroit, focaccia, deep-dish, thin-crust, brasileira, NY square.
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
   (`references/10-diagnostico.md`, seção 8). Não mande ninguém trocar de batedeira ou
   filtrar a água.
3. Distinga **preferência** de **defeito**. Crosta mole × crocante é preferência. Gum line,
   massa sub-salgada, crosta carbonizada e centro ensopado são defeito em qualquer estilo.
4. Quando a pergunta for um sintoma ("minha massa não estica"), vá direto ao
   `references/10-diagnostico.md`.
5. Percentual de padeiro sempre sobre **net contents** (a fórmula real, com a farinha e a
   água do pré-fermento contabilizadas).

## Roteiro de referências

| Arquivo | Quando abrir |
|---|---|
| `references/01-formulas-massas.md` | Fórmulas das 10 mestres, pesos por tamanho, cross-crusting, famílias de variação, aditivos |
| `references/02-mistura-e-gluten.md` | Percentual de padeiro, estágios de glúten, DDT, autólise, batedeiras, dupla hidratação, ferramentas |
| `references/03-fermentacao.md` | Bulk, dobras, prova (fria/ambiente/quente), temperar, chamar o ponto, dough CPR, poolish, levain, tipos e conversões de fermento |
| `references/04-divisao-modelagem.md` | Bancada, farinha de bancada, dividir, pré-modelar (bola, bâtard, wonton), massa molhada, transferir com pá/tela/papel |
| `references/05-fornos-e-cocao.md` | Física do assar, tipos de forno, temperaturas e tempos, rotação, pré-aquecimento, aço/pedra, gum line, leopardagem, pré-assar, problemas |
| `references/06-ingredientes.md` | Farinha (proteína, cinzas, W, partícula, marcas), água, sal, açúcar, gordura, relaxantes, melhoradores |
| `references/07-molhos.md` | Consistência por estilo, gramagem, tomates enlatados, receita paramétrica, marinara, molhos não-tomate |
| `references/08-queijos-e-coberturas.md` | Física do derretimento, gramagem de queijo, preparo por categoria, payload de cobertura, quando aplicar |
| `references/09-estilos.md` | O que define um estilo, atributos universais de qualidade, teste triangular, as 10 famílias |
| `references/10-diagnostico.md` | **Sintoma → causa → correção.** Comece por aqui em pergunta de problema |

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
| Focaccia | ~87% | 2,02% | 0,25% | 4,04% azeite | alta força 13,5–15% |

### Temperatura e tempo

| Estilo | Temperatura | Tempo |
|---|---|---|
| Napolitana | **425–480 °C** | **1–1½ min** |
| New York · al taglio | 315 °C | 4–5 min · 11 min |
| Thin-crust · brasileira | 285 °C | 5 min |
| Artisan | 285 °C | 6–7 min |
| NY square | 285 °C | 27 min (pré-assada) |
| Detroit | 275 °C | 15 min |
| Deep-dish | 250 °C | 27 min |
| Focaccia | 245 °C | 12–15 min |

### Prova

**Frio 4 °C**: thin-crust 24 h · brasileira 24 h · deep-dish 24 h · napolitana c/ poolish 48 h ·
New York 48 h · artisan 48 h.
**Ambiente 21 °C**: thin-crust 2 h · brasileira 1½ h · deep-dish 2–4 h · **napolitana 20–24 h
(bulk) + 3 h (bolas)** · focaccia 3 h · NY square 3 h · al taglio 3 h · Detroit 3 h.
**Quente 27 °C / 65% UR**: focaccia 2 h · NY square 2 h · al taglio 2 h · Detroit 2½ h.

Temperar massa fria: **2 h** antes de abrir. Tolerância de tempo de prova: **±15%**.

### Marcos de temperatura interna
50–60 °C levedura morre · 55–65 °C amido incha · 60–80 °C gelatinização + coagulação (fim do
oven spring) · ~85 °C amido "cozido" · 91–93 °C miolo estruturado · **130 °C na superfície:
Maillard**.

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
  **60% farinha de bolo + 40% farinha de pão**.
- Temperaturas estão em °C com o °F original entre barras quando o livro dá os dois.
