# Cálculo de fórmula e escalonamento

Fonte: *Modernist Pizza*, Vol. 2 — "Understanding Baker's Percentage" (p. 18–21) e
"Best Bets for Pizza Sizes" (p. 94).

O método e as definições estão em `02-mistura-e-gluten.md`; a tabela geral de pesos por
tamanho, em `01-formulas-massas.md`. Aqui estão as contas fechadas, item a item.

---

## 1. Peso de bola por tamanho: os que dependem da forma

A tabela de "best bets" existe porque **os tamanhos de pizza são ditados pelas formas
padrão disponíveis** — o livro partiu da forma e derivou o peso, não o contrário.

| Item | Peso | Pizza / forma |
|---|---|---|
| New York 50 cm / 20 in | **930 g** | sem forma |
| Deep-dish | 230 g | pizza de **21 cm / 8½ in**; forma 21 cm × **5 cm de profundidade** |
| Deep-dish | 700 g | pizza de **32 cm / 12½ in**; forma 32 cm × **5 cm de profundidade** |
| Focaccia · NY square | 1 kg · 700 g | meia chapa **46 × 33 cm / 18 × 13 in** |
| Al taglio | 700 g / 1,4 kg | meia forma romana **60 × 20 cm** / inteira **60 × 40 cm** |
| Detroit | 330 g / 500 g | meia forma **25 × 20 cm** / inteira **35 × 25 cm** |

Os demais pesos de New York (400/600/800 g, 1,1/1,2 kg) e todos os da artisan
(360/400/470/500/580/620 g) conferem com o que já está em `01-formulas-massas.md`.

Para um tamanho que **não está** na tabela, escale pelo **RCF** (§4). Não interpole peso
no olho. Para pizza acima de **50 cm**, confira antes se o pote de fermentação comporta o
volume maior.

---

## 2. Batelada mínima de batedeira de bancada

**800 g de massa** é o mínimo que uma stand mixer bate direito. A bola de New York de
35 cm pesa **400 g** e a de 40 cm pesa **600 g** — as duas abaixo do mínimo.

Conduta do livro: faça pelo menos 800 g, use o que precisa e **guarde o resto para o dia
seguinte** (ou congele). Capacidade mínima, máxima e multiplicador de cada bacia em
`17-batedeiras-e-tempos-de-mistura.md`.

---

## 3. Do percentual para o peso (DDW)

1. Defina o peso desejado de massa (**DDW**). Exemplo: **10 kg**.
2. Some todos os percentuais da fórmula. Exemplo: **228,31®**.
3. `DDW ÷ soma` = o peso de **1%**. → 10 kg ÷ 228,31 = **43,8 g**.
4. Multiplique 43,8 g por cada percentual.

| Ingrediente | ® | × peso de 1% | = peso |
|---|---|---|---|
| Farinha de pão | 100 | × 43,8 | **4,38 kg** |
| Água | 57,9 | × 43,8 | **2,54 kg** |
| Poolish | 66,64 | × 43,8 | **2,92 kg** |
| Sal fino | 3,19 | × 43,8 | **139,72 g** |
| Fermento | 0,58 | × 43,8 | **25,4 g** |
| **Total** | **228,31** | | **~10 kg** |

> **Ambiguidade a registrar.** Esta conta corre sobre a **lista de ingredientes** — o
> poolish aparece como uma linha só, de 66,64®. O net contents, onde o poolish deixa de
> existir (§7), **não serve para esta conta**: ele não é uma receita. Regra prática: pese
> pela lista de ingredientes, **compare, escale de estilo e diagnostique** pelo net contents.

---

## 4. RCF: escalar sem percentual de padeiro

`RCF = rendimento novo ÷ rendimento original`. Multiplique **cada** ingrediente pelo RCF.
Exemplo fechado do livro, de 1,707 kg para 3 kg: 3 ÷ 1,707 = **1,76**.

| Ingrediente | Receita original | × 1,76 | Receita nova |
|---|---|---|---|
| Farinha de pão | 1 kg | | **1,76 kg** |
| Água | 700 g | | **1,23 kg** |
| IDY | 5 g | | **8,8 g** |
| Sal | 2 g | | **3,5 g** |
| **Rendimento** | **1,707 kg** | | **3,002 kg** |

Ressalva do livro: **massa escalada muito para cima se comporta diferente**. Não é só
multiplicar e esperar o mesmo resultado — reveja tempo de mistura, carga da tigela e ponto.

> O exemplo é aritmético, não gastronômico: 2 g de sal para 1 kg de farinha são **0,2®**,
> um décimo do que qualquer mestre usa. Copie o método, não a fórmula.

---

## 5. Pesagem: bacia na balança ou potes pré-pesados

- Vai misturar **na hora** → pese os ingredientes **direto na bacia da batedeira sobre a
  balança**.
- Vai misturar **depois** → pese com antecedência **em potes separados** e despeje tudo de
  uma vez na hora. É aqui que está o ganho de tempo do mise en place de massa.

---

## 6. As duas notações de porcentagem

O livro usa **dois sinais diferentes**, e confundi-los é fonte de erro de fórmula:

