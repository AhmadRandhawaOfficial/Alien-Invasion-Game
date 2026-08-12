<div align="center">

# 👾 Alien Invasion

**A classic arcade shooter, built from scratch in Python with Pygame.**

Four-directional movement. A wave-based fleet with edge-aware collision detection. A difficulty engine that compounds speed and score with every level cleared — all sitting on a modular, single-responsibility architecture.

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white">
  <img alt="Pygame" src="https://img.shields.io/badge/Pygame-2.6.1-00b159?logo=pygame&logoColor=white">
  <img alt="Engine" src="https://img.shields.io/badge/Backend-SDL2-informational">
  <img alt="License" src="https://img.shields.io/badge/License-MIT-yellow.svg">
  <img alt="PRs Welcome" src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg">
</p>

</div>

---

## 🎬 See it in action

https://github.com/user-attachments/assets/3e16a161-4ef5-4315-9f37-ef64dac5b663

*A full run: fleet spawn → four-directional dodging → wave clear → difficulty spike → ship loss → game over screen.*

---

## 📑 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Controls](#️-controls)
- [Architecture](#️-architecture)
- [Installation](#️-installation)
- [Roadmap](#️-roadmap)
- [Contributing](#-contributing)
- [License](#-license)

## 📖 Overview

**Alien Invasion** is a top-down arcade shooter inspired by the classic Space Invaders formula, reimagined with a fully object-oriented architecture and a scaling difficulty curve. Pilot your ship, hold the alien fleet back, and survive as the game gets progressively faster and more punishing with every wave you clear.

This project was built as a deep dive into **game loop architecture, real-time input handling, collision systems, and state management** — the same fundamentals that show up in simulations, real-time systems, and interactive applications far beyond games.

## ✨ Features

- 🎮 Full four-directional ship movement (not just the classic left–right lane)
- 🚀 Real-time shooting with a configurable bullet cap
- 👽 Dynamic alien fleet with automatic edge detection and direction reversal
- 📈 Progressive difficulty — speed and score-per-kill compound after every cleared wave
- ❤️ Lives system with visual ship-life indicators
- 🏆 Live scoreboard with in-session high-score tracking
- 🖱️ Interactive Start/Restart flow

## 🕹️ Controls

| Key            | Action                |
|----------------|------------------------|
| `↑ ↓ ← →`      | Move the ship          |
| `Space`        | Fire bullet             |
| `Esc`          | Quit game               |
| `Mouse Click`  | Start / Restart game    |

## 🏗️ Architecture

```
main.py               # Entry point — owns the game loop, wires everything together
settings.py           # All tunable constants: speed, size, colors, difficulty curve
game_functions.py     # Game logic layer — input handling, collisions, fleet & difficulty rules
game_stats.py         # Tracks score, level, lives, high score
scoreboard.py         # Renders score/level/lives/high-score to screen
paths.py              # Working-directory-independent asset resolution

ship.py               # Player entity
alien.py              # Alien entity
bullet.py             # Bullet entity
life_ship.py          # Ship-life indicator icon
button.py             # Interactive Start/Restart button

assets/images/        # Sprites and game icon
```

## ⚙️ Installation

**1. Clone the repository**

```bash
git clone https://github.com/AhmadRandhawaOfficial/Alien-Invasion-Game.git
cd Alien-Invasion-Game
```

**2. System dependencies (Linux only)**

Pygame's SDL2 backend needs a few system libraries to build/run on Debian/Ubuntu-based systems:

```bash
sudo apt install build-essential python3-dev \
    libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev \
    libfreetype6-dev pkg-config
```

> macOS/Windows users can typically skip this step — Pygame ships prebuilt wheels for these platforms.

**3. Set up a virtual environment**

```bash
python3 -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
```

**4. Install dependencies and run**

```bash
pip install -r requirements.txt
python main.py
```

## 🗺️ Roadmap

- [ ] Sound effects and background music
- [ ] Persistent high-score storage across sessions
- [ ] Difficulty presets (Easy / Normal / Hard)
- [ ] Power-ups (shield, rapid fire, multi-shot)
- [ ] Pause menu
- [ ] Unit tests for collision and scoring logic
- [ ] Packaged executable builds (PyInstaller)

Have an idea not listed here? Open an issue — see [Contributing](#-contributing).

## 🤝 Contributing

Contributions are welcome — bug fixes, roadmap features, or documentation improvements. Please read [`CONTRIBUTING.md`](CONTRIBUTING.md) before opening a pull request. New to the codebase? `game_functions.py` is the best entry point — nearly every game rule lives there.

## 📜 License

Licensed under the **MIT License** — see [`LICENSE`](LICENSE) for details.

## 💬 Acknowledgement 
 
Built on the Alien Invasion project from **[*Python Crash Course*](https://ehmatthes.github.io/pcc/) by Eric Matthes** — extended with four-directional movement, portable asset paths, and centralized difficulty scaling.
 
---

<div align="center">

Built by **[Ahmad Hussain](https://github.com/AhmadRandhawaOfficial)**

If this project helped you learn something or you just enjoyed playing it, consider leaving a ⭐

</div>
