# ADR 0007: Export Modes and Active Field Rendering

Status: Accepted

Date: 2026-05-31

## Context

Resolved cue values reach TouchDesigner parameters through active fields and
renderer DAT/CHOP outputs. Numeric and text values take different paths.

## Decision

`ACTIVE_FIELDS` remains the canonical runtime value set. Numeric values are
rendered through `ActiveFloatParsRender` for CHOP export or direct writes in
ValueExport mode. Text values are preserved separately and written through the
text-aware callback/write path. Export mode changes must not change the resolved
cue state; they only change how that state is pushed back into TD.

## Consequences

- Channel names derived from full parameter paths are part of the export
  contract.
- Export changes must preserve text parameters and not assume all values are
  floats.
- Disabled/no-export mode is a valid operator workflow for manual adjustment and
  cue storage.

## Verification Notes

For export-related changes, verify ChopExport, ValueExport, and disabled export
against the same cue. Include at least one numeric parameter and one text
parameter if the edited path can affect text handling.

