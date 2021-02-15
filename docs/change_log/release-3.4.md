title: Release Notes for v3.4

# Python-Markdown 3.4 Release Notes

Python-Markdown version 3.4 supports Python versions 3.6, 3.7, 3.8, 3.9 and PyPy3.

## Backwards-incompatible changes

### The `table` extension now uses a `style` attribute instead of `align` attribute for alignment.

The [HTML4 spec][spec4] specifically
deprecates the use of the `align` attribute and it does not appear at all in the 
[HTML5 spec][spec5]. Therefore, by default, the [table] extension will now use the `style`
attribute (setting just the `text-align` property) in `td` and `th` blocks.

The former behavior is available by setting the setting `use_align_attribute` configuration
option to `True` when adding the extension.

For example, to configure the old `align` behavior:

```python
from markdown.extensions.tables import TableExtension

markdown.markdown(src, extensions=[TableExtension(use_align_attribute=True)])
```

In addition, tests were moved to the modern test environment.

## New features

The following new features have been included in the 3.3 release:

* Use `style` attribute in tables for alignment instead of `align` for better CSS
  inter-operation. The old behavior is available by setting `use_align_attribute=True` when
  adding the extension.

## Bug fixes

The following bug fixes are included in the 3.3 release:

[spec4]: https://www.w3.org/TR/html4/present/graphics.html#h-15.1.2
[spec5]: https://www.w3.org/TR/html53/tabular-data.html#attributes-common-to-td-and-th-elements
