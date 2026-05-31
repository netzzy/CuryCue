# CuryCue - Agent Project Notes

This file is the source of truth for agents working in this repository.

## Critical infrastructure operating rule

Treat CuryCue as critical live-show/media-server infrastructure. Before changing
TD logic, cue execution, UI mode switching, lister/callback behavior, exports,
database writes, or content activation, spend the tokens needed to map blast
radius explicitly.

For every non-trivial change, identify:

- live runtime side effects in TD, including hidden/dormant branches that may
  wake later
- cue, fixture, and content paths that can be affected
- whether the change touches show-critical flow, DB persistence, exports,
  callbacks, scheduler/run() timing, or parent allowCooking/display state
- how to verify safely in live TD and what state to restore afterward

Do not optimize for brevity when reliability is at stake. Prefer a longer,
evidence-backed analysis over a fast guess, and document assumptions when a risk
cannot be fully eliminated.

## Collaboration stance

Act as a mentor for the programmer-architect-product human working with you.
Do not blindly accept shameful shortcuts, risky simplifications, or commands
that would teach the wrong engineering habit. If the user asks for something
technically weak or unsafe, say so briefly, explain the better decision, and
continue with the safer implementation when possible.

This does not mean lecturing. It means protecting the architecture, the show
runtime, and the user's future judgment.

## Communication budget

The user's attention window is narrow. Default answers should be 3-7 lines.
Use long breakdowns only when the user explicitly asks for deep analysis with
phrases such as `ULTRATHINK`, `подробно`, or `разложи`.

- Avoid tables and numbered lists unless comparing real options or documenting
  a systematic plan.
- Avoid preambles such as "I will now analyze"; start with the result or the
  next concrete action.
- Do not add a final "what I did" essay when the diff already shows it.
- When a decision is needed, ask one question. If there is a recommendation,
  give it in one line and wait for ack/nack.
- Think deeply, but expose only the useful conclusion unless detail was asked
  for.

## Planning standard

Plans are decisions first, then systematic scope. A useful plan must answer, in
order:

1. User problem: what is broken or missing from the user's perspective.
2. Target experience: what the user sees or does after the change.
3. Design decision: the chosen approach and why alternatives were rejected.
4. Architecture impact: how it touches adjacent systems and future plans.
5. Full scope: every affected subsystem found by tracing references with `rg`,
   live TD inspection, and docs, not memory.

Plans fail when they miss the product/architecture "why" or when they miss
scope because references were guessed. Both are fatal in this project.

## Change history and ADRs

Always update `docs/changelog.md` for bug fixes, features, refactors, and other
large behavioral or architecture changes. Use this format:

```text
## [YYYY-MM-DD] Brief Title
- Summary of the user-visible/runtime change.
- Affected files: path, path, path.
- Migrations: none, or exact DB/TD/project migration steps.
```

Keep architectural decisions in `ADR/`. Add or update an ADR when changing cue
execution, database persistence, TD export behavior, UI mode/list behavior,
content preset routing, source-vs-live DAT workflow, or operational safety
rules.

## Mandatory: local TouchDesigner documentation

This repository includes local TouchDesigner documentation in `Docs_MD/`.

Do not guess TouchDesigner parameters, classes, callbacks, operator behavior, or
Python API details when local docs can answer the question. Search and read the
local docs before editing TD logic or answering TD-specific implementation
questions.

Useful filename patterns:

- Operators: `{Operator_Name}.md`, for example `Parameter_Execute_DAT.md`,
  `Script_CHOP.md`, `Constant_TOP.md`
- Python classes: `{ClassName}_Class.md`, for example `Par_Class.md`,
  `OP_Class.md`, `BaseCOMP_Class.md`
- Concepts: `Extensions.md`, `Custom_Parameters.md`, `Python.md`,
  `Working_with_OPs_in_Python.md`, `Working_with_DATs_in_Python.md`

Prefer `rg` over manual browsing:

```powershell
rg "parameterexecute" Docs_MD
rg "appendCustomPage" Docs_MD
rg "allowCooking" Docs_MD
rg "scriptCHOP" Docs_MD
```

Use the `twozero_td` MCP tools for live-patch inspection. Always start TD work
by listing instances, then inspect the relevant subtree:

```text
td_list_instances
td_get_network(path="/project1/CuryCue", mode="full")
td_get_network(path="/project1/Content", mode="full")
td_read_dat(path="/project1/CuryCue/CuryCueClass")
td_get_errors(path="/project1", recursive=true)
```

For broad architecture discovery, `td_parse_project` is appropriate. The current
project is below the 10k-operator warning threshold, but still prefer scoped
parses such as `/project1`, `/project1/CuryCue`, or `/project1/Content`.

## TouchDesigner conventions for this project

- Preserve existing indentation in TD DAT scripts. Many DAT scripts use tabs;
  several external `SRC` files use spaces. Do not normalize unrelated files.
- Do not shadow the global `op()` function.
- Prefer relative references, `parent` shortcuts, `opshortcut`, and `iop/ipar`
  helpers over hard-coded `/project1/...` paths when writing new code.
- When editing an extension DAT, inspect the live DAT first. Source files in
  `SRC/` are a mirror/source library, but the live patch can diverge.
- After changing extension DAT code, pulse `par.reinitextensions` on the owner
  COMP when needed.
- For parameter callbacks, read `Docs_MD/Parameter_Execute_DAT.md` first.
- For custom parameter creation, read `Docs_MD/Custom_Parameters.md` and the
  relevant class docs first.
- For Execute DAT logic, read `Docs_MD/Execute_DAT.md`.
- For Script CHOP/DAT/TOP callbacks, read the matching operator docs first.
- For UI or panel changes, use TD MCP inspection and run panel audits where
  applicable before calling the change done.

## Repository layout

Important files and folders:

```text
README.md                  User-facing overview and workflow docs
AGENTS.md                  Pointer to this file
CLAUDE.md                  Agent instructions and architecture notes
docs/changelog.md          Project change history for major edits
ADR/                       Architecture decision records
CuryCue.Settings.json      Small project settings file
DB/structure.sql           SQLite schema reference
DB/CuryCueSQLite.db        Active cue/fixture database
SRC/CuryCue/               Core CuryCue source DAT mirrors
SRC/ContentClasses/        Content preset system class mirrors
SRC/GlobalUI/              Global keyboard shortcut class mirrors
SRC/.deprecated/           Archived legacy scripts, not active architecture
TOX/                       External TOX components
Docs_MD/                   Local TouchDesigner docs
SOURCE_VIDEO/              Sample/source media
SOURCE_AUDIO/              Sample/source audio
*.toe                      TouchDesigner project files
```

`SRC/.deprecated` contains old camera, laser, viewport picker, sequence, and
keyframer code. No active reference to the large deprecated keyframer/sequence
files was found during the initial scan. Treat this folder as archive material
unless a live patch reference proves otherwise.

## Project overview

CuryCue is a TouchDesigner cue-control system for live performance work. It is
inspired by QLab and lighting-console cue lists:

- fixtures are TD components/operators under control
- fixture parameters are registered in SQLite
- cues store only parameter changes
- missing cue parameter values are inherited from previous cues or fixture
  defaults
- cue execution fades parameter values over time
- values are exported back to TD parameters either through CHOP export or direct
  parameter writes

The README also documents an alpha Content Preset System used alongside the core
cue system. Presets live under `/project1/Content`, route their outputs into
compositors, and expose side-panel UI/timeline widgets when active.

## Current live patch snapshot

Initial MCP scan on 2026-05-31:

- TD project: `CuryCue_31550.4.toe`
- TD build: `2025.32280`
- Repository/project path: `C:/Nextcloud/PROJECTS/CuryCue`
- Live scope parsed: `/project1`
- Parsed ops: 4137 with opaque widget internals skipped
- Project-level ops reported by `td_list_instances`: 6226
- DAT scripts indexed by parser: 532
- Extensions indexed: 80
- Wires indexed: 1877
- Runtime database counts from `DB/CuryCueSQLite.db`:
  - `cue`: 17 rows
  - `fixture`: 7 rows
  - `fixture_float_data`: 14 rows
  - `cue_float_data`: 42 rows

This is runtime state, not an architectural invariant.

## Top-level TD structure

Top-level `/project1` children observed in the live patch:

