# ADR 0012: Content Preset Timeline and Side-Panel Contract

Status: Accepted

Date: 2026-05-31

## Context

Active content presets can expose internal UI panels and timeline controls in
the show-mode side panel. Not every active module has the same internal
structure.

## Decision

Side-panel content integration must be tolerant. A preset may have an
`AnimationTimeControl`, custom panel UI, both, or neither. Timeline widgets may
control play, stop, rewind, and scrub only when the expected internal component
exists. Missing timeline or rollover helpers should not break the rest of show
mode.

## Consequences

- Content module discovery must handle active modules with incomplete optional
  UI/timeline contracts.
- Side-panel errors are operator-facing show risk because they share runtime
  with cue execution.
- Preset inner content may be cook-gated, so widgets must handle waking state.

## Verification Notes

Verify side-panel behavior with an active preset that has `AnimationTimeControl`,
one without it, and one whose inner content has just been armed or disarmed.

