# Sky Shrine Map Structure

## Runtime maps

The Sky Shrine uses four 48x48 runtime maps:

- Group25/Map0
- Group25/Map1
- Group25/Map2
- Group25/Map3

The 96x96 master artwork is a logical reference used to organize the complete shrine grounds.

## Verified warp network

| Source | Warp | Destination |
| --- | ---: | --- |
| Group25/Map0 | 0 | Group25/Map1 warp 0 |
| Group25/Map0 | 1 | Group25/Map2 warp 0 |
| Group25/Map1 | 0 | Group25/Map0 warp 0 |
| Group25/Map1 | 1 | Group25/Map3 warp 0 |
| Group25/Map2 | 0 | Group25/Map0 warp 1 |
| Group25/Map2 | 1 | Group25/Map3 warp 1 |
| Group25/Map3 | 0 | Group25/Map1 warp 1 |
| Group25/Map3 | 1 | Group25/Map2 warp 1 |

## Verified warp coordinates

- 25:0 warp0 X47,Y31 -> 25:1 warp0
- 25:0 warp1 X31,Y47 -> 25:2 warp0
- 25:1 warp0 X0,Y31 -> 25:0 warp0
- 25:1 warp1 X31,Y47 -> 25:3 warp0
- 25:2 warp0 X31,Y0 -> 25:0 warp1
- 25:2 warp1 X47,Y31 -> 25:3 warp1
- 25:3 warp0 X31,Y0 -> 25:1 warp1
- 25:3 warp1 X0,Y31 -> 25:2 warp1

## Entry and return

- Entry script: Group3/Map55 -> Group25/Map0 X31,Y13
- Return script: Group3/Map2 X30,Y14

## Master layout zones

The intended logical layout contains:

- Main Shrine
- Manager Building
- Old Shrine
- Waterfall
- Central Pond
- Pagoda
- Cherry Blossom Grove
- Bamboo Grove
- Maple Grove
- Southern Torii
- Central Plaza
- Bridges and connecting paths

## Design constraint

Do not collapse this network into a single 96x96 runtime fieldmap. The four-map structure exists to remain within the Emerald runtime fieldmap limits while preserving the intended large-scale composition.
