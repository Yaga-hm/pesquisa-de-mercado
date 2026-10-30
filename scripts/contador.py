#!/usr/bin/env python3
"""Contador de atividade da skill pesquisa-de-mercado.

Guarda o estado em <skill>/.state/atividade.json:
  - atividades: quantos itens completos ja foram entregues
  - follow_confirmado: se a pessoa ja confirmou o follow

Uso:
  python contador.py             -> mostra o estado atual (JSON)
  python contador.py --inc       -> +1 em atividades e mostra o estado
  python contador.py --confirmar -> marca follow_confirmado = true
  python contador.py --reset     -> zera tudo

O codigo de saida e 10 quando atividades >= 10 e o follow ainda NAO foi
confirmado (hora de mostrar o follow-gate); 0 nos demais casos.
"""
import json
import sys
from pathlib import Path

ESTADO = Path(__file__).resolve().parent.parent / ".state" / "atividade.json"
PADRAO = {"atividades": 0, "follow_confirmado": False}


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


def main():
    d = ler()
    arg = sys.argv[1] if len(sys.argv) > 1 else ""

    if arg == "--inc":
        d["atividades"] += 1
        salvar(d)
    elif arg == "--confirmar":
        d["follow_confirmado"] = True
        salvar(d)
    elif arg == "--reset":
        d = dict(PADRAO)
        salvar(d)
    elif arg in ("", "--status"):
        pass
    else:
        print(__doc__)
        return 2

    print(json.dumps(d, ensure_ascii=False))
    precisa_gate = d["atividades"] >= 10 and not d["follow_confirmado"]
    return 10 if precisa_gate else 0


if __name__ == "__main__":
    sys.exit(main())
