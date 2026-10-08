# ROM Baseline

## Verified ROM

- Filename: `Pokemon_SoulGold_Cinnamon_SKY_SHRINE_FINAL_SAFE_V2.gba`
- Size: 33,554,432 bytes
- SHA-256: `9de6c224e54a006ae361435d72da4524fdde6077365c95871715a31032e7c23f`

## Critical verified offsets

### Group3/Map55 header

File offset: `0x156CC38`

Expected header bytes:

```
e0 71 f3 09 cc 72 f3 09 7f 70 39 08 00 00 00 00
43 03 4d 02 cd 00 00 00 08 00 04 00
```

- Layout pointer: `0x09F371E0`
- Original event pointer: `0x09F372CC`

A previous unsafe build redirected the event pointer to `0x09F38100`; Safe V2 restores the original pointer.

### Sky Shrine entry script

File offset: `0x1F03C60`

Expected bytes:

```
3d 19 00 ff 1f 00 0d 00 27 02 ff ff
```

This targets Group25/Map0 at X31,Y13.

### Return script

File offset: `0x1F03C6C`

Expected bytes:

```
3d 03 02 ff 1e 00 0e 00 27 02 ff ff
```

This returns to Group3/Map2 at X30,Y14.

## Safety

These values are the verified Safe V2 reference points. Do not invent replacements. Runtime emulator validation is still required for behavioral claims.
