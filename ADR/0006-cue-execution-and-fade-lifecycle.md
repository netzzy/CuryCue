# ADR 0006: Cue Execution and Fade Lifecycle

Status: Accepted

Date: 2026-05-31

## Context

Show-critical cue changes pass through `/project1/CuryCue`. A cue selection can
change fixture parameters immediately, schedule fades, trigger linked cues, and
drive active field renderers.

## Decision

Cue execution must remain centralized in `CuryCueClass.RunCue()` and the
`QClass` evaluator lifecycle. UI, hotkeys, and frame-bind triggers should request
cue changes through the cue engine rather than writing active fields directly.
Completion behavior belongs to the evaluator callback path so linked cues fire
only after the relevant fade lifecycle finishes.

## Consequences

- Changes to fade creation or completion must trace `RunCue()`, `QClass`,
  `CallbackFromFader()`, active fields, and linked cue behavior.
- Cue selection guards such as `cueSwitchBlock` must always be released with
  `try/finally`.
- A no-op cue still matters: it must update current cue state even when no fade
  evaluators are created.

## Verification Notes

Test a normal cue, a blackout/no-op-style cue, a cue with active fades, and a
linked cue. Verify current cue parameters, active evaluators, exported values,
and textport errors.

