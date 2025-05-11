import sys
import os

# Add HEX paths
sys.path.append(os.path.abspath("../HexRoot"))
sys.path.append(os.path.abspath("../HexLib"))
sys.path.append(os.path.abspath("../HexDropper-Lite"))
sys.path.append(os.path.abspath("../HexClick"))
# sys.path.append(os.path.abspath("../HexTrackr"))

from hexstack.stack import HexStack
from hexstack.config import STACK_SEQUENCE

if __name__ == "__main__":
    print("[HexStack] Running bot chain...")
    HexStack(STACK_SEQUENCE).run()
