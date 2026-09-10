# Opik Self-Hosting Handbook

A Google Codelabs-style, 7-step handbook for self-hosting Opik locally with Docker.

## Project layout

```
opik-handbook/
├── index.html              # the codelab shell (loads steps from content/)
├── content/
│   ├── manifest.json       # step order + sidebar titles (edit to reorder/add)
│   ├── 01-overview.html     ← edit these files to change the content
│   ├── 02-install-docker.html
│   ├── 03-get-opik.html
│   ├── 04-start-opik.html
│   ├── 05-connect-sdk.html
│   ├── 06-trace-llm.html
│   └── 07-wrap-up.html
├── scripts/opik_inference.py   # run inference on any LLM, traced by Opik
├── build.py                # bundle everything into one shareable file
├── dist/index.html         # generated single-file build (after build.py)
└── progress.md             # sprint plan / status tracker
```

## Editing content (live)

Each step is its own file in `content/`. **Edit a file, save, refresh the browser** and the
change is on screen. Because browsers block `fetch()` over `file://`, run the included server:

```bash
cd opik-handbook
python3 serve.py            # open http://localhost:8000
```

> Use `serve.py`, not `python3 -m http.server`. The built-in server omits the UTF-8
> charset header, which makes browsers mis-decode emoji and punctuation
> (🎉 → `ðŸŽ‰`, · → `Â·`). `serve.py` sends `charset=utf-8` so text renders correctly.

- Change wording, commands, callouts → edit the matching `content/NN-*.html` file.
- Add, remove, or reorder steps → edit `content/manifest.json`.
- Add a screenshot → drop it in an `img/` folder and replace a `.shot` block with
  `<img src="./img/your-shot.png" alt="...">`.

## Sharing a single file

To hand someone one self-contained `.html` (no server, no folder), bundle it:

```bash
python3 build.py        # writes dist/index.html with all steps inlined
```

## The inference script

`scripts/opik_inference.py` calls any LLM via LiteLLM and logs the trace to your local Opik.
Pick a provider with env vars — see the header of that file for OpenAI / Anthropic / Ollama examples.
