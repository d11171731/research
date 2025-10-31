# Phân Tích So Sánh Tính Năng Lệnh Điều Kiện Chứng Khoán
## Comparative Analysis of Conditional Order Features: SSI, TCBS, VPS, and VNDIRECT

**Research Date:** October 2025
**Author:** Comprehensive Market Research
**Focus:** Conditional order (lệnh điều kiện) features across major Vietnamese securities companies

---

## Executive Summary

This document provides a comprehensive analysis of conditional order features offered by four major Vietnamese securities companies: SSI Securities Corporation, TCBS (Techcombank Securities), VPS Securities, and VNDIRECT. Conditional orders are advanced trading tools that allow investors to automate trading strategies by setting predefined conditions that trigger order execution without requiring constant market monitoring.

### Key Findings

1. **SSI** leads in variety with 6+ conditional order types for derivatives plus comprehensive equity conditional orders
2. **TCBS** emphasizes 24/7 availability with multi-session (up to 30 days) conditional order validity
3. **VPS** offers 4 core conditional order types with focus on automated risk management
4. **VNDIRECT** provides 24/7 conditional orders with same-day validity and multi-platform support

All platforms share the common goal of enabling automated trading while each differentiates through unique features and execution capabilities.

---

## 1. SSI Securities Corporation (SSI)

### Overview
SSI provides the most comprehensive conditional order system in the Vietnamese market, available through their SSI iBoard platform (web and mobile app). SSI officially launched derivatives conditional orders on their iBoard platform in May.

### Conditional Order Types

#### For Basic Securities (Equity Trading)

**1. TCO (Time Conditional Order / Lệnh đặt trước ngày)**
- **Purpose:** Schedule orders 1 to many days in advance
- **Features:**
  - Predetermined quantity and price
  - Multi-day validity
  - Pre-market placement (from 4:30 PM previous day)
- **Use Case:** Planning trades in advance without daily monitoring

**2. PRO (Priority Order / Lệnh tranh mua bán)**
- **Purpose:** Maximize matching probability
- **Features:**
  - Highest matching capability
  - Optimized for quick execution
- **Use Case:** Competitive trading sessions with high volatility

**3. Stop Orders (Lệnh dừng)**
- **Two Variants:**
  - **Stop (Market Stop Order):** Market price execution with predetermined trigger price
  - **Stop Limit:** Limit price execution with predetermined trigger price
- **Features:**
  - Price-based triggers
  - Automatic activation
- **Use Case:** Risk management and loss prevention

**4. Trailing Stop (Lệnh xu hướng)**
- **Purpose:** Dynamic price tracking for optimal entry/exit
- **Features:**
  - Automatic price adjustment following market trends
  - Sells at peaks when market trends upward
  - Buys at bottoms when market trends downward
  - No manual monitoring required
- **Use Case:** Trend following strategies and profit maximization

#### For Derivatives Trading

**6 Types Available:** Up, Down, T.Up, T.Down, OCO, and Bull&Bear

**1. Up/Down Orders**
- **Purpose:** Stop orders activated by market condition changes
- **Features:**
  - Highly favored by derivatives traders
  - Directional triggers
- **Use Case:** Breakout and breakdown strategies

**2. OCO (One Cancels Other)**
- **Purpose:** Combined profit-taking and stop-loss
- **Features:**
  - Two orders linked (when one executes, the other cancels)
  - Position-closing at expected price with stop-loss protection
  - Typically used with open positions
- **Use Case:** Automated position management with defined risk/reward

**3. Bull & Bear Orders**
- **Purpose:** Combined profit-taking and stop-loss features
- **Features:**
  - Dual-direction protection
  - Market direction agnostic
- **Use Case:** Volatile market conditions

### System Characteristics

**Validity Rules:**
- Conditional orders valid for 1 trading day
- Orders placed during pre-market (4:30 PM previous day) effective for next trading day
- Daily renewal required for ongoing strategies

**Modification Rules:**
- Can only cancel/modify orders with "waiting for condition" status
- Once triggered, standard order modification rules apply
- No amendment on iBoard - must cancel and re-place

**Balance Checking:**
- No balance check at order placement time
- Cash and stock balance verified when activation conditions are met
- Allows flexible planning without immediate capital requirements

### Platform & Technical Details

**Platform:** SSI iBoard (Web + Mobile App)

**API:** FastConnect API
- Communication protocol for system integration
- Documentation: https://guide.ssi.com.vn/ssi-products/fastconnect-trading/api-specs
- Security: RSA + SHA256 signatures
- Authentication: Secret Key + JSON body
- Supports: Place/Amend/Cancel orders

