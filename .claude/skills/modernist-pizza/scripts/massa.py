#!/usr/bin/env python3
"""
Calculadora das massas-mestre do Modernist Pizza (vols. 1 e 2).

Uso:
  massa.py listar
  massa.py ver <massa>
  massa.py calcular <massa> --pizzas N [--tamanho "40 cm"]
  massa.py calcular <massa> --bolas N --peso 250
  massa.py calcular <massa> --total 12kg
  massa.py fermento --de fresco --para instantaneo --peso 30
  massa.py poolish --farinha 500 --pronto 12-16h
  massa.py hidratacao

Todos os pesos em gramas. As porcentagens sao percentual de padeiro sobre a
farinha total (net contents).
"""
import argparse
import json
import os
import sys

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "massas.json")

with open(BASE, encoding="utf-8") as fh:
    DB = json.load(fh)

MASSAS = DB["massas"]


def fmt(g):
    """Arredonda como padeiro: 2 casas abaixo de 10 g, 1 casa abaixo de 100 g, inteiro acima."""
    if g < 10:
        return f"{g:.2f}".rstrip("0").rstrip(".")
    if g < 100:
        return f"{g:.1f}".rstrip("0").rstrip(".")
    return f"{g:.0f}"


def emkg(g):
    """Sufixo com o valor em kg quando ajuda a leitura."""
    return f"  ({g/1000:.2f} kg)" if g >= 1000 else ""


def resolver(chave):
    chave = chave.lower().replace("_", "-")
    if chave in MASSAS:
        return chave
    candidatos = [k for k in MASSAS if chave in k or chave in MASSAS[k]["nome"].lower()]
    if len(candidatos) == 1:
        return candidatos[0]
    if not candidatos:
        sys.exit(f"Massa '{chave}' nao encontrada. Rode: massa.py listar")
    sys.exit(f"'{chave}' e ambiguo: {', '.join(candidatos)}")


def peso_real_base(m):
    """Soma real dos ingredientes da receita-base.

    Nao use 'rendimento_g' como base de escalonamento: ele e o rendimento
    ARREDONDADO que o livro publica, e a soma dos ingredientes se afasta dele de
    -3,9% (focaccia) a +5,2% (New York). Escalar pelo arredondado faz a folga de
    bancada virar de -1% a +8% conforme a massa.
    """
    total = sum(i["g"] for i in m["massa"] if not i.get("e_prefermento"))
    if m.get("prefermento"):
        total += sum(i["g"] for i in m["prefermento"]["ingredientes"])
    return total


def cmd_listar(_):
    print(f"{'chave':<12} {'familia':<8} {'hidr.':>7} {'sal':>6} {'IDY':>6} {'gord.':>7}  forno")
    print("-" * 78)
    ordem = sorted(MASSAS, key=lambda k: MASSAS[k]["net"]["agua_pct"])
    for k in ordem:
        m = MASSAS[k]
        n = m["net"]
        f = m["forno"]
        print(
            f"{k:<12} {m['familia']:<8} {n['agua_pct']:>6.2f}% {n['sal_pct']:>5.2f}% "
            f"{n['fermento_pct']:>5.2f}% {n['gordura_pct']:>6.2f}%  {f['temp_c']} C / {f['tempo']}"
        )


