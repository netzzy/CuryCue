# ADR 0002: Source Mirrors and Live TouchDesigner DATs

Status: Accepted

Date: 2026-05-31

## Context

Python logic exists both as source mirrors under `SRC/` and as live DATs inside
the TouchDesigner patch. During active development or show operation, these can
diverge.

## Decision

Treat live DATs as runtime truth and `SRC/` files as the versioned source mirror.
Before editing TD logic, inspect the live DAT with MCP tools and read relevant
local TD docs in `Docs_MD/`. When a source mirror changes, confirm whether the
live DAT reloaded automatically or needs a manual update/reinit.

## Consequences

- Never assume `SRC/` exactly matches the running patch.
- Preserve TD DAT indentation and local style.
- Reinitialize extensions after editing extension code when needed.
- Verification must include live TD behavior, not only Python syntax checks.

