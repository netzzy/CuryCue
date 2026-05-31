# ADR 0009: Database Write Paths and Derived Cue Values

Status: Accepted

Date: 2026-05-31

## Context

Cues store sparse parameter rows. Runtime cue data includes derived values
inherited from previous cues or fixture defaults, and those derived values can
become stored rows when edited.

## Decision

SQLite write paths must go through the existing table edit and fixture utility
layers. Derived cue values are runtime projections until an edit/store operation
creates or replaces the corresponding `cue_float_data` row. After writes, the
system must reload from DB, rebuild derived values, refresh render DATs/CHOPs,
and restore current cue state.

## Consequences

- `id=-1` and `is_derived=True` values must not be treated as existing DB rows.
- `REPLACE INTO` behavior can overwrite rows because of unique constraints.
- Any schema or write-path change must document migrations in
  `docs/changelog.md`.

## Verification Notes

Verify editing an existing cue parameter, storing a derived parameter, deleting
a parameter, and reloading from DB. Confirm the same cue resolves identical
values after reload.

