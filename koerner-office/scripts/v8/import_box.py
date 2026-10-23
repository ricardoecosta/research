"""Import answers mined on Grok Bot's box: /tmp/v8/box_answers/<vid>.json -> mined/<vid>.json via mine_one post-processing."""
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import mine
from common8 import parse_json_text
A = Path("/tmp/v8/box_answers")
def boxed(prompt, effort="xhigh", logf=None, tag=""):
    return parse_json_text((A / f"{tag}.json").read_text()), "grokbot-box", 0
mine.call_llm = boxed
for f in sorted(A.glob("*.json")):
    if (mine.OUT / f"{f.stem}.json").exists(): continue
    vid, st = mine.mine_one(f.stem)
    mine.log(mine.LOGF, f"DONE {vid} {st} (box import) total={len(list(mine.OUT.glob('*.json')))}")
    print(vid, st)