**System Monitoring:**
- Condition checks at 8:30 AM and 1:00 PM
- Activates time conditional orders according to effective date
- Generates renewal orders as needed

### Benefits Summary

SSI's conditional order effectiveness focuses on:
1. **Profit Management:** Capturing optimal prices without constant monitoring
2. **Risk Management:** Quick stop-loss execution when market moves adversely
3. **Position Management:** Automated trading based on price targets

---

## 2. TCBS (Techcombank Securities)

### Overview
TCBS offers conditional order functionality through their TCInvest platform with emphasis on 24/7 availability and multi-session validity.

### Conditional Order Types

**Conditional Order 24/7 Feature**
- **Purpose:** Flexible order placement at any time
- **Features:**
  - Place orders any time of day
  - Valid for one or multiple trading sessions (up to 30 days)
  - Continuously sent to exchange when conditions met
  - Auto-execution until fully matched or expiration
- **Use Case:** Long-term automated trading strategies

**Stop Loss Orders**
- **Purpose:** Limit losses by automatic selling
- **Features:**
  - Price-based triggers
  - Automated risk management
- **Use Case:** Portfolio protection

**Periodic Orders**
- **Purpose:** Recurring order placement
- **Features:**
  - Scheduled execution
  - Regular interval trading
- **Use Case:** Dollar-cost averaging strategies

**Agreement Orders**
- **Purpose:** Special transaction types
- **Features:**
  - Pre-negotiated trades
- **Use Case:** Large block trades or special arrangements

### System Characteristics

**Validity:**
- Multi-session support (up to 30 days)
- Longest validity period among competitors
- Continuous monitoring and execution

**Order Status Types:**
- **Waiting for conditions:** Order in system but not sent to exchange
  - Effective date not reached
  - Price level not achieved
  - Buying power/assets insufficient
- **Active:** Conditions met, order sent to exchange
- **Can cancel/modify:** When in "waiting for conditions" status

**Order Management:**
- Comprehensive order status tracking
- Search by stock code, order type, status, placement time
- Centralized dashboard for all conditional orders

### Platform & Access

**Platform:** TCInvest (Mobile App + Web)

**API Documentation:**
- Developer portal: developers.tcbs.com.vn
- API PDF: static.tcbs.com.vn/oneclick/API.pdf
- Note: Full API documentation may require developer registration

**Third-Party Integration:**
- vnstock Python package provides unofficial API access
- Community-supported data retrieval

### Benefits Summary

TCBS focuses on:
1. **Flexibility:** 24/7 order placement
2. **Long-term Planning:** Up to 30-day validity
3. **Convenience:** Set and forget for extended periods

---

## 3. VPS Securities

### Overview
VPS Securities provides a focused set of conditional order types emphasizing automated risk management and trend following.

### Conditional Order Types

**1. Time-Contingent Order (TCO)**
- **Purpose:** Schedule trades in advance
- **Features:**
  - Specified quantity and price
  - Placement before trading sessions
  - Active from one to several days
  - Valid until fully matched or cancelled
- **Use Case:** Planned trading without daily intervention

**2. Stop Order**
- **Purpose:** Conditional pending orders with risk-based triggers
- **Features:**
  - Predetermined set price (execution price)
  - Activation price (trigger price)
  - Determined by investor risk tolerance
  - Automatic activation when market price moves favorably
  - Automatically pushed into system
- **Use Case:** Breakout trading and controlled entry

**3. Stop Loss / Take Profit Order**
- **Purpose:** Dual-purpose order for profit preservation and loss limitation
- **Features:**
  - Accompanies stock purchase orders
  - Conditions to sell securities
  - Preserves profits OR limits acceptable risk
  - Investor-defined parameters
- **Use Case:** Comprehensive position management

**4. Trailing Stop Order**
- **Purpose:** Dynamic price adjustment for optimal execution
- **Features:**
  - Prices automatically adjusted to follow market trends
  - Tracks upward/downward market movements
  - Achieves optimal price within expected range
  - No manual intervention required
- **Use Case:** Trend-following strategies with automated optimization

### System Characteristics

**Core Mechanism:**
- All orders require specific market conditions to trigger
- Automatic execution when conditions met
- Pre-planned strategy implementation without constant monitoring

**Activation Logic:**
- Market price monitoring
- Automatic trigger detection
- System push to exchange
- Standard order processing post-activation

