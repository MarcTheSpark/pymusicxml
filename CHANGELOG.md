# Changelog

> These changelogs are AI-written and human-reviewed, because no one (least of all my wife
> and kids) wants me wasting my precious time meticulously documenting this shit, useful
> though it may be.

All notable user-facing changes to pymusicxml are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Fixed

- Non-italic text annotations now write `font-style="normal"` explicitly, so readers that
  italicize `<words>` by default (e.g. Verovio) render them upright as intended.
- Notes now write an explicit `<accidental>` glyph, not just the `<alter>` pitch, so sharps,
  flats, and naturals show up in readers that don't infer them. Which accidental is drawn
  follows standard measure spelling: repeats within a measure are hidden, and the key
  signature and ties into the note are respected. (This also paves the way for a possible
  future feature of allowing different accidental spelling policies, such as showing accidentals
  on every note regardless of context.)
- Tied notes spanning three or more segments now emit their tie elements stop-before-start,
  fixing readers that drew one long tie across the whole group instead of separate ties.
- A note tied across a barline now carries its accidental as a hidden `<accidental>`, so
  readers that resolve pitch from the written accidental keep the tie instead of dropping it.

## [0.5.8] - 2026-07-12

A documentation release. There are no functional changes: every public class and function
now carries a docstring, so the API documentation is complete. Released so that the
published package matches the documented one.

### Changed

- Docstrings added across the public API — notably `AccidentalType`, `HookType`, and
  `NonTraditionalKeySignature`.
- The documented source-code link points at GitHub rather than sourcehut.

## Earlier versions

For changes prior to 0.5.8, see the commit history.
