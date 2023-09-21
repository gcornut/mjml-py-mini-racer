# mjml-py-mini-racer

Wrapper for JS `mjml` lib using `py-mini-racer` to provide a Python API.

TODO:
- Add documentation on Python API usage
- Add unit tests
- Test importing lib from another project
- Publish on PIP

## Setup

Setup project for local development:

0. Install python3 and node v16 (or newer)
1. (Optional) setup venv
   ```
    python3 -m venv venv
    export PATH=$(pwd)/venv/bin:$PATH
    pip install pip-tools
    ```
2. Install (python & js dependencies)
   ```
   make install
   ```

## Build package

Build JS bundle & build the python package.

```
make build
```