def cmd_ver(args):
    k = resolver(args.massa)
    m = MASSAS[k]
    n = m["net"]
    print(f"\n{m['nome']}  [{k}]  familia: {m['familia']}")
    real = peso_real_base(m)
    print(f"Rendimento base: {fmt(m['rendimento_g'])} g (declarado pelo livro)"
          f"  ·  soma dos ingredientes: {fmt(real)} g (base do escalonamento)\n")

    print("NET CONTENTS (a formula real)")
    print(f"  farinha total   {fmt(n['farinha_g'])} g   = 100%")
    print(f"  agua            {n['agua_pct']:.2f}%")
    print(f"  sal             {n['sal_pct']:.2f}%")
    print(f"  fermento (IDY)  {n['fermento_pct']:.2f}%")
    print(f"  gordura         {n['gordura_pct']:.2f}%")
    for nome, pct in n.get("outros", {}).items():
        print(f"  {nome:<15} {pct:.2f}%")

    if m["prefermento"]:
        p = m["prefermento"]
        print(f"\nPRE-FERMENTO ({p['tipo']}, {p['horas']})")
        for ing in p["ingredientes"]:
            print(f"  {ing['nome']:<42} {fmt(ing['g']):>12} g")

    print("\nMASSA")
    for ing in m["massa"]:
        print(f"  {ing['nome']:<42} {fmt(ing['g']):>12} g")

    print(f"\nPROCESSO\n  {m['processo']}")
    print(f"\nFORNO: {m['forno']['temp_c']} C por {m['forno']['tempo']}")
    print("\nTAMANHOS")
    for t in m["tamanhos"]:
        molho = DB["molho_g"].get(k, {}).get(t["desc"])
        queijo = DB["queijo_g"].get(k, {}).get(t["desc"])
        extra = []
        if molho:
            extra.append(f"molho {molho} g")
        if queijo:
            extra.append(f"queijo {queijo} g")
        sufixo = ("   " + " | ".join(extra)) if extra else ""
        print(f"  {t['desc']:<28} massa {t['peso_g']} g{sufixo}")
    print()


def escalar(k, fator, peso_bola=None, n_bolas=None, tamanho=None):
    m = MASSAS[k]
    print(f"\n{m['nome']}  —  fator {fator:.4f}x  (base {fmt(peso_real_base(m))} g)")
    if n_bolas:
        alvo = "  ".join(
            x for x in [
                f"{n_bolas} bolas de {fmt(peso_bola)} g" if peso_bola else None,
                f"tamanho: {tamanho}" if tamanho else None,
            ] if x
        )
        print(f"Alvo: {alvo}")
    print()

    total = 0.0
    if m["prefermento"]:
        p = m["prefermento"]
        print(f"PRE-FERMENTO ({p['tipo']}) — comecar {p['horas']} antes")
        for ing in p["ingredientes"]:
            g = ing["g"] * fator
            print(f"  {ing['nome']:<42} {fmt(g):>14} g{emkg(g)}")
        print()

    print("MASSA")
    for ing in m["massa"]:
        g = ing["g"] * fator
        total += g
        marca = "  <- do pre-fermento" if ing.get("e_prefermento") else ""
        print(f"  {ing['nome']:<42} {fmt(g):>14} g{emkg(g)}{marca}")
    print(f"  {'TOTAL':<42} {fmt(total):>14} g{emkg(total)}")

    if n_bolas and peso_bola:
        sobra = total - n_bolas * peso_bola
        print(f"\n  {n_bolas} x {fmt(peso_bola)} g = {fmt(n_bolas * peso_bola)} g{emkg(n_bolas * peso_bola)}"
              f"   (folga de {fmt(sobra)} g para perda de bancada)")

    print(f"\nPROCESSO\n  {m['processo']}")
    print(f"FORNO: {m['forno']['temp_c']} C por {m['forno']['tempo']}")

    if tamanho:
        molho = DB["molho_g"].get(k, {}).get(tamanho)
        queijo = DB["queijo_g"].get(k, {}).get(tamanho)
        if molho or queijo:
            print("\nPARA MONTAR (por pizza / total)")
            if molho:
                print(f"  molho    {molho} g  ->  {fmt(molho * (n_bolas or 1))} g{emkg(molho * (n_bolas or 1))}")
            if queijo:
                print(f"  queijo   {queijo} g  ->  {fmt(queijo * (n_bolas or 1))} g{emkg(queijo * (n_bolas or 1))}")

    aviso_mixer(total)
    print()


