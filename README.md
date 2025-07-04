# 🐉 Terminal Quest: The Ultimate Python Text RPG

Welcome to **Terminal Quest**, the geekiest, nerdiest, and most pixel-less fantasy adventure you'll ever run in your terminal! Slay monsters, level up, and face the mighty 🐲 **Dragão Supremo** – all while embracing the power of Python.

> “In a land of code and caffeine, only the boldest heroes survive...”

---

## 🚀 Features

- 🎭 **Three Epic Classes**: Choose to be a **Warrior**, **Mage**, or **Rogue** – each with unique stats and flavor.
- ⚔️ **Turn-Based Combat**: Attack, use potions, or make a tactical retreat.
- 🛒 **In-Game Shop**: Spend your gold on potions or permanent stat upgrades.
- 💾 **Auto Save/Load**: Your adventure is always remembered.
- 🐉 **Boss Battle**: After defeating 5 enemies, prepare for the ultimate showdown.
- 🔀 **Modular Design**: Each system is split into Python modules for easy hacking and expansion.

---

## 🧙‍♂️ Getting Started

Make sure you have Python 3.8+ installed.

```bash
python --version
```

Then, clone the repo and enter the project folder:

```bash
git clone https://your-repo-url.git
cd your-repo-folder
```

To run the game:

```bash
python main.py
```

---

## 🛠️ Developer Utilities

We’ve added a **Makefile** to make your life easier. Here are the available commands:

```bash
make help
```

### Useful Commands:

- `make run` – Run the game 🕹️
- `make lint` – Run linters with `ruff` 🔍
- `make format` – Auto-format with `black` 🎨
- `make test` – Run tests 🧪
- `make setup` – Install dependencies (e.g., `black`, `ruff`) ⚙️
- `make clean` – Remove Python cache files 🧼

> Pro Tip: All development tools are containerized with Docker for reproducible builds!

---

## 🐳 Docker Support

Don’t want to install anything? Build and run with Docker:

```bash
docker build -t terminal-quest .
docker run -it terminal-quest
```

---

## 📁 Project Structure

```
.
├── main.py             # Main game loop
├── personagem.py       # Player character classes
├── inimigo.py          # Enemy logic
├── combate.py          # Battle system
├── loja.py             # Shop and upgrades
├── save_load.py        # Save/load system
├── Makefile            # Automation tasks
├── Dockerfile          # Container setup
└── README.md           # You are here!
```

---

## ✨ Contributing

PRs welcome! Add new features, classes, or enemies – or just fix typos. Let’s build this fantasy world together!

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 🎮 Final Words

Whether you're a Python padawan or a terminal wizard, Terminal Quest offers a fun way to explore game development, code organization, and command-line fun.

Now go forth, brave hero. Destiny awaits! ⚔️🛡️
