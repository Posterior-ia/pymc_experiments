# Pymc experiments

Various experiments using the python pymc3 library for Bayesian learning.

## Quick start

### Installing `uv`

The Python project manager selected is `uv`.
You can install it following the instructions in the 
[documentation](https://docs.astral.sh/uv/getting-started/installation/).
To install the project dependencies, run the following command:

```bash
uv sync
```
### Example Notebook

In the [`notebooks/first_pymc_example.ipynb`](notebooks/first_pymc_example.ipynb) file, you can find an implementation of the official PyMC linear regression tutorial. You can refer to the [tutorial](https://www.pymc.io/projects/docs/en/stable/learn/core_notebooks/GLM_linear.html) for more details.

### Project management

`uv` is a project manager that works in a similar way to `poetry`. 
For instance, you can add or delete a dependence with the following 
commands:

```bash 
uv add <package>
uv remove <package>
```

And then, the package `<package>` will be added or removed from the
`pyproject.toml` file. For further information, you can check the
[documentation](https://docs.astral.sh/uv/guides/projects/#managing-dependencies).
