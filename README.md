# Project Upshift

A research-focused trading automation prototype for Indian stock brokers. The repository captures early implementation work for broker API authentication, order management, and a DCA-style trading strategy.

## What the project does

Project Upshift is intended to automate a trading workflow that:

- connects to broker APIs and handles TOTP-based authentication
- fetches market data, holdings, and active order details
- evaluates open orders for cancellation or adjustment
- applies a rule-based strategy for placing buy and sell orders
- plans to support stop-loss and trailing order behavior

## Why the project is useful

This repository is useful for developers and researchers who want to:

- explore Indian broker automation with Python
- understand broker authentication and order lifecycle handling
- prototype algorithmic trading workflows using a DCA-inspired strategy
- maintain a documented path from proof-of-concept to execution-ready code

## Current status

- Planning and exploratory development is in progress
- Authentication and TOTP integration is being researched
- Broker API workflows are still experimental
- No production-ready trading engine exists yet
- `codebase/` is currently empty or pending implementation

## Getting started

### Prerequisites

- Python 3.11+ (or compatible Python 3.x)
- access to an Indian broker API account (5paisa, Upstox, or similar)
- valid API credentials and any broker-specific registration requirements

### Install dependencies

```bash
python -m pip install -r requirements.txt
```

### Repository files

- `requirements.txt` — dependency manifest for Python packages used by the project
- `logic.txt` — trading strategy notes and planned logic flow
- `dev_log.txt` — development journal, research findings, and blocker notes
- `roadmap.md` — project phases and strategy roadmap
- `.github/prompts/` — workspace prompt templates for README generation and code review
- `codebase/` — primary implementation folder (under development)

### How to use

This repository is currently a prototype. The best way to get started is:

1. review the trading strategy in `logic.txt`
2. read the development notes in `dev_log.txt`
3. follow the planned phases in `roadmap.md`
4. begin implementing broker integration and execution code under `codebase/`

## Roadmap

The roadmap includes:

- setup and validation
- authentication and data retrieval
- order management (cancel, modify, place orders)
- operations and monitoring with a tracking database
- fail-safe controls such as a panic button or kill switch

## Where to get help

- Open an issue in this repository for bugs, questions, or feature requests
- Review `dev_log.txt`, `logic.txt`, and `roadmap.md` for project context
- Seek broker-specific support if you need help with API authentication or order execution

## Maintainers and contributing

This project is maintained by the repository owner and is open to contributions.

Contributions are welcome via:

- pull requests with implementation or documentation improvements
- issues for clarifications or feature ideas
- updates that improve onboarding and developer flow

> Note: This repository is a research/proof-of-concept project and is not financial advice.
