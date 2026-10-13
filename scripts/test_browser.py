"""Browser checks of assets/js/ltlab.js on the fixture build of scripts/test_render.py, in headless Chromium.
First run: uv run playwright install chromium. Run: uv run python scripts/test_browser.py"""

import functools
import http.server
import importlib.util
from pathlib import Path
import threading

from playwright.sync_api import Page, sync_playwright

spec = importlib.util.spec_from_file_location("test_render", Path(__file__).with_name("test_render.py"))
test_render = importlib.util.module_from_spec(spec)
spec.loader.exec_module(test_render)

PAGES = ["/", "/publication/", "/news/", "/projects/", "/work-with-us/", "/research/", "/people/"]
TRACK = '[aria-label="Latest papers"]'


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args) -> None:
        pass


def serve(root: Path) -> str:
    handler = functools.partial(QuietHandler, directory=str(root))
    server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    return f"http://127.0.0.1:{server.server_address[1]}"


def active(page: Page) -> int:
    return page.eval_on_selector(TRACK, "t => [...t.querySelectorAll(':scope > .lt-slide')].findIndex(s => s.classList.contains('is-active'))")


def centered(page: Page, index: int) -> bool:
    """Whether slide `index` sits in the middle of the track, within 2 px."""
    return page.eval_on_selector(TRACK, """(t, i) => { const s = t.querySelectorAll(':scope > .lt-slide')[i].getBoundingClientRect();
        const r = t.getBoundingClientRect(); return Math.abs((s.left + s.right) / 2 - (r.left + r.right) / 2) < 2; }""", index)


def click_visible(page: Page, index: int) -> None:
    """Click the middle of the part of slide `index` that the viewport shows."""
    box = page.locator(f"{TRACK} > .lt-slide").nth(index).bounding_box()
    left, right = max(box["x"], 60), min(box["x"] + box["width"], page.viewport_size["width"] - 60)
    # A person holds the button for some 100 ms, long enough for animation frames to run between press and release.
    page.mouse.move((left + right) / 2, box["y"] + box["height"] / 2)
    page.mouse.down()
    page.wait_for_timeout(120)
    page.mouse.up()
    page.wait_for_timeout(900)


def open_carousel(page: Page, base: str) -> None:
    page.goto(base + "/")
    page.locator(TRACK).scroll_into_view_if_needed()
    page.wait_for_timeout(600)


def test_pages_run_without_errors(page: Page, base: str, errors: list[str]) -> None:
    for path in PAGES:
        page.goto(base + path)
        page.wait_for_timeout(300)
    assert errors == [], errors


def test_clicking_a_side_card_moves_the_carousel(page: Page, base: str, errors: list[str]) -> None:
    open_carousel(page, base)
    for index in (1, 2, 1, 0):
        click_visible(page, index)
        assert page.url == base + "/", f"a click on card {index} followed its link to {page.url}"
        assert active(page) == index and centered(page, index), (index, active(page))


def test_keyboard_focus_centers_its_card(page: Page, base: str, errors: list[str]) -> None:
    open_carousel(page, base)
    page.keyboard.press("Tab")
    page.locator(f"{TRACK} > .lt-slide").nth(1).locator("a.lt-stretch").focus()
    page.wait_for_timeout(900)
    assert active(page) == 1 and centered(page, 1)


def test_arrow_buttons_stop_at_the_ends(page: Page, base: str, errors: list[str]) -> None:
    open_carousel(page, base)
    nav = page.locator(f'[data-lt-carousel]:has({TRACK})')
    assert nav.locator('[data-lt-step="-1"]').is_disabled()
    for _ in range(4):
        if nav.locator('[data-lt-step="1"]').is_enabled():
            nav.locator('[data-lt-step="1"]').click()
            page.wait_for_timeout(700)
    assert active(page) == 2 and nav.locator('[data-lt-step="1"]').is_disabled()


def test_a_hash_to_a_missing_step_opens_its_path(page: Page, base: str, errors: list[str]) -> None:
    page.goto(base + "/work-with-us/#thesis-step-99")
    page.wait_for_timeout(600)
    assert errors == [], errors
    assert page.locator("#thesis").is_visible()


def test_a_filter_hides_other_items_and_updates_counts(page: Page, base: str, errors: list[str]) -> None:
    page.goto(base + "/publication/")
    group = page.locator('[aria-label="Show publications by type"]')
    total = page.locator("[data-lt-tag]").count()
    preprints = group.locator('[data-lt-filter="preprint"]')
    expected = int(preprints.inner_text().rsplit("(", 1)[1].rstrip(")"))
    preprints.click()
    shown = page.locator("[data-lt-tag]:not([hidden])").count()
    assert shown == expected < total, (shown, expected, total)
    assert page.locator("[data-lt-count]").inner_text() == f"{shown} of {total} shown"
    group.locator('[data-lt-filter=""]').click()
    assert page.locator("[data-lt-tag]:not([hidden])").count() == total


def test_a_widget_that_fails_to_set_up_leaves_the_others_working(page: Page, base: str, errors: list[str]) -> None:
    # The type filter loses its pressed button, so the filter setup throws; the carousel set up after it still runs.
    def broken(route):
        html = route.fetch().text()
        route.fulfill(body=html.replace('aria-pressed="true" data-lt-filter="">All types', 'data-lt-filter="">All types', 1),
                      content_type="text/html")
    page.route(base + "/publication/", broken)
    page.goto(base + "/publication/")
    page.wait_for_timeout(300)
    assert errors, "the broken filter should report its error"
    assert page.locator(".lt-carousel.is-enhanced").count() >= 1


def test_reduced_motion_keeps_every_card_and_section_still(page: Page, base: str, errors: list[str]) -> None:
    page.emulate_media(reduced_motion="reduce")
    page.goto(base + "/")
    page.wait_for_timeout(300)
    assert not page.evaluate("document.body.classList.contains('lt-section-focus')")
    opacities = page.eval_on_selector_all(".lt-card", "cards => cards.map(card => getComputedStyle(card).opacity)")
    assert opacities and set(opacities) <= {"1", "0.94"}, set(opacities)


if __name__ == "__main__":
    base = serve(test_render.build())
    tests = [value for name, value in list(globals().items()) if name.startswith("test_") and callable(value)]
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        for test in tests:
            page = browser.new_page(viewport={"width": 1366, "height": 900})
            errors: list[str] = []
            page.on("pageerror", lambda error: errors.append(str(error)))
            test(page, base, errors)
            page.close()
            print(f"ok {test.__name__}")
        browser.close()
    print("Browser checks passed.")
