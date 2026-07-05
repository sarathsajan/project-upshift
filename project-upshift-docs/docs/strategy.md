# Strategy

This document describes the trading logic in plain English.

## Overview
The bot evaluates a list of candidate stocks that are priced above INR 500. It checks the current portfolio and any active sell orders before making decisions.

## Decision flow
1. For every active sell order, the bot compares the current market price with the order limit. If the price has moved close enough to the target, the existing sell order is cancelled and replaced with a fresh sell instruction that aims to capture gains while protecting the trade with a stop-loss.
2. For every stock already held in the portfolio, the bot checks whether the current price is above the average purchase price. If the price has risen sufficiently above the average cost, it places a sell order to take profits while keeping downside protection in place.
3. For every stock that is not currently held, the bot compares the 5-day moving average with the 20-day moving average. If the shorter-term trend is weaker than the longer-term trend, it places a buy order at market price.
4. For stocks that are already in the portfolio, the bot can also add more units when the current price falls to or below the average purchase price, which supports a systematic averaging approach.

## Expected outcome
The strategy is intended to reduce exposure to weak positions, capture gains when prices move upward, and add to positions only when the risk-reward setup is favorable.
