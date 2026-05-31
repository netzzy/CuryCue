# ADR 0015: Global Hotkeys and Command Routing

Status: Accepted

Date: 2026-05-31

## Context

Global keyboard handling lives under `/project1/CuryCue/GLOBAL_UI`. It reads
keyboard CHOP state, command tables, devices, actors, modifiers, and methods.

## Decision

Hotkeys are command routing, not business logic. A hotkey should resolve to a
device or actor method and then use that subsystem's public action path. Show
controls must route into the cue engine. UI and output controls must route into
their owning UI/output components. Hotkey tables must remain auditable and not
hide one-off logic inside the key processor.

## Consequences

- Hotkey edits can affect live show operation and need the same blast-radius
  review as UI button changes.
- Device, actor, and method names are runtime contracts; rename changes must
  trace command tables.
- Modifier handling must be tested for false positives, not only for the happy
  key combination.

## Verification Notes

After hotkey changes, verify the edited key combination, nearby modifier
variants that should not trigger, and the target subsystem state.