### Platform & Access

**Platform:** VPS trading platform (Web + Mobile)

**API Documentation:**
- Limited public information available
- May require client access for API documentation

### Benefits Summary

VPS emphasizes:
1. **Simplicity:** Clear, well-defined order types
2. **Risk Management:** Strong focus on stop-loss and take-profit
3. **Automation:** Trend-following without manual tracking

---

## 4. VNDIRECT (VND)

### Overview
VNDIRECT provides conditional order functionality through their DBOARD platform with 24/7 availability and same-day validity focus.

### Conditional Order Types

**Conditional Orders 24/7**
- **Purpose:** Anytime order placement with automatic day-end closure
- **Features:**
  - 24/7 placement capability
  - Automatically closed at end of trading day
  - Requires daily renewal for ongoing strategies
- **Use Case:** Intraday automated trading

**Good-Till-Date (GTD) Multi-Day Orders**
- **Purpose:** Extended validity for limit orders
- **Features:**
  - Multi-day validity for limit orders
  - Professional trader feature
- **Use Case:** Patient limit order strategies

**BUY STOP / SELL STOP**
- **Purpose:** Conditional entry/exit at specific price levels
- **Features:**
  - Price-based triggers
  - Directional breakout trading
- **Use Case:** Breakout and breakdown strategies

**Trailing Stop**
- **Purpose:** Dynamic stop-loss with price tracking
- **Features:**
  - Follows market movement
  - Automatic price adjustment
  - Protects profits while allowing trend continuation
- **Use Case:** Profit protection in trending markets

**Chốt Lời / Cắt Lỗ (Take Profit / Cut Loss)**
- **Purpose:** Combined profit-taking and loss-cutting
- **Features:**
  - Dual condition order
  - Automatic execution at profit or loss levels
- **Use Case:** Complete position risk management

### System Characteristics

**Validity:**
- Same-day validity (automatic closure at day end)
- GTD orders for multi-day limit orders
- Daily renewal required for continuous strategies

**Platform Support:**
- DBOARD platform (Web + Mobile)
- Multiple asset class support
- Integrated technical analysis
- One-click fast orders

### Platform & Access

**Platform:** DBOARD

**Key Features:**
- Technical analysis broadcasting
- Stock filters
- Conditional orders
- One-click fast order execution
- Suitable for both novice and professional traders

**Other Platforms:**
- **PROTRADE:** Professional trader platform
- **DSTOCK:** Advanced trader platform

**API:**
- Open API mentioned for institutional clients
- White Labeling services available
- Market data API: finfo-api.vndirect.com.vn
- Contact required for trading API access

**Support:**
- Hotline: 1900 54 54 09
- Email: support@vndirect.com.vn

### Benefits Summary

VNDIRECT focuses on:
1. **Accessibility:** 24/7 order placement
2. **Simplicity:** Same-day validity reduces complexity
3. **Integration:** Combined with technical analysis tools

---

## Comparative Feature Matrix

| Feature | SSI | TCBS | VPS | VNDIRECT |
|---------|-----|------|-----|----------|
| **Order Types** | | | | |
| Time-Contingent Orders | ✅ TCO | ✅ 24/7 | ✅ TCO | ✅ GTD |
| Stop Loss | ✅ Stop | ✅ Stop Loss | ✅ Stop Loss | ✅ SELL STOP |
| Take Profit | ✅ (via Stop Limit) | ❌ | ✅ Take Profit | ✅ Chốt Lời |
| Trailing Stop | ✅ | ❌ | ✅ | ✅ |
| OCO (One Cancels Other) | ✅ (Derivatives) | ❌ | ❌ | ❌ |
| Priority/Competitive Orders | ✅ PRO | ❌ | ❌ | ❌ |
| Bull & Bear Orders | ✅ (Derivatives) | ❌ | ❌ | ❌ |
| **Validity Period** | | | | |
| Max Validity | 1 day (equity)<br/>1 day (derivatives) | Up to 30 days | Multiple days | 1 day<br/>(GTD: multiple days) |
| 24/7 Placement | ✅ (from 4:30 PM) | ✅ | ❓ | ✅ |
| **Technical Features** | | | | |
| API Available | ✅ FastConnect | ⚠️ Limited public docs | ⚠️ Limited info | ⚠️ Institutional only |
| API Documentation | Public | Restricted | Restricted | Contact required |
| Multi-Platform | ✅ iBoard (Web+Mobile) | ✅ TCInvest (Web+Mobile) | ✅ Web+Mobile | ✅ DBOARD (Web+Mobile) |
| **Order Management** | | | | |
| Modify Before Trigger | ✅ (must cancel/re-place) | ✅ | ❓ | ❓ |
| Modify After Trigger | ❌ | Standard rules | ❓ | ❓ |
| Balance Check Timing | At trigger time | At trigger time | ❓ | ❓ |
| Order Status Tracking | ✅ | ✅ Comprehensive | ❓ | ✅ |
| **Special Features** | | | | |
| Derivatives Support | ✅ 6 types | ✅ | ❌ | ❌ |
| Periodic Orders | ❌ | ✅ | ❌ | ❌ |
| Agreement Orders | ❌ | ✅ | ❌ | ❌ |
| Technical Analysis Integration | ✅ | ❓ | ❓ | ✅ |
| One-Click Orders | ❓ | ❓ | ❓ | ✅ |

