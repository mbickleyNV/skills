# Scoped inspection, preparation and result recovery

Project adapter note: paths and commands outside this skill directory describe
optional integration examples. They are not bundled dependencies. Locate a
maintained equivalent and verify its interface before execution; no historical
helper, local service or schema is assumed to be installed.

Run these examples through the existing Blender MCP with the user's actual task
prompt. They do not authorize a live mutation or take ownership from another task.

## Read-only inspection

```python
import runpy
helper = runpy.run_path('/absolute/project/blender/tools/inspect_remodel.py')
helper['emit'](names=['kitchen-overview'], checks=['identity', 'visibility'])
```

For CAD use `prepared='/absolute/scratch/packet/prepared.json'` instead of names.
The adapter adds the project's CAD identity/digest keys; it uses the existing
shared inspector rather than copying its logic. `limit`, `offset`, `checks`,
`baseline` and `next_offset` retain shared semantics. No implicit whole-house
inventory. Keep the complete initial result outside Blender for comparison;
do not use a delta as the next full baseline. Missing objects and per-object
errors must be read before interpreting unchanged output.

## Explicit dependency preparation

```json
{
  "schema": "scoped-cad-installation/2",
  "selected": ["fixture-opening"],
  "scopes": [
    {"id": "fixture-opening", "kind": "ordinary-cad", "room": "entry",
     "parts": ["upper_plaster_cove_ceiling"], "requires": ["adjoining-ceiling"]},
    {"id": "adjoining-ceiling", "kind": "ordinary-cad", "room": "living",
     "parts": ["upper_plaster_cove_ceiling"]}
  ]
}
```

The example illustrates syntax, not a declaration that these parts always depend
on one another. `requires` means “include this scope whenever this scope is
selected.” The caller records actual affected dependencies from the source
contract. Missing references, cycles and unsupported producer kinds fail before
staging. Same-room scopes merge into one admitted part set; explicit material maps
must cover that complete set. Only ordinary CAD is admitted; tile/GN dependencies
must be prepared separately using their supported producer route. Unknown
procedural dependencies are not considered unchanged because CAD hashes match.

Run `python3 blender/tools/prepare_house_import_batches.py --manifest scope.json
--output scratch/my-task/prepared` from the project root. This branch bypasses the
broad house delta and unrelated synchronization. Use an empty output directory;
prepared packets cannot be overwritten. Source topology checks and live
material/normal/bounds gates remain active. Source preparation may maintain the
existing affected-room source inventory; it does not rebuild CAD or edit Blender.

## Structured application and recovery

```python
import json, runpy
helper = runpy.run_path('/absolute/project/blender/tools/apply_prepared_installation.py')
result = helper['apply']('/absolute/prepared.json', '/absolute/project/scratch/task/import-result.json')
print(json.dumps(result))
```

The helper takes the shared batch lock, refuses active captures, validates all
packets, and journals each room import before/after execution. It does not save,
publish or render. Existing object identity and material/normal validation remain
owned by the original importer. Each step reports phase, completed state,
source/owner context and exception traceback. Imports are not atomic rollback
transactions: an exception inside a room can leave partial work.

The receipt is `operation-result/1`. `completed_operations` means the callable
returned, not that a renderer accepted the change. `result_failed` means only
result serialization failed after it returned. `uncertain` means execution raised
and may have changed state. `running` after loss of control is also uncertain;
check for an active owner before attempting recovery. Never automatically retry.
Reusing a receipt with the same input/scene identity returns its prior result;
different inputs fail. Read receipts directly after scene reload rather than
trying to apply with the old scene UID.

Generic helpers can use `operation_receipts.run_operation(...)` with explicit
steps while holding their ownership lock. A save step must return only after its
own save/readback verification. The runner cannot infer whether arbitrary Blender
code saved successfully. A receipt cannot eliminate the crash window between a
mutation and its final disk acknowledgment; uncertain is deliberately retained.

The MCP transport still wraps output as text. Parse the returned JSON, and treat
outer `Error executing code:` responses as failures even if MCP `isError` is false.
This change does not replace the host's arbitrary-code tool or require a server
restart. A lost response is not permission to repeat a completed import/save.
