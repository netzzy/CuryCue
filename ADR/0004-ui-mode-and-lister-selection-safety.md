# ADR 0004: UI Mode and Lister Selection Safety

Status: Accepted

Date: 2026-05-31

## Context

The TD 2025 upgrade exposed that hidden or non-cooking lister widgets can lose
promoted `SelectRow()` methods while their wrapper parameters still exist. A
failed hidden-list sync blocked later cue selection.

## Decision

Lister selection sync must update wrapper selection state first and call visual
`SelectRow()` only after checking the widget is in a cooking parent chain. UI mode
switches may schedule selection sync one frame later because lister init can
clear state while waking.

## Consequences

- Do not call `SelectRow()` directly from project callbacks.
- Guard hidden/dormant UI branches as first-class runtime states.
- Any future listCOMP change must test Show, Edit, and Fixtures modes.
- Cue selection code must release blocking flags with `try/finally`.