**Legend:**
- ✅ = Confirmed available
- ❌ = Not available
- ⚠️ = Available with limitations
- ❓ = Information not available in research

---

## Detailed Feature Comparison

### 1. Order Variety and Sophistication

**Winner: SSI**
- Most comprehensive set of conditional orders
- Only platform with full derivatives conditional order support (6 types)
- Unique features: PRO (Priority Orders), Bull & Bear
- Both equity and derivatives coverage

**Runner-up: VPS**
- Well-rounded core set covering essential needs
- Strong stop-loss/take-profit integration
- Trailing stop support

### 2. Validity Period and Flexibility

**Winner: TCBS**
- Up to 30-day validity period (industry-leading)
- 24/7 placement with multi-session support
- Best for long-term automated strategies
- Continuous execution until fully matched or expired

**Runner-up: SSI**
- 24/7 placement (from 4:30 PM previous day)
- 1-day equity, 1-day derivatives validity
- Pre-market placement capability

### 3. API and Technical Integration

**Winner: SSI**
- Publicly documented FastConnect API
- Clear technical specifications
- RSA + SHA256 security
- Developer-friendly documentation at guide.ssi.com.vn

**Challenges for Others:**
- TCBS: API exists but documentation restricted
- VPS: Limited public API information
- VNDIRECT: API available for institutional clients only

### 4. User Experience and Accessibility

**Winner: VNDIRECT**
- Multi-platform support (DBOARD, PROTRADE, DSTOCK)
- Integrated technical analysis
- One-click fast orders
- Suitable for both novice and professional traders
- 24/7 placement

**Runner-up: SSI**
- Comprehensive iBoard platform
- Mobile and web support
- User-friendly interface

### 5. Risk Management Features

**Winner: VPS**
- Dedicated Stop Loss/Take Profit combined orders
- Clear risk-based order configuration
- Trailing stop for profit protection
- Simple, focused approach

**Runner-up: SSI**
- Multiple stop order variants
- OCO for derivatives
- Comprehensive risk tools across asset classes

### 6. Advanced Trading Features

**Winner: SSI**
- Derivatives conditional orders (unique in comparison)
- OCO implementation
- Bull & Bear orders
- Priority/competitive orders
- Most advanced feature set

**Runner-up: TCBS**
- Periodic orders for DCA strategies
- Agreement orders for special transactions
- Long-term validity for complex strategies

---

## Technical Implementation Analysis

### Execution Logic Patterns

All platforms follow similar execution patterns:

1. **Order Placement Phase**
   - User defines order parameters
   - System validates input
   - Order stored with "waiting for condition" status
   - No immediate balance check (most platforms)

2. **Monitoring Phase**
   - Continuous price monitoring
   - Scheduled condition checks (SSI: 8:30 AM, 1:00 PM)
   - Real-time trigger detection

3. **Activation Phase**
   - Condition met detection
   - Balance/asset verification
   - Order generation
   - Submission to exchange

4. **Execution Phase**
   - Standard order matching
   - Exchange processing
   - Execution confirmation

### Common Technical Challenges

Based on the research, platforms face similar challenges:

1. **Balance Timing**
   - When to check: placement vs. trigger time
   - SSI checks at trigger time (more flexible)
   - Allows planning without immediate capital

2. **Order Modification**
   - Limited modification capabilities
   - Most require cancel-and-replace pattern
   - Once triggered, standard order rules apply

3. **Multi-Day Coordination**
   - Daily renewal vs. persistent validity
   - TCBS leads with 30-day support
   - Others require daily renewal

