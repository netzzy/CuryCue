# ADR 0010: Fixture Registration and Drag-Drop Contract

Status: Accepted

Date: 2026-05-31

## Context

Operators become controllable only after fixture registration. Parameters are
registered separately and depend on the fixture row.

## Decision

The supported registration flow is fixture first, parameters second. Drag/drop
and fixture utilities should reject parameter registration when the parent
fixture is missing. DB fixture paths may be absolute paths or shortcut-derived
paths, but runtime export and UI code must tolerate stale paths that no longer
resolve to a TD OP.

## Consequences

- Do not add parameter rows for unknown fixtures as a convenience shortcut.
- Path normalization and shortcut resolution are part of fixture loading blast
  radius.
- Missing OPs should degrade to guarded no-ops, not crash show execution.

## Verification Notes

Verify adding a fixture, adding a parameter for that fixture, attempting a
parameter-first drop, and loading a DB row whose target OP is missing.

