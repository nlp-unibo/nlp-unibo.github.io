// DOM-free helpers of assets/js/ltlab.js, tested by scripts/test_ltcore.mjs. Hugo bundles them into ltlab.js.

// The step of an arrow key: 1 for ArrowRight, -1 for ArrowLeft, 0 for any other key.
export const arrowStep = (key) => ({ ArrowRight: 1, ArrowLeft: -1 })[key] || 0;

// The slide an index names among `count` slides: it wraps around when `loop` is set, and stops at the ends otherwise.
export const slideIndex = (index, count, loop) => (loop ? ((index % count) + count) % count : Math.max(0, Math.min(count - 1, index)));

// A hash naming a path of the Work with us page, or a place inside it such as #thesis-contact or #thesis-step-1, as
// { path, place }; null for any other hash. `place` is null when the hash names the path alone.
export const parsePlace = (hash) => {
  const match = hash.match(/^#([a-z0-9-]+?)(?:-(contact|about|inspiration|step-\d+))?$/);
  return match ? { path: match[1], place: match[2] || null } : null;
};

// Whether an item whose filter attribute holds the space-separated `values` fits the pressed filter `value`; an empty
// value (the "All" button) fits every item.
export const fits = (values, value) => !value || (values || "").split(" ").includes(value);

// The label of a button whose text ends with a count, such as "Speech (6)", or null when the text has no count.
export const countLabel = (text) => {
  const match = text.match(/^(.*?)\s*\((\d+)\)$/s);
  return match ? match[1].trim() : null;
};

// The index of the offset nearest to `position`; on a tie the first one wins.
export const nearest = (offsets, position) =>
  offsets.reduce((best, offset, index) => (Math.abs(offset - position) < Math.abs(offsets[best] - position) ? index : best), 0);

// The focus line of the section focus, in viewport pixels: it follows the scroll down to 40% of the viewport, moves
// further down as the page end nears (`below` is the scroll left), and never sits above the first section.
export const focusLine = ({ firstTop, scrollY, viewport, below }) =>
  Math.max(firstTop, Math.min(scrollY, viewport * 0.4) + Math.max(0, viewport * 0.4 - below) * 1.5);

// The focus value of a section from 0 to 1: 1 while it holds the focus line, fading to 0 over `fade` pixels away.
export const focusValue = (top, bottom, line, fade) => {
  const distance = line < top ? top - line : line > bottom ? line - bottom : 0;
  return Math.max(0, 1 - distance / fade);
};