4. **Condition Evaluation Frequency**
   - Real-time vs. scheduled checks
   - Trade-off between accuracy and system load
   - SSI uses hybrid approach (scheduled + real-time)

---

## API and Integration Comparison

### SSI FastConnect API (Most Documented)

**Strengths:**
- Public documentation
- Clear API specifications
- Well-defined endpoints
- Security model documented (RSA + SHA256)

**Key Endpoints (Inferred):**
- Place conditional order
- Amend conditional order
- Cancel conditional order
- Query conditional order status

**Authentication:**
- Secret Key based
- JSON body signing
- Signature verification

**Documentation:**
- https://guide.ssi.com.vn/ssi-products/fastconnect-trading/api-specs
- https://guide.ssi.com.vn/ssi-products/general-information

### TCBS API (Restricted Access)

**Known Resources:**
- Developer portal: developers.tcbs.com.vn
- API PDF: static.tcbs.com.vn/oneclick/API.pdf

**Challenges:**
- Documentation requires registration
- Limited public information
- Third-party libraries (vnstock) provide partial access

**Recommendation:**
- Contact TCBS directly for API access
- Review vnstock library for reference implementation

### VPS API (Limited Public Info)

**Status:**
- API existence not confirmed in public sources
- May require client access
- No public developer documentation found

**Recommendation:**
- Contact VPS directly for API information
- Request developer documentation

### VNDIRECT API (Institutional Focus)

**Known Resources:**
- White Labeling services mention API
- Market data API: finfo-api.vndirect.com.vn
- Open API referenced for institutional clients

**Access:**
- Contact: support@vndirect.com.vn or 1900 54 54 09
- Appears focused on institutional/corporate clients
- Public trading API documentation not available

**Recommendation:**
- Inquire about API access requirements
- Check institutional client eligibility

---

## Strengths and Weaknesses Analysis

### SSI Securities

**Strengths:**
- Most comprehensive order type coverage
- Only platform with full derivatives support
- Public API documentation
- Advanced features (OCO, Bull & Bear, Priority Orders)
- Pre-market placement capability
- Strong technical infrastructure

**Weaknesses:**
- 1-day validity requires daily renewal
- Cannot amend orders on iBoard (must cancel/re-place)
- More complex for beginners
- Scheduled condition checks may miss immediate opportunities

**Best For:**
- Active derivatives traders
- Professional traders needing advanced features
- Developers requiring API integration
- Multi-asset strategies

### TCBS (Techcombank Securities)

**Strengths:**
- Industry-leading 30-day validity period
- 24/7 order placement
- Comprehensive order management dashboard
- Multi-session support
- Periodic orders for DCA strategies
- Search and filter capabilities

**Weaknesses:**
- Fewer order type varieties vs. SSI
- No derivatives conditional orders
- Limited public API documentation
- No trailing stop support

**Best For:**
- Long-term investors
- Dollar-cost averaging strategies
- Passive investment approaches
- Users wanting "set and forget" functionality

### VPS Securities

**Strengths:**
- Focused, clear order types
- Strong stop-loss/take-profit integration
- Trailing stop support
- Simplified approach (easier to understand)
- Good risk management tools

**Weaknesses:**
- No derivatives conditional orders
- Limited public information
- Smaller variety of order types
- No API documentation available publicly
- Less differentiation from competitors

**Best For:**
- Risk-conscious traders
- Trend-following strategies
- Users wanting simplicity
- Stop-loss focused trading

### VNDIRECT

**Strengths:**
- 24/7 order placement
- Multi-platform ecosystem (DBOARD, PROTRADE, DSTOCK)
- Integrated technical analysis
- One-click fast orders
- Suitable for all skill levels
- GTD multi-day limit orders
- Strong mobile experience

**Weaknesses:**
- Same-day validity (auto-close at day end)
- No derivatives conditional orders
- API access restricted to institutional clients
- Requires daily renewal for ongoing strategies
- Limited order type variety

**Best For:**
- Retail investors
- Technical analysis users
- Mobile-first traders
- Users wanting integrated analysis + trading
- Intraday strategies

---

## Recommendations for VND Platform

Based on this competitive analysis, here are recommendations for VND's conditional order implementation:

### Priority 1: Core Conditional Order Types (Must-Have)

Implement these essential order types that are standard across all competitors:

1. **Time-Contingent Orders (TCO)**
   - Allow scheduling orders 1-N days in advance
   - Support pre-market placement
   - Provide flexible validity period (1-30 days)

2. **Stop Loss Orders**
   - Market stop (execute at market price when trigger hit)
   - Stop limit (execute at limit price when trigger hit)
   - Configurable trigger price

