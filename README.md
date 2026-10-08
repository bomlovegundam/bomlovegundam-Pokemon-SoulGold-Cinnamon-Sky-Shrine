# Pokémon SoulGold — Cinnamon Sky Shrine

Pokémon Emerald GBA fan ROM-hack project focused on the Cinnamon Sky Shrine / Seijintei Shrine Grounds.

## Verified Safe V2 baseline

- ROM: `Pokemon_SoulGold_Cinnamon_SKY_SHRINE_FINAL_SAFE_V2.gba`
- Size: 33,554,432 bytes (32 MiB)
- SHA-256: `9de6c224e54a006ae361435d72da4524fdde6077365c95871715a31032e7c23f`

## Safety rules

- Treat the Safe V2 ROM as an immutable baseline.
- Do not perform global graphics-ID or event-pointer replacements.
- Preserve unrelated map headers and scripts.
- Preserve the original Group3/Map55 event pointer.
- Do not use one 96x96 runtime map; the runtime design uses four 48x48 maps.
- Static validation does not replace emulator/runtime validation.

## Sky Shrine runtime structure

The shrine area is represented by four runtime maps:

- Group25/Map0
- Group25/Map1
- Group25/Map2
- Group25/Map3

The 96x96 artwork/reference is a logical master layout, not one runtime fieldmap.

See [docs/SKY_SHRINE_MAP.md](docs/SKY_SHRINE_MAP.md) for the verified warp network and layout zones.

## Validation

Run locally against the ROM:

```bash
python tools/validate_rom.py /path/to/Pokemon_SoulGold_Cinnamon_SKY_SHRINE_FINAL_SAFE_V2.gba
```

The validator checks the known-safe ROM size, SHA-256, Map55 header/event pointer, entry script, and return script.

## Project status

| Area | Status |
| --- | --- |
| Safe V2 baseline | Verified |
| Four-map Sky Shrine structure | Documented |
| Static validator | Included |
| Runtime emulator validation | Pending |
| Full in-game NPC/event verification | Pending |

This is a fan project and is not affiliated with Nintendo, Game Freak, or The Pokémon Company.
