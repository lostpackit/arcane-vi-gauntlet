#!/bin/bash
V4=/home/claude/cad/releases/v4/Vi_Gauntlet_X1C_V4_Print_Release
cd /home/claude/slicer
for f in "$V4"/Right_Shells/*.stl "$V4"/Lighting_Covers/R_*.stl "$V4"/Print_Hardware/*.stl; do
  b=$(basename "$f" .stl)
  prusa-slicer --export-gcode --load x1c_surrogate.ini --center 128,128 --dont-arrange -o "gcode/$b.gcode" "$f" > "gcode/$b.log" 2>&1
  python3 -I /home/claude/scripts/gstat.py "gcode/$b.gcode" >> results.jsonl 2>>errors.log
  grep -iE "warning|error|outside|exceed|empty|lost" "gcode/$b.log" | sort | uniq -c | head -5 > "gcode/$b.warn"
done
echo DONE >> results.jsonl
