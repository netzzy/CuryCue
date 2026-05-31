# ADR 0011: Frame Bind and Show Control Shortcuts

Status: Accepted

Date: 2026-05-31

## Context

Operators can trigger cues through UI clicks, GoNext/GoPrev methods, keyboard
shortcuts, linked cues, and frame-bind autocue logic.

## Decision

All show-control entry points must converge on the cue engine's cue-change
methods. Frame-bind logic may observe timeline frame ranges and trigger the next
cue, but it must respect current cue state and the same execution path used by
manual show controls.

## Consequences

- Shortcut changes must be tested as show-critical behavior.
- Frame-bind changes can affect automated cue timing and linked-cue chains.
- UI affordances and callable methods should remain equivalent from the cue
  engine's perspective.

## Verification Notes

Verify mouse cue selection, GoNext, GoPrev, relevant keyboard shortcuts, linked
cue completion, and frame-bind triggering when edited code touches show-control
logic.

