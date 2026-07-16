# Project Upshift

A work-in-progress trading automation prototype for Indian stock brokers, originally built around the 5paisa API and now exploring broker-agnostic automation with trailing stop loss support.

## What the project does

Project Upshift is designed to automate a disciplined trading strategy using broker APIs and algorithmic order management. The current plan focuses on:

- authenticating with broker APIs using TOTP-based 2FA
- fetching market data and position details
- evaluating active orders for modification or cancellation
- placing buy and sell orders using a DCA-style strategy
- managing stop-loss and trailing-profit order behavior

## Why the project is useful

This repository captures the research, strategy, and early implementation work for an automated stock trading bot in the Indian market. It is useful for:

- developers exploring brokerage API automation with Python
- traders building a rule-based entry/exit workflow
- maintainers testing a proof-of-concept for broker authentication and order management
- researchers documenting a trading strategy and migration path away from 5paisa

## Current status

- Project is in planning / development stage
- Authentication and TOTP research is underway
- Broker API integration is currently exploratory
- No production-ready trading engine is available yet

## Getting started

### Prerequisites

- Python 3.11+ (or compatible Python 3.x)
- access to an Indian broker API account (5paisa, Upstox, or similar)
- valid API credentials and any broker-specific registration requirements

### Install dependencies

```bash
python -m pip install -r requirements.txt
```

### Available files

- `requirements.txt` — dependency manifest for Python packages used by the project
- `logic.txt` — strategy notes and planned trading flow
- `dev_log.txt` — development journal and research notes
- `codebase/` — project source folder (currently empty or under development)

### How to use

This repository is currently a prototype; there is no ready-to-run script yet. Use the existing files to:

1. review the trading strategy in `logic.txt`
2. study authentication and API notes in `dev_log.txt`
3. add implementation code under `codebase/`

## Roadmap

Planned development phases include:

- setup and validation
- authentication and data retrieval
- order management (cancel, modify, place orders)
- operations and monitoring with a tracking database
- fail-safe controls such as panic button or kill switch

## Where to get help

- Open an issue in this repository for bugs, questions, or feature requests
- Review the project notes in `dev_log.txt` and `logic.txt` for implementation context
- Use community support channels for the chosen broker API if you need help with authentication or trade execution

## Maintainers and contributing

This project is maintained by the repository owner and is currently open to contributions.

Contributions are welcome via:

- pull requests with implementation improvements
- issues for clarifications or feature ideas
- documentation updates that improve onboarding and development flow

> Note: This repository is a research/proof-of-concept project and is not financial advice.
