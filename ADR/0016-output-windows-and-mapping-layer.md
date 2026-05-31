# ADR 0016: Output Windows and Mapping Layer

Status: Accepted

Date: 2026-05-31

## Context

CuryCue's final visible output passes through top-level output and mapping
components. Operator controls can open output windows, adjust mapping/keystone
tools, and route final TOPs to displays.

## Decision

Treat output windows and mapping as a separate operational boundary from cue
logic and content presets. Cue/content systems may feed final output TOPs, but
window open/close behavior, mapping tools, monitor selection, and output
container parameters belong to the output layer. Do not mix content-specific
behavior into this contract.

## Consequences

- Output-layer changes can break the show while cue execution remains correct.
- Window state, monitor routing, mapping parameters, and final TOP outputs must
  be verified together.
- Menu callbacks that open windows or mapping tools are part of this blast
  radius.

## Verification Notes

After output-layer changes, verify final output TOPs, relevant window open/close
controls, mapping tool access, and textport/errors.

