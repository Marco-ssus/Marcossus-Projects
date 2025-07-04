# Colors
YELLOW := $(shell tput -Txterm setaf 3)
GREEN  := $(shell tput -Txterm setaf 2)
RESET  := $(shell tput -Txterm sgr0)

# Virtual environment paths
VENV := .venv
PYTHON := $(VENV)/bin/python
PIP := $(VENV)/bin/pip
GUNICORN := $(VENV)/bin/gunicorn
BLACK := $(VENV)/bin/black
FLAKE8 := $(VENV)/bin/flake8

# Number of workers (default 4, can be overridden)
WORKERS ?= 4

# ===========================
# Help
# ===========================
help:
	@echo ""
	@echo "${YELLOW}Available commands:${RESET}"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  ${GREEN}%-20s${RESET} %s\n", $$1, $$2}'
	@echo ""

# ===========================
# Project Setup
# ===========================
setup: ## Create virtual environment and install dependencies
	@echo "${YELLOW}Creating virtual environment...${RESET}"
	python3 -m venv $(VENV)
	@echo "${YELLOW}Installing dependencies...${RESET}"
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt
	@echo "${GREEN}✔️ Environment setup complete!${RESET}"

# ===========================
# Running
# ===========================
run: ## Run the app 
	@echo "--- Iniciando o RPG de Terminal..."
	$(PYTHON) main.py

# ===========================
# Docker
# ===========================
docker-build: ## Build Docker image
	@echo "${YELLOW}Building Docker image...${RESET}"
	docker build -t rpg-game .

docker-run: ## Run Docker container
	@echo "${YELLOW}Running Docker container...${RESET}"
	docker run -it --rm -v "$(shell pwd)/saves":/app/saves rpg-game

# ===========================
# Code Quality
# ===========================
format: ## Format code with Black
	@echo "${YELLOW}Formatting code with Black...${RESET}"
	$(BLACK) app

lint: ## Lint code with Flake8
	@echo "${YELLOW}Linting code with Flake8...${RESET}"
	$(FLAKE8) app

# ===========================
# Cleaning
# ===========================
clean: ## Remove virtual environment and __pycache__
	@echo "${YELLOW}Cleaning project...${RESET}"
	rm -rf $(VENV)
	find . -type d -name "__pycache__" -exec rm -r {} +
