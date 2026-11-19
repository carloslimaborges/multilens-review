# multilens-review

[![validate](https://github.com/carloslimaborges/multilens-review/actions/workflows/validate.yml/badge.svg)](https://github.com/carloslimaborges/multilens-review/actions/workflows/validate.yml)
[![Version](https://img.shields.io/badge/version-1.1.0-blue)](https://github.com/carloslimaborges/multilens-review/releases)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)](https://github.com/carloslimaborges/multilens-review/pulls)
[![Compatibility](https://img.shields.io/badge/works%20with-Claude%20Code%20%7C%20Antigravity%20%7C%20Cursor%20%7C%20Codex-8A2BE2)](#instala%C3%A7%C3%A3o)

[English](README.md) | **Português (BR)**

**Uma meta-skill que transforma qualquer agente de código com IA em um revisor especialista multifocal, automaticamente.**

Compatível com Claude Code, Claude Cowork, Google Antigravity, Cursor, Codex e qualquer agente compatível com [agentskills.io](https://agentskills.io).

## O problema

A [biblioteca de skills wondel.ai](https://skills.wondel.ai) empacota 50 frameworks de livros consagrados de engenharia e negócios (Clean Code, DDIA, Release It!, Refactoring, A Philosophy of Software Design...) como skills de agente. Mas você precisa lembrar de invocá-las, pelo nome, a cada prompt. Ninguém faz isso de forma consistente, e a maior parte do valor da biblioteca evapora.

## A solução

O `multilens-review` é uma camada de roteamento. Instale uma vez e o agente:

1. **Classifica cada tarefa** (engenharia, UX, marketing, produto, estratégia, operações)
2. **Carrega as skills certas antes de trabalhar**, sem invocação manual
3. **Para tarefas de engenharia, aplica uma baseline obrigatória de 11 lentes simultaneamente**, produzindo uma revisão multifocal em vez de uma resposta de framework único:

   `clean-code` · `pragmatic-programmer` · `refactoring-patterns` · `working-with-legacy-code` · `software-design-philosophy` · `release-it` · `ddia-systems` · `high-perf-browser` · `ux-heuristics` · `microinteractions` · `steve-jobs-design-review`

4. **Adiciona lentes específicas de contexto**: projetos greenfield ganham `clean-architecture` + `domain-driven-design` + `system-design`; trabalho iOS ganha `ios-hig-design`; trabalho visual ganha `refactoring-ui` + `web-typography`
5. **Organiza os achados por lente**, mostrando o que cada framework capturou: qualidade de código, complexidade de design, resiliência em produção, tratamento de dados, performance, usabilidade, detalhe de interação, simplicidade

Antes: *"Refatora esse service"* → refatoração genérica.
Depois: o mesmo prompt dispara uma revisão por 11 lentes especialistas, o agente informa quais frameworks aplicou e o que cada um encontrou.

## Modo lite

A baseline completa de 11 lentes custa tokens. Quando quiser uma passada mais leve, diga **"lite"** ou **"review lite"** (ou apenas reclame do consumo de tokens) e o router carrega só 3 lentes:

`clean-code` · `software-design-philosophy` · `release-it`

Isso cobre os eixos de maior sinal, qualidade de código, complexidade de design, resiliência em produção, por uma fração do custo. A baseline completa continua sendo o padrão; o lite é sempre opt-in.

## Instalação

Pré-requisito, a biblioteca wondel.ai:

```bash
npx skills add wondelai/skills --all --global
```

Depois este router, por um dos métodos:

### Plugin marketplace do Claude Code (recomendado)

```
/plugin marketplace add carloslimaborges/multilens-review
/plugin install multilens-review@multilens-review
```

### skills.sh (Claude Code, Cursor, Codex e outros agentes agentskills.io)

```bash
npx skills add carloslimaborges/multilens-review --global
```

### Manual (Google Antigravity ou qualquer agente)

```bash
git clone https://github.com/carloslimaborges/multilens-review /tmp/war \
  && cp -r /tmp/war/multilens-review ~/.agents/skills/   # Antigravity
  # para Claude Code use ~/.claude/skills/
```

Sem configuração. O router ativa sozinho sempre que uma tarefa corresponder.

## Como funciona

Skills de agente são prompts com revelação progressiva: o agente sempre vê o nome + descrição de cada skill e só carrega o corpo completo quando relevante. Este router explora esse mecanismo, sua descrição foi escrita para disparar em qualquer tarefa de engenharia/produto/marketing, e seu corpo é uma tabela de roteamento que instrui o agente sobre quais skills wondel.ai carregar em seguida. Uma skill que carrega skills.

## Decisões de design

- **Baseline completa em vez de escolher a dedo (engenharia):** revisões de framework único perdem o que as lentes adjacentes capturam. Um refactor revisado só por Clean Code perde as lacunas de resiliência do Release It! e os problemas de tratamento de dados do DDIA. A passada multifocal custa mais tokens; ela os recupera em achados.
- **1–3 skills fora de engenharia:** tarefas de marketing/produto se beneficiam de foco, não de amplitude.
- **A escolha do usuário sempre vence:** skills nomeadas explicitamente ignoram o router.
- **Degradação graciosa:** se uma skill roteada não estiver instalada, o agente prossegue e sugere o comando de instalação uma única vez.

## Licença

MIT, veja [LICENSE](LICENSE).

Construído sobre a excelente biblioteca [wondelai/skills](https://github.com/wondelai/skills) (também MIT).
