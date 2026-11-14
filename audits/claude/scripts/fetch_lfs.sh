#!/bin/bash
# usage: fetch_lfs.sh <repo-relative path>
p="$1"
oid=$(git show "HEAD:$p" | sed -n 's/^oid sha256://p')
enc=$(python3 -I -c "import sys,urllib.parse;print(urllib.parse.quote(sys.argv[1]))" "$p")
for i in 1 2 3; do
  curl -sS -L --fail -o "$p.part" "https://media.githubusercontent.com/media/lostpackit/arcane-vi-gauntlet/main/$enc" || { sleep 5; continue; }
  got=$(sha256sum "$p.part" | cut -d' ' -f1)
  if [ "$got" = "$oid" ]; then mv "$p.part" "$p"; echo "OK $p"; exit 0; fi
  sleep 5
done
rm -f "$p.part"; echo "FAIL $p"
