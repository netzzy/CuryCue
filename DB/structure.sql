CREATE TABLE cue (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  "order" REAL DEFAULT NULL,
  name TEXT DEFAULT NULL,
  memo TEXT NOT NULL DEFAULT ' ',
  type TEXT NOT NULL DEFAULT 'Regular',
  update_mode TEXT NOT NULL DEFAULT 'Stored',
  osc_bind TEXT DEFAULT NULL,
  dmx_bind INTEGER DEFAULT NULL,
  linked INTEGER DEFAULT NULL,
  is_enabled INTEGER DEFAULT 1,
  order_new REAL DEFAULT NULL
, frame_bind INTEGER DEFAULT 0);

CREATE TABLE cue_float_data (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  id_cue INTEGER NOT NULL,
  id_fixture INTEGER NOT NULL,
  par_name TEXT NOT NULL,
  par_value REAL DEFAULT 0,
  par_text_value TEXT,  -- make the column nullable
  fade_in REAL DEFAULT 0,
  fade_out REAL DEFAULT 0,
  delay_in REAL DEFAULT 0,
  delay_out REAL DEFAULT 0,
  UNIQUE(id_cue, id_fixture, par_name)
);

CREATE TABLE fixture (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  "order" REAL DEFAULT 999,
  name TEXT DEFAULT NULL,
  global_object_location TEXT NOT NULL,
  type INTEGER DEFAULT 0,
  is_enabled INTEGER NOT NULL DEFAULT 1,
  UNIQUE(global_object_location)
);

CREATE TABLE fixture_float_data (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  id_fixture INTEGER NOT NULL,
  par_name TEXT NOT NULL,
  default_value REAL NOT NULL DEFAULT 0,
  fade_default REAL NOT NULL DEFAULT 1,
  delay_default REAL NOT NULL DEFAULT 0,
  is_enabled INTEGER DEFAULT 1
);

