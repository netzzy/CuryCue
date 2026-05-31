# ADR 0017: Archive and Deprecated Code Policy

Status: Accepted

Date: 2026-05-31

## Context

The repository contains deprecated source folders and inherited callback
references from older projects. Some names remain useful as historical context,
but they are not automatically active architecture.

## Decision

Treat `SRC/.deprecated` and legacy-looking callback references as archive
material until a live TD reference, source import, or runtime callback proves
they are active. Do not revive deprecated code to solve a current issue unless
the live patch depends on it and the dependency has been traced.

## Consequences

- Architecture docs should not describe archived systems as current behavior.
- Searches must include deprecated code when investigating references, but
  conclusions must separate active runtime paths from archive paths.
- Removing or moving archive code still needs a reference scan because TD
  projects can hold string-based references.

## Verification Notes

Before changing archived code, search source, live DATs, parameter strings, and
TD references. If no active reference exists, document it as archive-only.

