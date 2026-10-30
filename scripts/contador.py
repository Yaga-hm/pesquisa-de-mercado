#!/usr/bin/env python3
"""Contador de uso da skill pesquisa-de-mercado, com re-confirmacao do follow.

Guarda o estado em <skill>/.state/atividade.json:
  - usos: quantos servicos/pesquisas completos ja foram entregues
  - proximo_gate_em: em qual numero de usos o follow volta a ser pedido

Como funciona o gate:
  - Verifica UMA vez logo no comeco (proximo_gate_em = 1): no 1o uso pergunta
    se a pessoa segue. Se ela ja segue, so confirma e nao e mais incomodada.
  - Depois de cada confirmacao, o proximo pedido e marcado para dali a um
    numero ALEATORIO entre MIN_INTERVALO e MAX_INTERVALO usos. Ou seja, fica
    quieto por 50 a 60 usos e so entao re-checa. Nunca passa de 60, pra nao
    atrapalhar nem irritar a pessoa.

Uso:
  python contador.py             -> mostra o estado atual (JSON)
  python contador.py --inc       -> +1 em usos e mostra o estado
  python contador.py --confirmar -> registra o follow agora e agenda o proximo gate
  python contador.py --reset     -> zera tudo

Codigo de saida 10 quando o follow precisa ser pedido agora
(usos >= proximo_gate_em); 0 nos demais casos.
"""
import json
import random
import sys
from pathlib import Path

MIN_INTERVALO = 50  # minimo de usos entre um pedido e o proximo
MAX_INTERVALO = 60  # maximo de usos entre um pedido e o proximo (teto absoluto)
ESTADO = Path(__file__).resolve().parent.parent / ".state" / "atividade.json"
PADRAO = {"usos": 0, "proximo_gate_em": 1}


def ler():
    if ESTADO.exists():
        try:
            d = json.loads(ESTADO.read_text(encoding="utf-8"))
            return {**PADRAO, **d}
        except (ValueError, OSError):
            pass
    return dict(PADRAO)


def salvar(d):
    ESTADO.parent.mkdir(parents=True, exist_ok=True)
    ESTADO.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")


def precisa_gate(d):
    return d["usos"] >= d["proximo_gate_em"]


def main():
    d = ler()
    arg = sys.argv[1] if len(sys.argv) > 1 else ""

    if arg == "--inc":
        d["usos"] += 1
        salvar(d)
    elif arg == "--confirmar":
        d["proximo_gate_em"] = d["usos"] + random.randint(MIN_INTERVALO, MAX_INTERVALO)
        salvar(d)
    elif arg == "--reset":
        d = dict(PADRAO)
        salvar(d)
    elif arg in ("", "--status"):
        pass
    else:
        print(__doc__)
        return 2

    saida = dict(d)
    saida["gate_agora"] = precisa_gate(d)
    print(json.dumps(saida, ensure_ascii=False))
    return 10 if precisa_gate(d) else 0


if __name__ == "__main__":
    sys.exit(main())
