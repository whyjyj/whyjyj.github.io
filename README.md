# Yoonjae Baek's Homepage

This repository contains the source code for [my homepage](https://whyjyj.github.io).

Built with [al-folio](https://github.com/alshedivat/al-folio).

## Local development

```bash
bin/serve   # http://localhost:4000
```

`bin/serve` layers `_config_dev.yml` on top of `_config.yml` so that local page views
are not sent to Google Analytics. The deploy workflow runs a plain `jekyll build`.
