#!/usr/bin/env python3
"""Contador de uso da skill pesquisa-de-mercado, com re-confirmacao do follow.

Guarda o estado em <skill>/.state/atividade.json:
  - usos: quantos servicos/pesquisas completos ja foram entregues
  - confirmado_em: o numero de usos em que o follow foi confirmado pela
    ultima vez (0 = nunca)

Regra do gate: a cada INTERVALO usos desde a ultima confirmacao, o follow e
pedido de novo. Assim a pessoa precisa MANTER o follow: se ela parar de
seguir, no proximo pedido ela so continua se seguir de novo. Se continuar
seguindo e confirmar, passa mais INTERVALO usos ate o proximo pedido.

Uso:
  python contador.py             -> mostra o estado atual (JSON)
  python contador.py --inc       -> +1 em usos e mostra o estado
  python contador.py --confirmar -> registra que a pessoa confirmou o follow agora
  python contador.py --reset     -> zera tudo

Codigo de saida 10 quando o follow precisa ser pedido agora
(usos - confirmado_em >= INTERVALO); 0 nos demais casos.
"""
import json
import sys
from pathlib import Path

INTERVALO = 5  # a cada quantos usos o follow e pedido de novo
ESTADO = Path(__file__).resolve().parent.parent / ".state" / "atividade.json"
PADRAO = {"usos": 0, "confirmado_em": 0}


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
    return (d["usos"] - d["confirmado_em"]) >= INTERVALO


def main():
    d = ler()
    arg = sys.argv[1] if len(sys.argv) > 1 else ""

    if arg == "--inc":
        d["usos"] += 1
        salvar(d)
    elif arg == "--confirmar":
        d["confirmado_em"] = d["usos"]
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
    saida["intervalo"] = INTERVALO
    saida["gate_agora"] = precisa_gate(d)
    print(json.dumps(saida, ensure_ascii=False))
    return 10 if precisa_gate(d) else 0


if __name__ == "__main__":
    sys.exit(main())
