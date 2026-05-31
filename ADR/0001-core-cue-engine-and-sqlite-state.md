# ADR 0001: Core Cue Engine and SQLite State

Status: Accepted

Date: 2026-05-31

## Context

CuryCue is a live TouchDesigner cue-control system. Runtime cue state, fixture
registration, parameter inheritance, fade evaluation, and exports all converge
inside `/project1/CuryCue`.

## Decision

`/project1/CuryCue` remains the authoritative cue engine. SQLite is the active
persistence layer, even though some class and parameter names still say MySQL.
Cues store sparse parameter changes; runtime load expands them into inherited
active fields. Cue execution goes through `CuryCueClass`, `QClass`, render
DAT/CHOP outputs, then CHOP export or direct parameter writes.

## Consequences

- Do not bypass the cue engine for show-critical state changes.
- Any DB schema or write-path change must trace SQLite rows, connector reload,
  inherited cue values, active fields, render outputs, and export behavior.
- Stale DB fixture paths are expected operational risk; code must guard
  unresolved `op(path)` lookups.
- Changelog entries for DB changes must include migrations.

