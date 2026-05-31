# ADR 0013: Operational Debugging and Live Verification

Status: Accepted

Date: 2026-05-31

## Context

CuryCue is debugged inside a live TouchDesigner process. Static code checks are
not enough because runtime DATs, cooking state, panel widgets, exports, and DB
rows interact.

## Decision

Use the `twozero_td` MCP workflow for live verification. Start with
`td_list_instances`, inspect scoped networks and DATs, clear/read textport when
reproducing errors, and check relevant subtree errors after changes. Restore a
known safe runtime state after behavioral tests when the test changed the
current cue or UI mode.

## Consequences

- Do not declare TD behavior fixed from source edits alone.
- Prefer scoped MCP inspection before full project parses unless the task needs
  whole-project reference analysis.
- Test notes should identify final runtime state when it matters to operators.

## Verification Notes

For show-critical changes, verify live current cue, active evaluators, output or
export state, UI mode, and textport/log errors. Record unresolved risks in the
changelog or relevant ADR when they remain.

