# Electronics and string-actuation constraints

## Lighting
Goal: individually addressable **animated** LEDs rather than static lighting, with wearable button selection of effects. ESP32-class controller is a candidate, not a selected board.

Before buying or cutting parts, measure the circular channel's actual usable width, depth, circumference, corner radii and wire exit. Compare against **actual datasheets or samples** of candidate LED strips; nominal 10 mm strip width is not proof of fit. Also assess bend radius, density, voltage/current, diffuser spacing, power injection, thermal constraints and wire clearance.

## Controls and power
Specify physical board, switches, protected battery/pack, wiring gauge, connectors, charging arrangement, fuse/protection and access hatch before making permanent cavities. Keep the battery accessible and use appropriate protected electronics.

## Strings
Five candidate 4 mm OD PTFE routes were proposed, but have not been proven end-to-end. Check entry/exit locations, finger attachments, bend radii, friction, string travel and ability to rethread after assembly. Do not bond a seam that blocks a critical route.

## Electronics design package for Claude review (2026-11-14)

See [electronics/README.md](../electronics/README.md), [BOM](../electronics/BOM.md), [six effects and buttons](../electronics/EFFECTS.md), [wiring diagram](../electronics/WIRING.md), [WLED presets](../electronics/wled/presets.json), and [standalone reference firmware](../electronics/firmware/src/main.cpp). These are **proposed and untested**. The independent V4 audit found lighting FAIL; V5 is the active unprinted draft and its accent/crystal mounting remains unresolved. Do not purchase or modify CAD without owner approval.