# Capacidades das fichas de receita do vol. 2 (as fichas mandam sobre o quadro geral).
# Batelada minima de batedeira de bancada: 800 g.
SEM_GARFO = {"al-taglio"}        # unica mestre sem bloco de mistura em garfo
SEM_PROCESSADOR = {"artisan", "focaccia", "ny-square", "al-taglio"}


def aviso_mixer(total_g):
    kg = total_g / 1000
    print("\nBATEDEIRA (encha no maximo ate a metade da tigela)")
    if kg < 0.8:
        print(f"  {kg:.2f} kg — ABAIXO do minimo de 800 g de uma batedeira de bancada.")
        print("  Faca 800 g, use o que precisa e guarde ou congele o resto.")
    elif kg <= 1.25:
        print(f"  {kg:.2f} kg — bancada, bacia 4,5 qt (max. 1,25 kg).")
    elif kg <= 1.75:
        print(f"  {kg:.2f} kg — bancada, bacia 8 qt (max. 1,75 kg).")
    elif kg < 4:
        print(f"  {kg:.2f} kg — diving arm 6 qt (max. 3 kg), ou planetaria 12 qt pelo")
        print("  quadro da p. 34 (min. 3 kg). As fichas de receita pedem 4 kg na de 12 qt.")
    elif kg <= 6:
        print(f"  {kg:.2f} kg — planetaria comercial 12 qt (4-6 kg).")
    elif kg <= 8:
        print(f"  {kg:.2f} kg — planetaria comercial 20 qt (6-8 kg), ou espiral.")
    else:
        print(f"  {kg:.2f} kg — espiral, diving arm ou garfo (min. recomendado 8 kg).")
    if MASSA_ATUAL in SEM_GARFO:
        print("  AVISO: esta e a unica mestre SEM bloco de mistura em garfo no livro.")
    if MASSA_ATUAL in SEM_PROCESSADOR:
        print("  AVISO: sem opcao de processador — a lamina nao pega massa mole.")


MASSA_ATUAL = None


def cmd_calcular(args):
    global MASSA_ATUAL
    k = resolver(args.massa)
    MASSA_ATUAL = k
    m = MASSAS[k]

    if args.total:
        txt = args.total.lower().replace(",", ".")
        gramas = float(txt.replace("kg", "")) * 1000 if "kg" in txt else float(txt.replace("g", ""))
        escalar(k, gramas / peso_real_base(m))
        return

    if args.bolas:
        peso = args.peso
        tamanho = None
        if peso is None:
            if args.tamanho:
                achado = [t for t in m["tamanhos"] if t["desc"].lower().startswith(args.tamanho.lower())]
                if not achado:
                    sys.exit(f"Tamanho '{args.tamanho}' nao existe para {k}. "
                             f"Opcoes: {', '.join(t['desc'] for t in m['tamanhos'])}")
                peso, tamanho = achado[0]["peso_g"], achado[0]["desc"]
            else:
                peso, tamanho = m["tamanhos"][0]["peso_g"], m["tamanhos"][0]["desc"]
        elif args.tamanho:
            tamanho = args.tamanho
        # 3% de folga para perda de bancada (adicao nossa, nao do livro)
        necessario = args.bolas * peso * 1.03
        escalar(k, necessario / peso_real_base(m), peso, args.bolas, tamanho)
        return

    sys.exit("Informe --pizzas/--bolas ou --total. Ex.: massa.py calcular napolitana --pizzas 24")


def cmd_fermento(args):
    tabela = DB["conversao_fermento"]
    de, para = args.de.lower(), args.para.lower()
    if de not in tabela or para not in tabela:
        sys.exit("Tipos validos: instantaneo, seco-ativo, fresco")
    fator = tabela[de][para]
    print(f"\n{args.peso} g de fermento {de}  ->  {fmt(args.peso * fator):}"
          f" g de fermento {para}   (fator {fator})")
    if para == "seco-ativo":
        print("  Lembre: fermento seco ativo EXIGE bloom em agua a 43 C.")
    if de == "fresco" or para == "fresco":
        print("  A diferenca de agua entre eles e desprezivel nas quantidades de pizza.")
    print("  Fermento congelado perde viabilidade: aumente 25%.\n")


