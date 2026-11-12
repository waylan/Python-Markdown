# -*- coding: utf-8 -*-
"""
Python Markdown

A Python implementation of John Gruber's Markdown.

Documentation: https://python-markdown.github.io/
GitHub: https://github.com/Python-Markdown/markdown/
PyPI: https://pypi.org/project/Markdown/

Started by Manfred Stienstra (http://www.dwerg.net/).
Maintained for a few years by Yuri Takhteyev (http://www.freewisdom.org).
Currently maintained by Waylan Limberg (https://github.com/waylan),
Dmitry Shachnev (https://github.com/mitya57) and Isaac Muse (https://github.com/facelessuser).

Copyright 2007-2023 The Python Markdown Project (v. 1.7 and later)
Copyright 2004, 2005, 2006 Yuri Takhteyev (v. 0.2-1.6b)
Copyright 2004 Manfred Stienstra (the original version)

License: BSD (see LICENSE.md for details).
"""

from markdown.test_tools import TestCase


class TestIndentedHTMLBlocks(TestCase):
    """
    Raw HTML blocks which start on a line indented by more than `tab_length` spaces.

    Within a containing block (a list item, an admonition, etc.) such a block is raw HTML. Where it can not be
    (an indented code block, or a paragraph which it cannot interrupt), the document must render as it always has.
    """

    def test_mdih_admonition_markdown_attr(self):
        """
        Under md_in_html the extractor stores an `etree` Element, not `IndentedRawHtml`, and the element text
        keeps the 4-space indent, so `**test**` becomes an indented code block. Intended change: a raw block
        in a container.
        """

        self.assertMarkdownRenders(
            self.dedent(
                R'''

                !!! note "Title"
                    <div markdown>
                    **test**
                    </div>
                '''
            ),
            self.dedent(
                '''
                <div class="admonition note">
                <p class="admonition-title">Title</p>
                <div>
                <p><strong>test</strong></p>
                </div>
                </div>
                '''
            ),
            extensions=['admonition', 'md_in_html']
        )

    def test_mdih_admonition_markdown_1(self):
        """Same as above with markdown='1'. Intended change: a raw block in a container."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                !!! note "Title"
                    <div markdown="1">
                    **test**
                    </div>
                '''
            ),
            self.dedent(
                '''
                <div class="admonition note">
                <p class="admonition-title">Title</p>
                <div>
                <p><strong>test</strong></p>
                </div>
                </div>
                '''
            ),
            extensions=['admonition', 'md_in_html']
        )

    def test_mdih_admonition_markdown_block_blank_lines(self):
        """markdown='block' with blank lines inside the element. Intended change: a raw block in a container."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                !!! note "Title"
                    <div markdown="block">

                    **test**

                    - a
                    - b

                    </div>
                '''
            ),
            self.dedent(
                '''
                <div class="admonition note">
                <p class="admonition-title">Title</p>
                <div>
                <p><strong>test</strong></p>
                <ul>
                <li>a</li>
                <li>b</li>
                </ul>
                </div>
                </div>
                '''
            ),
            extensions=['admonition', 'md_in_html']
        )

    def test_mdih_admonition_markdown_span(self):
        """markdown='span' inside an admonition. Intended change: a raw block in a container."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                !!! note "Title"
                    <div markdown="span">
                    **test**
                    </div>
                '''
            ),
            self.dedent(
                '''
                <div class="admonition note">
                <p class="admonition-title">Title</p>
                <div>
                <strong>test</strong>
                </div>
                </div>
                '''
            ),
            extensions=['admonition', 'md_in_html']
        )

    def test_mdih_admonition_nested_markdown(self):
        """
        Nested md_in_html elements: inner indentation relative to the outer start tag must survive. Intended
        change: a raw block in a container.
        """

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                !!! note "Title"
                    <div markdown>
                    <div markdown>
                    **test**
                    </div>
                    </div>
                '''
            ),
            self.dedent(
                '''
                <div class="admonition note">
                <p class="admonition-title">Title</p>
                <div>
                <div>
                <p><strong>test</strong></p>
                </div>
                </div>
                </div>
                '''
            ),
            extensions=['admonition', 'md_in_html']
        )

    def test_mdih_admonition_markdown_deeper_content(self):
        """
        Content indented deeper than the start tag: that part is a real indented code block. Intended
        change: a raw block in a container.
        """

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                !!! note "Title"
                    <div markdown>
                        code

                    **test**
                    </div>
                '''
            ),
            self.dedent(
                '''
                <div class="admonition note">
                <p class="admonition-title">Title</p>
                <div>
                <pre><code>code
                </code></pre>
                <p><strong>test</strong></p>
                </div>
                </div>
                '''
            ),
            extensions=['admonition', 'md_in_html']
        )

    def test_mdih_list_item_markdown(self):
        """md_in_html element inside a list item. Intended change: a raw block in a container."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                - item

                    <div markdown>
                    **test**
                    </div>
                '''
            ),
            self.dedent(
                '''
                <ul>
                <li>
                <p>item</p>
                <div>
                <p><strong>test</strong></p>
                </div>
                </li>
                </ul>
                '''
            ),
            extensions=['admonition', 'md_in_html']
        )

    def test_mdih_admonition_raw_div(self):
        """
        No `markdown` attribute: raw, content must stay literal. Intended change: a raw block in a
        container.
        """

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                !!! note "Title"
                    <div>
                    **test**
                    </div>
                '''
            ),
            self.dedent(
                '''
                <div class="admonition note">
                <p class="admonition-title">Title</p>
                <div>
                **test**
                </div>
                </div>
                '''
            ),
            extensions=['admonition', 'md_in_html']
        )

    def test_mdih_code_block_root(self):
        """
        an indented code block containing `<div markdown>` must stay escaped code. Regression: renders as it
        always has.
        """

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                text

                    <div markdown>
                    **x**
                    </div>
                '''
            ),
            self.dedent(
                '''
                <p>text</p>
                <pre><code>&lt;div markdown&gt;
                **x**
                &lt;/div&gt;
                </code></pre>
                '''
            ),
            extensions=['admonition', 'md_in_html']
        )

    def test_mdih_code_block_root_blank_lines(self):
        """Same with blank lines inside the element. Regression: renders as it always has."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                text

                    <div markdown>

                    **x**

                    </div>
                '''
            ),
            self.dedent(
                '''
                <p>text</p>
                <pre><code>&lt;div markdown&gt;

                **x**

                &lt;/div&gt;
                </code></pre>
                '''
            ),
            extensions=['admonition', 'md_in_html']
        )

    def test_mdih_code_block_in_list(self):
        """
        Code block (8 spaces) in a list item containing `<div markdown>`. Regression: renders as it always
        has.
        """

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                - item

                        <div markdown>
                        **x**
                        </div>
                '''
            ),
            self.dedent(
                '''
                <ul>
                <li>item<pre><code>&lt;div markdown&gt;
                **x**
                &lt;/div&gt;
                </code></pre>
                </li>
                </ul>
                '''
            ),
            extensions=['admonition', 'md_in_html']
        )

    def test_mdih_code_block_in_admonition(self):
        """
        Code block (8 spaces) in an admonition containing `<div markdown>`. Regression: renders as it always
        has.
        """

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                !!! note "Title"
                        <div markdown>
                        **x**
                        </div>
                '''
            ),
            self.dedent(
                '''
                <div class="admonition note">
                <p class="admonition-title">Title</p>
                <pre><code>&lt;div markdown&gt;
                **x**
                &lt;/div&gt;
                </code></pre>
                </div>
                '''
            ),
            extensions=['admonition', 'md_in_html']
        )

    def test_mdih_code_block_with_more_code(self):
        """
        Code after the element in the same code block must not gain blank lines. Regression: renders as it
        always has.
        """

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                text

                    <div markdown>
                    **x**
                    </div>
                    more code
                '''
            ),
            self.dedent(
                '''
                <p>text</p>
                <pre><code>&lt;div markdown&gt;
                **x**
                &lt;/div&gt;
                more code
                </code></pre>
                '''
            ),
            extensions=['admonition', 'md_in_html']
        )

    def test_mdih_unclosed(self):
        """
        Unclosed `markdown` element in a container (source no longer available at close()). Intended change:
        a raw block in a container.
        """

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                !!! note "Title"
                    <div markdown>
                    **test**
                '''
            ),
            self.dedent(
                '''
                <div class="admonition note">
                <p class="admonition-title">Title</p>
                <div>
                <p><strong>test</strong></p>
                </div>
                </div>
                '''
            ),
            extensions=['admonition', 'md_in_html']
        )

    def test_mdih_unclosed_in_code_block(self):
        """
        Unclosed `markdown` element inside an indented code block must show its source as written (no
        `markdown='block'`, no double escaping, no invented </div>). Regression: renders as it always has.
        """

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                text

                    <div markdown>
                    **x** & <b>y</b>
                '''
            ),
            self.dedent(
                '''
                <p>text</p>
                <pre><code>&lt;div markdown&gt;
                **x** &amp; &lt;b&gt;y&lt;/b&gt;
                </code></pre>
                '''
            ),
            extensions=['admonition', 'md_in_html']
        )

    def test_mdih_unclosed_nested_in_code_block(self):
        """Same with an unclosed nested element. Regression: renders as it always has."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                text

                    <div markdown>
                    <p markdown>
                    **x**
                '''
            ),
            self.dedent(
                '''
                <p>text</p>
                <pre><code>&lt;div markdown&gt;
                &lt;p markdown&gt;
                **x**
                </code></pre>
                '''
            ),
            extensions=['admonition', 'md_in_html']
        )

    def test_mdih_unclosed_in_admonition_code_block(self):
        """Same inside an admonition (8 spaces). Regression: renders as it always has."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                !!! note
                        <div markdown>
                        **x**
                '''
            ),
            self.dedent(
                '''
                <div class="admonition note">
                <p class="admonition-title">Note</p>
                <pre><code>&lt;div markdown&gt;
                **x**
                </code></pre>
                </div>
                '''
            ),
            extensions=['admonition', 'md_in_html']
        )

    def test_mdih_tail_text(self):
        """Text after the closing tag on the same line. Intended change: a raw block in a container."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                !!! note "Title"
                    <div markdown>
                    **test**
                    </div> tail

                    after
                '''
            ),
            self.dedent(
                '''
                <div class="admonition note">
                <p class="admonition-title">Title</p>
                <div>
                <p><strong>test</strong></p>
                </div>
                <p>tail</p>
                <p>after</p>
                </div>
                '''
            ),
            extensions=['admonition', 'md_in_html']
        )

    def test_admonition_div(self):
        """ Intended change: a raw block in a container."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                !!! note "Title"
                    <div>
                    **test**
                    </div>
                    after
                '''
            ),
            self.dedent(
                '''
                <div class="admonition note">
                <p class="admonition-title">Title</p>
                <div>
                **test**
                </div>
                <p>after</p>
                </div>
                '''
            ),
            extensions=['admonition']
        )

    def test_admonition_div_blank_lines(self):
        """ Intended change: a raw block in a container."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                !!! note "Title"
                    <div>

                    **test**

                    </div>

                    after
                '''
            ),
            self.dedent(
                '''
                <div class="admonition note">
                <p class="admonition-title">Title</p>
                <div>

                **test**

                </div>
                <p>after</p>
                </div>
                '''
            ),
            extensions=['admonition']
        )

    def test_list_item_div(self):
        """
        raw block in a list item should not be split at blank lines. Intended change: a raw block in a
        container.
        """

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                - item

                    <div>

                    **test**

                    </div>

                    after
                '''
            ),
            self.dedent(
                '''
                <ul>
                <li>
                <p>item</p>
                <div>

                **test**

                </div>
                <p>after</p>
                </li>
                </ul>
                '''
            )
        )

    def test_nested_admonition_div(self):
        """Two levels of containers; indent of the tag is 8. Intended change: a raw block in a container."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                !!! note "Outer"
                    !!! note "Inner"
                        <div>
                        **test**
                        </div>
                '''
            ),
            self.dedent(
                '''
                <div class="admonition note">
                <p class="admonition-title">Outer</p>
                <div class="admonition note">
                <p class="admonition-title">Inner</p>
                <div>
                **test**
                </div>
                </div>
                </div>
                '''
            ),
            extensions=['admonition']
        )

    def test_admonition_div_deeper_lines(self):
        """
        Lines inside the raw block indented deeper than the start tag must keep the extra indent. Intended
        change: a raw block in a container.
        """

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                !!! note "Title"
                    <div>
                        <p>deeper</p>
                    </div>
                '''
            ),
            self.dedent(
                '''
                <div class="admonition note">
                <p class="admonition-title">Title</p>
                <div>
                    <p>deeper</p>
                </div>
                </div>
                '''
            ),
            extensions=['admonition']
        )

    def test_admonition_pre(self):
        """Whitespace-sensitive <pre> in a container. Intended change: a raw block in a container."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                !!! note "Title"
                    <pre>
                      keep
                        this
                    </pre>
                '''
            ),
            self.dedent(
                '''
                <div class="admonition note">
                <p class="admonition-title">Title</p>
                <pre>
                  keep
                    this
                </pre>
                </div>
                '''
            ),
            extensions=['admonition']
        )

    def test_admonition_script(self):
        """<script> in a container. Intended change: a raw block in a container."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                !!! note "Title"
                    <script>
                    var x = "**no**";
                    </script>
                '''
            ),
            self.dedent(
                '''
                <div class="admonition note">
                <p class="admonition-title">Title</p>
                <script>
                var x = "**no**";
                </script>
                </div>
                '''
            ),
            extensions=['admonition']
        )

    def test_admonition_comment(self):
        """
        Indented HTML comment (handled by handle_empty_tag / parse_comment path). Regression: renders as it
        always has.
        """

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                !!! note "Title"
                    <!-- a **comment** -->

                    after
                '''
            ),
            self.dedent(
                '''
                <div class="admonition note">
                <p class="admonition-title">Title</p>
                <!-- a **comment** -->
                <p>after</p>
                </div>
                '''
            ),
            extensions=['admonition']
        )

    def test_admonition_unclosed_div(self):
        """
        Unclosed raw block at end of document (flush in close()). Intended change: a raw block in a
        container.
        """

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                !!! note "Title"
                    <div>
                    **test**
                '''
            ),
            self.dedent(
                '''
                <div class="admonition note">
                <p class="admonition-title">Title</p>
                <div>
                **test**
                </div>
                '''
            ),
            extensions=['admonition']
        )

    def test_paragraph_continuation_div(self):
        """
        An indented line directly after paragraph text is a paragraph continuation, not code. Regression:
        renders as it always has.
        """

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                some text
                    <div>x</div>
                '''
            ),
            self.dedent(
                '''
                <p>some text
                    <div>x</div></p>
                '''
            )
        )

    def test_paragraph_continuation_div_multiline(self):
        """Same, multi-line raw block. Regression: renders as it always has."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                some text
                    <div>
                    **x**
                    </div>
                more text
                '''
            ),
            self.dedent(
                '''
                <p>some text
                    <div>
                    <strong>x</strong>
                    </div>
                more text</p>
                '''
            )
        )

    def test_paragraph_chain_with_text(self):
        """
        Blocks that start where the last one ended, mid-paragraph, then text. Must stay one inline run.
        Regression: renders as it always has.
        """

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                some text
                    <div>a</div><div>b</div> trailing
                '''
            ),
            self.dedent(
                '''
                <p>some text
                    <div>a</div><div>b</div> trailing</p>
                '''
            )
        )

    def test_paragraph_chain_with_more_lines(self):
        """
        Same with an indented continuation line and a following paragraph. Regression: renders as it always
        has.
        """

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                some text
                    <div>a</div><div>b</div> trailing
                    more

                after
                '''
            ),
            self.dedent(
                '''
                <p>some text
                    <div>a</div><div>b</div> trailing
                    more</p>
                <p>after</p>
                '''
            )
        )

    def test_paragraph_chain_of_three(self):
        """Three blocks in a row. Regression: renders as it always has."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                some text
                    <div>a</div><div>b</div><div>c</div>
                '''
            ),
            self.dedent(
                '''
                <p>some text
                    <div>a</div><div>b</div><div>c</div></p>
                '''
            )
        )

    def test_paragraph_chain_multiline(self):
        """ Regression: renders as it always has."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                some text
                    <div>
                    a
                    </div><div>
                    b
                    </div> trailing
                more
                '''
            ),
            self.dedent(
                '''
                <p>some text
                    <div>
                    a
                    </div><div>
                    b
                    </div> trailing
                more</p>
                '''
            )
        )

    def test_paragraph_chain_multiline_indented(self):
        """Same with the continuation line indented. Regression: renders as it always has."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                some text
                    <div>
                    a
                    </div><div>
                    b
                    </div> trailing
                    more
                '''
            ),
            self.dedent(
                '''
                <p>some text
                    <div>
                    a
                    </div><div>
                    b
                    </div> trailing
                    more</p>
                '''
            )
        )

    def test_code_chain_blocks(self):
        """ Regression: renders as it always has."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                text

                    <div>a</div><div>b</div><div>c</div> trailing
                    more
                '''
            ),
            self.dedent(
                '''
                <p>text</p>
                <pre><code>&lt;div&gt;a&lt;/div&gt;&lt;div&gt;b&lt;/div&gt;&lt;div&gt;c&lt;/div&gt; trailing
                more
                </code></pre>
                '''
            )
        )

    def test_code_chain_multiline(self):
        """Same, multi-line blocks. Regression: renders as it always has."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                text

                    <div>
                    a
                    </div><div>
                    b
                    </div> trailing
                    more
                '''
            ),
            self.dedent(
                '''
                <p>text</p>
                <pre><code>&lt;div&gt;
                a
                &lt;/div&gt;&lt;div&gt;
                b
                &lt;/div&gt; trailing
                more
                </code></pre>
                '''
            )
        )

    def test_list_lazy_chain(self):
        """ Regression: renders as it always has."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                - item
                    <div>a</div><div>b</div> trailing
                '''
            ),
            self.dedent(
                '''
                <ul>
                <li>item
                    <div>a</div><div>b</div> trailing</li>
                </ul>
                '''
            )
        )

    def test_list_lazy_div_next_item(self):
        """
        Indented div on a lazy line of a list item, followed by another item. Both items must stay tight (no
        <p>): nothing may be inserted between the placeholder and the next item. Regression: renders as it
        always has.
        """

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                - item
                    <div>x</div>
                - b
                '''
            ),
            self.dedent(
                '''
                <ul>
                <li>item
                    <div>x</div></li>
                <li>b</li>
                </ul>
                '''
            )
        )

    def test_list_lazy_tail_next_item(self):
        """
        Same with text after the closing tag. The next item must not be swallowed into the paragraph.
        Regression: renders as it always has.
        """

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                - item
                    <div>x</div> trailing
                - b
                '''
            ),
            self.dedent(
                '''
                <ul>
                <li>item
                    <div>x</div> trailing</li>
                <li>b</li>
                </ul>
                '''
            )
        )

    def test_list_lazy_tail_next_item_ordered(self):
        """Same in an ordered list. Regression: renders as it always has."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                1. item
                    <div>x</div> trailing
                2. b
                '''
            ),
            self.dedent(
                '''
                <ol>
                <li>item
                    <div>x</div> trailing</li>
                <li>b</li>
                </ol>
                '''
            )
        )

    def test_paragraph_tail_then_code(self):
        """
        Text after the closing tag in a paragraph, then a blank line and an indented code block. The code
        block must stay a code block. Regression: renders as it always has.
        """

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                some text
                    <div>x</div> trailing

                    code
                '''
            ),
            self.dedent(
                '''
                <p>some text
                    <div>x</div> trailing</p>
                <pre><code>code
                </code></pre>
                '''
            )
        )

    def test_fn_div_blank_lines(self):
        """Raw HTML with blank lines in a footnote. Intended change: a raw block in a container."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                Text[^1]

                [^1]:
                    <div>

                    **x**

                    </div>

                    after
                '''
            ),
            '<p>Text<sup id="fnref:1"><a class="footnote-ref" href="#fn:1">1</a></sup></p>\n'
            '<div class="footnote">\n'
            '<hr />\n'
            '<ol>\n'
            '<li id="fn:1">\n'
            '<div>\n'
            '\n'
            '**x**\n'
            '\n'
            '</div>\n'
            '<p>after&#160;<a class="footnote-backref" href="#fnref:1" title="Jump'
            ' back to footnote 1 in the text">&#8617;</a></p>\n'
            '</li>\n'
            '</ol>\n'
            '</div>',
            extensions=['footnotes']
        )

    def test_fn_text_then_div(self):
        """Raw HTML after the text of a footnote. Intended change: a raw block in a container."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                Text[^1]

                [^1]: Note text.

                    <div>
                    **x**
                    </div>

                    after
                '''
            ),
            '<p>Text<sup id="fnref:1"><a class="footnote-ref" href="#fn:1">1</a></sup></p>\n'
            '<div class="footnote">\n'
            '<hr />\n'
            '<ol>\n'
            '<li id="fn:1">\n'
            '<p>Note text.</p>\n'
            '<div>\n'
            '**x**\n'
            '</div>\n'
            '<p>after&#160;<a class="footnote-backref" href="#fnref:1" title="Jump'
            ' back to footnote 1 in the text">&#8617;</a></p>\n'
            '</li>\n'
            '</ol>\n'
            '</div>',
            extensions=['footnotes']
        )

    def test_fn_lazy_div(self):
        """
        Indented HTML on a lazy line of a footnote is part of the paragraph. Regression: renders as it
        always has.
        """

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                Text[^1]

                [^1]: Note text.
                    <div>x</div>
                '''
            ),
            '<p>Text<sup id="fnref:1"><a class="footnote-ref" href="#fn:1">1</a></sup></p>\n'
            '<div class="footnote">\n'
            '<hr />\n'
            '<ol>\n'
            '<li id="fn:1">\n'
            '<p>Note text.\n'
            '<div>x</div>&#160;<a class="footnote-backref" href="#fnref:1"'
            ' title="Jump back to footnote 1 in the text">&#8617;</a></p>\n'
            '</li>\n'
            '</ol>\n'
            '</div>',
            extensions=['footnotes']
        )

    def test_fn_code_with_html(self):
        """Indented code with HTML in a footnote. Regression: renders as it always has."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                Text[^1]

                [^1]: Note.

                        <div>

                        code
                        </div>
                '''
            ),
            '<p>Text<sup id="fnref:1"><a class="footnote-ref" href="#fn:1">1</a></sup></p>\n'
            '<div class="footnote">\n'
            '<hr />\n'
            '<ol>\n'
            '<li id="fn:1">\n'
            '<p>Note.</p>\n'
            '<pre><code>&lt;div&gt;\n'
            '\n'
            'code\n'
            '&lt;/div&gt;\n'
            '</code></pre>\n'
            '<p><a class="footnote-backref" href="#fnref:1" title="Jump back to'
            ' footnote 1 in the text">&#8617;</a></p>\n'
            '</li>\n'
            '</ol>\n'
            '</div>',
            extensions=['footnotes']
        )

    def test_fn_mdhtml(self):
        """A `markdown` element with blank lines in a footnote. Intended change: a raw block in a container."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                Text[^1]

                [^1]:
                    <div markdown>

                    **x**

                    </div>
                '''
            ),
            '<p>Text<sup id="fnref:1"><a class="footnote-ref" href="#fn:1">1</a></sup></p>\n'
            '<div class="footnote">\n'
            '<hr />\n'
            '<ol>\n'
            '<li id="fn:1">\n'
            '<div>\n'
            '<p><strong>x</strong></p>\n'
            '</div>\n'
            '<p><a class="footnote-backref" href="#fnref:1" title="Jump back to'
            ' footnote 1 in the text">&#8617;</a></p>\n'
            '</li>\n'
            '</ol>\n'
            '</div>',
            extensions=['footnotes', 'md_in_html']
        )

    def test_fn_unclosed(self):
        """An unclosed raw block in a footnote. Intended change: a raw block in a container."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                Text[^1]

                [^1]:
                    <div>

                    **x**
                '''
            ),
            '<p>Text<sup id="fnref:1"><a class="footnote-ref" href="#fn:1">1</a></sup></p>\n'
            '<div class="footnote">\n'
            '<hr />\n'
            '<ol>\n'
            '<li id="fn:1">\n'
            '<p><div>\n'
            '\n'
            '**x**&#160;<a class="footnote-backref" href="#fnref:1" title="Jump'
            ' back to footnote 1 in the text">&#8617;</a></p>\n'
            '</li>\n'
            '</ol>\n'
            '</div>',
            extensions=['footnotes']
        )

    def test_dl_div_blank_lines(self):
        """Raw HTML with blank lines in a definition. Intended change: a raw block in a container."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                Term
                :   para

                    <div>

                    **x**

                    </div>

                    after
                '''
            ),
            self.dedent(
                '''
                <dl>
                <dt>Term</dt>
                <dd>
                <p>para</p>
                <div>

                **x**

                </div>
                <p>after</p>
                </dd>
                </dl>
                '''
            ),
            extensions=['def_list']
        )

    def test_dl_div_after_definition(self):
        """Raw HTML after the text of a definition. Intended change: a raw block in a container."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                Term
                :   definition

                    <div>
                    **x**
                    </div>
                '''
            ),
            self.dedent(
                '''
                <dl>
                <dt>Term</dt>
                <dd>
                <p>definition</p>
                <div>
                **x**
                </div>
                </dd>
                </dl>
                '''
            ),
            extensions=['def_list']
        )

    def test_dl_lazy_div(self):
        """
        Indented HTML on a lazy line of a definition is part of the paragraph. Regression: renders as it
        always has.
        """

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                Term
                :   definition
                    <div>x</div>
                '''
            ),
            self.dedent(
                '''
                <dl>
                <dt>Term</dt>
                <dd>definition
                <div>x</div></dd>
                </dl>
                '''
            ),
            extensions=['def_list']
        )

    def test_dl_code_with_html(self):
        """Indented code with HTML in a definition. Regression: renders as it always has."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                Term
                :   definition

                        <div>

                        code
                        </div>
                '''
            ),
            self.dedent(
                '''
                <dl>
                <dt>Term</dt>
                <dd>definition<pre><code>&lt;div&gt;

                code
                &lt;/div&gt;
                </code></pre>
                </dd>
                </dl>
                '''
            ),
            extensions=['def_list']
        )

    def test_dl_mdhtml(self):
        """A `markdown` element with blank lines in a definition. Intended change: a raw block in a container."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                Term
                :   para

                    <div markdown>

                    **x**

                    </div>
                '''
            ),
            self.dedent(
                '''
                <dl>
                <dt>Term</dt>
                <dd>
                <p>para</p>
                <div>
                <p><strong>x</strong></p>
                </div>
                </dd>
                </dl>
                '''
            ),
            extensions=['def_list', 'md_in_html']
        )

    def test_dl_unclosed(self):
        """An unclosed raw block in a definition. Intended change: a raw block in a container."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                Term
                :   para

                    <div>

                    **x**
                '''
            ),
            self.dedent(
                '''
                <dl>
                <dt>Term</dt>
                <dd>
                <p>para</p>
                <div>

                **x**
                </dd>
                </dl>
                '''
            ),
            extensions=['def_list']
        )

    def test_adm_in_footnote(self):
        """Raw HTML in an admonition in a footnote. Intended change: a raw block in a container."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                Text[^1]

                [^1]:
                    !!! note
                        <div>

                        **x**

                        </div>
                '''
            ),
            '<p>Text<sup id="fnref:1"><a class="footnote-ref" href="#fn:1">1</a></sup></p>\n'
            '<div class="footnote">\n'
            '<hr />\n'
            '<ol>\n'
            '<li id="fn:1">\n'
            '<div class="admonition note">\n'
            '<p class="admonition-title">Note</p>\n'
            '<div>\n'
            '\n'
            '**x**\n'
            '\n'
            '</div>\n'
            '</div>\n'
            '<p><a class="footnote-backref" href="#fnref:1" title="Jump back to'
            ' footnote 1 in the text">&#8617;</a></p>\n'
            '</li>\n'
            '</ol>\n'
            '</div>',
            extensions=['footnotes', 'admonition']
        )

    def test_list_in_admonition(self):
        """Raw HTML with blank lines in a list in an admonition. Intended change: a raw block in a container."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                !!! note
                    - item

                        <div>

                        **x**

                        </div>

                        after
                '''
            ),
            self.dedent(
                '''
                <div class="admonition note">
                <p class="admonition-title">Note</p>
                <ul>
                <li>
                <p>item</p>
                <div>

                **x**

                </div>
                <p>after</p>
                </li>
                </ul>
                </div>
                '''
            ),
            extensions=['admonition']
        )

    def test_admonition_in_list_in_definition(self):
        """Three levels of containers. Intended change: a raw block in a container."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                Term
                :   - item

                        !!! note
                            <div>

                            **x**

                            </div>
                '''
            ),
            self.dedent(
                '''
                <dl>
                <dt>Term</dt>
                <dd>
                <ul>
                <li>
                <p>item</p>
                <div class="admonition note">
                <p class="admonition-title">Note</p>
                <div>

                **x**

                </div>
                </div>
                </li>
                </ul>
                </dd>
                </dl>
                '''
            ),
            extensions=['def_list', 'admonition']
        )

    def test_admonition_in_blockquote(self):
        """
        An admonition in a blockquote is a container, so its indented HTML is raw. Intended change: a raw
        block in a container.
        """

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                > !!! note
                >     <div>
                >     **x**
                >     </div>
                '''
            ),
            self.dedent(
                '''
                <blockquote>
                <div class="admonition note">
                <p class="admonition-title">Note</p>
                <div>
                **x**
                </div>
                </div>
                </blockquote>
                '''
            ),
            extensions=['admonition']
        )

    def test_blockquote_in_admonition(self):
        """A blockquote is a container too, so HTML in one is raw. Intended change: a raw block in a container."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                !!! note
                    > <div>
                    > **x**
                    > </div>
                '''
            ),
            self.dedent(
                '''
                <div class="admonition note">
                <p class="admonition-title">Note</p>
                <blockquote>
                <div>
                **x**
                </div>
                </blockquote>
                </div>
                '''
            ),
            extensions=['admonition']
        )

    def test_blockquote_div(self):
        """A block of HTML in a blockquote is raw. Intended change: a raw block in a container."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                > <div>
                > **x**
                > </div>
                '''
            ),
            self.dedent(
                '''
                <blockquote>
                <div>
                **x**
                </div>
                </blockquote>
                '''
            )
        )

    def test_blockquote_div_blank_lines(self):
        """Blank lines in the raw block do not end it. Intended change: a raw block in a container."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                > <div>
                >
                > **x**
                >
                > </div>
                '''
            ),
            self.dedent(
                '''
                <blockquote>
                <div>

                **x**

                </div>
                </blockquote>
                '''
            )
        )

    def test_blockquote_div_after_paragraph(self):
        """Raw block after a paragraph in a blockquote. Intended change: a raw block in a container."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                > para
                >
                > <div>
                > **x**
                > </div>
                '''
            ),
            self.dedent(
                '''
                <blockquote>
                <p>para</p>
                <div>
                **x**
                </div>
                </blockquote>
                '''
            )
        )

    def test_blockquote_div_then_paragraph(self):
        """A paragraph follows the raw block. Intended change: a raw block in a container."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                > <div>
                > x
                > </div>
                >
                > after
                '''
            ),
            self.dedent(
                '''
                <blockquote>
                <div>
                x
                </div>
                <p>after</p>
                </blockquote>
                '''
            )
        )

    def test_blockquote_text_after_close(self):
        """
        Text after the end of the raw block starts its own paragraph. Intended change: a raw block in a
        container.
        """

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                > <div>x</div>
                > more
                '''
            ),
            self.dedent(
                '''
                <blockquote>
                <div>x</div>
                <p>more</p>
                </blockquote>
                '''
            )
        )

    def test_blockquote_two_blocks(self):
        """Two raw blocks in a blockquote. Intended change: a raw block in a container."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                > <div>a</div>
                >
                > <div>b</div>
                '''
            ),
            self.dedent(
                '''
                <blockquote>
                <div>a</div>
                <div>b</div>
                </blockquote>
                '''
            )
        )

    def test_blockquote_chained_blocks(self):
        """Raw blocks that start where the last one ended. Intended change: a raw block in a container."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                > <div>a</div><div>b</div> tail
                '''
            ),
            self.dedent(
                '''
                <blockquote>
                <div>a</div>
                <div>b</div>
                <p>tail</p>
                </blockquote>
                '''
            )
        )

    def test_blockquote_lazy_line_in_html(self):
        """A lazy line inside the raw block belongs to it. Intended change: a raw block in a container."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                > <div>
                lazy
                > </div>
                '''
            ),
            self.dedent(
                '''
                <blockquote>
                <div>
                lazy
                </div>
                </blockquote>
                '''
            )
        )

    def test_blockquote_lazy_line_after_html(self):
        """
        A lazy line after the raw block is a paragraph in the blockquote. Intended change: a raw block in a
        container.
        """

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                > <div>x</div>
                lazy
                '''
            ),
            self.dedent(
                '''
                <blockquote>
                <div>x</div>
                <p>lazy</p>
                </blockquote>
                '''
            )
        )

    def test_blockquote_unclosed_html(self):
        """
        A raw block that is never closed ends with the blockquote. Intended change: a raw block in a
        container.
        """

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                > <div>
                > x

                after
                '''
            ),
            self.dedent(
                '''
                <blockquote>
                <div>
                x
                </blockquote>
                <p>after</p>
                '''
            )
        )

    def test_blockquote_nested(self):
        """Raw block in a nested blockquote. Intended change: a raw block in a container."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                > > <div>
                > > **x**
                > > </div>
                '''
            ),
            self.dedent(
                '''
                <blockquote>
                <blockquote>
                <div>
                **x**
                </div>
                </blockquote>
                </blockquote>
                '''
            )
        )

    def test_blockquote_nested_after_text(self):
        """Raw block in a blockquote nested after text. Intended change: a raw block in a container."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                > text
                > > <div>
                > > x
                > > </div>
                '''
            ),
            self.dedent(
                '''
                <blockquote>
                <p>text</p>
                <blockquote>
                <div>
                x
                </div>
                </blockquote>
                </blockquote>
                '''
            )
        )

    def test_blockquote_in_list(self):
        """Raw block in a blockquote in a list item. Intended change: a raw block in a container."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                - item

                    > <div>
                    > **x**
                    > </div>
                '''
            ),
            self.dedent(
                '''
                <ul>
                <li>
                <p>item</p>
                <blockquote>
                <div>
                **x**
                </div>
                </blockquote>
                </li>
                </ul>
                '''
            )
        )

    def test_blockquote_on_list_marker(self):
        """Raw block in a blockquote on the line of a list marker. Intended change: a raw block in a container."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                - > <div>
                  > **x**
                  > </div>
                '''
            ),
            self.dedent(
                '''
                <ul>
                <li>
                <blockquote>
                <div>
                **x**
                </div>
                </blockquote>
                </li>
                </ul>
                '''
            )
        )

    def test_blockquote_comment(self):
        """A comment in a blockquote is raw. Intended change: a raw block in a container."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                > <!-- c -->
                > text
                '''
            ),
            self.dedent(
                '''
                <blockquote>
                <!-- c -->
                <p>text</p>
                </blockquote>
                '''
            )
        )

    def test_blockquote_pre_blank_line(self):
        """A blank line in a raw block does not split it. Intended change: a raw block in a container."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                > <pre>
                > a
                >
                > b
                > </pre>
                '''
            ),
            self.dedent(
                '''
                <blockquote>
                <pre>
                a

                b
                </pre>
                </blockquote>
                '''
            )
        )

    def test_blockquote_script(self):
        """The content of a raw block is not escaped. Intended change: a raw block in a container."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                > <script>
                > var a = 1 < 2;
                > </script>
                '''
            ),
            self.dedent(
                '''
                <blockquote>
                <script>
                var a = 1 < 2;
                </script>
                </blockquote>
                '''
            )
        )

    def test_blockquote_table(self):
        """A table in a blockquote. Intended change: a raw block in a container."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                > <table>
                > <tr><td>x</td></tr>
                > </table>
                '''
            ),
            self.dedent(
                '''
                <blockquote>
                <table>
                <tr><td>x</td></tr>
                </table>
                </blockquote>
                '''
            )
        )

    def test_blockquote_md_in_html(self):
        """A `markdown` attribute works in a blockquote. Intended change: a raw block in a container."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                > <div markdown>
                > **x**
                > </div>
                '''
            ),
            self.dedent(
                '''
                <blockquote>
                <div>
                <p><strong>x</strong></p>
                </div>
                </blockquote>
                '''
            ),
            extensions=['md_in_html']
        )

    def test_blockquote_md_in_html_block(self):
        """A `markdown` attribute with blank lines. Intended change: a raw block in a container."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                > <div markdown="block">
                >
                > **x**
                >
                > </div>
                '''
            ),
            self.dedent(
                '''
                <blockquote>
                <div>
                <p><strong>x</strong></p>
                </div>
                </blockquote>
                '''
            ),
            extensions=['md_in_html']
        )

    def test_blockquote_in_footnote(self):
        """Raw block in a blockquote in a footnote. Intended change: a raw block in a container."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                text[^1]

                [^1]:
                    > <div>
                    > x
                    > </div>
                '''
            ),
            '<p>text<sup id="fnref:1"><a class="footnote-ref" href="#fn:1">1</a></sup></p>\n'
            '<div class="footnote">\n'
            '<hr />\n'
            '<ol>\n'
            '<li id="fn:1">\n'
            '<blockquote>\n'
            '<div>\n'
            'x\n'
            '</div>\n'
            '</blockquote>\n'
            '<p><a class="footnote-backref" href="#fnref:1" title="Jump back to'
            ' footnote 1 in the text">&#8617;</a></p>\n'
            '</li>\n'
            '</ol>\n'
            '</div>',
            extensions=['footnotes']
        )

    def test_blockquote_paragraph_continuation(self):
        """A raw block can not interrupt a paragraph in a blockquote. Regression: renders as it always has."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                > a
                > <div>x</div>
                '''
            ),
            self.dedent(
                '''
                <blockquote>
                <p>a
                <div>x</div></p>
                </blockquote>
                '''
            )
        )

    def test_blockquote_inline_tag(self):
        """An inline tag in a blockquote is not a raw block. Regression: renders as it always has."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                > <span>x</span> text
                '''
            ),
            self.dedent(
                '''
                <blockquote>
                <p><span>x</span> text</p>
                </blockquote>
                '''
            )
        )

    def test_blockquote_code_block(self):
        """An indented code block in a blockquote is code. Regression: renders as it always has."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                >     <div>
                >     x
                >     </div>
                '''
            ),
            self.dedent(
                '''
                <blockquote>
                <pre><code>&lt;div&gt;
                x
                &lt;/div&gt;
                </code></pre>
                </blockquote>
                '''
            )
        )

    def test_blockquote_fenced_code(self):
        """HTML in a fenced code block in a blockquote is code. Regression: renders as it always has."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                > ```
                > <div>
                > ```
                '''
            ),
            self.dedent(
                '''
                <blockquote>
                <p><code>&lt;div&gt;</code></p>
                </blockquote>
                '''
            ),
            extensions=['fenced_code']
        )

    def test_blockquote_list_marker_html(self):
        """
        What follows a list marker in a blockquote is parsed as it always has been. Regression: renders as
        it always has.
        """

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                > - <div>x</div>
                '''
            ),
            self.dedent(
                '''
                <blockquote>
                <ul>
                <li><div>x</div></li>
                </ul>
                </blockquote>
                '''
            )
        )

    def test_blockquote_invalid_declaration(self):
        """
        Something the extractor does not treat as a raw block is left alone. Regression: renders as it
        always has.
        """

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                > <!invalid>
                > text
                '''
            ),
            self.dedent(
                '''
                <blockquote>
                <p>&lt;!invalid&gt;
                text</p>
                </blockquote>
                '''
            )
        )

    def test_comment_blank_line_admonition(self):
        """A comment with a blank line in it is one raw block. Intended change: a raw block in a container."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                !!! note
                    <!--
                    c

                    -->
                    text
                '''
            ),
            self.dedent(
                '''
                <div class="admonition note">
                <p class="admonition-title">Note</p>
                <!--
                c

                -->
                <p>text</p>
                </div>
                '''
            ),
            extensions=['admonition']
        )

    def test_comment_blank_line_list(self):
        """A comment with a blank line in a list item. Intended change: a raw block in a container."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                - a

                    <!--
                    c

                    -->
                    text
                '''
            ),
            self.dedent(
                '''
                <ul>
                <li>
                <p>a</p>
                <!--
                c

                -->
                <p>text</p>
                </li>
                </ul>
                '''
            )
        )

    def test_comment_blank_line_definition(self):
        """A comment with a blank line in a definition. Intended change: a raw block in a container."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                Term
                :   a

                    <!--
                    c

                    -->
                    text
                '''
            ),
            self.dedent(
                '''
                <dl>
                <dt>Term</dt>
                <dd>
                <p>a</p>
                <!--
                c

                -->
                <p>text</p>
                </dd>
                </dl>
                '''
            ),
            extensions=['def_list']
        )

    def test_comment_blank_line_blockquote(self):
        """A comment with a blank line in a blockquote. Intended change: a raw block in a container."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                > <!--
                > c
                >
                > -->
                > text
                '''
            ),
            self.dedent(
                '''
                <blockquote>
                <!--
                c

                -->
                <p>text</p>
                </blockquote>
                '''
            )
        )

    def test_comment_blank_line_blockquote_in_list(self):
        """
        A comment with a blank line in a blockquote in a list item. Intended change: a raw block in a
        container.
        """

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                - a

                    > <!--
                    > c
                    >
                    > -->
                    > text
                '''
            ),
            self.dedent(
                '''
                <ul>
                <li>
                <p>a</p>
                <blockquote>
                <!--
                c

                -->
                <p>text</p>
                </blockquote>
                </li>
                </ul>
                '''
            )
        )

    def test_comment_blank_line_footnote(self):
        """A comment with a blank line in a footnote. Intended change: a raw block in a container."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                x[^1]

                [^1]:
                    <!--
                    c

                    -->
                    text
                '''
            ),
            '<p>x<sup id="fnref:1"><a class="footnote-ref" href="#fn:1">1</a></sup></p>\n'
            '<div class="footnote">\n'
            '<hr />\n'
            '<ol>\n'
            '<li id="fn:1">\n'
            '<!--\n'
            'c\n'
            '\n'
            '-->\n'
            '<p>text&#160;<a class="footnote-backref" href="#fnref:1" title="Jump'
            ' back to footnote 1 in the text">&#8617;</a></p>\n'
            '</li>\n'
            '</ol>\n'
            '</div>',
            extensions=['footnotes']
        )

    def test_comment_many_blank_lines(self):
        """A comment with several blank lines in it. Intended change: a raw block in a container."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                !!! note
                    <!--
                    a

                    b

                    c
                    -->
                    text
                '''
            ),
            self.dedent(
                '''
                <div class="admonition note">
                <p class="admonition-title">Note</p>
                <!--
                a

                b

                c
                -->
                <p>text</p>
                </div>
                '''
            ),
            extensions=['admonition']
        )

    def test_comment_blank_line_then_div(self):
        """A raw block follows a comment with a blank line. Intended change: a raw block in a container."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                !!! note
                    <!--
                    a

                    -->

                    <div>x</div>
                '''
            ),
            self.dedent(
                '''
                <div class="admonition note">
                <p class="admonition-title">Note</p>
                <!--
                a

                -->
                <div>x</div>
                </div>
                '''
            ),
            extensions=['admonition']
        )

    def test_comment_blank_line_two_comments(self):
        """Two comments with blank lines in them. Intended change: a raw block in a container."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                !!! note
                    <!--
                    a

                    -->

                    <!--
                    b

                    -->
                '''
            ),
            self.dedent(
                '''
                <div class="admonition note">
                <p class="admonition-title">Note</p>
                <!--
                a

                -->
                <!--
                b

                -->
                </div>
                '''
            ),
            extensions=['admonition']
        )

    def test_comment_blank_line_after_paragraph(self):
        """A comment with a blank line after a paragraph. Intended change: a raw block in a container."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                !!! note
                    para

                    <!--
                    c

                    -->
                '''
            ),
            self.dedent(
                '''
                <div class="admonition note">
                <p class="admonition-title">Note</p>
                <p>para</p>
                <!--
                c

                -->
                </div>
                '''
            ),
            extensions=['admonition']
        )

    def test_comment_blank_line_div_after_close(self):
        """A raw block starts on the line where the comment ends. Intended change: a raw block in a container."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                !!! note
                    <!--
                    c

                    --> <div>x</div>
                '''
            ),
            self.dedent(
                '''
                <div class="admonition note">
                <p class="admonition-title">Note</p>
                <!--
                c

                -->
                <div>x</div>
                </div>
                '''
            ),
            extensions=['admonition']
        )

    def test_comment_blank_line_md_in_html(self):
        """
        A `markdown` attribute after a comment with a blank line. Intended change: a raw block in a
        container.
        """

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                !!! note
                    <!--
                    c

                    -->
                    <div markdown>
                    **x**
                    </div>
                '''
            ),
            self.dedent(
                '''
                <div class="admonition note">
                <p class="admonition-title">Note</p>
                <!--
                c

                -->
                <div>
                <p><strong>x</strong></p>
                </div>
                </div>
                '''
            ),
            extensions=['admonition', 'md_in_html']
        )

    def test_processing_instruction_blank_line(self):
        """A processing instruction with a blank line in it. Intended change: a raw block in a container."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                !!! note
                    <?php
                    c

                    ?>
                '''
            ),
            self.dedent(
                '''
                <div class="admonition note">
                <p class="admonition-title">Note</p>
                <?php
                c

                ?>
                </div>
                '''
            ),
            extensions=['admonition']
        )

    def test_processing_instruction_blank_line_blockquote(self):
        """
        A processing instruction with a blank line in a blockquote. Intended change: a raw block in a
        container.
        """

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                > <?php
                > c
                >
                > ?>
                '''
            ),
            self.dedent(
                '''
                <blockquote>
                <?php
                c

                ?>
                </blockquote>
                '''
            )
        )

    def test_cdata_blank_line(self):
        """A `CDATA` section with a blank line in it. Intended change: a raw block in a container."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                !!! note
                    <![CDATA[
                    c

                    ]]>
                '''
            ),
            self.dedent(
                '''
                <div class="admonition note">
                <p class="admonition-title">Note</p>
                <![CDATA[
                c

                ]]>
                </div>
                '''
            ),
            extensions=['admonition']
        )

    def test_declaration_blank_line(self):
        """A declaration with a blank line in it. Intended change: a raw block in a container."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                !!! note
                    <!DOCTYPE
                    c

                    html>
                '''
            ),
            self.dedent(
                '''
                <div class="admonition note">
                <p class="admonition-title">Note</p>
                <!DOCTYPE
                c

                html>
                </div>
                '''
            ),
            extensions=['admonition']
        )

    def test_comment_unclosed_admonition(self):
        """A comment which is never closed is text. Regression: renders as it always has."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                !!! note
                    <!--
                    a

                    text
                '''
            ),
            self.dedent(
                '''
                <div class="admonition note">
                <p class="admonition-title">Note</p>
                <p>&lt;!--
                a</p>
                <p>text</p>
                </div>
                '''
            ),
            extensions=['admonition']
        )

    def test_comment_unclosed_list(self):
        """
        What follows a comment which is never closed is parsed as it always has been. Regression: renders as
        it always has.
        """

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                - item

                    <!--
                    a

                    - nested
                    - list

                    para
                '''
            ),
            self.dedent(
                '''
                <ul>
                <li>
                <p>item</p>
                <p>&lt;!--
                a</p>
                <ul>
                <li>nested</li>
                <li>list</li>
                </ul>
                <p>para</p>
                </li>
                </ul>
                '''
            )
        )

    def test_comment_unclosed_list_item(self):
        """
        A comment which is never closed does not change the list around it. Regression: renders as it always
        has.
        """

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                - a
                - b

                    <!-- x

                    more
                - c
                '''
            ),
            self.dedent(
                '''
                <ul>
                <li>a</li>
                <li>
                <p>b</p>
                <p>&lt;!-- x</p>
                <p>more
                - c</p>
                </li>
                </ul>
                '''
            )
        )

    def test_comment_unclosed_blockquote(self):
        """A comment which is never closed in a blockquote is text. Regression: renders as it always has."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                > <!-- x
                >
                > more

                after
                '''
            ),
            self.dedent(
                '''
                <blockquote>
                <p>&lt;!-- x</p>
                <p>more</p>
                </blockquote>
                <p>after</p>
                '''
            )
        )

    def test_comment_unclosed_root(self):
        """A comment which is never closed at the root is text. Regression: renders as it always has."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                <!-- x

                more
                '''
            ),
            self.dedent(
                '''
                <p>&lt;!-- x</p>
                <p>more</p>
                '''
            )
        )

    def test_comment_closed_then_unclosed(self):
        """Only the comment that is closed is raw. Regression: renders as it always has."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                !!! note
                    <!-- a -->

                    <!-- b

                    text
                '''
            ),
            self.dedent(
                '''
                <div class="admonition note">
                <p class="admonition-title">Note</p>
                <!-- a -->
                <p>&lt;!-- b</p>
                <p>text</p>
                </div>
                '''
            ),
            extensions=['admonition']
        )

    def test_comment_in_text_line(self):
        """A comment that does not start a block is text. Regression: renders as it always has."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                !!! note
                    text <!--
                    c

                    --> more
                '''
            ),
            self.dedent(
                '''
                <div class="admonition note">
                <p class="admonition-title">Note</p>
                <p>text &lt;!--
                c</p>
                <p>--&gt; more</p>
                </div>
                '''
            ),
            extensions=['admonition']
        )

    def test_processing_instruction_unclosed(self):
        """A processing instruction which is never closed is text. Regression: renders as it always has."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                !!! note
                    <?php
                    c

                    text
                '''
            ),
            self.dedent(
                '''
                <div class="admonition note">
                <p class="admonition-title">Note</p>
                <p>&lt;?php
                c</p>
                <p>text</p>
                </div>
                '''
            ),
            extensions=['admonition']
        )

    def test_cdata_unclosed(self):
        """A `CDATA` section which is never closed is text. Regression: renders as it always has."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                !!! note
                    <![CDATA[
                    c

                    text
                '''
            ),
            self.dedent(
                '''
                <div class="admonition note">
                <p class="admonition-title">Note</p>
                <p>&lt;![CDATA[
                c</p>
                <p>text</p>
                </div>
                '''
            ),
            extensions=['admonition']
        )

    def test_cdata_spaced_close(self):
        """A `CDATA` section is closed by `]]>` only. Regression: renders as it always has."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                !!! note
                    <![CDATA[
                    c

                    ] ]>
                    after
                '''
            ),
            self.dedent(
                '''
                <div class="admonition note">
                <p class="admonition-title">Note</p>
                <p>&lt;![CDATA[
                c</p>
                <p>] ]&gt;
                after</p>
                </div>
                '''
            ),
            extensions=['admonition']
        )

    def test_declaration_unclosed(self):
        """A declaration which is never closed is text. Regression: renders as it always has."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                !!! note
                    <!DOCTYPE
                    c

                    text
                '''
            ),
            self.dedent(
                '''
                <div class="admonition note">
                <p class="admonition-title">Note</p>
                <p>&lt;!DOCTYPE
                c</p>
                <p>text</p>
                </div>
                '''
            ),
            extensions=['admonition']
        )

    def test_list_lazy_continuation_div(self):
        """Indented div right after a list item line (no blank line). Regression: renders as it always has."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                - item
                    <div>x</div>
                '''
            ),
            self.dedent(
                '''
                <ul>
                <li>item
                    <div>x</div></li>
                </ul>
                '''
            )
        )

    def test_code_block_in_list(self):
        """
        Code block (8 spaces) inside a list item containing HTML with blank lines. Regression: renders as it
        always has.
        """

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                - item

                        <div>

                        code
                        </div>
                '''
            ),
            self.dedent(
                '''
                <ul>
                <li>item<pre><code>&lt;div&gt;

                code
                &lt;/div&gt;
                </code></pre>
                </li>
                </ul>
                '''
            )
        )

    def test_code_block_in_admonition(self):
        """Code block (8 spaces) inside an admonition containing HTML. Regression: renders as it always has."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                !!! note "Title"
                        <div>
                        code
                        </div>
                '''
            ),
            self.dedent(
                '''
                <div class="admonition note">
                <p class="admonition-title">Title</p>
                <pre><code>&lt;div&gt;
                code
                &lt;/div&gt;
                </code></pre>
                </div>
                '''
            ),
            extensions=['admonition']
        )

    def test_trailing_text_after_close(self):
        """
        Text on the same line after the closing tag. Text after a block starts its own paragraph (as at the
        root). Intended change: a raw block in a container.
        """

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                !!! note "Title"
                    <div>x</div> trailing

                    after
                '''
            ),
            self.dedent(
                '''
                <div class="admonition note">
                <p class="admonition-title">Title</p>
                <div>x</div>
                <p>trailing</p>
                <p>after</p>
                </div>
                '''
            ),
            extensions=['admonition']
        )

    def test_trailing_text_multiline_block(self):
        """
        Multi-line block followed by text on the closing line, then a lazy continuation line. Intended
        change: a raw block in a container.
        """

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                !!! note "Title"
                    <div>
                    **x**
                    </div> trailing
                    more

                    after
                '''
            ),
            self.dedent(
                '''
                <div class="admonition note">
                <p class="admonition-title">Title</p>
                <div>
                **x**
                </div>
                <p>trailing
                more</p>
                <p>after</p>
                </div>
                '''
            ),
            extensions=['admonition']
        )

    def test_trailing_text_chained_blocks(self):
        """
        A second block starts on the closing line of the first, followed by text. Intended change: a raw
        block in a container.
        """

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                !!! note "Title"
                    <div>a</div><div>b</div> trailing

                    after
                '''
            ),
            self.dedent(
                '''
                <div class="admonition note">
                <p class="admonition-title">Title</p>
                <div>a</div>
                <div>b</div>
                <p>trailing</p>
                <p>after</p>
                </div>
                '''
            ),
            extensions=['admonition']
        )

    def test_trailing_text_after_comment(self):
        """
        Text after an indented comment on the same line (empty-tag path). Intended change: a raw block in a
        container.
        """

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                !!! note "Title"
                    <!-- c --> trailing

                    after
                '''
            ),
            self.dedent(
                '''
                <div class="admonition note">
                <p class="admonition-title">Title</p>
                <!-- c -->
                <p>trailing</p>
                <p>after</p>
                </div>
                '''
            ),
            extensions=['admonition']
        )

    def test_trailing_text_in_list(self):
        """Text after the closing tag inside a list item. Intended change: a raw block in a container."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                - item

                    <div>x</div> trailing

                    after
                '''
            ),
            self.dedent(
                '''
                <ul>
                <li>
                <p>item</p>
                <div>x</div>
                <p>trailing</p>
                <p>after</p>
                </li>
                </ul>
                '''
            )
        )

    def test_trailing_text_in_code_block(self):
        """
        Indented CODE with HTML followed by text on the same line must stay one code line. Regression:
        renders as it always has.
        """

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                text

                    <div>x</div> trailing
                    more code
                '''
            ),
            self.dedent(
                '''
                <p>text</p>
                <pre><code>&lt;div&gt;x&lt;/div&gt; trailing
                more code
                </code></pre>
                '''
            )
        )

    def test_trailing_text_in_code_block_in_admonition(self):
        """Same inside an admonition (8 spaces). Regression: renders as it always has."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                !!! note "Title"
                        <p>x</p> trailing
                        more code
                '''
            ),
            self.dedent(
                '''
                <div class="admonition note">
                <p class="admonition-title">Title</p>
                <pre><code>&lt;p&gt;x&lt;/p&gt; trailing
                more code
                </code></pre>
                </div>
                '''
            ),
            extensions=['admonition']
        )

    def test_trailing_text_nested_admonition(self):
        """Two container levels. Intended change: a raw block in a container."""

        self.assertMarkdownRenders(
            self.dedent(
                R'''
                !!! note "Outer"
                    !!! note "Inner"
                        <div>x</div> trailing

                        after
                '''
            ),
            self.dedent(
                '''
                <div class="admonition note">
                <p class="admonition-title">Outer</p>
                <div class="admonition note">
                <p class="admonition-title">Inner</p>
                <div>x</div>
                <p>trailing</p>
                <p>after</p>
                </div>
                </div>
                '''
            ),
            extensions=['admonition']
        )
