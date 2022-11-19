import asyncio
import os
import sys

# This is important for ipykernel to show the same string
# instead of randomly generated file names in outputs.
# See: https://github.com/ipython/ipykernel/blob/360685c6/ipykernel/compiler.py#L50-L55
os.environ["IPYKERNEL_CELL_NAME"] = "<IPY-INPUT>"

if os.name == "nt" and sys.version_info >= (3, 7):
    asyncio.set_event_loop_policy(
        asyncio.WindowsSelectorEventLoopPolicy()  # type:ignore[attr-defined]
    )
