title: Change Log

Python-Markdown Change Log
=========================

Under development: version 3.4.0 ([Notes](release-3.4.md)).

Under development: version 3.3.4 (a bug-fix release).

* Properly parse unclosed tags in code spans (#1066).
* Properly parse processing instructions in md_in_html (#1070).
* Properly parse code spans in md_in_html (#1069).
* Preserve text immediately before an admonition (#1092).
* Simplified regex for HTML placeholders (#928) addressing (#932).

Oct 25, 2020: version 3.3.3 (a bug-fix release).

* Unify all block-level tags (#1047).
* Fix issue where some empty elements would have text rendered as `None` when using `md_in_html` (#1049).
* Avoid catastrophic backtracking in `hr` regex (#1055).
* Fix `hr` HTML handling (#1053).

Oct 19, 2020: version 3.3.2 (a bug-fix release).

* Properly parse inline HTML in md_in_html (#1040 & #1045).
* Avoid crashing when md_in_html fails (#1040).

Oct 12, 2020: version 3.3.1 (a bug-fix release).

* Correctly parse raw `script` and `style` tags (#1036).
* Ensure consistent class handling by `fenced_code` and `codehilite` (#1032).

Oct 6, 2020: version 3.3 ([Notes](release-3.3.md)).

May 8, 2020: version 3.2.2 (a bug-fix release).

* Add `checklinks` tox environment to ensure all links in documentation are good.
* Refactor extension API documentation (#729).
* Load entry_points (for extensions) only once using `importlib.metadata`.
* Do not double escape entities in TOC.
* Correctly report if an extension raises a `TypeError` (#939).
* Raise a `KeyError` when attempting to delete a nonexistent key from the
  extension registry (#939).
* Remove import of `packaging` (or `pkg_resources` fallback) entirely.
* Remove `setuptools` as a run-time dependency (`install_required`).

Feb 12, 2020: Released version 3.2.1 (a bug-fix release).

* The `name` property in `toc_tokens` from the TOC extension now
  escapes HTML special characters (`<`, `>`, and `&`).

Feb 7, 2020: Released version 3.2 ([Notes](release-3.2.md)).

May 20, 2019: Released version 3.1.1 (a bug-fix release).

* Fixed import failure in `setup.py` when the source directory is not
  on `sys.path` (#823).
* Prefer public `packaging` module to pkg_resources' private copy of
  it (#825).

Mar 25, 2019: Released version 3.1 ([Notes](release-3.1.md)).

Sept 28, 2018: Released version 3.0.1 (a bug-fix release).

* Brought back the `version` and `version_info` variables (#709).
* Added support for hexadecimal HTML entities (#712).

Sept 21, 2018: Released version 3.0 ([Notes](release-3.0.md)).

Jan 4, 2018: Released version 2.6.11 (a bug-fix release). Added a new
`BACKLINK-TITLE` option to the footnote extension so that non-English
users can provide a custom title to back links (see #610).

Dec 7, 2017: Released version 2.6.10 (a documentation update).

Aug 17, 2017: Released version 2.6.9 (a bug-fix release).

Jan 25, 2017: Released version 2.6.8 (a bug-fix release).

Sept 23, 2016: Released version 2.6.7 (a bug-fix release).

Mar 20, 2016: Released version 2.6.6 (a bug-fix release).

Nov 24, 2015: Released version 2.6.5 (a bug-fix release).

Nov 6, 2015: Released version 2.6.4 (a bug-fix release).

Oct 26, 2015: Released version 2.6.3 (a bug-fix release).

Apr 20, 2015: Released version 2.6.2 (a bug-fix release).

Mar 8, 2015: Released version 2.6.1 (a bug-fix release). The (new)
`yaml` option has been removed from the Meta-Data Extension as it was buggy
(see [#390](https://github.com/Python-Markdown/markdown/issues/390)).

Feb 19, 2015: Released version 2.6 ([Notes](release-2.6.md)).

Nov 19, 2014: Released version 2.5.2 (a bug-fix release).

Sept 26, 2014: Released version 2.5.1 (a bug-fix release).

Sept 12, 2014: Released version 2.5.0 ([Notes](release-2.5.md)).

Feb 16, 2014: Released version 2.4.0 ([Notes](release-2.4.md)).

Mar 22, 2013: Released version 2.3.1 (a bug-fix release).

Mar 14, 2013: Released version 2.3.0 ([Notes](release-2.3.md))

Nov 4, 2012: Released version 2.2.1 (a bug-fix release).

Jul 5, 2012: Released version 2.2.0 ([Notes](release-2.2.md)).

Jan 22, 2012: Released version 2.1.1 (a bug-fix release).

Nov 24, 2011: Released version 2.1.0 ([Notes](release-2.1.md)).

Oct 7, 2009: Released version 2.0.3. (a bug-fix release).

Sept 28, 2009: Released version 2.0.2 (a bug-fix release).

May 20, 2009: Released version 2.0.1 (a bug-fix release).

Mar 30, 2009: Released version 2.0 ([Notes](release-2.0.md)).

Mar 8, 2009: Release Candidate 2.0-rc-1.

Feb 2009: Added support for multi-level lists to new Blockprocessors.

Jan 2009: Added HTML 4 output as an option (thanks Eric Abrahamsen)

Nov 2008: Added Definition List ext. Replaced old core with Blockprocessors.
Broken up into multiple files.

Oct 2008: Changed logging behavior to work better with other systems.
Refactored tree traversing. Added `treap` implementation, then replaced with
OrderedDict. Renamed various processors to better reflect what they actually
do. Refactored footnote ext to match PHP Extra's output.

Sept 2008: Moved `prettifyTree` to a Postprocessor, replaced WikiLink ext
with WikiLinks (note the s) ext (uses bracketed links instead of CamelCase)
and various bug fixes.

August 18 2008: Reorganized directory structure. Added a 'docs' directory
and moved all extensions into a 'markdown-extensions' package.
Added additional documentation and a few bug fixes. (v2.0-beta)

August 4 2008: Updated included extensions to ElementTree. Added a
separate command line script. (v2.0-alpha)

July 2008: Switched from home-grown NanoDOM to ElementTree and
various related bugs (thanks Artem Yunusov).

June 2008: Fixed issues with nested inline patterns and cleaned
up testing framework (thanks Artem Yunusov).

May 2008: Added a number of additional extensions to the
distribution and other minor changes. Moved repository to git from svn.

Mar 2008: Refactored extension API to accept either an
extension name (as a string) or an instance of an extension
(Thanks David Wolever). Fixed various bugs and added doc strings.

Feb 2008: Various bug-fixes mostly regarding extensions.

Feb 18, 2008: Version 1.7.

Feb 13, 2008: A little code cleanup and better documentation
and inheritance for Preprocessors/Postprocessors.

Feb 9, 2008: Double-quotes no longer HTML escaped and raw HTML
honors `<?foo>`, `<@foo>`, and `<%foo>` for those who run markdown on
template syntax.

Dec 12, 2007: Updated docs. Removed encoding argument from Markdown
and markdown as per list discussion. Clean up in prep for 1.7.

Nov 29, 2007: Added support for images inside links. Also fixed
a few bugs in the footnote extension.

Nov 19, 2007: `message` now uses python's logging module. Also removed
limit imposed by recursion in `_process_section()`. You can now parse as
long of a document as your memory can handle.

Nov 5, 2007: Moved `safe_mode` code to a `textPostprocessor` and added
escaping option.

Nov 3, 2007: Fixed convert method to accept empty strings.

Oct 30, 2007: Fixed `BOM` removal (thanks Malcolm Tredinnick). Fixed
infinite loop in bracket regular expression for inline links.

Oct 11, 2007: `LineBreaks` is now an `inlinePattern`. Fixed `HR` in
blockquotes. Refactored `_processSection` method (see tracker #1793419).

Oct 9, 2007: Added `textPreprocessor` (from 1.6b).

Oct 8, 2008: Fixed Lazy Blockquote. Fixed code block on first line.
Fixed empty inline image link.

Oct 7, 2007: Limit recursion on inline patterns. Added a 'safe' tag
to `htmlStash`.

March 18, 2007: Fixed or merged a bunch of minor bugs, including
multi-line comments and markup inside links. (Tracker #s: 1683066,
1671153, 1661751, 1627935, 1544371, 1458139.) -> v. 1.6b

Oct 10, 2006: Fixed a bug that caused some text to be lost after
comments.  Added "safe mode" (user's HTML tags are removed).

Sept 6, 2006: Added exception for PHP tags when handling HTML blocks.

August 7, 2006: Incorporated Sergej Chodarev's patch to fix a problem
with ampersand normalization and HTML blocks.

July 10, 2006: Switched to using `optparse`.  Added proper support for
Unicode.

July 9, 2006: Fixed the `<!--@address.com>` problem (Tracker #1501354).

May 18, 2006: Stopped catching unquoted titles in reference links.
Stopped creating blank headers.

May 15, 2006: A bug with lists, recursion on block-level elements,
run-in headers, spaces before headers, Unicode input (thanks to Aaron
Swartz). Sourceforge tracker #s: 1489313, 1489312, 1489311, 1488370,
1485178, 1485176. (v. 1.5)

Mar. 24, 2006: Switched to a not-so-recursive algorithm with
`_handleInline`.  (Version 1.4)

Mar. 15, 2006: Replaced some instance variables with class variables
(a patch from Stelios Xanthakis).  Chris Clark's new regexps that do
not trigger mid-word underlining.

Feb. 28, 2006: Clean-up and command-line handling by Stewart
Midwinter. (Version 1.3)

Feb. 24, 2006: Fixed a bug with the last line of the list appearing
again as a separate paragraph.  Incorporated Chris Clark's "mail-to"
patch.  Added support for `<br />` at the end of lines ending in two or
more spaces.  Fixed a crashing bug when using `ImageReferencePattern`.
Added several utility methods to `Nanodom`.  (Version 1.2)

Jan. 31, 2006: Added `hr` and `hr/` to BLOCK_LEVEL_ELEMENTS and
changed `<hr/>` to `<hr />`.  (Thanks to Sergej Chodarev.)

Nov. 26, 2005: Fixed a bug with certain tabbed lines inside lists
getting wrapped in `<pre><code>`.  (v. 1.1)

Nov. 19, 2005: Made `<!...`, `<?...`, etc. behave like block-level
HTML tags.

Nov. 14, 2005: Added entity code and email auto-link fix by Tiago
Cogumbreiro.  Fixed some small issues with backticks to get 100%
compliance with John's test suite.  (v. 1.0)

Nov. 7, 2005: Added an `unlink` method for documents to aid with memory
collection (per Doug Sauder's suggestion).

Oct. 29, 2005: Restricted a set of HTML tags that get treated as
block-level elements.

Sept. 18, 2005: Refactored the whole script to make it easier to
customize it and made footnote functionality into an extension.
(v. 0.9)

Sept. 5, 2005: Fixed a bug with multi-paragraph footnotes.  Added
attribute support.

Sept. 1, 2005: Changed the way headers are handled to allow inline
syntax in headers (e.g. links) and got the lists to use p-tags
correctly (v. 0.8)

Aug. 29, 2005: Added flexible tabs, fixed a few small issues, added
basic support for footnotes.  Got rid of xml.dom.minidom and added
pretty-printing. (v. 0.7)

Aug. 13, 2005: Fixed a number of small bugs in order to conform to the
test suite.  (v. 0.6)

Aug. 11, 2005: Added support for inline HTML and entities, inline
images, auto-links, underscore emphasis. Cleaned up and refactored the
code, added some more comments.

Feb. 19, 2005: Rewrote the handling of high-level elements to allow
multi-line list items and all sorts of nesting.

Feb. 3, 2005: Reference-style links, single-line lists, backticks,
escape, emphasis in the beginning of the paragraph.

Nov. 2004: Added links, blockquotes, HTML blocks to Manfred
Stienstra's code

Apr. 2004: Manfred's version at `http://www.dwerg.net/projects/markdown/`
