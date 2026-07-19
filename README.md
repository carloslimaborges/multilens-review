# wondel-auto-router

**A meta-skill that turns any AI coding agent into a multifocal expert reviewer — automatically.**

Compatible with Claude Code, Claude Cowork, Google Antigravity, Cursor, Codex, and any [agentskills.io](https://agentskills.io)-compatible agent.

## The problem

The [wondel.ai skills library](https://skills.wondel.ai) packages 50 frameworks from bestselling engineering and business books (Clean Code, DDIA, Release It!, Refactoring, A Philosophy of Software Design...) as agent skills. But you have to remember to invoke them, by name, on every prompt. Nobody does that consistently — so most of the library's value evaporates.

## The solution

`wondel-auto-router` is a routing layer. Install it once and the agent:

1. **Classifies every task** (engineering, UX, marketing, product, strategy, ops)
2. **Loads the right skills before working** — no manual invocation
3. **For engineering tasks, applies a mandatory 11-lens baseline simultaneously**, producing a multifocal review instead of a single-framework answer:

   `clean-code` · `pragmatic-programmer` · `refactoring-patterns` · `working-with-legacy-code` · `software-design-philosophy` · `release-it` · `ddia-systems` · `high-perf-browser` · `ux-heuristics` · `microinteractions` · `steve-jobs-design-review`

4. **Adds context-specific lenses** on top: greenfield projects get `clean-architecture` + `domain-driven-design` + `system-design`; iOS work gets `ios-hig-design`; visual work gets `refactoring-ui` + `web-typography`
5. **Organizes findings by lens**, so you see what each framework caught: code quality, design complexity, production resilience, data handling, performance, usability, interaction detail, simplicity

Before: *"Refactor this service"* → generic refactor.
After: the same prompt triggers a review through 11 expert lenses — the agent tells you which frameworks it applied and what each one found.

## Install

Prerequisite — the wondel.ai library:

```bash
npx skills add wondelai/skills --all --global
```

Then this router, via one of:

### Claude Code plugin marketplace (recommended)

```
/plugin marketplace add carloslimaborges/wondel-auto-router
/plugin install wondel-auto-router@wondel-auto-router
```

### skills.sh (Claude Code, Cursor, Codex, and other agentskills.io agents)

```bash
npx skills add carloslimaborges/wondel-auto-router --global
```

### Manual (Google Antigravity or any agent)

```bash
git clone https://github.com/carloslimaborges/wondel-auto-router /tmp/war \
  && cp -r /tmp/war/wondel-auto-router ~/.agents/skills/   # Antigravity
  # for Claude Code use ~/.claude/skills/ instead
```

No configuration. The router activates on its own whenever a task matches.

## How it works

Agent skills are progressive-disclosure prompts: the agent always sees each skill's name + description, and loads the full body only when relevant. This router exploits that mechanism — its description is written to trigger on any engineering/product/marketing task, and its body is a routing table that instructs the agent which wondel.ai skills to load next. A skill that loads skills.

## Design decisions

- **Full baseline over cherry-picking (engineering):** single-framework reviews miss what adjacent lenses catch. A refactor reviewed only through Clean Code misses the Release It! resilience gaps and the DDIA data-handling issues. The multifocal pass costs more tokens; it earns them back in findings.
- **1–3 skills for non-engineering:** marketing/product tasks benefit from focus, not breadth.
- **User override always wins:** explicitly named skills bypass the router.
- **Graceful degradation:** if a routed skill isn't installed, the agent proceeds and suggests the install command once.

## License

MIT — see [LICENSE](LICENSE).

Built on top of the excellent [wondelai/skills](https://github.com/wondelai/skills) library (also MIT).
