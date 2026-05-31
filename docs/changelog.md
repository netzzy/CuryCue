# Changelog

## [2026-05-31] ADR Infrastructure Edge Coverage

- Added architecture decision records for operator menus, global hotkeys, output
  windows/mapping, and deprecated/archive code policy.
- Kept ADRs focused on system contracts and avoided documenting concrete content
  presets as architecture.
- Affected files: `ADR/0014-operator-menu-and-project-shortcuts.md`, `ADR/0015-global-hotkeys-and-command-routing.md`, `ADR/0016-output-windows-and-mapping-layer.md`, `ADR/0017-archive-and-deprecated-code-policy.md`, `docs/changelog.md`.
- Migrations: none.

## [2026-05-31] ADR Runtime Coverage Expansion

- Added architecture decision records for cue fade lifecycle, export modes, UI
  lifecycle, DB write paths, fixture registration, show-control shortcuts,
  content side-panel contracts, and live verification workflow.
- Affected files: `ADR/0006-cue-execution-and-fade-lifecycle.md`, `ADR/0007-export-modes-and-active-field-rendering.md`, `ADR/0008-ui-architecture-and-mode-lifecycle.md`, `ADR/0009-database-write-paths-and-derived-cue-values.md`, `ADR/0010-fixture-registration-and-drag-drop-contract.md`, `ADR/0011-frame-bind-and-show-control-shortcuts.md`, `ADR/0012-content-preset-timeline-and-side-panel-contract.md`, `ADR/0013-operational-debugging-and-live-verification.md`, `docs/changelog.md`.
- Migrations: none.

## [2026-05-31] Project Governance Baseline

- Added agent operating rules for critical-infrastructure review, concise
  communication, mentor-style engineering judgment, changelog updates, and ADRs.
- Added initial architecture decision records for the cue engine, source/live
  DAT workflow, content routing, lister selection safety, and change governance.
- Affected files: `CLAUDE.md`, `docs/changelog.md`, `ADR/0001-core-cue-engine-and-sqlite-state.md`, `ADR/0002-source-mirrors-and-live-touchdesigner-dats.md`, `ADR/0003-content-preset-routing-and-cook-gating.md`, `ADR/0004-ui-mode-and-lister-selection-safety.md`, `ADR/0005-change-governance-for-critical-infrastructure.md`.
- Migrations: none.

## [2026-05-31] TD 2025 Lister Selection Guard

- Fixed cue selection sync after the TD 2025 upgrade so selecting `Blackout`
  Order 10 updates the current cue and releases active channel fades.
- Guarded hidden/non-cooking listers: selection state is written to
  `Selectedrows`, while visual `SelectRow()` calls run only when the widget is in
  a cooking parent chain.
- Fixed `UtilsClass.CheckParentCooking()` for TD 2025 parent traversal and
  ensured `cueSwitchBlock` is released with `try/finally`.
- Affected files: `SRC/CuryCue/UtilsClass.py`, `SRC/CuryCue/CuryCueUIClass.py`,
  `SRC/CuryCue/CueParListUICallbacks.py`, `CLAUDE.md`.
- Migrations: none.
