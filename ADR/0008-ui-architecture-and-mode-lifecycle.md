# ADR 0008: UI Architecture and Mode Lifecycle

Status: Accepted

Date: 2026-05-31

## Context

`/project1/CuryCueUI` coordinates Show, Edit, and Fixtures modes while
`ServerUI`, `ServerShowModeSideUI`, and bottom panels provide project-specific
operator surfaces.

## Decision

Mode switching remains owned by `CuryCueUIClass`. Each mode branch may be hidden,
display-disabled, or cooking-disabled while still holding state that must be
correct when the branch wakes. UI callbacks should route show-critical actions
to `/project1/CuryCue` and keep visual widgets synchronized as a side effect,
not as the source of cue truth.

## Consequences

- Hidden UI branches are runtime states, not dead code.
- Show mode must stay optimized for safe execution; Edit and Fixtures mode can
  expose mutating controls.
- Server-side custom UI and side-panel widgets are adjacent blast radius for UI
  mode changes.

## Verification Notes

After UI lifecycle changes, switch Show -> Edit -> Fixtures -> Show and verify
cue selection, selected rows, side panel state, and textport errors.