```text
/project1
  LED                         nullTOP final LED output
  PROJ1                       nullTOP final projector output
  Content                     baseCOMP, tag DevicesUnderControl, content system
  CuryCue                     containerCOMP, core cue engine
  ServerUI                    containerCOMP, top/header/status UI custom layer
  CuryCueUI                   containerCOMP, main operator UI
  BottomPanel                 containerCOMP, user bottom controls
  CamerasInput                baseCOMP, global shortcut op.cam
  ServerShowModeSideUI        containerCOMP, show-mode side panel
  PREPARE_FEED_FOR_REAL_PROJ  baseCOMP, projector/stoner mapping, op.pproj
  annotate*                   annotations
```

Important global/parent shortcuts:

```text
op.curycue        -> /project1/CuryCue
parent.curycue    -> /project1/CuryCue
parent.curycueui  -> /project1/CuryCueUI
op.DP             -> /project1/CuryCue/base_print_and_display
parent.vcont      -> /project1/Content
op.pproj          -> /project1/PREPARE_FEED_FOR_REAL_PROJ
op.cam            -> /project1/CamerasInput
parent.ssui/op.ssui -> /project1/ServerShowModeSideUI
parent.sui        -> /project1/ServerUI
```

## Core cue system: `/project1/CuryCue`

`/project1/CuryCue` is the main cue engine. It is a `containerCOMP` with promoted
extension:

```text
/project1/CuryCue/CuryCueClass
op("./CuryCueClass").module.CuryCueClass(me)
```

Important child DATs and CHOP/DAT renderers:

```text
CuryCueClass              main extension class
CuryCueConnector          loads SQLite rows into dataclasses
MysqlBase                 SQLite connection/query helper
QClass                    fade/delay evaluator queue
CuryCueStructsDef         dataclasses for cues, fixtures, active fields
InTableEditBase           lister edit callbacks -> SQLite updates
CuryCueAddByDragAndDrop   drag/drop fixture and parameter registration
FixtureUtils              delete fixture/parameter/cue parameter helpers
ActiveFloatParsRender     scriptCHOP numeric active field output/export
ActiveParsRender          scriptDAT active field table
ActiveEvaluators          scriptCHOP fade progress
CueListRender             scriptDAT cue list rows
CueParListRender          scriptDAT parameters for selected cue
FixListRender             scriptDAT fixture list
FixListRenderV2           scriptDAT fixture list with original paths
FixParListRender          scriptDAT fixture parameter rows
UpdateEveryFrame          executeDAT frame-start update loop
GLOBAL_UI                 keyboard shortcut processor
```

Important `iop` shortcuts configured on `/project1/CuryCue`:

```text
MysqlBase, CuryCueConnector, cuelist, utils, floatsrender,
fixlistrender, cuepars, fixparlistrender, activeparsrender,
activeparsrenderlive, storedat, Qclass, fixlistrender_orig_paths_for_edit,
uiEditModeFixlistWidget, uiFixtureModeFixlistWidget, active_evaluators
```

Important custom parameters on `/project1/CuryCue`:

```text
Parsselmode                 existing / all field highlight behavior
Fades                       fade enabled/disabled
Exportmode                  No export / ChopExport / ValueExport
Autoselectdevicebycomp      Off / selection modes
Cuearrayindex, Cueid,
Cueorder, Cuename           current cue state
Framebind                   current cue frame bind
Isframebindenabled          enables frame-based autocue
Currentframe                expression: me.time.frame
Framebindrange1..3          frame bind range channels
Ui                          /project1/CuryCueUI
Sideui                      ServerShowModeSideUI
Sqlitedatabasefile          DB/CuryCueSQLite.db
Dbhost, Dbname, Dbuser,
Dbpassword                  legacy DB parameters, SQLite is active
Reloadsql                   reload database pulse
```

### SQLite schema

Active database schema is in `DB/structure.sql` and mirrored in
`MysqlBase.createNewDatabase()`:

