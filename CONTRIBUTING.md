# Contributing to Alien Invasion

First off — thank you for considering contributing. Whether it's a bug fix, a new feature from the [roadmap](README.md#️-roadmap), better docs, or just a well-written issue, it's genuinely appreciated.

This document exists so that contributing is predictable: you'll know what a good PR looks like here before you open one, and I'll be able to review and merge faster because there's less back-and-forth on basics.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Ways to Contribute](#ways-to-contribute)
- [Branching Strategy](#branching-strategy)
- [Commit Message Guidelines](#commit-message-guidelines)
- [Pull Request Process](#pull-request-process)
- [Code Style](#code-style)
- [Reporting Bugs](#reporting-bugs)
- [Suggesting Features](#suggesting-features)
- [Good First Issues](#good-first-issues)
- [Questions](#questions)

## Code of Conduct

Be respectful, be constructive, assume good faith. Disagreements on technical approach are welcome and encouraged — personal attacks are not. If you experience or witness unacceptable behavior, open an issue or contact the maintainer directly.

## Getting Started

1. **Fork** the repository and clone your fork:

   ```bash
   git clone https://github.com/<your-username>/Alien-Invasion-Game.git
   cd Alien-Invasion-Game
   ```

2. **Add the upstream remote** so you can stay in sync:

   ```bash
   git remote add upstream https://github.com/AhmadRandhawaOfficial/Alien-Invasion-Game.git
   ```

3. **Set up your environment** — follow the [Installation](README.md#️-installation) section in the README (system dependencies, virtual environment, `pip install -r requirements.txt`).

4. **Verify it runs** before you change anything:

   ```bash
   python main.py
   ```

If the game doesn't launch cleanly on a fresh clone, that's worth an issue on its own.

## Project Structure

Before touching code, know where things live — this avoids logic ending up in the wrong layer:

| File | Responsibility |
|---|---|
| `main.py` | Game loop entry point only. No game rules should live here. |
| `settings.py` | All tunable constants — speed, size, colors, difficulty curve. If you're adding a new tunable value, it belongs here, not hardcoded elsewhere. |
| `game_functions.py` | All game logic — input handling, collisions, fleet behavior, difficulty progression. This is where most feature work happens. |
| `game_stats.py` | Score, level, lives, high score state. |
| `scoreboard.py` | Rendering of score/level/lives/high-score to screen. |
| `paths.py` | Asset path resolution. Any new asset should be resolved through here, not hardcoded. |
| `ship.py`, `alien.py`, `bullet.py`, `life_ship.py`, `button.py` | Individual entities — each owns its own state and rendering only. Game rules do **not** belong inside entity classes. |

If you're unsure where new code belongs, ask in the issue or PR before writing it — it's a five-minute conversation that saves a rewrite.

## Ways to Contribute

- **Bug fixes** — see [open issues](../../issues) labeled `bug`.
- **Roadmap features** — see the [README roadmap](README.md#️-roadmap): sound effects, persistent high scores, difficulty presets, power-ups, pause menu, unit tests, packaged builds.
- **Documentation** — README clarity, code comments, docstrings, this file.
- **Tests** — the project currently has no automated tests. A well-scoped test suite for collision detection and scoring logic (see `game_functions.py`) is one of the highest-value contributions available right now.
- **Performance** — profiling the game loop, reducing per-frame allocations, sprite rendering optimizations.

If you want to work on something **not** already listed as an issue, open one first describing what you intend to do. This avoids duplicate work and lets us align on approach before you invest time.

## Branching Strategy

This project uses a simple, single-branch-per-change workflow off `main`:

```
main                  # always stable, always runnable
feature/<name>        # new functionality
fix/<name>            # bug fixes
refactor/<name>       # internal restructuring, no behavior change
docs/<name>           # documentation-only changes
```

- Branch from an up-to-date `main`.
- One branch = one logical unit of work. If your feature branch starts accumulating unrelated changes, split it.
- Keep branches short-lived — open the PR as soon as the change is complete and reviewable, rather than batching multiple features into one branch.

## Commit Message Guidelines

This project follows **[Conventional Commits](https://www.conventionalcommits.org/)**. Every commit message should have the form:

```
<type>: <short, present-tense description>
```

**Types used in this project:**

| Type | When to use it |
|---|---|
| `feat` | A new feature or capability |
| `fix` | A bug fix |
| `refactor` | Code restructuring with no behavior change |
| `docs` | Documentation only |
| `test` | Adding or updating tests |
| `build` | Dependency or build-related changes |
| `ci` | CI/CD configuration changes |
| `perf` | Performance improvements |
| `style` | Formatting, whitespace — no logic change |
| `chore` | Maintenance tasks not covered above |

**Rules:**

- **Atomic commits.** Each commit should represent a single, coherent change. If your commit message needs "and" to describe it, it's probably two commits.
- **No vague messages.** `update`, `changes`, `fix bugs`, `final` are not acceptable — they're meaningless to anyone reading `git log` six months from now, including you.
- **Explain the why when it isn't obvious.** The subject line says *what* changed; use the commit body if *why* needs explaining and isn't self-evident from the diff.

**Good examples:**

```
feat: add pause menu triggered by P key
fix: prevent bullet cap from resetting mid-wave
refactor: extract fleet-spawn logic into dedicated function
docs: document difficulty scaling formula in README
```

**Bad examples (will be asked to amend):**

```
update
fix stuff
wip
final final v2
```

## Pull Request Process

1. **Sync with upstream** before opening your PR:

   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. **Keep the diff focused.** A PR should do one thing. If review comments reveal it's actually doing two things, expect to be asked to split it.

3. **Write a clear PR description** covering:
   - What changed and why
   - How you tested it (there's no CI yet, so manual testing steps matter — e.g., "played through 5 waves, confirmed difficulty scaling and lives decrement correctly")
   - Any breaking changes
   - Screenshots or a short clip if the change is visual

4. **Expect review feedback.** This is a learning project as much as a game — reviews will sometimes be about code quality and architecture fit, not just "does it work."

5. **Squash noisy commits before merge** if your branch has exploratory or fixup commits (`wip`, `oops`, `address review`). The final history on `main` should read cleanly. Use:

   ```bash
   git rebase -i upstream/main
   ```

6. Once approved, the PR will be merged — typically via **squash merge** for small features/fixes to keep `main` history clean, or a **regular merge** for larger multi-commit features where the individual commits are each independently meaningful.

## Code Style

- Follow **[PEP 8](https://peps.python.org/pep-0008/)**.
- Match the existing naming conventions in the file you're editing (e.g., `ai_settings` as the parameter name for the settings instance, consistent with the current codebase).
- Prefer clear, descriptive names over comments explaining unclear ones.
- Keep functions single-purpose — this codebase already separates concerns cleanly (see [Project Structure](#project-structure)); new code should preserve that, not erode it.
- Docstrings aren't currently used consistently in this project — for new non-trivial functions, a one-line docstring explaining purpose is encouraged but inline comments are also acceptable for now.

## Reporting Bugs

Open an issue with:

- **Steps to reproduce** — as specific as possible
- **Expected behavior** vs **actual behavior**
- **Environment** — OS, Python version, Pygame version (`pip show pygame`)
- Screenshot or short clip if it's a visual bug

## Suggesting Features

Open an issue describing:

- The problem it solves or the experience it improves
- Why it belongs in this project (does it fit the current scope, or is it a bigger design change?)
- Any implementation ideas you already have

Roadmap items in the README are pre-approved in concept — feel free to just claim one in the issue thread rather than re-pitching it.

## Good First Issues

If this is your first contribution, look for issues labeled `good first issue`. Strong first contributions on this codebase tend to be:

- Adding a new tunable setting (e.g., a new power-up multiplier) to `settings.py` and wiring it through
- Small, well-isolated fixes in `game_functions.py`
- Documentation improvements
- Writing the first unit tests for collision/scoring logic

## Questions

Open a [discussion](../../discussions) or issue, or reach out via [@AhmadHussainRandhawa](https://github.com/AhmadHussainRandhawa). No question is too small — an unclear onboarding step is a documentation bug worth reporting.

---

Thanks again for contributing — every PR, issue, and suggestion makes this project better for the next person who finds it.
