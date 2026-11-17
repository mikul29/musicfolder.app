// User Guide events (assets/guide.js → /ev). Pure, so worker/tap.test.js can test it.
// Only these types; the page must be a guide page; the value is a search query (letters, digits,
// spaces, a few symbols, ≤ 60 chars) or a site path. Anything else is dropped, never stored raw.

const TYPES = new Set(["search", "noresult", "open", "nav", "contact", "read"]);

export function guideEvent(params) {
  const type = params.get("t");
  const page = String(params.get("p") ?? "");
  if (!TYPES.has(type) || !/^\/guide(\/[a-z0-9-]{1,80})?$/.test(page)) return null;
  let value = String(params.get("v") ?? "").toLowerCase().replace(/\s+/g, " ").trim().slice(0, 60);
  if (type === "search" || type === "noresult") {
    value = value.replace(/[^a-z0-9 #+.\-]/g, "").trim();
    if (value.length < 2) return null;
  } else if (type === "read") {
    value = "";
  } else if (!/^\/[a-z0-9/._#-]{0,99}$/.test(value)) {
    return null;
  }
  const n = Number.parseInt(params.get("n") ?? "0", 10);
  const count = Number.isFinite(n) && n >= 0 && n < 100 ? n : 0;
  return { type, page, value, count };
}