```text
cue
  id, order, name, memo, type, update_mode, osc_bind, dmx_bind,
  linked, is_enabled, order_new, frame_bind

cue_float_data
  id, id_cue, id_fixture, par_name, par_value, par_text_value,
  fade_in, fade_out, delay_in, delay_out
  UNIQUE(id_cue, id_fixture, par_name)

fixture
  id, order, name, global_object_location, type, is_enabled
  UNIQUE(global_object_location)

fixture_float_data
  id, id_fixture, par_name, default_value, fade_default,
  delay_default, is_enabled
```

SQLite is the active implementation. Some legacy MySQL names remain in class
names and custom parameters.

### Data model

`CuryCueStructsDef` defines these dataclasses:

- `FIXTURE`: registered TD operator/component under cue control
- `FIXPAR`: registered parameter for a fixture
- `CUE`: cue metadata and cue parameter collections
- `CUEPARFLOAT`: parameter value stored on a specific cue
- `ACTIVE_FIELDS`: current resolved value for every registered fixture parameter
- `FRAMEBINDRANGE`: helper for frame-bind autocue

`CuryCueConnector.UpdateFromDb()` rebuilds all runtime data:

```text
LoadCue()
LoadFixtureData()
LoadFixturePars()
LoadCueFloatData()
LoadCueFloatDataV2()
ResortCuesByID()
CreateActiveFields()
```

`LoadCueFloatDataV2()` is the inheritance pass. It walks cues in order and fills
missing cue parameters from the previous resolved value or the fixture default.
Derived cue parameters use `id=-1` and `is_derived=True`; they appear in the UI
but are not stored rows until explicitly written.

### Cue execution flow

Typical cue run:

```text
UI/lister callback or hotkey
  -> CuryCueUIClass.SetSelectedCue()
  -> CuryCueClass.CueChangeByRow()
  -> CuryCueClass.RunCue(cue)
  -> QClass creates per-parameter FadeEvaluator tasks
  -> UpdateEveryFrame calls q.UpdateEveryFrame()
  -> CallbackFromFader updates ActiveFields
  -> ActiveFloatParsRender / ActiveParsRender recook
  -> parameter export writes values to TD
```

`RunCue()` compares each `ACTIVE_FIELDS.full_par_path` against the target cue's
resolved `pars_float_by_path`. Only changed values create fade tasks. Text
parameters are carried in `par_text_value`.

Linked cues: when all evaluators finish, `CallbackFromFaderComplete()` checks
`cue.linked == 1` for the current cue and triggers `Gonextcue()`.

Frame-bind autocue: `UpdateEveryFrame()` can use `FRAME_RANGE_FOR_AUTOCUE_TRIGGER`
channels and `Framebindrange1..3` to trigger the next cue when the timeline frame
enters the trigger range after satisfying the precondition range.

### Export modes

`Exportmode` controls how active values reach TD:

- `ChopExport`: recooks `ActiveFloatParsRender`; numeric channels are exported
  to matching parameters. Text values are still written directly by
  `ActiveFloatParsCallBack`.
- `ValueExport`: `ExportCopyAllPars()` directly writes all active field values
  into TD parameters.
- disabled/no-export mode: used for manual fine tuning before storing values.

The README mentions Ctrl/Shift + Tab as the operator shortcut for cycling export
mode.

### Editing and persistence

Lister edit callbacks go through `InTableEditBase` subclasses:

- cue list edits update `cue`
- selected cue parameter edits update `cue_float_data`
- active parameter edits can insert a missing derived row via `Storeselected()`
- fixture list edits update `fixture`
- fixture parameter edits update `fixture_float_data`

All successful edits call `UpdateFromDb()`, recook render DATs, and run
`SetInitCue(1)`.

Drag-and-drop behavior:

- Drop a TD OP onto `/project1/CuryCue` or head UI: add a `fixture` row.
- Drop a parameter after the fixture exists: add a `fixture_float_data` row.
- Adding parameters before adding the fixture is rejected.

## Main UI: `/project1/CuryCueUI`

`/project1/CuryCueUI` is the main 1280x720 operator UI. It is docked to
`/project1/CuryCue` and has promoted extension:

```text
/project1/CuryCueUI/CuryCueUIClass
op("./CuryCueUIClass").module.CuryCueUIClass(me)
```

Main areas:

