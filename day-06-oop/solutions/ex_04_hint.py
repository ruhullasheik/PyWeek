"""Hints for ex_04

    class HTMLBuilder:
        def __init__(self):
            self.lines = []
            self.indent = 0

        def _tag(self, tag, content=None, **attrs):
            attrs_str = "".join(f' {k}="{v}"' for k, v in attrs.items())
            self.lines.append("  " * self.indent + f"<{tag}{attrs_str}>")
            if content:
                self.lines[-1] += content
            elif tag not in ("br", "hr", "img", "input"):
                self.indent += 1
                self._closing_tag = tag

        def h1(self, text): self._tag("h1", text)
        def p(self, text): self._tag("p", text)

        def __enter__(self):
            self.lines = ["<html>"]
            self.indent = 1
            return self

        def __exit__(self, *args):
            self.lines.append("</html>")
            print("\n".join(self.lines))
"""
