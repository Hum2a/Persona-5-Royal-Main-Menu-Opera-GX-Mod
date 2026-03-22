# Persona 5 Royal — Main Menu

Opera GX mod themed after **Persona 5 Royal**’s main menu: **Royal Days** background music, full **browser UI sounds**, **keyboard sounds**, a **red and black** GX theme, **animated wallpapers** for dark and light modes, and **web modding** so pages pick up a matching crimson-on-black look.

**Author:** Humza · **Version:** 1.1.0 · **Manifest:** `manifest_version` 3, `mod.schema_version` 1

---

## Preview

Light-mode wallpaper asset (**WebM** — same clip as in the mod’s light theme):

<!-- If your default branch is `main`, replace `master` with `main` in the URLs below. -->
<video controls muted playsinline width="100%" style="max-width: 720px; border-radius: 8px;" poster="https://raw.githubusercontent.com/Hum2a/Persona-5-Royal-Main-Menu/master/wallpaper/first_frame2.png">
  <source src="https://raw.githubusercontent.com/Hum2a/Persona-5-Royal-Main-Menu/master/wallpaper/screen2.webm" type="video/webm" />
  Your browser does not support embedded WebM. Open <a href="./wallpaper/screen2.webm"><code>wallpaper/screen2.webm</code></a> locally.
</video>

Dark mode uses **`wallpaper/screen1.mp4`** (not shown here to keep the README on a WebM-friendly embed).

---

## Features

| Area | Details |
|------|---------|
| **Wallpaper** | Dark: `screen1.mp4` + `first_frame1.png`. Light: `screen2.webm` + `first_frame2.png`. Custom clock text colours per mode. |
| **Music** | `music/RoyalDays.mp3` as background music. |
| **Browser sounds** | All standard GX events: click (with `click` + `select` variants), hovers, tab open/close/slash, limiter, switches, level upgrade, important click, etc. (`sound/*.mp3`) |
| **Keyboard** | `TYPING_LETTER` (3 variants), backspace, enter, space (`keyboard/*.wav`) |
| **Theme** | HSL accent ~355° red; dark near-black secondary; light mode tuned companion colours. |
| **Web modding** | `webmodding/p5-royal-global.css` on all `http(s)` pages, plus `sites-01`–`sites-07` for extra rules on many popular domains. |

---

## Repository layout

```text
manifest.json          # Opera GX mod manifest
license.txt            # Author + fan-project disclaimer
icon_512.png           # Mod icon
music/                 # Background music
sound/                 # Browser UI sounds (.mp3)
keyboard/              # Keyboard sounds (.wav)
wallpaper/             # Video wallpapers + first-frame stills
webmodding/            # Injected page CSS (global + site bundles)
scripts/               # check_file_sizes.py (size limit helper)
.githooks/             # Optional pre-commit hook (see below)
.github/workflows/     # CI: JSON + assets + schema + file-size checks
```

---

## Installing the mod (Opera GX)

1. Zip **this folder’s contents** (so `manifest.json` is at the root of the zip), or use the folder as Opera expects for local mods.
2. In **Opera GX**, open the mods / GX corner area and **install** or **load** the mod from that package (exact UI wording can vary by version).
3. Enable the mod and adjust **GX colours** if you want; the mod already sets accent/secondary HSL values.

---

## Development

### Pre-commit file-size check

Git cannot ignore files by size. This repo includes a hook that blocks commits over **~100 MiB** per file (GitHub’s usual non-LFS limit):

```bash
git config core.hooksPath .githooks
```

Requires **Python** on your PATH for the check to run.

### Large `screen1.mp4`

If **`wallpaper/screen1.mp4`** is too large for normal Git, use **[Git LFS](https://git-lfs.com/)** (`git lfs track "wallpaper/screen1.mp4"`) and commit `.gitattributes` with the LFS rules.

### CI

On push/PR to **`main`** or **`master`**, the workflow validates `manifest.json`, checks that expected asset paths exist, verifies core `mod.payload` keys, and runs `scripts/check_file_sizes.py --tracked`.

---

## Disclaimer

This is an independent **fan project**, not affiliated with Opera, Atlus, or Sega. See **`license.txt`** for wording and trademark notes.

---

## Persona / Atlus

*Persona 5 Royal* and related marks belong to **Atlus** and their respective owners.