3. **Take Profit Orders**
   - Automatic profit-taking at target price
   - Can be combined with stop-loss for complete position management

4. **Trailing Stop Orders**
   - Dynamic stop-loss that follows price movements
   - Percentage-based or fixed-point trailing
   - Protects profits while allowing trend continuation

### Priority 2: Advanced Features (Competitive Differentiation)

Implement these to match or exceed SSI's capabilities:

5. **OCO (One Cancels Other)**
   - Critical for professional traders
   - Links two orders (profit target + stop loss)
   - When one executes, other automatically cancels
   - Particularly valuable for derivatives (if VND expands to derivatives)

6. **Bracket Orders**
   - Combines entry + profit target + stop loss in one order
   - Automates complete trade lifecycle
   - Reduces execution risk

7. **Conditional Order Chaining**
   - Allow one order to trigger another
   - Support complex multi-leg strategies
   - Example: When position opens, automatically place OCO

### Priority 3: Validity and Flexibility (Learn from TCBS)

8. **Extended Validity Periods**
   - Support up to 30 days like TCBS
   - Reduce need for daily renewal
   - Better user experience for long-term strategies

9. **24/7 Order Placement**
   - Accept orders any time
   - Queue for next trading session
   - Match TCBS and VNDIRECT capabilities

10. **Multi-Session Orders**
    - Orders that persist across multiple trading days
    - Automatic renewal until fully matched or expired
    - Reduces manual intervention

### Priority 4: Technical Infrastructure

11. **Robust API**
    - Follow SSI's example with public API documentation
    - RESTful API design
    - WebSocket support for real-time updates
    - Comprehensive authentication (OAuth 2.0 or similar)
    - Clear error handling and status codes

