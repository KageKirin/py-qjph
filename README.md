# QJPH -- Quick Json Parser Hack

**Quick Json Parser Hack** is, as the name indicates
a quick hack to have Python parse JSON as Python.

CAVEAT: This lib relies on `eval()` with a few specific globals
to parse JSON. As such, it might not be safe against code injection attacks.

## ⚡ Usage

```python
import qjph

from_file = qjph.load("file.json")

from_string = qjph.loads("""
{
    "json": {
        "data": "value"
    }
}
""")
```

## 🔧 Building

```shell
uv build
```

## 🤝 Collaborate with My Project

Please refer to the [collaboration guidelines](./COLLABORATION.md) for details.
