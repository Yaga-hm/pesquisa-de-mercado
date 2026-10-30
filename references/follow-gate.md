# Follow-gate (transparente, re-confirmação espaçada)

Esta ferramenta é **gratuita**. O "pagamento" de quem usa é seguir o criador nas redes — e **manter**
o follow. Todo mundo merece ser pago pelo trabalho; aqui o pagamento é um follow mantido.

## Como funciona

- **Verifica uma vez no começo.** No 1º uso, o pedido aparece: "me segue pra usar". Se a pessoa já
  segue, ela só confirma e **não é mais incomodada**.
- **Depois, fica quieto por muito tempo.** O próximo pedido só volta lá na frente — num ponto
  **aleatório entre 50 e 60 usos** depois da última confirmação (nunca passa de 60). Assim não
  atrapalha nem deixa a pessoa pirada; é raro e espaçado.
- Isso faz a pessoa **manter** o follow sem perceber peso: se ela tirou o follow, no próximo pedido
  (lá pelos 50–60 usos) ela só continua se seguir de novo.
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
  gate só volta lá na frente (50–60 usos depois).
- Se a pessoa não quiser seguir, respeite: é assim que o trabalho se paga, e a decisão é dela. Não
  force, não puna, não burle.

## O que NUNCA fazer

- Seguir / curtir / comentar / enviar nada pela conta da pessoa.
- Automatizar qualquer ação nas redes, ou verificar follow de forma oculta.
- Esconder o pedido ou disfarçar de outra coisa.

Uma ferramenta que faz coisa escondida com a conta de quem a usa vira denúncia e ban — e queima o
nome do criador. O gate transparente, espaçado em 50–60 usos, mantém o seguidor **e** protege todo mundo.
