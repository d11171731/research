# Research: Basic Automatic Conditional Orders for Vietnamese Stock Trading

**Research Date:** October 31, 2025
**Level:** BASIC - For Retail Investors & Beginners
**Market:** Vietnamese Stock Exchanges (HOSE, HNX, UPCOM)
**Methodology:** Multi-dimensional analysis using Tavily search + Ultrathink framework

---

## Executive Summary

Automatic conditional orders (lệnh điều kiện tự động) are pre-programmed trading instructions that execute automatically when specific market conditions are met. For Vietnamese retail investors, these tools solve the fundamental challenge of continuous market monitoring during trading hours (9:00-14:30) while enforcing disciplined risk management.

**Key Finding:** Conditional orders are BROKER-SIDE automation (not exchange-level), meaning different Vietnamese brokers (SSI, VPS, TCBS, DNSE, MBS) offer varying features and implementations.

---

## Table of Contents

1. [What Are Conditional Orders?](#1-what-are-conditional-orders)
2. [Basic Types for Beginners](#2-basic-types-for-beginners)
3. [How They Work on Vietnamese Exchanges](#3-how-they-work-on-vietnamese-exchanges)
4. [Practical Applications](#4-practical-applications)
5. [Risk Management Perspective](#5-risk-management-perspective)
6. [Common Misconceptions](#6-common-misconceptions)
7. [Essential Terminology](#7-essential-terminology)
8. [Implementation Guide](#8-implementation-guide)
9. [Platform Comparison](#9-platform-comparison)
10. [Best Practices](#10-best-practices)

---

## 1. What Are Conditional Orders?

### Definition

**Vietnamese:** Lệnh điều kiện tự động
**English:** Automatic Conditional Orders

A conditional order is a trading instruction that remains dormant on the broker's system until specific predefined conditions are met. Once triggered, the broker automatically sends the order to the exchange for execution.

### Core Purpose

For Vietnamese retail investors, conditional orders solve three critical problems:

1. **Time Constraint:** Most investors work 9-5 and cannot monitor markets during trading hours
2. **Emotional Discipline:** Removes emotion from buy/sell decisions
3. **Risk Management:** Enforces predetermined loss limits and profit targets

### Key Distinction

**NOT Exchange-Side:** Conditional orders sit on your broker's system, not on HOSE/HNX/UPCOM
**Broker Monitors:** Your broker watches market prices and triggers orders when conditions match
**Platform Dependent:** Features vary significantly between Vietnamese brokers

---

## 2. Basic Types for Beginners

### 2.1 Stop Loss Order (Lệnh Dừng Lỗ / Lệnh Cắt Lỗ)

**Purpose:** Protect capital by automatically selling when price falls to a predetermined level

**How It Works:**
- You set a trigger price below current market price
- When market price falls to or below trigger → broker sends SELL order
- Execution happens at market price (may differ from trigger price)

**Example:**
```
Stock: VNM (Vinamilk)
Current Price: 85,000 VND
Your Entry: 85,000 VND
Stop Loss Set: 78,000 VND (8.2% loss)

Scenario: Price drops to 78,000
→ Broker automatically sends sell order
→ Order executes at best available price (may be 78,000 or slightly lower)
→ Loss limited to approximately 8.2%
```

**Vietnamese Expert Recommendation:** 7-10% stop loss for typical market volatility

### 2.2 Take Profit Order (Lệnh Chốt Lời)

**Purpose:** Lock in gains automatically when profit target is reached

**How It Works:**
- You set a trigger price above current market price
- When market price rises to or above trigger → broker sends SELL order
- Removes greed and ensures profit capture

**Example:**
```
Stock: HPG (Hoa Phat Group)
Your Entry: 25,000 VND
Current Price: 27,500 VND (+10%)
Take Profit Set: 29,000 VND (16% gain)

Scenario: Price rises to 29,000
→ Broker automatically sends sell order
→ Profit locked at approximately 16%
→ No manual intervention needed
```

**Vietnamese Expert Recommendation:** 15-20% take profit for short-term trading

### 2.3 Conditional Buy Order (Lệnh Mua Điều Kiện)

**Purpose:** Enter position when momentum is confirmed (breakout trading)

**How It Works:**
- You set a trigger price above current market price
- When market price rises to trigger → broker sends BUY order
- Confirms strength before entering

**Example:**
```
Stock: FPT Corporation
Current Price: 118,000 VND
Resistance Level: 120,000 VND
Conditional Buy Set: 120,500 VND

Scenario: Price breaks above 120,500
→ Broker automatically sends buy order
→ You enter only after breakout confirmed
→ Avoid buying too early in consolidation
```

### 2.4 Time Conditional Order - TCO (Lệnh Điều Kiện Theo Thời Gian)

**Purpose:** Schedule orders for future execution when you can't be online

**How It Works:**
- You set specific date/time and price
- Order activates at scheduled time
- Automatically cancels if not executed by expiry

**Example:**
```
Stock: VCB (Vietcombank)
Target Price: 95,000 VND
Schedule: Tomorrow 9:30 AM
Expiry: End of week

Scenario: Tomorrow at 9:30 AM
→ If price is favorable, order executes
→ If not executed by Friday close, order cancels
→ Useful for vacation or busy periods
```

---

## 3. How They Work on Vietnamese Exchanges

### 3.1 Technical Architecture

```
[Investor] → Sets Conditional Order → [Broker's System]
                                            ↓
                                    (Monitors Market)
                                            ↓
                                    Condition Met?
                                            ↓
                                          YES
                                            ↓
                            Sends Order → [HOSE/HNX/UPCOM]
                                            ↓
                                    Order Matching
                                            ↓
                                    Execution Report
```

### 3.2 Exchange-Specific Details

#### HOSE (Ho Chi Minh Stock Exchange)
- **Price Band:** ±7% from reference price
- **Reference Price:** Previous day's closing price
- **Trading Hours:** 9:00-14:30
- **Sessions:**
  - ATO (9:00-9:15): Opening auction
  - Continuous (9:15-14:30): Main trading
  - ATC (14:30): Closing auction

#### HNX (Hanoi Stock Exchange)
- **Price Band:** ±10% from reference price
- **Wider Volatility:** Allow larger price movements
- **Similar Sessions:** ATO, Continuous, ATC

#### UPCOM (Unlisted Public Company Market)
- **Price Band:** ±15% from reference price
- **Highest Volatility:** Smaller companies, higher risk
- **Less Liquidity:** May have execution challenges

### 3.3 Order Types Available

**LO (Limit Order):** Execute only at specified price or better
```
Buy LO at 50,000 = Will only buy at 50,000 or lower
Sell LO at 50,000 = Will only sell at 50,000 or higher
```

**MTL (Market To Limit):** Market order that converts to limit if partially filled
```
Buy 1,000 shares MTL at 50,000
→ Tries to execute at market price immediately
→ If only 600 shares filled, remaining 400 becomes limit order
```

**Critical:** Conditional orders typically trigger during CONTINUOUS SESSION only, not during auctions.

### 3.4 Timing Considerations

**Trading Schedule:**
```
09:00-09:15  ATO (Opening Auction)     - Orders accumulate, no matching
09:15-14:30  Continuous Session        - Conditional orders can trigger
14:30-14:45  ATC (Closing Auction)     - Determines closing price
```

**Overnight Gaps:**
- Conditional orders do NOT protect against overnight news
- Market can gap up/down between sessions
- Stop loss at 50,000 won't help if stock opens at 45,000 next day

---

## 4. Practical Applications

### Scenario 1: The Busy Professional

**Profile:** Works 9-6, cannot watch market during trading hours

**Situation:**
- Bought VCB at 95,000 VND
- Stock now at 102,000 VND (+7.4% unrealized gain)
- Has meetings all day tomorrow

**Solution:**
```
Set DUAL conditional orders:
1. Take Profit: 105,000 VND (10.5% gain target)
2. Stop Loss: 99,000 VND (4.2% loss limit from current price)

Result: Automatic execution regardless of market direction
No need to check phone during meetings
```

### Scenario 2: Vacation Protection

**Profile:** Going on 2-week beach vacation, has profitable portfolio

**Situation:**
- Portfolio up 15-20% across multiple stocks
- Worried about market reversal while away
- Will have limited internet access

**Solution:**
```
For each holding, set trailing stop loss:
- Calculate 7-8% below CURRENT price (not entry price)
- Example: Stock bought at 40,000, now 50,000
  → Set stop at 46,000 (8% below current)
  → Protects most of the 25% gain

Alternative: Set take profit at current level +5%
→ Captures gains if market continues up
→ Exits automatically if hit
```

### Scenario 3: Breakout Trading

**Profile:** Technical trader waiting for resistance break

**Situation:**
- Stock consolidating between 48,000-52,000 for 2 weeks
- Wants to buy only if breakout confirms
- Doesn't want to buy prematurely

**Solution:**
```
Set Conditional Buy Order:
- Trigger: 52,500 VND (above resistance)
- Quantity: 500 shares
- Order Type: Limit at 53,000 VND

Result: Only enters if momentum confirmed
Avoids false breakouts
Systematic entry, not emotional
```

### Scenario 4: Dollar Cost Averaging (DCA)

**Profile:** Long-term investor building position gradually

**Situation:**
- Wants to accumulate VNM over 3 months
- Budget: 50 million VND total
- Prefers systematic approach

**Solution:**
```
Use TCO for scheduled purchases:
Week 1: Buy 10M at market price, date: Monday 9:30 AM
Week 2: Buy 10M at market price, date: Monday 9:30 AM
(Repeat for 5 weeks)

Benefit: Removes timing guesswork
Enforces discipline
Some brokers allow multi-day orders without upfront payment
```

---

## 5. Risk Management Perspective

### 5.1 The Psychology Problem

**Vietnamese Market Reality:**
- Strong cultural resistance to "losing face" by admitting losses
- Tendency to hold losing positions hoping for recovery
- Emotional attachment to stocks that go down

**Conditional Orders Solution:**
- Pre-commit to loss limit BEFORE emotion kicks in
- Automatic execution removes hesitation
- Treats trading as business, not gambling

### 5.2 Position Sizing Integration

**Proper Risk Framework:**
```
Account Size: 100,000,000 VND (100 million)
Risk Per Trade: 2% = 2,000,000 VND
Stop Loss: 8%

Maximum Position Size Calculation:
2,000,000 / 0.08 = 25,000,000 VND position

Example:
Stock Price: 50,000 VND
Position Size: 25,000,000 / 50,000 = 500 shares
Stop Loss: 46,000 VND (8% below entry)
Risk: 500 shares × 4,000 loss = 2,000,000 VND ✓

If stopped out: Lose exactly 2% of account
Account drops to: 98,000,000 VND
Still have 98% to continue trading
```

### 5.3 The Margin Call Reality

**Critical Vietnamese Market Feature:**

Brokers automatically monitor margin accounts and execute FORCED SELLING:

```
Margin Deal Structure:
- Warning Threshold: When deal ratio hits warning level
  → System sends automatic notification via app/email
  → Investor should add cash or sell positions

- Liquidation Threshold: When deal ratio hits force-sell level
  → System AUTOMATICALLY sells at FLOOR PRICE
  → NO manual intervention possible
  → Protects broker, not investor

Example:
Deal Value: 100,000,000 VND
Margin Loan: 60,000,000 VND
Maintenance Ratio: 130%

If stock prices drop and deal ratio falls to 125%:
→ AUTOMATIC FORCE SELL triggered
→ Sells at whatever price available (often floor price)
→ Investor has no control
```

**Lesson:** Set YOUR OWN stop losses BEFORE broker's force-sell triggers. Broker's automation protects broker, your automation protects YOU.

### 5.4 Recommended Risk Parameters

**For Vietnamese Market Volatility:**

| Trader Type | Stop Loss | Take Profit | Position Hold |
|-------------|-----------|-------------|---------------|
| Day Trader | 3-5% | 5-8% | Intraday only |
| Swing Trader | 7-10% | 15-20% | Days to weeks |
| Position Trader | 12-15% | 30-50% | Weeks to months |

**Beginner Recommendation:** Start with 8% stop loss, 15% take profit

---

## 6. Common Misconceptions

### Misconception 1: "Stop Loss Guarantees Exact Price"

**What Beginners Think:**
"I set stop loss at 50,000, so I'll sell exactly at 50,000"

**Reality:**
- Stop loss TRIGGERS at 50,000
- Execution happens at MARKET PRICE
- In fast-falling market, may execute at 49,500 or 49,000
- This is called "SLIPPAGE"

**Vietnamese Market Example:**
```
Your Stop: 50,000 VND
Market Scenario: Bad news, stock gaps down
- 50,500 (last trade before news)
- GAP
- 48,500 (next available price)

Result: Your order executes at 48,500, not 50,000
Slippage: 1,500 VND (3%)
```

**Solution:** Build slippage buffer into your risk calculations

### Misconception 2: "Tighter Stop = Better Risk Control"

**What Beginners Think:**
"I'll set 2-3% stop loss to minimize risk"

**Reality:**
- Gets stopped out by normal market noise
- Vietnamese stocks often move 5-7% daily
- "Whipsaw" effect: Stopped out, then stock recovers

**Better Approach:**
- Use ATR (Average True Range) for stop distance
- Vietnamese market typically needs 7-10% stops
- Consider stock's volatility, not arbitrary percentage

### Misconception 3: "Set and Forget"

**What Beginners Think:**
"Once I set stop loss, I never need to adjust it"

**Reality:**
- As stock moves in your favor, initial stop becomes too far
- Should "trail" stop loss upward to protect gains
- Never move stop LOWER (only higher for long positions)

**Example:**
```
Entry: 50,000 with stop at 46,000 (8% loss)
Stock moves to: 60,000 (+20% gain)

Bad: Leave stop at 46,000 (could lose all gains)
Good: Move stop to 55,000 (locks in 10% profit minimum)
```

### Misconception 4: "Stop Loss = Admitting Defeat"

**Cultural Issue:**
- Vietnamese investors view cutting losses as "failure"
- Pride prevents admitting wrong decision
- Hope-based holding leads to major losses

**Professional Reality:**
- Stop loss is tuition fee for learning
- Small controlled losses preserve capital for next trade
- Big losses destroy accounts and confidence

**Quote from Vietnamese Experts:**
"Thà mất 8% hôm nay, còn hơn mất 50% sau 6 tháng chờ đợi"
"Better to lose 8% today than 50% after 6 months of hoping"

### Misconception 5: "Works 24/7"

**What Beginners Think:**
"My conditional orders protect me all the time"

**Reality:**
- Only active during trading hours (9:00-14:30)
- Cannot protect against overnight gaps
- Weekend news creates Monday gaps

**Vietnamese Market Pattern:**
```
Friday Close: 50,000 VND
Your Stop Loss: 46,000 VND

Weekend: Major negative news announced
Monday Open: 43,000 VND (gap down past your stop)

Result: Stop triggers at 43,000, not 46,000
Gap Risk: 3,000 VND (6%)
```

### Misconception 6: "All Brokers Offer Same Features"

**What Beginners Think:**
"Conditional orders work the same everywhere"

**Reality:**
- SSI has different features than VPS
- TCBS interface differs from DNSE
- Some offer OCO orders, some don't
- Some have trailing stops, some don't

**Action Required:** Check YOUR specific broker's documentation and test on paper trading first

---

## 7. Essential Terminology

### 7.1 Order Types (Bilingual)

| Vietnamese | English | Description |
|------------|---------|-------------|
| Lệnh điều kiện | Conditional Order | Order that activates when conditions met |
| Lệnh thị trường (MKT) | Market Order | Execute immediately at best available price |
| Lệnh giới hạn (LO/LMT) | Limit Order | Execute only at specified price or better |
| Lệnh dừng (STP) | Stop Order | Triggers market/limit order when price hit |
| Lệnh dừng lỗ | Stop Loss | Sell order to limit losses |
| Lệnh chốt lời | Take Profit | Sell order to lock in gains |
| Lệnh trailing stop | Trailing Stop | Stop that moves with price |
| Lệnh TCO | Time Conditional Order | Scheduled order for future time |
| Lệnh OCO | One-Cancels-Other | Two orders, one cancels the other |

### 7.2 Trigger Conditions

| Vietnamese | English | Usage |
|------------|---------|-------|
| Giá điều kiện | Trigger/Condition Price | Price that activates order |
| Giá kích hoạt | Activation Price | Same as trigger price |
| Khi giá chạm ngưỡng | When price hits threshold | Trigger event |
| Giá >= X | Price greater than or equal X | Buy condition |
| Giá <= X | Price less than or equal X | Sell condition |

### 7.3 Market Mechanics

| Vietnamese | English | Description |
|------------|---------|-------------|
| Giá tham chiếu | Reference Price | Previous day's closing price |
| Giá trần | Ceiling Price | Maximum allowed price (+7%/10%/15%) |
| Giá sàn | Floor Price | Minimum allowed price (-7%/10%/15%) |
| Biên độ dao động | Price Fluctuation Band | Allowed price range |
| Khớp lệnh | Order Matching | Order execution process |
| Thanh khoản | Liquidity | Ease of buying/selling |
| Trượt giá | Slippage | Difference between trigger and execution |

### 7.4 Position Management

| Vietnamese | English | Context |
|------------|---------|---------|
| Cắt lỗ | Cut Loss | Close losing position |
| Chốt lời | Take Profit | Close winning position |
| Bảo vệ vốn | Protect Capital | Risk management goal |
| Quản lý rủi ro | Risk Management | Overall strategy |
| Mức thua lỗ | Loss Limit | Maximum acceptable loss |
| Mục tiêu lợi nhuận | Profit Target | Desired gain level |
| Tỷ lệ rủi ro/lợi nhuận | Risk/Reward Ratio | Trade evaluation metric |

### 7.5 Time Elements

| Vietnamese | English | Application |
|------------|---------|-------------|
| Phiên liên tục | Continuous Trading Session | Main trading period |
| Phiên ATO | Opening Auction | 9:00-9:15 |
| Phiên ATC | Closing Auction | 14:30-14:45 |
| Thời hạn lệnh | Order Validity Period | How long order stays active |
| Lệnh hết hiệu lực | Order Expiration | When order auto-cancels |
| Tự động hủy | Automatic Cancellation | System cancels order |

---

## 8. Implementation Guide

### 8.1 Step-by-Step Setup Process

**Step 1: Verify Broker Capabilities**
```
1. Log into your trading platform (SSI iBoard, VPS, TCBS, DNSE, etc.)
2. Navigate to "Advanced Orders" or "Conditional Orders" section
3. Check which order types are available:
   - Stop Loss? ✓ or ✗
   - Take Profit? ✓ or ✗
   - TCO? ✓ or ✗
   - OCO? ✓ or ✗
4. Read broker's documentation on fees and conditions
```

**Step 2: Calculate Your Parameters**
```
Before placing ANY conditional order, calculate:

Account Size: _______________ VND
Risk Per Trade: ___% (recommended 1-2%)
Maximum Loss Amount: _______________ VND

Stock: ___________
Entry Price: _______________ VND
Position Size: ___________ shares
Stop Loss %: ___% (recommended 7-10%)
Stop Loss Price: _______________ VND
Take Profit %: ___% (recommended 15-20%)
Take Profit Price: _______________ VND
```

**Step 3: Place Conditional Order**
```
For Stop Loss:
1. Select stock symbol (e.g., VNM)
2. Choose "Conditional Order" or "Stop Order"
3. Select Direction: SELL
4. Enter Trigger Price: _________ VND
5. Enter Order Type: LO or Market
6. If LO, enter Limit Price: _________ VND
7. Enter Quantity: _________ shares
8. Set Expiry: Good Till Cancelled or specific date
9. Confirm and enter OTP
10. Verify order appears in "Conditional Orders" section
```

**Step 4: Monitor and Adjust**
```
Daily:
- Check if orders still appropriate given price movement
- Adjust take profit/stop loss if stock moved significantly

Weekly:
- Review all active conditional orders
- Cancel outdated orders
- Set new ones for new positions

Monthly:
- Evaluate effectiveness of your stop loss/take profit levels
- Adjust percentages if needed based on results
```

### 8.2 Testing Strategy

**CRITICAL: Test Before Real Money**

```
Phase 1: Paper Trading (2-4 weeks)
- Use broker's demo account if available
- Place conditional orders on paper
- Track what WOULD have happened
- Learn the interface without risk

Phase 2: Small Position Testing (1-2 months)
- Use smallest allowed position size
- Place real conditional orders
- Monitor execution quality
- Verify slippage and timing

Phase 3: Gradual Scale-Up
- Increase position sizes slowly
- Build confidence in automation
- Fine-tune parameters based on results
```

---

## 9. Platform Comparison

### 9.1 Major Vietnamese Brokers

**Research Note:** Features change frequently. Verify current capabilities with your broker.

| Broker | Conditional Orders | Notable Features | Limitations |
|--------|-------------------|------------------|-------------|
| **SSI** (SSI Securities) | ✓ Yes | Advanced order types, good documentation, iBoard app | May have fees for advanced features |
| **VPS** (VPS Securities) | ✓ Yes | Professional platform, multiple order types | Learning curve for interface |
| **TCBS** (Techcombank Securities) | ✓ Yes | User-friendly app, integrated with bank | Limited advanced features |
| **DNSE** (DNSE Securities) | ✓ Yes | Modern interface, mobile-first | Newer broker, smaller support |
| **MBS** (MB Securities) | ✓ Yes | Integration with MB Bank | Check specific features |
| **VCBS** (Vietcombank Securities) | ✓ Varies | Established name, reliable | May be conservative on features |

### 9.2 Key Questions to Ask Your Broker

```
1. Do you offer Stop Loss orders? How are they implemented?
2. Do you offer Take Profit orders?
3. Can I set both Stop Loss and Take Profit on same position (OCO)?
4. Do you offer Trailing Stop Loss?
5. What are the fees for conditional orders?
6. How is slippage handled?
7. Do conditional orders work in all sessions or only continuous?
8. Can I set Time Conditional Orders (TCO)?
9. What happens to conditional orders if I have insufficient funds/shares?
10. Do you offer demo/paper trading to test conditional orders?
```

---

## 10. Best Practices

### 10.1 The 8 Rules of Conditional Order Success

**Rule 1: Never Enter Without a Stop**
```
Before buying ANY stock:
- Calculate stop loss price
- Set conditional sell order immediately after purchase
- Don't delay - emotion increases with every tick
```

**Rule 2: Use 2:1 Risk/Reward Minimum**
```
Example:
Entry: 50,000
Stop: 46,000 (risk: 4,000 or 8%)
Target: 58,000 (reward: 8,000 or 16%)

Risk/Reward = 8,000 / 4,000 = 2:1 ✓

Never trade if potential gain < 2× potential loss
```

**Rule 3: Never Move Stops Against You**
```
ALLOWED:
- Long position: Move stop UP to protect gains
- Short position: Move stop DOWN to protect gains

FORBIDDEN:
- Long position: Move stop DOWN (increases risk)
- Short position: Move stop UP (increases risk)

If tempted to widen stop = position is wrong, exit now
```

**Rule 4: Adjust for Market Volatility**
```
Calm Market (VN-Index daily change < 1%):
- Can use tighter stops (5-7%)

Volatile Market (VN-Index daily change > 2%):
- Need wider stops (10-12%)
- Or reduce position size to maintain same dollar risk
```

**Rule 5: Account for Gaps**
```
Before holidays or major events:
- Tighten position sizes
- Consider closing positions entirely
- Remember: Stop losses don't protect against gaps
```

**Rule 6: Monitor Execution Quality**
```
Track every triggered order:
- Trigger price: _______
- Execution price: _______
- Slippage: _______ VND (_____%)
- Time to execute: _______ seconds

If slippage consistently > 1%, reconsider broker or order type
```

**Rule 7: Update with Price Movement**
```
After 10% gain:
- Move stop loss to breakeven (entry price)
- Now trading with "house money"

After 20% gain:
- Move stop to entry +10%
- Guaranteed minimum profit

After 30% gain:
- Move stop to entry +20%
- Consider taking partial profits
```

**Rule 8: Keep Records**
```
Maintain log of all conditional orders:
- Date set
- Stock, price, trigger levels
- Reason for trade
- Outcome when triggered
- Lessons learned

Monthly review reveals patterns in your decision-making
```

### 10.2 Weekly Checklist

```
Every Monday Morning:
□ Review all active conditional orders
□ Check if stop losses need adjustment for new week
□ Verify take profit levels still make sense
□ Cancel any outdated or irrelevant orders
□ Plan new positions with stops calculated in advance

Every Friday Afternoon:
□ Assess weekend gap risk
□ Consider tightening stops before weekend
□ Review week's triggered orders for slippage patterns
□ Update trading journal with lessons learned
```

### 10.3 Advanced Concepts (For Future Learning)

Once comfortable with basic conditional orders, explore:

- **Trailing Stops:** Stop loss that moves up with price automatically
- **OCO Orders:** One-Cancels-Other (both stop and target set together)
- **Bracket Orders:** Entry + Stop + Target in single order
- **Scale-In/Scale-Out:** Multiple conditional orders at different levels
- **Algorithmic Triggers:** Volume-based or indicator-based conditions

---

## Research Methodology

This research employed multi-dimensional analysis across three perspectives:

### 1. Investor Perspective
- Searched for practical applications and user experiences
- Identified pain points of Vietnamese retail investors
- Analyzed real-world scenarios and solutions

### 2. Risk Management Perspective
- Examined stop loss and take profit strategies
- Investigated position sizing and capital preservation
- Studied margin call mechanisms and forced liquidation

### 3. Market Mechanics Perspective
- Researched exchange-specific rules (HOSE, HNX, UPCOM)
- Analyzed order types and execution processes
- Investigated broker-side vs exchange-side automation

### Search Sources
- Vietnamese financial education sites
- Broker documentation (SSI, VPS, TCBS, DNSE)
- Trading platform tutorials
- Expert analysis and commentary
- Regulatory guidelines

---

## Key Takeaways

1. **Conditional orders are ESSENTIAL tools**, not optional features, for successful trading in Vietnamese stock market

2. **Different brokers offer different features** - must verify your specific platform's capabilities

3. **7-10% stop loss is appropriate** for Vietnamese market volatility, not the 2-3% seen in calmer markets

4. **Stop losses trigger but don't guarantee exact prices** - understand and plan for slippage

5. **Set stops IMMEDIATELY after entering position** - waiting allows emotion to interfere

6. **Conditional orders work only during trading hours** - overnight gaps remain a risk

7. **Position sizing must integrate with stop loss** - risk fixed % of account per trade

8. **Never move stops against your position** - only adjust to protect gains

9. **Test thoroughly before real money** - use paper trading to build confidence

10. **Keep detailed records** - track triggers, slippage, and outcomes to improve

---

## Next Steps for Implementation

### For Beginners
1. Open demo account with your broker
2. Practice placing conditional orders on paper
3. Start with 1% account risk per trade
4. Use simple stop loss and take profit only
5. Track results for 2-3 months before increasing complexity

### For Intermediate Traders
1. Review current positions and add missing stop losses
2. Calculate proper position sizes based on stop distances
3. Implement trailing stops on winning positions
4. Begin using OCO orders if broker supports
5. Analyze historical trades to optimize stop/target levels

### For System Developers
1. Build automated order management system
2. Integrate broker APIs for conditional orders
3. Implement position sizing calculators
4. Create monitoring dashboard for active orders
5. Develop backtesting framework for stop/target optimization

---

## References & Further Research

### Vietnamese Resources
- HOSE Trading Rules: https://www.hsx.vn
- HNX Trading Regulations: https://www.hnx.vn
- SSC Guidelines: State Securities Commission publications

### Recommended Reading
- "Technical Analysis for Vietnamese Stock Market" (Vietnamese)
- "Risk Management in Emerging Markets" (English)
- Broker-specific conditional order documentation

### Tools
- TradingView for charting and alerts
- Broker mobile apps (SSI iBoard, TCBS, etc.)
- Excel/Google Sheets for position sizing calculators

---

## Document Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-10-31 | Initial research compilation - Basic level focus |

---

## Disclaimer

This research document is for educational purposes only and does not constitute financial advice. Vietnamese stock market regulations and broker features change frequently. Always verify current rules with official sources and your broker. Past performance does not guarantee future results. Trading stocks involves risk of loss.

---

**Research compiled by:** Research Team
**Target audience:** Vietnamese retail investors - beginner level
**Last updated:** October 31, 2025
**Language:** English (with Vietnamese terminology integrated)
