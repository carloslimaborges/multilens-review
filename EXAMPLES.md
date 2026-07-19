# Examples

Real prompts — no skill names needed. The router detects the task and loads the lenses.

## Engineering (11-lens baseline fires automatically)

```
Refactor this payment service. It has no tests and nobody wants to touch it.
```
→ Full baseline loaded; heaviest lenses: working-with-legacy-code, refactoring-patterns.
Findings reported per lens: code quality, complexity, resilience, data handling, performance, UX.

```
Review this PR before I merge it.
```
→ Full baseline as a multifocal code review checklist.

```
Let's build a scheduling app from scratch.
```
→ Baseline + clean-architecture, domain-driven-design, system-design (greenfield additions).

```
Why is the dashboard so slow on mobile?
```
→ Baseline with high-perf-browser and ux-heuristics leading the analysis.

## Non-engineering (focused routing, 1–3 skills)

```
Write the copy for my landing page hero.
```
→ storybrand-messaging, made-to-stick

```
How should I price the pro plan?
```
→ monetizing-innovation, hundred-million-offers

```
Users sign up but stop using the app after a week.
```
→ improve-retention, hooked-ux

## Overriding the router

Explicitly named skills always win:

```
Use only the clean-code skill and review this file.
```
→ Router steps aside; only clean-code is applied.
