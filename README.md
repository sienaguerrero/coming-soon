# coming-soon

The siena.codes Under construction page, packaged as a GitHub Action. Any GitHub Pages repo can switch to it with one repo variable and switch back without a code change.

## Use it in a Pages workflow

Put the action between the build and the upload, and upload whatever folder it hands back:

```yaml
      - id: soon
        uses: sienaguerrero/coming-soon@v1
        with:
          path: site
          enabled: ${{ vars.COMING_SOON }}
      - uses: actions/upload-pages-artifact@v5
        with:
          path: ${{ steps.soon.outputs.path }}
```

`path` is the folder your build already uploads. When `enabled` is `true`, the action writes the Under construction page to a temporary folder as both `index.html` and `404.html`, so every URL on the site lands on it. Otherwise it passes `path` through untouched. Tests and other build steps still run either way.

Optional inputs: `title`, `message`, `back-url` (an `https://` link or a same-site path like `/`), and `back-label`. Text is HTML-escaped. The page shows the site's own hostname, is marked `noindex`, and needs no JavaScript beyond filling in that hostname.

## Switch a site

Take it offline:

```bash
gh variable set COMING_SOON --body true -R sienaguerrero/<repo> && gh workflow run pages -R sienaguerrero/<repo> --ref main
```

Bring it back:

```bash
gh variable set COMING_SOON --body false -R sienaguerrero/<repo> && gh workflow run pages -R sienaguerrero/<repo> --ref main
```

## Preview locally

```bash
python3 render.py --out _preview && python3 -m http.server 4223 --directory _preview
```

## Releasing

Consumers pin `@v1`. After a change lands on `main`, move the tag:

```bash
git tag -f v1 && git push -f origin v1
```
