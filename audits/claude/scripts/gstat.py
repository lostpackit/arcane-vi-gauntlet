import sys, re, json, math
f = sys.argv[1]; typ = 'none'; E = {}; foot = {}; maxz = 0
for line in open(f, errors='ignore'):
    if line.startswith(';TYPE:'): typ = line[6:].strip(); continue
    if line.startswith('G1'):
        m = re.search(r' E(-?[\d.]+)', line)
        if m and (' X' in line or ' Y' in line):
            e = float(m.group(1))
            if e > 0: E[typ] = E.get(typ, 0) + e
    elif line.startswith('; ') and '=' in line:
        k, v = line[2:].split('=', 1); k = k.strip()
        if k in ('filament used [mm]','filament used [cm3]','filament used [g]','total filament used [g]','estimated printing time (normal mode)'): foot[k] = v.strip()
a = math.pi*(1.75/2)**2
g = {k: round(v*a/1000*1.24, 1) for k, v in E.items()}
print(json.dumps(dict(file=f.split('/')[-1], footer=foot, grams_by_type=g)))
