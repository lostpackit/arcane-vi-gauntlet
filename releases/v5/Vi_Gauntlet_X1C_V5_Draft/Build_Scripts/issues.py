import subprocess, json, sys
R = 'repos/lostpackit/arcane-vi-gauntlet'
def api(method, path, body=None):
    cmd = ['gh', 'api', '-X', method, f'{R}/{path}'] + (['--input', '-'] if body is not None else [])
    r = subprocess.run(cmd, input=json.dumps(body) if body is not None else None, capture_output=True, text=True)
    if r.returncode: print('ERR', path, r.stdout[:200], r.stderr[:200]); return None
    return json.loads(r.stdout) if r.stdout.strip() else {}
for name, color, desc in (('cad', '1d76db', 'Model geometry'), ('electronics', 'fbca04', 'LEDs, wiring, power'), ('firmware', '5319e7', 'WLED / ESP32 code'), ('physical-test', 'd93f0b', 'Needs a real print or bench test'), ('owner-action', 'b60205', 'Needs the owner or a local agent'), ('simulation', '0e8a16', 'Checked by computation only'), ('low-priority', 'c5def5', 'Cosmetic or optional')):
    api('POST', 'labels', dict(name=name, color=color, description=desc))
V = 'releases/v5/Vi_Gauntlet_X1C_V5_Draft'
F = '\n\n_Opened by Claude from the 2026-11-15 project review. Simulation evidence: `' + V + '/V5_2_SIMULATION_REPORT.md`. Nothing has been printed or bench-tested by an agent._'
issues = [
 ('Upload V5.2 files (shell 08 both arms, mount concepts) and retire shell 08 V5.1', ['cad', 'owner-action'],
  f"Claude's session cannot upload Git LFS objects.\n\n- [ ] Unzip `V5_2_changed_files.zip` over `{V}/`\n- [ ] `sha256sum -c V5_2_SHA256_MANIFEST.txt` (expect 4 OK)\n- [ ] Commit and push (LFS)\n- [ ] `git mv` the two `*_08_*_V5_1.3mf` files into `Superseded_V5_DO_NOT_PRINT/` and fix their paths in `V5_1_SHA256_MANIFEST.txt`\n- [ ] Confirm `Right_Shells/` and `Left_Shells/` each hold exactly 13 files\n\nWhy: V5.2 shell 08 widens the wire link from the ring trough to the hand LED channel from 2 mm to 4 mm.", None),
 ('Slice the V5.x print set in Bambu Studio and record per-part results', ['physical-test', 'owner-action'],
  "No agent has run Bambu Studio. All filament and support numbers so far come from a PrusaSlicer surrogate.\n\n- [ ] Slice all 13 right shells with the real X1C profile and the LW-PLA profile actually used\n- [ ] Record filament, time, supports per part in `notes/04_Test_Log.md`\n- [ ] Check layer preview of shells 05, 06, 08, 12, 13 (the surrogate reported unreachable support branches there)\n- [ ] Check bed keep-out zones for shells 10/11 (181 x 225 mm footprint)\n- [ ] Compare 2 walls / 8 % with other settings for weight\n\nSurrogate reference at 2 walls / 8 % gyroid, standard PLA: 3,843 g per arm including 760 g support.", None),
 ('T-1: ring light fit with the real LED strip', ['physical-test', 'electronics'],
  "- [ ] Print `R_Ring_Light_Cover_translucent` and either `R_08_..._V5_2` or the original `Circle_Light.stl` stand-in\n- [ ] Measure printed trough: width (CAD 27.1 mm) and wall height under the seated cover (CAD about 13.0 mm)\n- [ ] Seat 50 LEDs of the 7.2 mm 144 LEDs/m strip on the outer wall; joint at the notch\n- [ ] Wires out through the notch; cover seats fully; cover and gauge lift out by hand\n- [ ] Leave 24 h, power up, check for dead pixels\n- [ ] Judge the halo with the gauge on; decide whether the gauge should be printed translucent\n\nSimulation: strip modelled as a solid fits with zero interference and 5.6 mm clear under the cover.", None),
 ('T-2: finger coupon and string pull', ['physical-test'],
  f"Digital fit passes: finger cores clear V5.1 shells 12/13 by 0.8-1.8 mm and slot pieces overlap by at most 0.15 mm (press fit). This print confirms it before about 480 g per knuckle shell is committed.\n\n- [ ] Print `{V}/Test_Coupons/T2_Knuckle_Slot_Forefinger_Coupon.3mf`\n- [ ] Seat a printed forefinger core and slot piece without filing\n- [ ] Pass a cord through the string bore (modelled 3.4-3.8 mm; it prints horizontally and will close up) and check free return\n- [ ] Full curl and release with a pull ring; note force and travel\n- [ ] Record in `notes/04_Test_Log.md`", None),
 ('Dowel fit and seam alignment in LW-PLA', ['physical-test'],
  "- [ ] Print `R_07` and `R_09` (both fit the A1 Mini with a brim of 7 mm or less)\n- [ ] Try 6 x 30 mm dowels in the 6.4 mm sockets; foaming filament may close them\n- [ ] When `R_08` exists, dry-fit 07 | 08 | 09 and check the seam faces close\n- [ ] If sockets are tight, record the drill size or XY compensation that works\n\nSimulation: 57 dowels placed with zero interference and 0.2 mm minimum radial gap; no socket shallower than 15 mm per side.", None),
 ('Handle: print, socket fit and load check', ['physical-test'],
  "The handle is one 18.8 x 250 mm bar in 19.3 mm sockets with collars (12.3 mm engagement each side). It must go in before shells 10 and 11 are joined.\n\n- [ ] Print the handle in standard PLA or PETG lying flat (not LW-PLA), or cut an 18-19 mm tube or dowel to 250 mm\n- [ ] Check it enters both sockets\n- [ ] After bonding 10 | 11, hang at least 3x the expected gauntlet weight from mid-span\n\nSimulation: zero interference, 0.25 mm radial gap.", None),
 ('Gauge and cover retention: decide method', ['cad', 'owner-action'],
  "The gauge sits on the light cover and nothing holds it down.\n\nTried: 6 x 2 mm magnet pockets. Dropped, because the gauge only touches the shell on narrow rims (no flat contact area for a magnet).\n\nRecommended: glue the gauge to the cover so they lift out as one cap, and hold the cap with two or three dots of removable mounting putty.\n\n- [ ] Owner: accept this, or ask for a mechanical latch (needs new geometry in shell 08 and the gauge)\n- [ ] Test on the first printed shell 08", None),
 ('Electronics mounts: validate concepts against purchased hardware', ['cad', 'electronics'],
  f"Concept parts in `{V}/Mounts_CONCEPT/` (after upload):\n- Button pod: snap-on clip for the 18.8 mm handle with pockets for two 12 x 12 mm tactile switches\n- Electronics sled: 80 x 45 mm rimmed tray with zip-tie slots, fixed with hook-and-loop to the cuff wall\n\nBoth were sized from catalogue dimensions.\n\n- [ ] Measure the real switches, controller board, level shifter and power bank\n- [ ] Print the pod; check snap-on force on the handle and thumb reach while gripping\n- [ ] Adjust pocket and tray sizes in `Build_Scripts/mounts.py` and regenerate\n- [ ] Decide power bank location (cuff wall or belt) and add a cradle if wanted", None),
 ('Choose the controller board and fix the pin map', ['electronics', 'owner-action'],
  "The reference wiring and firmware use an ESP32-WROOM DevKit (GPIO 16 / 25 / 26). A XIAO ESP32-C3/S3 is smaller but has different pins.\n\n- [ ] Owner: pick the board\n- [ ] Update `electronics/WIRING.md`, the `-DLED_PIN/-DMODE_PIN/-DACTION_PIN` flags and WLED pin settings to match", None),
 ('WLED on the device: effects, presets, current limit', ['firmware', 'electronics', 'physical-test'],
  "`electronics/wled/presets_144.json` has never been loaded on a device.\n\n- [ ] Flash WLED; set 83 LEDs, WS281x, colour order (expect GRB), current limit 1000 mA\n- [ ] Import the presets; confirm segments ring [0,50), hand [50,73), crystal [73,83)\n- [ ] Open `/json/eff` and choose the chase and surge effects by name (IDs 13 and 15 in the file are probably not the intended look); re-save presets 3 and 4\n- [ ] Assign button macros 21-25; check short / long / double press\n- [ ] Confirm the 0.4 s flash burst (preset 8) returns to idle\n- [ ] Tune speeds for 50 ring pixels", None),
 ('Standalone firmware: real ESP32 build and bench test', ['firmware', 'physical-test'],
  "`electronics/firmware/src/main.cpp` passes a PC logic check only (83, 50 and 35 pixel builds).\n\n- [ ] `pio run -e ring144` and `-e full144`\n- [ ] Flash; test with 3-5 pixels first\n- [ ] Compare measured current with the software limiter's estimate\n- [ ] Check button feel", None),
 ('LED current and temperature test in the closed ring', ['electronics', 'physical-test'],
  "- [ ] Measure current at each preset and at the 1000 mA limit\n- [ ] 30 minutes at the limit with cover and gauge fitted; no surface above about 45 C\n- [ ] Check power bank low-current shut-off behaviour\n- [ ] Only then consider raising the limit", None),
 ('Thumb: mount and string route are not resolved', ['cad'],
  "The audit found four finger string bores but no thumb bore, and the thumb base is not part of the shells.\n\n- [ ] Owner: is the thumb string-actuated?\n- [ ] Locate the thumb base seat on shell 13 and check it against the printed thumb\n- [ ] Design a string route if needed", None),
 ('Reduce supports: re-orient shells 05, 06, 08, 12, 13', ['cad', 'simulation'],
  "Supports are about 20 % of the filament (roughly 105-130 g on each of these shells) and three shells give unreachable-branch warnings with build-plate-only supports.\n\n- [ ] Evaluate alternative orientations or split-free support blockers in Bambu Studio\n- [ ] Keep dowel faces printable", None),
 ('Cosmetic: centre seam crosses visible top details', ['cad', 'low-priority'],
  "The X = 211 seam runs through the top plate, crystal base and hand lens line. The crystal and lens inserts bridge and hide part of it. Moving the seam would change shells 05-06 and 10-13 and all their dowels, so it is parked unless the owner wants it.", None),
 ('Wire link from ring trough to hand LED channel too narrow (V5.1)', ['cad', 'simulation'],
  "Found by simulation: in V5.1 the largest sphere that passes from the trough to the hand channel is 2.0 mm, too small for three wires.\n\nFixed in V5.2 shell 08 with a 9 mm wide wire slot at trough-floor level: now 4.0 mm. Trough to arm cavity passes 11 mm in both.", 'Fixed in V5.2 (shell 08). Evidence: `V5_2_SIMULATION_REPORT.md` section 4. File upload is tracked in the V5.2 upload issue.'),
 ('Audit C-3: finger mount revision mismatch', ['cad', 'simulation'],
  "The audit found the printable 3MF `Fingers_Base` differs from the finger base fused into the shells and rated it critical.", 'Resolved digitally: the finger cores and slot pieces being printed match the assembled reference by volume and clear V5.1 shells 12/13 in position (0.8-1.8 mm gap; slot pieces at most 0.15 mm press overlap). V5 does not use the stand-alone `Fingers_Base`. Physical confirmation is tracked in the T-2 coupon issue.'),
 ('Hand LED count: channel holds 33 LEDs, not 34', ['electronics', 'simulation'],
  "A 34-LED strip (236 mm) modelled as a solid collides with the ends of the 232.5 mm deepened channel.", 'Fixed: layout is 83 per arm (ring 50 + hand 33). Firmware default, `presets_144.json` and `ORDER_LIST.md` updated; PC firmware check passes.'),
]
out = []
for title, labels, body, close in issues:
    r = api('POST', 'issues', dict(title=title, body=body + F, labels=labels))
    if not r: continue
    n = r['number']; out.append((n, title, 'closed' if close else 'open'))
    if close:
        api('POST', f'issues/{n}/comments', dict(body=close)); api('PATCH', f'issues/{n}', dict(state='closed', state_reason='completed'))
    print(n, 'closed' if close else 'open', title)
json.dump(out, open('/home/claude/out/issues_created.json', 'w'), indent=1)
