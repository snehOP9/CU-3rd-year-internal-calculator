"""Static accessibility checks for the single-file calculator UI.

These checks complement, but do not replace, browser + screen-reader testing.
"""
from html.parser import HTMLParser
from pathlib import Path
import unittest


HTML = Path(__file__).resolve().parents[1].joinpath("index.html").read_text(encoding="utf-8")


class Controls(HTMLParser):
    def __init__(self):
        super().__init__()
        self.nodes = {}

    def handle_starttag(self, tag, attrs):
        properties = dict(attrs)
        if properties.get("id"):
            self.nodes[properties["id"]] = (tag, properties)


class AccessibilityMarkupTests(unittest.TestCase):
    def test_calculator_mode_has_button_toggle_semantics(self):
        parser = Controls()
        parser.feed(HTML)
        for control in ("internalModeBtn", "sgpaModeBtn"):
            tag, props = parser.nodes[control]
            self.assertEqual(tag, "button")
            self.assertIn(props["aria-pressed"], ("true", "false"))
            self.assertNotIn("role", props)
        self.assertIn('setAttribute("aria-pressed"', HTML)

    def test_subject_search_has_accessible_name(self):
        parser = Controls()
        parser.feed(HTML)
        tag, props = parser.nodes["subjectSearch"]
        self.assertEqual(tag, "input")
        self.assertTrue(props.get("aria-label"))

    def test_dynamic_marks_fields_expose_validation(self):
        self.assertIn('aria-describedby="${field.key}-error"', HTML)
        self.assertIn('aria-invalid="${Boolean(errorMessage)}"', HTML)
        self.assertIn('input.setAttribute("aria-invalid", String(Boolean(message)))', HTML)

    def test_reduced_motion_disables_scripted_animation_and_row_removal_delay(self):
        self.assertIn('window.matchMedia("(prefers-reduced-motion: reduce)").matches', HTML)
        self.assertIn('if (prefersReducedMotion() || Math.abs(target - current) < 0.0001)', HTML)
        self.assertIn('if (!element || element.hidden || prefersReducedMotion()) return;', HTML)
        self.assertIn('if (prefersReducedMotion()) {\n          removeRow();', HTML)
        self.assertIn('setTimeout(removeRow, 180);', HTML)

    def test_dynamic_sgpa_fields_have_individual_labels(self):
        for label in (
            "Subject name for row", "Credits for row",
            "Grade for row", "Remove subject row"
        ):
            self.assertIn(label, HTML)


if __name__ == "__main__":
    unittest.main()
