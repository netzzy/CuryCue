# ADR 0005: Change Governance for Critical Infrastructure

Status: Accepted

Date: 2026-05-31

## Context

CuryCue runs live-show/media-server workflows. Small-looking changes can affect
cue execution, routing, DB persistence, hidden TD branches, or operator behavior.

## Decision

Treat CuryCue as critical infrastructure. For major bug fixes, features, and
refactors, map blast radius explicitly, update `docs/changelog.md`, and add or
update ADRs when architecture or operating rules change.

## Consequences

- Reliability beats brevity during risk assessment.
- Plans must include user problem, target experience, design decision,
  architecture impact, and systematically traced scope.
- Documentation changes are part of the implementation, not cleanup.
- If a risk cannot be eliminated, document the assumption and verification path.

