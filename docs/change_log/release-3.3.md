title: Release Notes for v3.3

# Python-Markdown 3.3 Release Notes

Python-Markdown version 3.3 supports Python versions 3.6, 3.7, 3.8, 3.9 and PyPy3.

## Backwards-incompatible changes

### The prefix `language-` is now prepended to all language classes by default on code blocks.

The [HTML5 spec][spec] recommends that the class defining the language of a code block be prefixed with `language-`.
Therefore, by default, both the [fenced_code] and [codehilite] extensions now prepend the prefix when code
highlighting is disabled.

If you have previously been including the prefix manually in your fenced code blocks, then you will not want a second
instance of the prefix. Similarly, if you are using a third party syntax highlighting tool which does not recognize
the prefix, or requires a different prefix, then you will want to redefine the prefix globally using the `lang_prefix`
configuration option of either the `fenced_code` or `codehilite` extensions.

For example, to configure `fenced_code` to not apply any prefix (the previous behavior), set the option to an empty string:

```python
from markdown.extensions.fenced_code import FencedCodeExtension

markdown.markdown(src, extensions=[FencedCodeExtension(lang_prefix='')])
```

!!! note
    When code highlighting is [enabled], the output from Pygments is used unaltered. Currently, Pygments does not
    provide an option to include the language class in the output, let alone prefix it. Therefore, any language prefix
    is only applied when syntax highlighting is disabled.

### Attribute Lists are more strict (#898).

Empty curly braces are now completely ignored by the [Attribute List] extension. Previously, the extension would
recognize them as attribute lists and remove them from the document. Therefore, it is no longer necessary to backslash
escape a set of curly braces which are empty or only contain whitespace.

Despite not being documented, previously an attribute list could be defined anywhere within a table cell and get
applied to the cell (`<td>` element). Now the attribute list must be defined at the end of the cell content and must
be separated from the rest of the content by at least one space. This makes it easy to differentiate between attribute
lists defined on inline elements within a cell and the attribute list for the cell itself. It is also more consistent
with how attribute lists are defined on other types of elements.

The extension has also added support for defining attribute lists on table header cells (`<th>` elements) in the same
manner as data cells (`<td>` elements).

In addition, the documentation for the extensions received an overhaul. The features (#987) and limitations (#965) of the extension are now fully documented.

## New features

The following new features have been included in the 3.3 release:

* All Pygments' options are now available for syntax highlighting (#816).
    - The [Codehilite](../extensions/code_hilite.md) extension now accepts any options
      which Pygments supports as global configuration settings on the extension.
    - [Fenced Code Blocks](../extensions/fenced_code_blocks.md) will accept any of the
      same options on individual code blocks.
    - Any of the previously supported aliases to Pygments' options continue to be
      supported at this time. However, it is recommended that the Pygments option names
      be used directly to ensure continued compatibility in the future.

* [Fenced Code Blocks](../extensions/fenced_code_blocks.md) now work with
  [Attribute Lists](../extensions/attr_list.md) when syntax highlighting is disabled.
  Any random HTML attribute can be defined and set on the `<code>` tag of fenced code
  blocks when the `attr_list` extension is enabled (#816).

* The HTML parser has been completely replaced. The new HTML parser is built on Python's
  [html.parser.HTMLParser](https://docs.python.org/3/library/html.parser.html), which
  alleviates various bugs and simplify maintenance of the code (#803, #830).

* The [Markdown in HTML](../extensions/md_in_html.md) extension has been rebuilt on the
  new HTML Parser, which drastically simplifies it. Note that raw HTML elements with a
  `markdown` attribute defined are now converted to ElementTree Elements and are rendered
  by the serializer. Various bugs have been fixed (#803, #595, #780, and #1012).

* Link reference parsing, abbreviation reference parsing and footnote reference parsing
  has all been moved from `preprocessors` to `blockprocessors`, which allows them to be
  nested within other block level elements. Specifically, this change was necessary to
  maintain the current behavior in the rebuilt Markdown in HTML extension. A few random
  edge-case bugs (see the included tests) were resolved in the process (#803).

* An alternate function `markdown.extensions.headerid.slugify_unicode` has been included
  with the [Table of Contents](../extensions/toc.md) extension which supports Unicode
  characters in table of contents slugs. The old `markdown.extensions.headerid.slugify`
  method which removes non-ASCII characters remains the default. Import and pass
  `markdown.extensions.headerid.slugify_unicode` to the `slugify` configuration option
  to use the new behavior.

* A table of contents level class has been added to the [Table of Contents](../extensions/toc.md)
  extension, e.g. class="toc1". This allows for individual styling for each table of contents level.

* Support was added for Python 3.9 and dropped for Python 3.5.

## Bug fixes

The following bug fixes are included in the 3.3 release:

* Document how to pass configuration options to Extra (#1019).
* Fix HR which follows strong em (#897).
* Support short reference image links (#894).
* Avoid a `RecursionError` from deeply nested blockquotes (#799).
* Fix issues with complex emphasis (#979).
* Fix unescaping of HTML characters `<>` in CodeHilite (#990).
* Fix complex scenarios involving lists and admonitions (#1004).
* Fix complex scenarios with nested ordered and unordered lists in a definition list (#918).
* Fix corner cases with lists under admonitions.

[spec]: https://www.w3.org/TR/html5/text-level-semantics.html#the-code-element
[fenced_code]: ../extensions/fenced_code_blocks.md
[codehilite]: ../extensions/code_hilite.md
[enabled]: ../extensions/fenced_code_blocks.md#enabling-syntax-highlighting
[Attribute List]: ../extensions/attr_list.md