```text
topMenu          Top menu widget built from common + local tables/callbacks
HEAD_ROW         Header/status/custom UI row
EDITMODE         cue list, cue parameter list, fixture list, active fields
FIXTURES         fixture and fixture-parameter management
SHOWMODE_CUES    show-mode cue list plus side panel
addKeyUI         create cue dialog
BottomCustomPanel selectCOMP pulling from /project1/BottomPanel
```

`CuryCueUIClass` responsibilities:

- switch between `fixturesui`, `editmodeui`, and `showmodeui`
- route cue selection to `CuryCue.CueChangeByRow()`
- keep multiple cue listers selected in sync
- run cue context menu actions: duplicate with/without parameters, delete,
  create blank cue
- show/hide UI modes by toggling `display` and delayed `allowCooking`
- expose content system bar path for the header

TD 2025 upgrade note from MCP investigation:

```text
Symptom: selecting Blackout row 1 highlighted the lister row but did not change
/project1/CuryCue from the previous cue.

Root cause: UtilsClass.CheckParentCooking() started parent traversal at
parent(0). In TD 2025 parent(0) returns None; parent(1) is the first real
parent. The function therefore returned True for hidden/non-cooking UI branches.
CuryCueUIClass then tried to SelectRow() on hidden EDITMODE listers whose
ListerExt was not initialized, raised td.tdAttributeError, and left
cueSwitchBlock=True because selection sync had no finally block.

Fix: CheckParentCooking() now starts at parent(1) and checks the target OP
itself; CuryCueUIClass synchronizes lister selection via SyncCueListSelection()
with a SelectCueListRow() guard and always releases cueSwitchBlock in finally.
Selection sync writes the widget wrapper `Selectedrows` parameter even when a
mode branch is hidden, but calls visual `SelectRow()` only when the lister is in
a cooking parent chain. This keeps dormant EDIT/FIXTURES lists in sync without
forcing their uninitialized ListerExt methods.
When UI modes switch, `SyncCurrentCueListSelection()` is scheduled one frame
after activation because lister init can clear `Selectedrows` while
`Saveselectedrows` is off.
```

Keep this pattern for any future lister sync: hidden/non-cooking listers can
have missing promoted extension methods after a TD restart or version upgrade.
Do not call `SelectRow()` directly from project callbacks; update
`Selectedrows` first and guard promoted Lister methods behind a cooking-chain
check.

## Server/custom UI layers

`/project1/ServerUI` is a project-specific header/status/custom UI layer used by
`CuryCueUI.par.Customui`.

Observed custom parameters:

```text
Preview1 -> PROJ1
Preview2 -> LED
Preview3 -> CamerasInput/CAM_1
Preview4 -> CamerasInput/CAM_2
Display flags and aspect ratios for preview panes
```

`SRC/topMenuCallbacksLocal.py` and `SRC/CuryCue/topMenuDefineLocal.csv` contain
project-specific menu callbacks and labels. Some callback names/reference paths
look inherited from older projects (`VideoProjectorContent`, `Seq`, `Env`, etc.).
Treat local top-menu callbacks as project-specific and verify live paths before
using or editing them.

`/project1/ServerShowModeSideUI` is the show-mode side panel. It contains
`ContentSystemBar`, camera tabs, and timeline/status widgets. Its promoted
shortcut is `ssui`.

`ContentSystemBar` receives active content module names from `/project1/Content`
and updates a replicator that creates per-module status bars. Each replicated
status bar can find the active module, its internal `AnimationTimeControl`, and
set/play/rewind the module timeline.

## Content preset system: `/project1/Content`

`/project1/Content` is a `baseCOMP` tagged `DevicesUnderControl`. It has promoted
extension:

```text
/project1/Content/ProjectorsMasterClass
me.op("./ProjectorsMasterClass").module.ProjectorsMasterClass(me)
```

The class hierarchy is:

```text
ProjectorsMasterClass -> ContentMasterBase -> SceneToggleObject
ProjectorsPresetClass -> ContentPresetBase -> SceneObjectControlBase
```

Important source mirrors:

```text
SRC/ContentClasses/BaseContentMasterClass.py
SRC/ContentClasses/BasePresetContentClass.py
SRC/ContentClasses/VideoClasses/ProjectorsMasterClass.py
SRC/ContentClasses/VideoClasses/ProjectorsPresetClass.py
SRC/ContentClasses/LocalPresetClass.py
SRC/ContentClasses/AnimationTimeControl.py
```