12. **Real-Time Condition Monitoring**
    - Move beyond scheduled checks (SSI's limitation)
    - Real-time price monitoring with low latency
    - Event-driven architecture
    - Consider cloud-native scaling

13. **Balance Management**
    - Check balance at trigger time (SSI approach)
    - Allow planning without immediate capital
    - Pre-validation option for user awareness
    - Clear error messages when balance insufficient

### Priority 5: User Experience

14. **Order Templates**
    - Save common conditional order configurations
    - Quick re-use of strategies
    - Reduce setup time

15. **Backtesting Integration**
    - Allow users to test conditional order strategies
    - Show historical performance
    - Build confidence before live trading

16. **Order Modification Flexibility**
    - Allow in-place editing (improve on SSI's cancel/re-place)
    - Preserve order queue position when possible
    - Partial modification support

17. **Comprehensive Order Dashboard**
    - TCBS-style management interface
    - Filter by status, type, symbol, date
    - Bulk operations
    - Export functionality

18. **Mobile-First Design**
    - Follow VNDIRECT's strong mobile experience
    - Touch-optimized order entry
    - Push notifications for triggers and executions
    - Offline order queuing

### Priority 6: Risk Management Tools

19. **Portfolio-Level Risk Controls**
    - Maximum daily loss limits
    - Position size limits
    - Concentration limits
    - Auto-liquidation rules

20. **Smart Notifications**
    - When conditions are approaching
    - When orders are triggered
    - When orders are executed
    - When orders fail (with clear reasons)

### Technical Architecture Recommendations

**Database Design:**
```
Conditional Orders Table:
- order_id (PK)
- user_id (FK)
- symbol
- order_type (ENUM: TCO, STOP_LOSS, TAKE_PROFIT, TRAILING_STOP, OCO, etc.)
- direction (BUY/SELL)
- quantity
- trigger_conditions (JSON: price, time, volume, indicator-based)
- execution_params (JSON: limit_price, market_price, time_in_force)
- validity_period (start_date, end_date)
- status (ENUM: PENDING, ACTIVE, TRIGGERED, EXECUTED, CANCELLED, EXPIRED)
- linked_order_id (for OCO, brackets)
- created_at
- updated_at
- triggered_at
- executed_at
```

**Monitoring Service:**
- Event-driven architecture (Apache Kafka or similar)
- Real-time price stream processing
- Distributed condition evaluation
- High availability setup

**API Design Principles:**
- RESTful for CRUD operations
- WebSocket for real-time updates
- GraphQL option for complex queries
- Rate limiting and throttling
- Comprehensive error responses

**Security Considerations:**
- Multi-factor authentication for API access
- Request signing (HMAC-SHA256 or RSA)
- IP whitelisting option
- Audit logging for all order operations
- Encryption at rest and in transit

---

## Implementation Roadmap for VND

### Phase 1: Foundation (Months 1-3)
**Goal:** Basic conditional order infrastructure

**Deliverables:**
- Database schema and migration
- Core monitoring service
- Basic API endpoints
- Stop Loss and Take Profit orders
- Time-Contingent Orders
- Simple web interface

**Success Metrics:**
- 99.9% uptime
- <100ms condition evaluation latency
- Support 1000 concurrent conditional orders

### Phase 2: Advanced Orders (Months 4-6)
**Goal:** Competitive feature parity

**Deliverables:**
- Trailing Stop orders
- OCO orders
- Bracket orders
- Extended validity (up to 30 days)
- Enhanced API with WebSocket
- Mobile app integration

**Success Metrics:**
- 95% user satisfaction
- 50% of active users using conditional orders
- <1% order execution errors

### Phase 3: Differentiation (Months 7-9)
**Goal:** Exceed competitor capabilities

**Deliverables:**
- Order templates
- Backtesting integration
- Smart notifications
- Portfolio-level risk controls
- Advanced order dashboard
- Public API documentation

**Success Metrics:**
- Industry-leading features
- 10% month-over-month user growth
- Positive reviews highlighting conditional orders

### Phase 4: Optimization (Months 10-12)
**Goal:** Performance and scale

**Deliverables:**
- Real-time monitoring optimization
- Auto-scaling infrastructure
- Advanced analytics
- Machine learning for order suggestions
- International language support

**Success Metrics:**
- Support 10,000+ concurrent conditional orders
- <50ms median latency
- 99.99% uptime

---

## Competitive Positioning Strategy

### Differentiation Opportunities

**1. Superior API Experience (vs. All Competitors)**
- Make API public and well-documented (SSI model)
- Exceed SSI with modern API design (GraphQL, comprehensive WebSocket)
- Developer community building
- Open-source SDKs (Python, JavaScript, Java)

**2. Intelligent Order Assistance (Unique)**
- ML-powered order suggestions based on user patterns
- Risk assessment before order placement
- Success probability indicators
- Market condition warnings

**3. Advanced Validity Management (vs. SSI, VNDIRECT)**
- Match or exceed TCBS's 30-day validity
- Add "Good Till Cancelled" (GTC) option
- Smart renewal with user notifications
- Calendar-based order management

**4. Unified Multi-Asset Support (Future)**
- When derivatives expand, comprehensive support like SSI
- Single interface for all asset classes
- Cross-asset conditional strategies
- Portfolio-wide automation

**5. Education and Support (vs. All)**
- Interactive tutorials
- Strategy library with examples
- Paper trading for conditional orders
- Live webinars and support

### Marketing Messages

**vs. SSI:**
- "Simpler, more intuitive, with equal power"
- "Modern API designed for developers"
- "Real-time monitoring, not scheduled checks"

**vs. TCBS:**
- "All the flexibility of 30-day orders, with more order types"
- "Advanced features without complexity"
- "Professional tools for serious traders"

**vs. VPS:**
- "Complete conditional order suite, not just basics"
- "Advanced risk management and automation"
- "API-first approach for integration"

**vs. VNDIRECT:**
- "Beyond same-day: Multi-day strategies made easy"
- "Professional-grade conditional orders for everyone"
- "More order types, more possibilities"

---

## Risk Considerations and Mitigation

### Technical Risks

**1. System Latency**
- **Risk:** Delayed condition evaluation causes missed opportunities or poor execution
- **Mitigation:**
  - Real-time event-driven architecture
  - Distributed processing
  - Performance SLAs and monitoring
  - Graceful degradation

**2. High Load During Market Volatility**
- **Risk:** System overload when many conditions trigger simultaneously
- **Mitigation:**
  - Auto-scaling infrastructure
  - Queue-based processing
  - Priority ordering (market orders first)
  - Load testing and capacity planning

**3. API Security**
- **Risk:** Unauthorized access or order manipulation
- **Mitigation:**
  - Multi-layer authentication
  - Request signing and validation
  - Rate limiting
  - Real-time fraud detection

### Business Risks

**4. User Error and Misconfiguration**
- **Risk:** Users set up orders incorrectly, leading to unintended trades
- **Mitigation:**
  - Confirmation dialogs for high-risk orders
  - Order preview before submission
  - Paper trading mode
  - Educational resources
  - Clear error messages

**5. Regulatory Compliance**
- **Risk:** Conditional orders may violate trading regulations
- **Mitigation:**
  - Consult with State Securities Commission (SSC)
  - Implement required safeguards
  - Audit trail for all orders
  - Regular compliance reviews

**6. Market Maker Dependencies**
- **Risk:** Exchange limitations affect conditional order execution
- **Mitigation:**
  - Understand exchange capabilities
  - Clear communication to users about limitations
  - Fallback mechanisms
  - Regular exchange coordination

### Operational Risks

**7. 24/7 Support Requirements**
- **Risk:** Users need help outside business hours
- **Mitigation:**
  - Comprehensive self-service documentation
  - Chatbot for common questions
  - Escalation procedures
  - On-call support team

**8. Data Integrity**
- **Risk:** Order data corruption or loss
- **Mitigation:**
  - Database replication
  - Regular backups
  - Transaction logging
  - Recovery procedures

---

## Conclusion

The Vietnamese securities market shows strong conditional order adoption across all major platforms, with each firm offering unique approaches:

- **SSI** leads in sophistication and variety, particularly for derivatives traders
- **TCBS** excels in long-term flexibility with 30-day validity
- **VPS** focuses on core risk management features with clarity
- **VNDIRECT** emphasizes accessibility and integration

For **VND** to compete effectively, the recommended strategy is:

1. **Match Core Features:** Implement all standard conditional order types (TCO, Stop Loss, Take Profit, Trailing Stop)
2. **Exceed on API:** Create the best developer experience with public, comprehensive documentation
3. **Match TCBS Validity:** Support up to 30-day order validity
4. **Add Unique Features:** OCO, bracket orders, and intelligent order assistance
5. **Optimize UX:** Make complex orders simple through excellent interface design
6. **Build for Scale:** Real-time monitoring, cloud-native architecture, high availability

The market opportunity is significant, as conditional orders represent a key differentiator for attracting professional traders while also serving retail investors who want to automate their strategies.

**Success will require:**
- Strong technical execution
- Comprehensive testing
- Excellent documentation
- User education
- Regulatory compliance
- Continuous improvement based on user feedback

By implementing these recommendations, VND can build a conditional order system that matches or exceeds competitors while providing unique value through superior API, intelligent assistance, and modern architecture.

---

## Appendix A: Order Type Glossary

**Time-Contingent Order (TCO) / Lệnh đặt trước ngày:**
Order placed in advance to execute on a future trading session

**Stop Loss / Lệnh cắt lỗ:**
Order to sell when price falls to a predetermined level, limiting losses

**Take Profit / Lệnh chốt lời:**
Order to sell when price rises to a target level, securing profits

**Trailing Stop / Lệnh xu hướng:**
Stop-loss that automatically adjusts as price moves favorably

**OCO (One Cancels Other) / Lệnh hủy đối ứng:**
Two linked orders where execution of one automatically cancels the other

**Bracket Order:**
Entry order with attached profit target and stop-loss

**Good Till Date (GTD):**
Order valid until a specified date

**Good Till Cancelled (GTC):**
Order valid until explicitly cancelled by user

---

## Appendix B: Research Methodology

**Data Sources:**
- Official company websites and support documentation
- Web searches for technical documentation and API specifications
- Developer forums and community resources
- User guides and tutorials

**Research Date:** October 2025

**Limitations:**
- Some API documentation not publicly available
- Technical details inferred from user-facing documentation
- Real-world performance metrics not available
- Actual implementation details may vary from documented features

**Validation:**
- Cross-referenced multiple sources
- Focused on officially confirmed features
- Noted uncertainties with "❓" in comparison tables
- Separated confirmed facts from inferences

---

## Appendix C: Contact Information for Further Research

**SSI Securities:**
- API Documentation: https://guide.ssi.com.vn/ssi-products/fastconnect-trading/api-specs
- Website: https://www.ssi.com.vn

**TCBS (Techcombank Securities):**
- Developer Portal: developers.tcbs.com.vn
- Support: help.tcbs.com.vn
- Website: https://www.tcbs.com.vn

**VPS Securities:**
- Website: https://www.vps.com.vn
- English FAQ: https://www.vps.com.vn/en/retail-sales/support/frequently-asked-questions

**VNDIRECT:**
- Support: support@vndirect.com.vn
- Hotline: 1900 54 54 09
- Support Center: support.vndirect.com.vn
- Website: https://www.vndirect.com.vn

---

**Document Version:** 1.0
**Last Updated:** October 29, 2025
**Next Review:** January 2026
