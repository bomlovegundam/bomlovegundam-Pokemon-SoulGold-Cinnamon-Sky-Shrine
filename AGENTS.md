# Agent Instructions — Pokémon SoulGold Cinnamon Sky Shrine

## Mission

Work autonomously where safe. Inspect first, make the smallest verified change, validate it, review the diff, and report the exact result.

## Repository safety

- Preserve existing user work.
- Never invent ROM offsets, pointers, map IDs, or binary structures.
- Never overwrite the verified Safe V2 baseline.
- Never perform global graphics-ID or event-pointer replacements.
- Never modify unrelated map headers or scripts.
- Never commit an unverified ROM/binary modification.
- If a requested change cannot be verified safely, stop before committing and explain the blocker.

## Runtime map rules

Sky Shrine uses four runtime maps:

- Group25/Map0
- Group25/Map1
- Group25/Map2
- Group25/Map3

Each runtime map is 48x48. The 96x96 artwork is a logical/master reference and must not be treated as a single 96x96 runtime map.

All warp destinations must be checked in both directions.

## Known-safe baseline

ROM: Pokemon_SoulGold_Cinnamon_SKY_SHRINE_FINAL_SAFE_V2.gba

SHA-256: 9de6c224e54a006ae361435d72da4524fdde6077365c95871715a31032e7c23f

Map55's original event pointer must remain 0x09F372CC unless a task explicitly and safely replaces it.

## Validation workflow

After every significant change:

1. Run available static validation.
2. Check map dimensions and pointers when relevant.
3. Check scripts and warp destinations when relevant.
4. Review git diff.
5. Fix failures before committing.
6. Do not claim success unless the command/test actually passed.

## Git workflow

For completed tasks, create a descriptive commit and push only when authorized by the task. Report:
- changed files
- tests/validation
- commit SHA
- final repository state
- remaining blockers
