# ADR 0003: Content Preset Routing and Cook Gating

Status: Accepted

Date: 2026-05-31

## Context

The content preset system under `/project1/Content` is alpha but actively used
beside the core cue system. It controls projector, LED, laser, timeline, and
side-panel behavior.

## Decision

Presets are outer `ContentPreset` COMPs with optional inner content containers.
The outer layer stays available for control and registration. The inner layer may
be cook-gated by `Activefade`, `Armed`, and arming mode. Routing is driven by
`PresetsRoutingTable`, which maps active preset outputs into compositor
parameters.

## Consequences

- Changes to content activation can affect performance, routing, side-panel UI,
  and cue exports at the same time.
- Hidden or uncooked inner content can have stale state after reload.
- Route edits must verify compositor parameter strings and final `/project1/LED`
  and `/project1/PROJ1` outputs.
- Preset timeline widgets must tolerate active modules without expected timeline
  children.

