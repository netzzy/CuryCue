# ADR 0014: Operator Menu and Project Shortcuts

Status: Accepted

Date: 2026-05-31

## Context

The operator-facing menu layer combines shared CuryCue callbacks with
project-local callbacks and table rows. Some local callbacks open panes,
parameters, output windows, or project control surfaces through global shortcuts.

## Decision

Treat operator menus as a show-control surface, not decoration. Shared menu
behavior belongs in the CuryCue menu callbacks. Project-local callbacks and menu
tables may reference local shortcuts, but each referenced OP, shortcut, and
callback must be verified in the live patch before editing or relying on it.
Legacy project references in menu files are allowed only as dormant/archive
entries, not as assumed active architecture.

## Consequences

- Menu changes can affect live operation even when they do not touch cue code.
- Top-menu table rows and callback functions must be kept in sync.
- Broken local shortcut references should degrade to obvious no-op/error
  reporting, not silent operator confusion.
- Do not encode content-specific scene assumptions in menu ADRs.

## Verification Notes

After menu changes, open the menu, trigger edited callbacks, verify target panes
or parameters open correctly, and check textport errors.

