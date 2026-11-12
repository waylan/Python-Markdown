---
title: Changelog
toc_depth: 2
---

# Python-Markdown Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to the
[Python Version Specification](https://packaging.python.org/en/latest/specifications/version-specifiers/).
See the [Contributing Guide](contributing.md) for details.

## Unreleased

### Fixed

* Fix for complex cases in new emphasis handling where text could be unexpectedly
  dropped (#1694).
* Fix rule of 3 handling in new emphasis handling where an opener skipped by the rule could still be paired
  with the closer, dropping text.
* Fix the unused part of a partially consumed closing delimiter run being classified using the replacement
  placeholder instead of the text that preceded it.
* Fix quadratic processing time in the `fenced_code` extension for documents
  with many fenced code blocks (#1660).
* Reduce processing time for long blocks which are split into many smaller
  blocks: the rest of the block is no longer scanned with a regular expression
  for a hash header or an admonition when it cannot contain one, and Setext
  headers no longer split and rejoin the rest of the block (#1703).
* Stop list nesting short of the interpreter's recursion limit, as blockquote
  nesting already is, instead of raising `RecursionError` on a deeply nested
  list. The markers which no longer nest are kept as text (#1679).
* Fix quadratic-time splitting of a list block whose items span many lines,
  which dominated the time taken to render a deeply nested list.
* Stop definition list nesting short of the recursion limit, so deeply nested
  definitions are kept as text instead of raising an uncaught
  `RecursionError` (#1700).
* Fix quadratic processing time in the `tables` extension for long blocks which
  are split into many smaller blocks, such as many headers with no blank lines
  between them (#1704).

## [3.11.3] - 2026-11-05

### Fixed

* Fix cases in new emphasis handling that did not handle long chains of tokens
  like they should (#1690).
* Fix quadratic-time parsing of many consecutive reference definitions, and of
  many consecutive footnote definitions in the `footnotes` extension.
* Support automatic links with URL schemes other than HTTP and FTP, such as
  `<ssh://example.org>` (#1244).
* Fix quadratic-time id generation in the `toc` extension when many headers
  share the same text.
* Ignore glossary abbreviations with empty definitions after inline elements,
  consistently with abbreviations before inline elements.
* Strip complete HTML tags with quoted `>` characters from `toc` labels and
  generated heading IDs.
* Fix quadratic-time regex backtracking in `attr_list` when a block ends with an
  unclosed attribute list followed by a long run of spaces, e.g. a line
  consisting only of `{` and some text with many trailing spaces (#1656).
* Fix quadratic-time regex backtracking in hash headers when a long run of `#`
  characters is followed by more text on the same line.
* Fix quadratic time when a document contains many unclosed HTML comments (`<!--`
  with no matching `-->`).
* Fix regression in `BacktickInlineProcessor` where text could be lost when opening
  and closing backticks did not match (#1668).
* Escape the language name in the `codehilite` extension's non-Pygments output to
  maintain consistency with Pygments output.
* Preserve attributes without a value in the `attr_list` extension exactly as
  provided, rather than rendering them as `key="key"`, so the same source
  renders consistently under both the `html` and `xhtml` output formats
  (#1501).
* Treat a block-level raw HTML tag indented by more than three spaces as a raw
  HTML block when it is nested in a containing block (a list item, an
  admonition, etc.), instead of splitting it into paragraphs at blank lines.
  Within an indented code block such HTML is still rendered as code (#1096).

## [3.11.2] - 2026-10-19

### Fixed

* Sanitize attribute names in the `fenced_code` and `legacy_attrs` extensions so an
  attribute name cannot break out of its tag and inject markup (#1663).
* For backwards compatibility, revert the enforcement of CommonMark style
  punctuation rules (#1657).

## [3.11.1] - 2026-10-13

### Fixed

* Update serializer to be non-recursive (#1644).
* Improve ancestor handling in the inline `Treeprocessor` (#1646).
* Keep a raw HTML comment inside an inline HTML element that closes in the
  same paragraph, instead of splitting the paragraph around it (#1643).
* Fix issue where inline HTML attributes were rejected if they had `<` or `>` in the attribute (#1647).
* Fix issue where an unterminated end tag (`</foo`) could cause all remaining content to be dropped (#1651).
* Complete rework of emphasis handling to improve nested emphasis handling better (#1632).

## [3.11.0] - 2026-09-25

### Changed

* Inline processors now resume searching after the previous match, improving
  performance for repeated inline patterns (#1619).
* Officially support Python 3.15 and drop support for Python 3.10
* Walk backtick runs in `BacktickInlineProcessor` without a regex (#1620).
* Switch static site generator for documentation from MkDocs to Zensical
  (#1627, #1635, #1637, and #1638).

### Fixed

* Ensure removing Abbreviations does not raise an error (#1634).
* Fix an issue with excessive backtracking when matching inline code blocks (#1617).
* `md_in_html` now honors tags added to `Markdown.block_level_elements` after
  the extension is loaded (#1246).
* Fix quadratic-time regex backtracking in `ReferenceProcessor` when a link
  reference definition has no URL, e.g. a line consisting only of `[id]:`
  followed by many trailing spaces (#798).
* Document `attr_list` usage for `def_list` (#1123).

## [3.10.3] - 2026-07-30

### Fixed

* Fix `SetextHeaderProcessor` regex to prevent mixed `=` and `-` chars in setext-style headers (#1606).
* Add AI Policy to Contributing Guide.
* Officially document all included extensions as being in maintenance mode.
* Link the Extension API documentation to the API Reference (#1612).

## [3.10.2] - 2026-02-09

### Fixed

* Fix a regression related to comment handling (#1590).
* More reliable fix for `</` (#1593).

## [3.10.1] - 2026-01-21

### Fixed

* Ensure nested elements inside inline comments are properly unescaped (#1571).
* Make the docs build successfully with mkdocstrings-python 2.0 (#1575).
* Fix infinite loop when multiple bogus or unclosed HTML comments appear in input (#1578).
* Fix another infinite loop when handling bad comments (#1586).

## [3.10.0] - 2025-11-03

### Changed

* Officially support Python 3.14 and PyPy 3.11 and drop support for Python 3.9
  and PyPy 3.9.

### Fixed

* Fix an HTML comment parsing case in some Python versions that can cause an
  infinite loop (#1554).
* Revert the default behavior of `USE_DEFINITION_ORDER` (to `True`). The new
  behavior introduced in 3.9.0 is experimental and results are inconsistent.
  It should not have been made the default behavior (#1561).

## [3.9.0] - 2025-09-04

### Changed

* Footnotes are now ordered by the occurrence of their references in the
  document. A new configuration option for the footnotes extension,
  `USE_DEFINITION_ORDER`, has been added to support restoring the previous
  behavior of ordering footnotes by the occurrence of definitions (#1367).

### Fixed

* Ensure inline processing iterates through elements in document order (#1546).
* Fix handling of incomplete HTML tags in code spans in Python 3.14 (#1547).

## [3.8.2] - 2025-06-19

### Fixed

* Fix `codecs` deprecation in Python 3.14 (#1537).
* Fix issue with unclosed comment parsing in Python 3.14 (#1537).
* Fix issue with unclosed declarations in Python 3.14 (#1537).
* Fix issue with unclosed HTML tag `<foo` and Python 3.14 (#1537).

## [3.8.1] - 2025-06-18

### Fixed

* Ensure incomplete markup declaration in raw HTML doesn't crash parser (#1534).
* Fixed dropped content in `md_in_html` (#1526).
* Fixed HTML handling corner case that prevented some content from not being rendered (#1528).

## [3.8.0] - 2025-04-09

### Changed

* DRY fix in `abbr` extension by introducing method `create_element` (#1483).
* Clean up test directory by removing some redundant tests and port
  non-redundant cases to the newer test framework.
* Improved performance of the raw HTML post-processor (#1510).

### Fixed

* Backslash Unescape IDs set via `attr_list` on `toc` (#1493).
* Ensure `md_in_html` processes content inside "markdown" blocks as they are
  parsed outside of "markdown" blocks to keep things more consistent for
  third-party extensions (#1503).
* `md_in_html` handle tags within inline code blocks better (#1075).
* `md_in_html` fix handling of one-liner block HTML handling (#1074).
* Ensure `<center>` is treated like a block-level element (#1481).
* Ensure that `abbr` extension respects `AtomicString` and does not process
  perceived abbreviations in these strings (#1512).
* Ensure `smarty` extension correctly renders nested closing quotes (#1514).

## [3.7.0] - 2024-08-16

### Changed

* Refactor `abbr` Extension

    A new `AbbrTreeprocessor` has been introduced, which replaces the now deprecated
    `AbbrInlineProcessor`. Abbreviation processing now happens after Attribute Lists,
    avoiding a conflict between the two extensions (#1460).

    The `AbbrPreprocessor` class has been renamed to `AbbrBlockprocessor`, which
    better reflects what it is. `AbbrPreprocessor` has been deprecated.

    A call to `Markdown.reset()` now clears all previously defined abbreviations.

    Abbreviations are now sorted by length before executing `AbbrTreeprocessor`
    to ensure that multi-word abbreviations are implemented even if an abbreviation
    exists for one of those component words. (#1465)

    Abbreviations without a definition are now ignored. This avoids applying
    abbr tags to text without a title value.

    Added an optional `glossary` configuration option to the abbreviations extension.
    This provides a simple and efficient way to apply a dictionary of abbreviations
    to every page.

    Abbreviations can now be disabled by setting their definition to `""` or `''`.
    This can be useful when using the `glossary` option.

### Fixed

* Fixed links to source code on GitHub from the documentation (#1453).

## [3.6.0] - 2024-03-14

### Changed

* Refactor TOC Sanitation

    * All postprocessors are now run on heading content.
    * Footnote references are now stripped from heading content. Fixes #660.
    * A more robust `striptags` is provided to convert headings to plain text.
      Unlike, the `markupsafe` implementation, HTML entities are not unescaped.
    * The plain text `name`, rich `html`, and unescaped raw `data-toc-label` are
      saved to `toc_tokens`, allowing users to access the full rich text content of
      the headings directly from `toc_tokens`.
    * The value of `data-toc-label` is sanitized separate from heading content
      before being written to `name`. This fixes a bug which allowed markup through
      in certain circumstances. To access the raw unsanitized data, retrieve the
      value from `token['data-toc-label']` directly.
    * An `html.unescape` call is made just prior to calling `slugify` so that
      `slugify` only operates on Unicode characters. Note that `html.unescape` is
      not run on `name`, `html`, or `data-toc-label`.
    * The functions `get_name` and `stashedHTML2text` defined in the `toc` extension
      are both **deprecated**. Instead, third party extensions should use some
      combination of the new functions `run_postprocessors`, `render_inner_html` and
      `striptags`.

### Fixed

* Include `scripts/*.py` in the generated source tarballs (#1430).
* Ensure lines after heading in loose list are properly detabbed (#1443).
* Give smarty tree processor higher priority than toc (#1440).
* Permit carets (`^`) and square brackets (`]`) but explicitly exclude
  backslashes (`\`) from abbreviations (#1444).
* In attribute lists (`attr_list`, `fenced_code`), quoted attribute values are
  now allowed to contain curly braces (`}`) (#1414).

## [3.5.2] - 2024-01-10

### Fixed

* Fix type annotations for `convertFile` - it accepts only bytes-based buffers.
  Also remove legacy checks from Python 2 (#1400)
* Remove legacy import needed only in Python 2 (#1403)
* Fix typo that left the attribute `AdmonitionProcessor.content_indent` unset
  (#1404)
* Fix edge-case crash in `InlineProcessor` with `AtomicString` (#1406).
* Fix edge-case crash in `codehilite` with an empty `code` tag (#1405).
* Improve and expand type annotations in the code base (#1401).
* Fix handling of bogus comments (#1425).

## [3.5.1] - 2023-10-31

### Fixed

* Fix a performance problem with HTML extraction where large HTML input could
  trigger quadratic line counting behavior (#1392).
* Improve and expand type annotations in the code base (#1394).

## [3.5.0] - 2023-10-06

### Added

* Add `permalink_leading` configuration option to the toc extension (#1339)

    A new boolean option `permalink_leading` controls the position of the permanent
    link anchors generated with `permalink`. Setting `permalink_leading` to `True`
    will cause the links to be inserted at the start of the header, before any other
    header content. The default behavior for `permalink` is to append permanent
    links to the header, placing them after all other header content.

### Changed

* Add support for cPython version 3.12 (and PyPy 3.10) and drop support for
  Python version 3.7 (#1357).
* Refactor changelog to use the format defined at <https://keepachangelog.com/>.
* Update the list of empty HTML tags (#1353).
* Add customizable TOC title class to TOC extension (#1293).
* Add API documentation of the code base which is generated by
  [mkdocstrings](https://mkdocstrings.github.io/) (#1220).

### Fixed

* Fix a corner case in admonitions where if an indented code block was provided
  as the first block, the output would be malformed (#1329).

## [3.4.4] - 2023-07-25

### Fixed

* Add a special case for initial `'s` to smarty extension (#1305).
* Unescape any backslash escaped inline raw HTML (#1358).
* Unescape backslash escaped TOC token names (#1360).

## [3.4.3] - 2023-03-23

### Fixed

* Restore console script (#1327).

## [3.4.2] - 2023-03-22

### Fixed
* Officially support Python 3.11.
* Improve standalone * and _ parsing (#1300).
* Consider `<html>` HTML tag a block-level element (#1309).
* Switch from `setup.py` to `pyproject.toml`.

## [3.4.1] - 2022-07-15

### Fixed

* Fix an import issue with `importlib.util` (#1274).

## [3.4.0] - 2022-07-15

### Changed

* The `tables` extension now uses a `style` attribute instead of an `align` attribute for alignment.

    The [HTML4 spec](https://www.w3.org/TR/html4/present/graphics.html#h-15.1.2)
    specifically deprecates the use of the `align` attribute and it does not appear
    at all in the [HTML5
    spec](https://www.w3.org/TR/html53/tabular-data.html#attributes-common-to-td-and-th-elements).
    Therefore, by default, the [tables](extensions/tables.md) extension will now use
    the `style` attribute (setting just the `text-align` property) in `td` and `th`
    blocks.

    The former behavior is available by setting the `use_align_attribute`
    configuration option to `True` when enabling the extension.

    For example, to configure the old `align` behavior:

        from markdown.extensions.tables import TableExtension

        markdown.markdown(src, extensions=[TableExtension(use_align_attribute=True)])

* Backslash unescaping moved to Treeprocessor (#1131).

    Unescaping backslash escapes has been moved to a Treeprocessor, which  enables
    proper HTML escaping during serialization. However, it is recognized that
    various third-party extensions may be calling the old class at
    `postprocessors.UnescapePostprocessor`. Therefore, the old class remains in the
    code base, but has been deprecated and will be removed in a future release. The
    new class `treeprocessors.UnescapeTreeprocessor` should be used instead.

* Previously deprecated objects have been removed

    Various objects were deprecated in version 3.0 and began raising deprecation
    warnings (see the [version 3.0 release notes](#300-2018-09-21) for details). Any of those objects
    which remained in version 3.3 have been removed from the code base in version 3.4
    and will now raise errors. The relevant objects are listed below.


    | Deprecated Object                      | Replacement Object                  |
    |----------------------------------------|-------------------------------------|
    | `markdown.version`                     | `markdown.__version__`              |
    | `markdown.version_info`                | `markdown.__version_info__`         |
    | `markdown.util.etree`                  | `xml.etree.ElementTree`             |
    | `markdown.util.string_type`            | `str`                               |
    | `markdown.util.text_type`              | `str`                               |
    | `markdown.util.int2str`                | `chr`                               |
    | `markdown.util.iterrange`              | `range`                             |
    | `markdown.util.isBlockLevel`           | `markdown.Markdown().is_block_level`|
    | `markdown.util.Processor().markdown`   | `markdown.util.Processor().md`      |
    | `markdown.util.Registry().__setitem__` | `markdown.util.Registry().register` |
    | `markdown.util.Registry().__delitem__` |`markdown.util.Registry().deregister`|
    | `markdown.util.Registry().add`         | `markdown.util.Registry().register` |

    In addition, the `md_globals` parameter of
    `Markdown.extensions.Extension.extendMarkdown()` is no longer recognized as a
    valid parameter and will raise an error if provided.

### Added

* Some new configuration options have been added to the
  [footnotes](extensions/footnotes.md) extension (#1218):

    * Small refactor of the `BACKLINK_TITLE` option; The use of `format()`
      instead of "old" `%d` formatter allows one to specify text without the
      need to have the number of the footnote in it (like footnotes on
      Wikipedia for example). The modification is backward compatible so no
      configuration change is required.

    * Addition of a new option `SUPERSCRIPT_TEXT` that allows one to specify a
      custom placeholder for the footnote itself in the text.
      Ex: `[{}]` will give `<sup>[1]</sup>`, `({})` will give `<sup>(1)</sup>`,
      or by default, the current behavior: `<sup>1</sup>`.

* The [Table of Contents](extensions/toc.md) extension now accepts a
  `toc_class` parameter which can be used to set the CSS class(es) on the
  `<div>` that contains the Table of Contents (#1224).

* The CodeHilite extension now supports a `pygments_formatter` option that can
  be set to a custom formatter class (#1187).

    - If `pygments_formatter` is set to a string (ex: `'html'`), Pygments'
      default formatter by that name is used.
    - If `pygments_formatter` is set to a formatter class (or any callable
      which returns a formatter instance), then an instance of that class is
      used.

    The formatter class is now passed an additional option, `lang_str`, to
    denote the language of the code block (#1258). While Pygments' built-in
    formatters will ignore the option, a custom formatter assigned to the
    `pygments_formatter` option can make use of the `lang_str` to include the
    code block's language in the output.

### Fixed

* Extension entry-points are only loaded if needed (#1216).
* Added additional checks to the `<pre><code>` handling of
  `PrettifyTreeprocessor` (#1261, #1263).
* Fix XML deprecation warnings.

## [3.3.7] - 2022-05-05

### Fixed

* Disallow square brackets in reference link ids (#1209).
* Retain configured `pygments_style` after first code block (#1240).
* Ensure fenced code attributes are properly escaped (#1247).

## [3.3.6] - 2021-11-17

### Fixed

* Fix a dependency issue (#1195, #1196).

## [3.3.5] - 2021-11-16

### Fixed

* Make the `slugify_unicode` function not remove diacritical marks (#1118).
* Fix `[toc]` detection when used with `nl2br` extension (#1160).
* Re-use compiled regex for block level checks (#1169).
* Don't process shebangs in fenced code blocks when using CodeHilite (#1156).
* Improve email address validation for Automatic Links (#1165).
* Ensure `<summary>` tags are parsed correctly (#1079).
* Support Python 3.10 (#1124).

## [3.3.4] - 2021-02-24

### Fixed

* Properly parse unclosed tags in code spans (#1066).
* Properly parse processing instructions in md_in_html (#1070).
* Properly parse code spans in md_in_html (#1069).
* Preserve text immediately before an admonition (#1092).
* Simplified regex for HTML placeholders (#928) addressing (#932).
* Ensure `permalinks` and `anchorlinks` are not restricted by `toc_depth` (#1107).
* Fix corner cases with lists under admonitions (#1102).

## [3.3.3] - 2020-10-25

### Fixed

* Unify all block-level tags (#1047).
* Fix issue where some empty elements would have text rendered as `None` when using `md_in_html` (#1049).
* Avoid catastrophic backtracking in `hr` regex (#1055).
* Fix `hr` HTML handling (#1053).

## [3.3.2] - 2020-10-19

### Fixed

* Properly parse inline HTML in md_in_html (#1040 & #1045).
* Avoid crashing when md_in_html fails (#1040).

## [3.3.1] - 2020-10-12

### Fixed

* Correctly parse raw `script` and `style` tags (#1036).
* Ensure consistent class handling by `fenced_code` and `codehilite` (#1032).

## [3.3.0] - 2020-10-06

### Changed

* The prefix `language-` is now prepended to all language classes by default on code blocks.

    The [HTML5
    spec](https://www.w3.org/TR/html5/text-level-semantics.html#the-code-element)
    recommends that the class defining the language of a code block be prefixed with
    `language-`. Therefore, by default, both the
    [fenced_code](extensions/fenced_code_blocks.md) and
    [codehilite](extensions/code_hilite.md) extensions now prepend the prefix when
    code highlighting is disabled.

    If you have previously been including the prefix manually in your fenced code blocks, then you will not want a second
    instance of the prefix. Similarly, if you are using a third party syntax highlighting tool which does not recognize
    the prefix, or requires a different prefix, then you will want to redefine the prefix globally using the `lang_prefix`
    configuration option of either the `fenced_code` or `codehilite` extensions.

    For example, to configure `fenced_code` to not apply any prefix (the previous behavior), set the option to an empty string:

        from markdown.extensions.fenced_code import FencedCodeExtension

        markdown.markdown(src, extensions=[FencedCodeExtension(lang_prefix='')])

    !!! note
        When code highlighting is
        [enabled](extensions/fenced_code_blocks.md#enabling-syntax-highlighting),
        the output from Pygments is used unaltered. Currently, Pygments does not
        provide an option to include the language class in the output, let alone
        prefix it. Therefore, any language prefix is only applied when syntax
        highlighting is disabled.

* Attribute Lists are more strict (#898).

    Empty curly braces are now completely ignored by the [Attribute List](extensions/attr_list.md) extension. Previously, the extension would
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

### Added

* All Pygments' options are now available for syntax highlighting (#816).
    - The [Codehilite](extensions/code_hilite.md) extension now accepts any options
      which Pygments supports as global configuration settings on the extension.
    - [Fenced Code Blocks](extensions/fenced_code_blocks.md) will accept any of the
      same options on individual code blocks.
    - Any of the previously supported aliases to Pygments' options continue to be
      supported at this time. However, it is recommended that the Pygments option names
      be used directly to ensure continued compatibility in the future.

* [Fenced Code Blocks](extensions/fenced_code_blocks.md) now work with
  [Attribute Lists](extensions/attr_list.md) when syntax highlighting is disabled.
  Any random HTML attribute can be defined and set on the `<code>` tag of fenced code
  blocks when the `attr_list` extension is enabled (#816).

* The HTML parser has been completely replaced. The new HTML parser is built on Python's
  [`html.parser.HTMLParser`](https://docs.python.org/3/library/html.parser.html), which
  alleviates various bugs and simplify maintenance of the code (#803, #830).

* The [Markdown in HTML](extensions/md_in_html.md) extension has been rebuilt on the
  new HTML Parser, which drastically simplifies it. Note that raw HTML elements with a
  `markdown` attribute defined are now converted to ElementTree Elements and are rendered
  by the serializer. Various bugs have been fixed (#803, #595, #780, and #1012).

* Link reference parsing, abbreviation reference parsing and footnote reference parsing
  has all been moved from `preprocessors` to `blockprocessors`, which allows them to be
  nested within other block level elements. Specifically, this change was necessary to
  maintain the current behavior in the rebuilt Markdown in HTML extension. A few random
  edge-case bugs (see the included tests) were resolved in the process (#803).

* An alternate function `markdown.extensions.headerid.slugify_unicode` has been included
  with the [Table of Contents](extensions/toc.md) extension which supports Unicode
  characters in table of contents slugs. The old `markdown.extensions.headerid.slugify`
  method which removes non-ASCII characters remains the default. Import and pass
  `markdown.extensions.headerid.slugify_unicode` to the `slugify` configuration option
  to use the new behavior.

* Support was added for Python 3.9 and dropped for Python 3.5.

### Fixed

* Document how to pass configuration options to Extra (#1019).
* Fix HR which follows strong em (#897).
* Support short reference image links (#894).
* Avoid a `RecursionError` from deeply nested blockquotes (#799).
* Fix issues with complex emphasis (#979).
* Fix unescaping of HTML characters `<>` in CodeHilite (#990).
* Fix complex scenarios involving lists and admonitions (#1004).
* Fix complex scenarios with nested ordered and unordered lists in a definition list (#918).

## [3.2.2] - 2020-05-08

### Fixed

* Add `checklinks` tox environment to ensure all links in documentation are good.
* Refactor extension API documentation (#729).
* Load entry_points (for extensions) only once using `importlib.metadata`.
* Do not double escape entities in TOC.
* Correctly report if an extension raises a `TypeError` (#939).
* Raise a `KeyError` when attempting to delete a nonexistent key from the
  extension registry (#939).
* Remove import of `packaging` (or `pkg_resources` fallback) entirely.
* Remove `setuptools` as a run-time dependency (`install_required`).

## [3.2.1] - 2020-02-12

### Fixed

* The `name` property in `toc_tokens` from the TOC extension now
  escapes HTML special characters (`<`, `>`, and `&`).

## [3.2.0] - 2020-02-07

### Changed

* Drop support for Python 2.7

    Python 2.7 reaches end-of-life on 2020-01-01 and Python-Markdown 3.2 has dropped
    support for it. Please upgrade to Python 3, or use Python-Markdown 3.1.

* `em` and `strong` inline processor changes

    In order to fix issue #792, `em`/`strong` inline processors were refactored. This
    translated into removing many of the existing inline processors that handled this
    logic:

    * `em_strong`
    * `strong`
    * `emphasis`
    * `strong2`
    * `emphasis`

    These processors were replaced with two new ones:

    * `em_strong`
    * `em_strong2`

    The [`legacy_em`](extensions/legacy_em.md) extension was also modified with new,
    refactored logic and simply overrides the `em_strong2` inline processor.

* CodeHilite now always wraps with `<code>` tags

    Before, the HTML generated by CodeHilite looked like:
    - `<pre><code>foo = 'bar'</code></pre>` if you **were not** using Pygments.
    - `<pre>foo = 'bar'</pre>`  if you **were** using Pygments.

    To make the cases more consistent (and adhere to many Markdown specifications and
    HTML code block markup suggestions), CodeHilite will now always additionally wrap
    code with `<code>` tags. See #862 for more details.

    This change does not alter the Python-Markdown API, but users relying on the old
    markup will find their output now changed.

    Internally, this change relies on the Pygments 2.4, so you must be using at least
    that version to see this effect. Users with earlier Pygments versions will
    continue to see the old behavior.

* `markdown.util.etree` deprecated

    Previously, Python-Markdown was using either the `xml.etree.cElementTree` module
    or the `xml.etree.ElementTree` module, based on their availability. In modern
    Python versions, the former is a deprecated alias for the latter. Thus, the
    compatibility layer is deprecated and extensions are advised to use
    `xml.etree.ElementTree` directly. Importing `markdown.util.etree` will raise
    a `DeprecationWarning` beginning in version 3.2 and may be removed in a future
    release.

    Therefore, extension developers are encouraged to replace
    `from markdown.util import etree` with
    `import xml.etree.ElementTree as etree` in their code.

### Added

* Some new configuration options have been added to the [toc](extensions/toc.md)
  extension:

    * The `anchorlink_class` and `permalink_class` options allow class(es) to be
      assigned to the `anchorlink` and `permalink` respectively. This allows using
      icon fonts from CSS for the links. Therefore, an empty string passed to
      `permalink` now generates an empty `permalink`. Previously no `permalink`
      would have been generated. (#776)

    * The `permalink_title` option allows the title attribute of a `permalink` to be
      set to something other than the default English string `Permanent link`. (#877)

* Document thread safety (#812).

* Markdown parsing in HTML has been exposed via a separate extension called
  [`md_in_html`](extensions/md_in_html.md).

* Add support for Python 3.8.

### Fixed

* HTML tag placeholders are no longer included in  `.toc_tokens` (#899).
* Unescape backslash-escaped characters in TOC ids (#864).
* Refactor bold and italic logic in order to solve complex nesting issues (#792).
* Always wrap CodeHilite code in `code` tags (#862).

## [3.1.1] - 2019-05-20

### Fixed

* Fixed import failure in `setup.py` when the source directory is not
  on `sys.path` (#823).
* Prefer public `packaging` module to pkg_resources' private copy of
  it (#825).

## [3.1.0] - 2019-03-25

### Changed

* `markdown.version` and `markdown.version_info` deprecated

    Historically, version numbers were acquired via the attributes
    `markdown.version` and `markdown.version_info`. As of 3.0, a more standardized
    approach is being followed and versions are acquired via the
    `markdown.__version__` and `markdown.__version_info__` attributes.  As of 3.1
    the legacy attributes will raise a `DeprecationWarning` if they are accessed. In
    a future release the legacy attributes will be removed.

### Added

* A [Contributing Guide](contributing.md) has been added (#732).

* A new configuration option to set the footnote separator has been added. Also,
  the `rel` and `rev` attributes have been removed from footnotes as they are
  not valid in HTML5. The `refs` and `backrefs` classes already exist and
  serve the same purpose (#723).

* A new option for `toc_depth` to set not only the bottom section level,
  but also the top section level. A string consisting of two digits
  separated by a hyphen in between (`"2-5"`), defines the top (`t`) and the
  bottom (`b`) (`<ht>..<hb>`). A single integer still defines the bottom
  section level (`<h1>..<hb>`) only. (#787).

### Fixed

* Update CLI to support PyYAML 5.1.
* Overlapping raw HTML matches no longer leave placeholders behind (#458).
* Emphasis patterns now recognize newline characters as whitespace (#783).
* Version format had been updated to be PEP 440 compliant (#736).
* Block level elements are defined per instance, not as class attributes
  (#731).
* Double escaping of block code has been eliminated (#725).
* Problems with newlines in references has been fixed (#742).
* Escaped `#` are now handled in header syntax (#762).

## [3.0.1] - 2018-09-28

### Fixed

* Brought back the `version` and `version_info` variables (#709).
* Added support for hexadecimal HTML entities (#712).

## [3.0.0] - 2018-09-21

### Changed

* `enable_attributes` keyword deprecated

    The `enable_attributes` keyword is deprecated in version 3.0 and will be
    ignored. Previously the keyword was `True` by default and enabled an
    undocumented way to define attributes on document elements. The feature has been
    removed from version 3.0. As most users did not use the undocumented feature, it
    should not affect most users. For the few who did use the feature, it can be
    enabled by using the [Legacy Attributes](extensions/legacy_attrs.md)
    extension.

* `smart_emphasis` keyword and `smart_strong` extension deprecated

    The `smart_emphasis` keyword is deprecated in version 3.0 and will be ignored.
    Previously the keyword was `True` by default and caused the parser to ignore
    middle-word emphasis. Additionally, the optional `smart_strong` extension
    provided the same behavior for strong emphasis. Both of those features are now
    part of the default behavior, and the [Legacy
    Emphasis](extensions/legacy_em.md) extension is available to disable that
    behavior.

* `output_formats` simplified to `html` and `xhtml`.

    The `output_formats` keyword now only accepts two options: `html` and `xhtml`
    Note that if `(x)html1`, `(x)html4` or `(x)html5` are passed in, the number is
    stripped and ignored.

* `safe_mode` and `html_replacement_text` keywords deprecated

    Both `safe_mode` and the associated `html_replacement_text` keywords are
    deprecated in version 3.0 and will be ignored. The so-called "safe mode" was
    never actually "safe" which has resulted in many people having a false sense of
    security when using it. As an alternative, the developers of Python-Markdown
    recommend that any untrusted content be passed through an HTML sanitizer (like
    [Bleach](https://bleach.readthedocs.io/)) after being converted to HTML by
    markdown. In fact, [Bleach
    Whitelist](https://github.com/yourcelf/bleach-whitelist) provides a curated list
    of tags, attributes, and styles suitable for filtering user-provided HTML using
    bleach.

    If your code previously looked like this:

        html = markdown.markdown(text, safe_mode=True)

    Then it is recommended that you change your code to read something like this:

        import bleach
        from bleach_whitelist import markdown_tags, markdown_attrs
        html = bleach.clean(markdown.markdown(text), markdown_tags, markdown_attrs)

    If you are not interested in sanitizing untrusted text, but simply desire to
    escape raw HTML, then that can be accomplished through an extension which
    removes HTML parsing:

        from markdown.extensions import Extension

        class EscapeHtml(Extension):
            def extendMarkdown(self, md):
                md.preprocessors.deregister('html_block')
                md.inlinePatterns.deregister('html')

        html = markdown.markdown(text, extensions=[EscapeHtml()])

    As the HTML would not be parsed with the above Extension, then the serializer
    will escape the raw HTML, which is exactly what happened in previous versions
    with `safe_mode="escape"`.

* Positional arguments deprecated

    Positional arguments on the `markdown.Markdown()` class are deprecated as are
    all except the `text` argument on the `markdown.markdown()` wrapper function.
    Using positional arguments will raise an error. Only keyword arguments should be
    used. For example, if your code previously looked like this:

        html = markdown.markdown(text, [SomeExtension()])

    Then it is recommended that you change it to read something like this:

        html = markdown.markdown(text, extensions=[SomeExtension()])

    !!! Note
        This change is being made as a result of deprecating `"safe_mode"` as the
        `safe_mode` argument was one of the positional arguments. When that argument
        is removed, the two arguments following it will no longer be at the correct
        position. It is recommended that you always use keywords when they are
        supported for this reason.

* Extension name behavior has changed

    In previous versions of Python-Markdown, the built-in extensions received
    special status and did not require the full path to be provided. Additionally,
    third party extensions whose name started with `"mdx_"` received the same
    special treatment. This is no longer the case.

    Support has been added for extensions to define an [entry
    point](extensions/api.md#entry_point). An entry point is a string name which
    can be used to point to an `Extension` class. The built-in extensions now have
    entry points which match the old short names. And any third-party extensions
    which define entry points can now get the same behavior. See the documentation
    for each specific extension to find the assigned name.

    If an extension does not define an entry point, then the full path to the
    extension must be used. See the [documentation](library.md#extensions) for
    a full explanation of the current behavior.

* Extension configuration as part of extension name deprecated

    The previously documented method of appending the extension configuration
    options as a string to the extension name is deprecated and will raise an error.
    The [`extension_configs`](library.md#extension_configs) keyword should be
    used instead. See the [documentation](library.md#extension_configs) for a
    full explanation of the current behavior.

* HeaderId extension deprecated

    The HeaderId Extension is deprecated and will raise an error if specified. Use
    the [Table of Contents](extensions/toc.md) Extension instead, which offers
    most of the features of the HeaderId Extension and more (support for meta data
    is missing).

    Extension authors who have been using the `slugify` and `unique` functions
    defined in the HeaderId Extension should note that those functions are now
    defined in the Table of Contents extension and should adjust their import
    statements accordingly (`from markdown.extensions.toc import slugify, unique`).

* Homegrown `OrderedDict` has been replaced with a purpose-built `Registry`

    All processors and patterns now get "registered" to a
    [Registry](extensions/api.md#registry). A backwards compatible shim is
    included so that existing simple extensions should continue to work.
    A `DeprecationWarning` will be raised for any code which calls the old API.

* Markdown class instance references.

    Previously, instances of the `Markdown` class were represented as any one of
    `md`, `md_instance`, or `markdown`. This inconsistency made it difficult when
    developing extensions, or just maintaining the existing code. Now, all instances
    are consistently represented as `md`.

    The old attributes on class instances still exist, but raise a
    `DeprecationWarning` when accessed. Also on classes where the instance was
    optional, the attribute always exists now and is simply `None` if no instance
    was provided (previously the attribute would not exist).

* `markdown.util.isBlockLevel` deprecated

    The `markdown.util.isBlockLevel` function is deprecated and will raise a
    `DeprecationWarning`. Instead, extensions should use the `isBlockLevel` method
    of the `Markdown` class instance. Additionally, a list of block level elements
    is defined in the `block_level_elements` attribute of the `Markdown` class which
    extensions can access to alter the list of elements which are treated as block
    level elements.

* `md_globals` keyword deprecated from extension API

    Previously, the `extendMarkdown` method of a `markdown.extensions.Extension`
    subclasses accepted an `md_globals` keyword, which contained the value returned
    by Python's `globals()` built-in function. As all of the configuration is now
    held within the `Markdown` class instance, access to the globals is no longer
    necessary and any extensions which expect the keyword will raise a
    `DeprecationWarning`. A future release will raise an error.

* `markdown.version` and `markdown.version_info` deprecated

    Historically, version numbers were acquired via the attributes
    `markdown.version` and `markdown.version_info`. Moving forward, a more
    standardized approach is being followed and versions are acquired via the
    `markdown.__version__` and `markdown.__version_info__` attributes.  The legacy
    attributes are still available to allow distinguishing versions between the
    legacy Markdown 2.0 series and the Markdown 3.0 series, but in the future the
    legacy attributes will be removed.

* Added new, more flexible `InlineProcessor` class

    A new `InlineProcessor` class handles inline processing much better and allows
    for more flexibility. The new `InlineProcessor` classes no longer utilize
    unnecessary pretext and post-text captures. New class can accept the buffer that
    is being worked on and manually process the text without regular expressions and
    return new replacement bounds. This helps us to handle links in a better way and
    handle nested brackets and logic that is too much for regular expression.

### Added

* A new [testing framework](test_tools.md) is included as a part of the
  Markdown library, which can also be used by third party extensions.

* A new `toc_depth` parameter has been added to the
  [Table of Contents Extension](extensions/toc.md).

* A new `toc_tokens` attribute has been added to the Markdown class by the
  [Table of Contents Extension](extensions/toc.md), which contains the raw
  tokens used to build the Table of Contents. Users can use this to build their
  own custom Table of Contents rather than needing to parse the HTML available
  on the `toc` attribute of the Markdown class.

* When the [Table of Contents Extension](extensions/toc.md) is used in
  conjunction with the [Attribute Lists Extension](extensions/attr_list.md)
  and a `data-toc-label` attribute is defined on a header, the content of the
  `data-toc-label` attribute is now used as the content of the Table of Contents
  item for that header.

* Additional CSS class names can be appended to
  [Admonitions](extensions/admonition.md).

# Previous Releases

For information on prior releases, see their changelogs:

* [2.x and earlier](change_log/index.md)