- `®` (baker's %) — tudo relativo à **farinha = 100**. A soma passa de 100.
- `%` (scaling %) — cada ingrediente como fatia do **peso total**. A soma dá 100.

A **mesma massa** nas duas notações (585 g farinha / 400 g água / 12 g sal / 4 g IDY):

| Ingrediente | Peso | Scaling % | Baker's ® |
|---|---|---|---|
| Farinha de pão | 585 g | 58,44% | **100** |
| Água | 400 g | 39,96% | **68,38** |
| Sal fino | 12 g | 1,2% | **2,05** |
| IDY | 4 g | 0,4% | **0,68** |
| **Total** | **1.001 g** | **100%** | **171,11** |

Leitura do total em baker's %: **171,11** significa que **71,11% do peso da farinha** é
tudo o que não é farinha (água + sal + fermento).

**Várias farinhas**: **some** as farinhas e ponha a soma em 100 — nunca eleja uma delas
como 100. Fazer o contrário inviabiliza comparar duas receitas.

| Ingrediente | Peso | ® |
|---|---|---|
| Farinha de pão | 375 g | 64,1 |
| Farinha de espelta | 85 g | 14,53 |
| Centeio médio | 125 g | 21,37 |
| **(soma das farinhas)** | **585 g** | **100** |
| Água | 451 g | 77,09 (?) |
| Sal fino | 13,5 g | 2,3 |
| IDY | 4,5 g | 0,77 |
| **Total** | **1.054 g** | **180,14** |

> `(?)`: o texto extraído do livro traz "7Z09" para a água. 451 ÷ 585 = **77,09**, e é
> 77,09 que fecha o total de 180,14 (72,09 daria 175). Use 77,09.

---

## 7. Fechar o net contents quando há pré-fermento

Quando há poolish ou levain, a coluna de ® da lista de ingredientes **não é a fórmula**:
a farinha, a água e o fermento do pré-fermento estão escondidos dentro de um número só.
Sem abrir isso, **é impossível escalar**: você não sabe quanta água a massa realmente quer.

**Receita D do livro** (poolish 100/100):

| | Ingrediente | Peso | ® |
|---|---|---|---|
| Poolish | Farinha de pão | 145 g | 100 |
| | Água | 145 g | 100 |
| | IDY | 0,15 g | 0,1 |
| Massa final | Farinha de pão | 440 g | 100 |
| | Água | 255 g | 57,95 |
| | Poolish | 290 g | 65,91 |
| | Sal fino | 14 g | 3,18 |
| | IDY | 2,5 g | 0,57 |
| | **Peso total** | **1.001,65 g** | |

**A soma, item a item:**

- farinha: 145 (poolish) + 440 (massa) = **585 g** → este é o novo **100**
- água: 145 + 255 = **400 g** → **68,37®**
- fermento: 0,15 + 2,5 = **2,65 g** → **0,45®**
- sal: 14 g → **2,39®**

| NET CONTENTS | Peso | ® |
|---|---|---|
| Farinha de pão | 585 g | **100** |
| Água | 400 g | **68,37** |
| Poolish\* | — | — |
| Sal fino | 14 g | **2,39** |
| IDY | 2,65 g | **0,45** |
| **Total** | **1.001,65 g** | |

\* **O poolish deixa de existir como item** — os componentes dele foram absorvidos pelas
categorias correspondentes.

Traduzindo: massa magra de **68,37® de hidratação**, **2,39® de sal**, fermentada com
**0,45® de fermento**.

**O erro de ler a coluna errada.** A mesma massa aparece com dois pares de números:

| | Lista de ingredientes | Net contents | Erro se você usar o primeiro |
|---|---|---|---|
| Sal | 3,18® | **2,39®** | **+33%** de sal |
| IDY | 0,57® | **0,45®** | **+27%** de fermento |

Escalar pela coluna da lista de ingredientes usando a farinha **total** sala e fermenta a
massa muito acima — em torno de um terço a mais nos dois casos.

---

## 8. Manteiga, fubá e o que não entra inteiro na fórmula

> **Manteiga = ~81® gordura + ~19® água.** Some cada metade **separadamente** à gordura e
> à água do net contents. É a única forma de fechar a conta de qualquer massa com manteiga.

Conferência na **Deep-Dish com Poolish**: banha 18 g + manteiga 18 g = 36 g de ingrediente,
mas o net contents publica **33 g de gordura (8,68®)** e **228 g de água (60®)**.

- gordura = 18 + (18 × 0,81) = 32,58 ≈ **33 g**
- água = 60 (poolish) + 165 (massa) + (18 × 0,19 = 3,42) = 228,42 ≈ **228 g**

**Fubá fino fora dos 100® de farinha**, porque não contribui para a estrutura de glúten —
entra como percentual à parte. Na deep-dish, os mesmos 40 g valem **12,5®** na lista de
ingredientes (sobre 320 g de farinha) e **10,53®** no net contents (sobre 380 g). A regra
geral de quem entra e quem não entra nos 100 está em `02-mistura-e-gluten.md`.

---

## 9. Fermento abaixo da balança

Para os **0,06 g** de IDY de um poolish, nenhuma balança de 1 g serve e a de 0,01 g é
imprecisa nessa faixa. O livro manda medir **¼ tsp de fermento e dividir em seis partes
iguais** — use uma parte.