def cmd_poolish(args):
    print(f"\nPOOLISH com {fmt(args.farinha)} g de farinha")
    print(f"  Farinha  {fmt(args.farinha):>10} g")
    print(f"  Agua     {fmt(args.farinha):>10} g   (100% — poolish e sempre 1:1)")
    print("\n  Fermento instantaneo conforme quando voce quer usar (a 21-24 C):")
    for linha in DB["poolish_fermento_pct"]:
        gmin = args.farinha * linha["pct_min"] / 100
        gmax = args.farinha * linha["pct_max"] / 100
        marca = "  <-" if args.pronto and args.pronto.replace(" ", "") in linha["pronto_em"].replace(" ", "") else ""
        print(f"    pronto em {linha['pronto_em']:<9} "
              f"{linha['pct_min']}-{linha['pct_max']}%  =  "
              f"{fmt(gmin)}-{fmt(gmax)} g{marca}")
    print("\n  Ponto: poolish maduro BOIA na agua. Poolish mais velho contribui mais.\n")


def cmd_hidratacao(_):
    print("\nHIDRATACAO DAS MASSAS-MESTRE (net contents) e limites testados pelo livro\n")
    limites = {
        "brasileira": "ate 55% da resultado muito parecido",
        "deep-dish": "+-5% funciona",
        "napolitana": "55% vira massa de modelar; ate 70% ok; com amido pre-gelatinizado chega a ~82% (canotto)",
        "new-york": "tolera +-5%; +-10% fica dificil de abrir e nao segura o formato",
        "detroit": "+-5% da pizzas bem equilibradas",
        "thin-crust": "aumentar deu os MELHORES resultados; nao passar de 80%",
        "artisan": "reduzir 5-10% facilita o manuseio mas PIORA o sabor; aumentar exige muito esforco",
        "ny-square": "65% derruba o volume de forma significativa; 65 e 70% ficam duras",
        "al-taglio": "mais alto fica sem graca e borrachudo; 70% e 75% sao boas alternativas",
        "focaccia": "+-10% nao muda nada; 100% e 110% PIORAM o volume",
    }
    for k in sorted(MASSAS, key=lambda x: MASSAS[x]["net"]["agua_pct"]):
        print(f"  {k:<12} {MASSAS[k]['net']['agua_pct']:>6.2f}%   {limites.get(k, '')}")
    print("\n  Conclusao do livro: as hidratacoes das mestres ja sao as otimas.")
    print("  E a massa mais molhada NAO produz o maior volume.\n")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("listar", help="lista as 10 massas-mestre").set_defaults(func=cmd_listar)

    v = sub.add_parser("ver", help="fórmula completa de uma massa")
    v.add_argument("massa")
    v.set_defaults(func=cmd_ver)

    c = sub.add_parser("calcular", help="escala uma massa")
    c.add_argument("massa")
    c.add_argument("--pizzas", "--bolas", dest="bolas", type=int)
    c.add_argument("--peso", type=float, help="peso da bola em g (senao usa o do tamanho)")
    c.add_argument("--tamanho", help='ex.: "40 cm"')
    c.add_argument("--total", help='peso total de massa, ex.: 12kg ou 3500g')
    c.set_defaults(func=cmd_calcular)

    f = sub.add_parser("fermento", help="converte tipos de fermento")
    f.add_argument("--de", required=True)
    f.add_argument("--para", required=True)
    f.add_argument("--peso", type=float, required=True)
    f.set_defaults(func=cmd_fermento)

    po = sub.add_parser("poolish", help="monta um poolish")
    po.add_argument("--farinha", type=float, required=True)
    po.add_argument("--pronto", help="3h, 8h, 12-16h ou 17-18h")
    po.set_defaults(func=cmd_poolish)

    sub.add_parser("hidratacao", help="tabela de hidratacao e limites").set_defaults(func=cmd_hidratacao)

    args = p.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