Important note: `SceneObjectBase` and the content-side `UtilsClass` are present
as live DATs under `/project1/Content`, but are not mirrored in the active
`SRC/ContentClasses/` folder. Inspect the live DATs before editing classes that
import them.

### Preset structure

Each content preset is an outer `baseCOMP` tagged `ContentPreset` and usually has
an inner container with the same name tagged `content`:

```text
/project1/Content/Scene1          outer preset, always available
/project1/Content/Scene1/Scene1   inner content container, cook-gated
```

The outer preset holds common parameters such as:

```text
Active
Activefade
Armed
Armingtype: byfade or bytoggle
Arm pulse
Disarm pulse
```

`ContentPresetBase.Update()` controls the inner container:

- if `Armingtype == byfade` and `Activefade == 0`, it clears `Armed`
- if `Armed == 0`, the inner content COMP `allowCooking` is set false
- if `Armed == 1`, the inner content COMP `allowCooking` is set true
- if the inner content has `LocalPresetClass`, its `__del__` is called when the
  content is disarmed

`Copycustomparup()` copies custom parameters from the inner content or an
`contentPreset_iPar` helper to the outer preset and binds parameters between the
outer and inner layers.

### Routing

Routing is configured by `/project1/Content/PresetsRoutingTable`:

```text
Preset source | Composite node | Composite par
PROJ1_OUT     | PROJ1_COMP     | tops
LED_OUT       | LED_COMP       | tops
LASER         | LASER_COMP     | sops
```

`ContentMasterBase.Update()` runs each frame through
`/project1/Content/executeEveryFrame`. It:

1. finds preset COMPs from `FindContentPresets`
2. calls `myPreset.Update()`
3. builds `ActiveList` from presets where `Armed == 1`
4. writes active preset names to `Content.par.Active`
5. for each routing table row, finds matching output nodes in active presets
6. writes space-separated OP paths into compositor parameters
7. pushes active module names to `ServerShowModeSideUI/ContentSystemBar`

Top-level content outputs:

```text
/project1/Content/PROJ1_OUT -> /project1/PROJ1
/project1/Content/LED_OUT   -> /project1/LED
/project1/Content/LASER_GEO_OUT
```

### Current presets

Observed current presets:

```text
Calibrate
Scene1
CireWheel
presetTemplate
```

`Scene1`:

- has `PROJ1_OUT` and `LED_OUT`
- contains `AnimationTimeControl`
- uses `feedbackEdge` for feedback/edge processing
- registered in SQLite as a fixture with parameters including `Active`, `Drywet`,
  `Scale`, `Edgestrength`, `Feedbackgain`, `File`, `Transfer`

`Calibrate`:

- has outer `Active` fixture registration
- has inner switch registered as `CalibrateSwitch.index`

`CireWheel`:

- includes audio analysis, simulation, lights, SpringSim/WallRender networks
- has multiple clone masters under `audioAnalysis`: `low`, `kick`, `smsd`
- clones include `mid`, `high`, `rythm`, `snare`, `fmsd`, `spectralCentroid`
- registered cues use outer `Active` and inner `Gopre`/`Go`

`presetTemplate`:

- template for new content presets
- includes standard always-executing outer layer and cook-gated inner layer

### AnimationTimeControl

Several inner preset containers contain an `AnimationTimeControl` COMP with an
`InternalClass` extension. Main methods:

```text
Play()
Stop()
PlayOrStop()
Rewind()
SetTimeFrame(frame)
GetCurrentFrame()
```

It controls `T/local/time`. Side-panel timeline widgets inspect this path.
Several methods in the source use `self.my.op("local/time")` while others use
`self.my.op("T/local/time")`; verify live behavior before changing.

## Database runtime notes

Current DB fixtures from initial scan:

```text
CalibrateToggle   /project1/Content/Calibrate
CalibrateSwitch   /project1/Content/Calibrate/Calibrate/switch1
Scene1            /project1/Content/Scene1
Scene2            /project1/Content/Scene2
CireWheelContent  /project1/Content/CireWheel/CireWheel
CireWheel         /project1/Content/CireWheel
level1            /project1/level1
```

