import { mkdir, writeFile } from "node:fs/promises";
import path from "node:path";

const markerPath = path.join(
  process.cwd(),
  "gen/python/pulsefield/protocol/py.typed",
);

await mkdir(path.dirname(markerPath), { recursive: true });
await writeFile(markerPath, "\n");
