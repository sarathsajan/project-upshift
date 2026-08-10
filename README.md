# Project Upshift

Project Upshift is a Python workspace for exploring and prototyping with the Upstox API. The repository contains small, script-oriented API examples for account access, holdings, brokerage, market prices, instrument data, and a Telegram-driven alert bot that evaluates current portfolio conditions and emits Buy/Sell/Hold decisions.

## What the project does

This codebase is organized as a research and integration sandbox around the Upstox Python SDK. It reads credential material from a shared local configuration file, authenticates through a configured access token, and demonstrates how core broker-side endpoints can be called from Python scripts.

The code currently covers these interfaces:

- User/profile and fund-margin access via the `UserApi` contract.
- Portfolio and holdings retrieval through `PortfolioApi`.
- Market LTP examples through `MarketQuoteV3Api`.
- Brokerage calculations through `ChargeApi`.
- Order request construction via `OrderApiV3`.
- A Telegram alert workflow in the alert bot that reports price thresholds for holdings and sends action-oriented messages.

## Why the project is useful

The repository is useful for developers and researchers who want to:

- Understand how the Upstox SDK maps to common broker functions.
- Learn how to structure a Python automation prototype around a live API surface.
- Evaluate DCA-style decision logic around portfolio positions and price movement.
- Extend individual scripts into a larger algorithmic trading or alerting workflow.

The repository layout keeps each API topic isolated inside a folder so that examples can be extended independently:

- [orders/place_order.py](orders/place_order.py) builds a live V3 order payload.
- [market/get_ltp_quotes.py](market/get_ltp_quotes.py) reads the last traded price for a market symbol.
- [user/get_profile.py](user/get_profile.py) and [user/get_fund_and_margin.py](user/get_fund_and_margin.py) read account context.
- [portfolio/get_holdings.py](portfolio/get_holdings.py) reads portfolio holdings.
- [charges/brokerage_details.py](charges/brokerage_details.py) demonstrates brokerage lookup calls.
- [instruments/get_instrument_info.py](instruments/get_instrument_info.py) downloads and analyzes instrument metadata.
- [alert-bot/price_alert_bot.py](alert-bot/price_alert_bot.py) evaluates holdings and sends notifications.

## Current status

This repository is best understood as a research, proof-of-concept, and planning workspace.

Current status highlights:

- Upstox SDK integration is active and the dependency manifest is present.
- API examples are implemented as scripts rather than as a packaged service.
- A long-range DCA strategy is described in [roadmap.md](roadmap.md).
- The workspace is appropriate for learning, prototyping, and API exploration, but it is not a production-ready execution engine.
- This is not financial advice and should be treated as a research-driven trading workflow.

## Project structure

```text
project-upshift/
├── env.json                     # runtime credentials and tokens
├── requirements.txt             # Python dependency manifest
├── roadmap.md                   # high-level execution plan
├── dev_log.txt                  # development notes and research journal
├── alert-bot/                   # alert-style bot logic and supporting credentials
├── charges/                     # brokerage examples
├── instruments/                 # complete instrument data download and search helpers
├── market/                      # market quote examples
├── orders/                      # order request examples
├── portfolio/                   # portfolio APIs and holdings examples
└── user/                        # login, profile, margin, and logout examples
```

## Getting started

### Prerequisites

Before using the repository, make sure you have:

- Python 3.11 or a compatible Python 3.x runtime.
- An Upstox developer account and a valid access token.
- A local [env.json](env.json) file containing the required token values for API access and, when using the Telegram bot, the Telegram credentials.
- Internet access for broker APIs and instrument-data retrieval.
- A controlled environment that can safely exercise the API contract.

### Install dependencies

Install dependencies from the repository root:

```bash
python -m pip install -r requirements.txt
```

The current dependency manifest in [requirements.txt](requirements.txt) includes:

```text
upstox-python-sdk==2.28.0
tzdata==2026.3
requests==2.34.2
```

### Configure credentials

Update [env.json](env.json) with the values expected by the credential helpers:

```json
{
  "UPSTOX_ACCESS_TOKEN": "<your-access-token>",
  "UPSTOX_ACCESS_TOKEN_SANDBOX": "<optional-sandbox-token>",
  "TELEGRAM_BOT_TOKEN": "<telegram-token>",
  "TELEGRAM_CHAT_ID": "<telegram-chat-id>"
}
```

The credential helpers in each topic folder read the same shared configuration file through a relative working-directory path. That means these scripts are expected to be run from the relevant folder context so the local credential resolution remains consistent.

### Example usage

A typical profile read from the repository looks like this:

```bash
cd user
python get_profile.py
```

Market last-traded-price reads can be exercised from the market directory:

```bash
cd market
python get_ltp_quotes.py
```

A V3 order payload example is located here:

```bash
cd orders
python place_order.py
```

The alert bot is a polling workflow launched through the folder runner:

```bash
cd alert-bot
python manage.py
```

That bot calls [alert-bot/price_alert_bot.py](alert-bot/price_alert_bot.py), which pulls portfolio holdings and emits Telegram notifications for BUY/SELL/HOLD conditions. The folder also contains [alert-bot/telegram_bot.py](alert-bot/telegram_bot.py) for message posting and [alert-bot/read_creds.py](alert-bot/read_creds.py) for environment loading.

## Operational notes

### Account and network behavior

The APIs in this repository expect a real Upstox account context and a valid access token. In practice, login, OTP, developer-dashboard generation, and static-IP registration are part of the workflow described in [dev_log.txt](dev_log.txt), so the scripts should be treated as examples that require broker-side setup.

### Safety and research warning

The code can trigger real broker interactions if credentials and runtime environment are configured. The order and alert logic should not be run in a production or paper-trading context without validation, risk controls, and explicit response review. This repository is research-oriented and should not be interpreted as operational financial automation.

## Where to get help

Useful reference points for this project are:

- [roadmap.md](roadmap.md) for the implementation phases and DCA-style strategy notes.
- [dev_log.txt](dev_log.txt) for historical implementation notes and workflow details.
- The Upstox Python SDK examples that correspond to the API contracts being exercised.
- The Upstox developer documentation for credentials, APIs, static IP requirements, and protocol details.

For implementation questions or feature discussions, open an issue in the repository and include the script name, the expected input, and the API response details when possible.

## Maintainers and contributing

This repository is currently maintained as an open development workspace. Contributions are welcome in the form of:

- Bug fixes and examples that improve API correctness.
- Documentation updates that clarify setup or broker workflows.
- New API wrappers or strategy modules that fit the current project structure.

Before opening or reviewing a change, please keep the code aligned with the existing folder structure and the Python dependency manifest in [requirements.txt](requirements.txt).

> Note: Project Upshift is a research and proof-of-concept project. It is not intended as financial advice and should not be used as a production trading system without security, risk, and validation review.

