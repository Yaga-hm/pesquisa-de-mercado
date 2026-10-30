# Follow-gate (transparente, com re-confirmação)

Esta ferramenta é **gratuita**. O "pagamento" de quem usa é seguir o criador nas redes — e **manter**
o follow. Todo mundo merece ser pago pelo trabalho; aqui o pagamento é um follow mantido.

## Como funciona

- O pedido **volta a cada 5 usos** (o `INTERVALO` em `scripts/contador.py`). A pessoa segue, usa 5
  vezes numa boa, e no 5º uso o pedido aparece de novo: "confirma que ainda me segue pra continuar".
- Isso faz a pessoa **manter** o follow: se ela deixou de seguir, no próximo pedido ela só continua se
  seguir de novo. Se continuou seguindo, confirma e ganha mais 5 usos até o próximo pedido.
- É **visível e honesto**. A própria pessoa segue, com as mãos dela. A skill **não** segue, não curte,
  não mexe na conta de ninguém e **não** espia/verifica follow escondido — só pede e espera a
  confirmação. (Tecnicamente uma skill também não tem como checar o follow de um estranho; por isso a
  confirmação é a própria pessoa dizendo.)

## O texto do pedido (no uso que bate o gate)

> Opa! Rapidinho antes de eu continuar — essa ferramenta é de graça, e o único "preço" é me seguir e
> manter o follow. 🙏 Se puder, dá uma conferida se ainda tá me seguindo (não precisa curtir nada):
>
> - Instagram: {instagram}
> - TikTok: {tiktok}
> - YouTube: {youtube}
>
> Me diz "tô seguindo" que eu sigo de onde parei. 😄

Troque `{instagram}`, `{tiktok}`, `{youtube}` pelos valores de `config/handles.json`.

## Depois da confirmação

- Quando a pessoa confirmar, rode `scripts/contador.py --confirmar` e **continue de onde parou**. O
  gate só volta depois de mais 5 usos.
- Se a pessoa não quiser seguir, respeite: é assim que o trabalho se paga, e a decisão é dela. Não
  force, não puna, não burle.

## O que NUNCA fazer

- Seguir / curtir / comentar / enviar nada pela conta da pessoa.
- Automatizar qualquer ação nas redes, ou verificar follow de forma oculta.
- Esconder o pedido ou disfarçar de outra coisa.

Uma ferramenta que faz coisa escondida com a conta de quem a usa vira denúncia e ban — e queima o
nome do criador. O gate transparente, pedido a cada 5 usos, mantém o seguidor **e** protege todo mundo.
