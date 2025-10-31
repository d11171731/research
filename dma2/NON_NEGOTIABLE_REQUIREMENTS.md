# DMA System - Non-Negotiable Requirements

## Overview
These are the **absolute non-negotiable requirements** for the DMA (Direct Market Access) trading system. These constraints cannot be compromised and drive all architectural decisions.

---

## 1. Ultra-Low Latency + Zero GC in Critical Path

**Cannot change**: Sub-100μs order latency target

**Why**: DMA systems compete in microseconds. If latency exceeds ~150-200μs, you're commercially non-viable.

**Implications**:
- Must use off-heap memory, object pooling, pre-allocation
- Lock-free data structures mandatory
- Single-threaded event loops
- NO blocking I/O, NO locks, NO allocations in hot path

---

## 2. Inline Pre-Trade Risk Management

**Cannot change**: Risk checks MUST happen before orders reach exchange

**Why**: Regulatory requirement (SEC Rule 15c3-5, MiFID II)

**Implications**:
- Risk engine must be < 10μs (can't add significant latency)
- Cannot skip or make async for speed
- Must validate: position limits, order size, credit limits, duplicate orders

---

## 3. Co-location/Bare Metal Deployment

**Cannot change**: Must be physically close to exchange

**Why**: Network latency to exchange must be < 500μs. Cloud adds 1-5ms+ latency

**Implications**:
- Cloud deployment (AWS/Azure) is NOT viable for production
- Must pay for co-location rack space near exchanges
- Higher infrastructure costs

---

## 4. Deterministic Architecture

**Cannot change**: Predictable, consistent latency (not just "fast average")

**Why**: p99 latency matters more than average. A single 10ms spike can cause major loss

**Implications**:
- Must use CPU pinning, NUMA tuning
- Kernel bypass networking
- Disable CPU frequency scaling, power management

---

## The Core Paradox

**You must achieve both extreme speed AND comprehensive risk checking simultaneously.**

This drives every architectural decision:
- Modularization strategy
- Technology choices
- Deployment strategy
- Integration patterns

---

## What CAN Be Changed

Everything else is negotiable:
- Specific frameworks (Aeron vs Chronicle vs custom)
- Number of modules/microservices
- Monitoring tools
- Programming language for non-critical components
- Database choices for back-office systems
- UI/API technologies

But the four core requirements above are immutable constraints that define the system's viability.