Live TD check showed these DB fixture paths missing:

```text
/project1/Content/Scene2
/project1/level1
```

Do not assume DB rows all point to existing OPs. `CuryCueConnector` and export
code often guard with `op(path)` / `hasattr`, but stale rows can still explain
missing exports or no-op cues.

Current cue names include `Blackout`, `Calibrate 1`, `Calibrate 2`, `Scene1 +`,
`Scene1 FX1 ON`, `Transfer 2 LED screen`, `Scene1 movie 2 ON`,
`Generative heavy scene LOAD`, and `Generative scene GO`.

## Known live issues from initial MCP scan

These are notes, not requested fixes.

- `td_get_errors(path="/project1", recursive=true)` reported many issues.
  A large share is in `Content/CireWheel` and nested widget/slider/audioAnalysis
  internals.
- `CuryCueUIClass.SetSelectedCue()` previously triggered repeated
  `'td.listCOMP' object has no attribute 'SelectRow'` after TD 2025 upgrade;
  fixed by guarded lister sync and parent(1)-based cooking checks.
- `Content/CireWheel/CireWheel/SSim1` has broken expressions referencing
  `CireWheel/fixedPointsMove/out1`, `meshGrow/out1`, `meta2xpos/out1`, and
  `meta2ypos/out1`.
- `Content/CireWheel/CireWheel/Simulation/Simulation` has missing values around
  `simResolution`, `computeInfo`, and GLSL simulation dispatch/resolution.
- `Content/CireWheel/CireWheel/audioAnalysis` has many broken UI/widget
  references and missing CHOP-derived parameters.
- `ServerShowModeSideUI/ContentSystemBar/.../TimelineHeader` has errors when
  active modules lack expected timeline or rollover CHOPs.
- `PREPARE_FEED_FOR_REAL_PROJ/stoner` has grid/pattern warnings and errors.
- Several parser unresolved refs are likely parser limitations or dormant UI
  widget references, but project-specific hard-coded paths should still be
  verified before use.
- A one-time `td_get_perf` sample during MCP activity showed very low FPS and
  large UI/TOP costs. Treat that sample as noisy until measured without active
  inspection tools.

## Safe editing workflow

Before changing TD behavior:

1. Read this file and the relevant source mirror in `SRC/`.
2. Inspect the live TD subtree:

```text
td_list_instances
td_get_network(path="/project1/CuryCue", mode="full")
td_get_network(path="/project1/Content", mode="full")
td_read_dat(path="/project1/CuryCue/CuryCueClass")
td_read_dat(path="/project1/Content/ContentMasterBase")
td_get_errors(path="/project1", recursive=true)
```

3. Search local TD docs for the exact feature being changed.
4. Keep changes scoped to the relevant DAT/source file and preserve local style.
5. If editing a source mirror, remember the live patch may need the corresponding
   DAT updated or reloaded.
6. Reinitialize extensions if needed.
7. Recook relevant Script DAT/CHOP outputs after database or render logic edits.
8. Re-run `td_get_errors` on the edited subtree.
9. For UI/panel work, inspect actual panel layout and run available panel audits.

## Implementation cautions

- `MysqlBase.executeUpdateQuery()` swallows exceptions and returns
  `(False, "Something went wrong")`; inspect textport/logs when DB writes fail.
- `insertIntoTable()` uses SQLite `REPLACE INTO`, so cue parameter writes can
  overwrite existing rows due to the unique constraint.
- Text parameter values use `cue_float_data.par_text_value`; numeric values use
  `par_value`. Several code paths switch field names based on float conversion.
- `LoadFixtureData()` resolves DB paths like `op.someShortcut` into absolute
  paths when the shortcut exists.
- `ActiveFloatParsRender` exports numeric channels named by full parameter path
  (`/path/to/op:Parname`). Changing channel naming affects CHOP export.
- `ContentPresetBase.Update()` toggles `allowCooking`; remember that disabled
  inner COMPs may have stale/empty outputs after reload until armed/cooked.
- The source tree has old MySQL and deprecated code. Do not revive it unless the
  live patch requires it.
