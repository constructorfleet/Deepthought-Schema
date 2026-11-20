# External generator probe

This temporary distribution exercises the `deepthought.generators` entry-point contract without changing the Deepthought source package. Install it into the disposable environment used for the capture:

```sh
uv pip install --python "$VENV/bin/python" docs/baseline/m0/probes/external-generator
"$VENV/bin/deepthought" --help
"$VENV/bin/deepthought" m0-probe --help
"$VENV/bin/deepthought" m0-probe build --out "$OUT/external-generator"
cat "$OUT/external-generator/discovered.txt"
```

Expected: the top-level help lists `m0-probe`; its help lists `build`; the build exits 0 and writes `discovered.txt` with `external generator loaded`. Keep this package installed only in a disposable environment.
