import os

# This is important for ipykernel to show the same string
# instead of randomly generated file names in outputs.
# See: https://github.com/ipython/ipykernel/blob/360685c6/ipykernel/compiler.py#L50-L55
os.environ["IPYKERNEL_CELL_NAME"] = "<IPY-INPUT>"

# Opt in to JUPYTER_PLATFORM_DIRS
os.environ["JUPYTER_PLATFORM_DIRS"] = "1"
