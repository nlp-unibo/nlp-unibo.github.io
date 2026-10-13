// Checks of the DOM-free helpers that assets/js/ltlab.js imports: node --test scripts/test_ltcore.mjs
import { test } from "node:test";
import assert from "node:assert/strict";
import { arrowStep, countLabel, fits, focusLine, focusValue, nearest, parsePlace, slideIndex } from "../assets/js/lt-core.mjs";

test("arrow keys step one place; other keys do not step", () => {
  assert.equal(arrowStep("ArrowRight"), 1);
  assert.equal(arrowStep("ArrowLeft"), -1);
  assert.equal(arrowStep("Enter"), 0);
});

test("a looping index wraps at both ends; a bounded one stops", () => {
  assert.equal(slideIndex(3, 3, true), 0);
  assert.equal(slideIndex(-1, 3, true), 2);
  assert.equal(slideIndex(3, 3, false), 2);
  assert.equal(slideIndex(-1, 3, false), 0);
  assert.equal(slideIndex(1, 3, false), 1);
});

test("a path hash names the path and an optional place inside it", () => {
  assert.deepEqual(parsePlace("#thesis"), { path: "thesis", place: null });
  assert.deepEqual(parsePlace("#thesis-step-12"), { path: "thesis", place: "step-12" });
  assert.deepEqual(parsePlace("#open-project-contact"), { path: "open-project", place: "contact" });
  assert.equal(parsePlace("#Thesis"), null);
  assert.equal(parsePlace(""), null);
});

test("an item fits a filter value among its space-separated values; no value fits all", () => {
  assert.ok(fits("speech argument-mining", "speech"));
  assert.ok(!fits("speech", "spee"));
  assert.ok(!fits(undefined, "speech"));
  assert.ok(fits(undefined, ""));
});

test("a counted button label is the text before its count", () => {
  assert.equal(countLabel("Speech (6)"), "Speech");
  assert.equal(countLabel("Argument\n  mining (12)"), "Argument\n  mining");
  assert.equal(countLabel("All"), null);
});

test("the nearest offset to a scroll position wins; ties keep the first", () => {
  assert.equal(nearest([0, 500, 1000], 740), 1);
  assert.equal(nearest([0, 500, 1000], 760), 2);
  assert.equal(nearest([0, 500], 250), 0);
});

test("the focus line follows the scroll down to 40% of the viewport and moves down near the page end", () => {
  assert.equal(focusLine({ firstTop: 0, scrollY: 100, viewport: 1000, below: 5000 }), 100);
  assert.equal(focusLine({ firstTop: 0, scrollY: 900, viewport: 1000, below: 5000 }), 400);
  assert.equal(focusLine({ firstTop: 0, scrollY: 900, viewport: 1000, below: 0 }), 1000);
  assert.equal(focusLine({ firstTop: 600, scrollY: 0, viewport: 1000, below: 5000 }), 600);
});

test("a section holding the focus line has full focus, which fades over the fade distance", () => {
  assert.equal(focusValue(100, 500, 300, 350), 1);
  assert.equal(focusValue(475, 900, 300, 350), 0.5);
  assert.equal(focusValue(-400, -50, 300, 350), 0);
});
