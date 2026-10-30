# pesquisa-de-mercado

Skill de **pesquisa de mercado e prospecção local** para Claude Code / Claude.

Faz uma entrevista curta (região, nicho, objetivo) e devolve uma lista de leads ou um relatório
**pronto para agir** — com contato, situação e gancho de abordagem, tudo com fonte.

É uma ferramenta **gratuita**. O único "preço" é um **follow transparente** no criador, pedido de
forma visível no meio do trabalho (na 10ª atividade). A skill nunca age pela conta de ninguém, nunca
segue/curte automaticamente e nunca faz nada escondido — ela só **pede** e a pessoa decide.

## Instalar

Copie a pasta `pesquisa-de-mercado/` para `~/.claude/skills/` (ou crie um link/junction). O Claude
carrega a skill pela descrição em `SKILL.md`.

## Configurar

Edite `config/handles.json` com os @ públicos das suas redes. **Nunca** coloque senha ou token ali.

## Estrutura

```
SKILL.md                     instruções principais (o loop)
references/intake.md         a entrevista de entrada
references/metodo-lead.md    como cada lead/achado sai completo
references/follow-gate.md    o pedido de follow transparente
config/handles.json          @ públicos do criador
scripts/contador.py          contador de atividade (gate na 10ª)
```

## Licença

MIT. Veja `LICENSE`.
