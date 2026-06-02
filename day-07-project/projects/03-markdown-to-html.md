# Markdown to HTML Converter

**Difficulty**: Medium-Hard  
**Skills**: Regex, string processing, OOP

## Spec

Build a tool that converts a subset of Markdown to HTML.

### Supported Syntax

```markdown
# Heading 1
## Heading 2
**bold text**
*italic text*
- List item
1. Numbered item
`inline code`
```
Code block
```
[link text](https://example.com)
```

### Usage

```
python md2html.py input.md output.html
```

### Requirements

- Implement a `Parser` class with methods for each element
- Handle nested formatting (bold inside a paragraph)
- Output valid HTML5 with `<html><body>...</body></html>`
- Preserve blank lines as `<br>` or spacing
- Use regex but don't go overboard — keep it readable

### Extension Ideas

- Support tables
- Add a `--watch` flag that re-renders on file change
- Add a simple CSS theme with `--theme`
