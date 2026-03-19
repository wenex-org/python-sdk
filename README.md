# Python SDK

Environment

```sh
# hatch env remove default
hatch env create default
hatch shell default
```

Installation

```sh
pip install -e "."
pre-commit install
```

## Build and Deploy

```sh
pip install build twine
uv build && uv publish
```

## License

`wenex` is distributed under the terms of the [Apache-2.0](https://spdx.org/licenses/Apache-2.0.html) license.
