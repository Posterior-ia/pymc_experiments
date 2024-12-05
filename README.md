# Pymc experiments

Various experiments using the python pymc3 library for Bayesian learning.

## Quick start

### Installing `uv`

The Python project manager selected is `uv`. To install the project 
dependencies, run the following command:

```bash
pip install uv
uv sync
```

### Project management

`uv` is a project manager that works in a similar way to `poetry`. 
For this reason, the commands are similar. For instance, you can add or 
delete a dependence with the following commands:

```bash 
uv add <package>
uv remove <package>
```

And then, the package `<package>` will be added or removed from the
`pyproject.toml` file. For further information, you can check the
[documentation](https://docs.astral.sh/uv/guides/projects/#managing-dependencies).
