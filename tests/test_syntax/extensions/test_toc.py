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

Copyright 2007-2019 The Python Markdown Project (v. 1.7 and later)
Copyright 2004, 2005, 2006 Yuri Takhteyev (v. 0.2-1.6b)
Copyright 2004 Manfred Stienstra (the original version)

License: BSD (see LICENSE.md for details).
"""

from markdown.test_tools import TestCase
from markdown.extensions.toc import TocExtension


class TestTOC(TestCase):
    maxDiff = None

    # TODO: Move the rest of the TOC tests here.

    def testAnchorLink(self):
        self.assertMarkdownRenders(
            self.dedent(
                '''
                # Header 1

                ## Header *2*
                '''
            ),
            self.dedent(
                '''
                <h1 id="header-1"><a class="toclink" href="#header-1">Header 1</a></h1>
                <h2 id="header-2"><a class="toclink" href="#header-2">Header <em>2</em></a></h2>
                '''
            ),
            extensions=[TocExtension(anchorlink=True)]
        )

    def testAnchorLinkWithSingleInlineCode(self):
        self.assertMarkdownRenders(
            '# This is `code`.',
            '<h1 id="this-is-code">'                        # noqa
                '<a class="toclink" href="#this-is-code">'  # noqa
                    'This is <code>code</code>.'            # noqa
                '</a>'                                      # noqa
            '</h1>',                                        # noqa
            extensions=[TocExtension(anchorlink=True)]
        )

    def testAnchorLinkWithDoubleInlineCode(self):
        self.assertMarkdownRenders(
            '# This is `code` and `this` too.',
            '<h1 id="this-is-code-and-this-too">'                           # noqa
                '<a class="toclink" href="#this-is-code-and-this-too">'     # noqa
                    'This is <code>code</code> and <code>this</code> too.'  # noqa
                '</a>'                                                      # noqa
            '</h1>',                                                        # noqa
            extensions=[TocExtension(anchorlink=True)]
        )

    def testPermalink(self):
        self.assertMarkdownRenders(
            '# Header',
            '<h1 id="header">'                                                            # noqa
                'Header'                                                                  # noqa
                '<a class="headerlink" href="#header" title="Permanent link">&para;</a>'  # noqa
            '</h1>',                                                                      # noqa
            extensions=[TocExtension(permalink=True)]
        )

    def testPermalinkWithSingleInlineCode(self):
        self.assertMarkdownRenders(
            '# This is `code`.',
            '<h1 id="this-is-code">'                                                            # noqa
                'This is <code>code</code>.'                                                    # noqa
                '<a class="headerlink" href="#this-is-code" title="Permanent link">&para;</a>'  # noqa
            '</h1>',                                                                            # noqa
            extensions=[TocExtension(permalink=True)]
        )

    def testPermalinkWithDoubleInlineCode(self):
        self.assertMarkdownRenders(
            '# This is `code` and `this` too.',
            '<h1 id="this-is-code-and-this-too">'                                                            # noqa
                'This is <code>code</code> and <code>this</code> too.'                                       # noqa
                '<a class="headerlink" href="#this-is-code-and-this-too" title="Permanent link">&para;</a>'  # noqa
            '</h1>',                                                                                         # noqa
            extensions=[TocExtension(permalink=True)]
        )

    def testMinMaxLevel(self):
        self.assertMarkdownRenders(
            self.dedent(
                '''
                # Header 1 not in TOC

                ## Header 2 not in TOC

                ### Header 3

                #### Header 4

                ##### Header 5 not in TOC
                '''
            ),
            self.dedent(
                '''
                <h1 id="header-1-not-in-toc">Header 1 not in TOC</h1>
                <h2 id="header-2-not-in-toc">Header 2 not in TOC</h2>
                <h3 id="header-3">Header 3</h3>
                <h4 id="header-4">Header 4</h4>
                <h5 id="header-5-not-in-toc">Header 5 not in TOC</h5>
                '''
            ),
            expected_attrs={
                'toc': (
                    '<div class="toc">\n'
                      '<ul>\n'                                                          # noqa
                        '<li class="toc3"><a href="#header-3">Header 3</a>'             # noqa
                          '<ul>\n'                                                      # noqa
                            '<li class="toc4"><a href="#header-4">Header 4</a></li>\n'  # noqa
                          '</ul>\n'                                                     # noqa
                        '</li>\n'                                                       # noqa
                      '</ul>\n'                                                         # noqa
                    '</div>\n'                                                          # noqa
                ),
                'toc_tokens': [
                    {
                        'level': 3,
                        'id': 'header-3',
                        'name': 'Header 3',
                        'children': [
                            {
                                'level': 4,
                                'id': 'header-4',
                                'name': 'Header 4',
                                'children': []
                            }
                        ]
                    }
                ]
            },
            extensions=[TocExtension(toc_depth='3-4')]
        )

    def testMaxLevel(self):
        self.assertMarkdownRenders(
            self.dedent(
                '''
                # Header 1

                ## Header 2

                ### Header 3 not in TOC
                '''
            ),
            self.dedent(
                '''
                <h1 id="header-1">Header 1</h1>
                <h2 id="header-2">Header 2</h2>
                <h3 id="header-3-not-in-toc">Header 3 not in TOC</h3>
                '''
            ),
            expected_attrs={
                'toc': (
                    '<div class="toc">\n'
                      '<ul>\n'                                                          # noqa
                        '<li class="toc1"><a href="#header-1">Header 1</a>'             # noqa
                          '<ul>\n'                                                      # noqa
                            '<li class="toc2"><a href="#header-2">Header 2</a></li>\n'  # noqa
                          '</ul>\n'                                                     # noqa
                        '</li>\n'                                                       # noqa
                      '</ul>\n'                                                         # noqa
                    '</div>\n'                                                          # noqa
                ),
                'toc_tokens': [
                    {
                        'level': 1,
                        'id': 'header-1',
                        'name': 'Header 1',
                        'children': [
                            {
                                'level': 2,
                                'id': 'header-2',
                                'name': 'Header 2',
                                'children': []
                            }
                        ]
                    }
                ]
            },
            extensions=[TocExtension(toc_depth=2)]
        )

    def testMinMaxLevelwithAnchorLink(self):
        self.assertMarkdownRenders(
            self.dedent(
                '''
                # Header 1 not in TOC

                ## Header 2 not in TOC

                ### Header 3

                #### Header 4

                ##### Header 5 not in TOC
                '''
            ),
            '<h1 id="header-1-not-in-toc">'                                                      # noqa
                '<a class="toclink" href="#header-1-not-in-toc">Header 1 not in TOC</a></h1>\n'  # noqa
            '<h2 id="header-2-not-in-toc">'                                                      # noqa
                '<a class="toclink" href="#header-2-not-in-toc">Header 2 not in TOC</a></h2>\n'  # noqa
            '<h3 id="header-3">'                                                                 # noqa
                '<a class="toclink" href="#header-3">Header 3</a></h3>\n'                        # noqa
            '<h4 id="header-4">'                                                                 # noqa
                '<a class="toclink" href="#header-4">Header 4</a></h4>\n'                        # noqa
            '<h5 id="header-5-not-in-toc">'                                                      # noqa
                '<a class="toclink" href="#header-5-not-in-toc">Header 5 not in TOC</a></h5>',   # noqa
            expected_attrs={
                'toc': (
                    '<div class="toc">\n'
                      '<ul>\n'                                                          # noqa
                        '<li class="toc3"><a href="#header-3">Header 3</a>'             # noqa
                          '<ul>\n'                                                      # noqa
                            '<li class="toc4"><a href="#header-4">Header 4</a></li>\n'  # noqa
                          '</ul>\n'                                                     # noqa
                        '</li>\n'                                                       # noqa
                      '</ul>\n'                                                         # noqa
                    '</div>\n'                                                          # noqa
                ),
                'toc_tokens': [
                    {
                        'level': 3,
                        'id': 'header-3',
                        'name': 'Header 3',
                        'children': [
                            {
                                'level': 4,
                                'id': 'header-4',
                                'name': 'Header 4',
                                'children': []
                            }
                        ]
                    }
                ]
            },
            extensions=[TocExtension(toc_depth='3-4', anchorlink=True)]
        )

    def testMinMaxLevelwithPermalink(self):
        self.assertMarkdownRenders(
            self.dedent(
                '''
                # Header 1 not in TOC

                ## Header 2 not in TOC

                ### Header 3

                #### Header 4

                ##### Header 5 not in TOC
                '''
            ),
            '<h1 id="header-1-not-in-toc">Header 1 not in TOC'                                                # noqa
                '<a class="headerlink" href="#header-1-not-in-toc" title="Permanent link">&para;</a></h1>\n'  # noqa
            '<h2 id="header-2-not-in-toc">Header 2 not in TOC'                                                # noqa
                '<a class="headerlink" href="#header-2-not-in-toc" title="Permanent link">&para;</a></h2>\n'  # noqa
            '<h3 id="header-3">Header 3'                                                                      # noqa
                '<a class="headerlink" href="#header-3" title="Permanent link">&para;</a></h3>\n'             # noqa
            '<h4 id="header-4">Header 4'                                                                      # noqa
                '<a class="headerlink" href="#header-4" title="Permanent link">&para;</a></h4>\n'             # noqa
            '<h5 id="header-5-not-in-toc">Header 5 not in TOC'                                                # noqa
                '<a class="headerlink" href="#header-5-not-in-toc" title="Permanent link">&para;</a></h5>',   # noqa
            expected_attrs={
                'toc': (
                    '<div class="toc">\n'
                      '<ul>\n'                                                          # noqa
                        '<li class="toc3"><a href="#header-3">Header 3</a>'             # noqa
                          '<ul>\n'                                                      # noqa
                            '<li class="toc4"><a href="#header-4">Header 4</a></li>\n'  # noqa
                          '</ul>\n'                                                     # noqa
                        '</li>\n'                                                       # noqa
                      '</ul>\n'                                                         # noqa
                    '</div>\n'                                                          # noqa
                ),
                'toc_tokens': [
                    {
                        'level': 3,
                        'id': 'header-3',
                        'name': 'Header 3',
                        'children': [
                            {
                                'level': 4,
                                'id': 'header-4',
                                'name': 'Header 4',
                                'children': []
                            }
                        ]
                    }
                ]
            },
            extensions=[TocExtension(toc_depth='3-4', permalink=True)]
        )

    def testMinMaxLevelwithBaseLevel(self):
        self.assertMarkdownRenders(
            self.dedent(
                '''
                # First Header

                ## Second Level

                ### Third Level

                #### Forth Level
                '''
            ),
            self.dedent(
                '''
                <h3 id="first-header">First Header</h3>
                <h4 id="second-level">Second Level</h4>
                <h5 id="third-level">Third Level</h5>
                <h6 id="forth-level">Forth Level</h6>
                '''
            ),
            expected_attrs={
                'toc': (
                    '<div class="toc">\n'
                      '<ul>\n'                                                                  # noqa
                        '<li class="toc4"><a href="#second-level">Second Level</a>'             # noqa
                          '<ul>\n'                                                              # noqa
                            '<li class="toc5"><a href="#third-level">Third Level</a></li>\n'    # noqa
                          '</ul>\n'                                                             # noqa
                        '</li>\n'                                                               # noqa
                      '</ul>\n'                                                                 # noqa
                    '</div>\n'                                                                  # noqa
                ),
                'toc_tokens': [
                    {
                        'level': 4,
                        'id': 'second-level',
                        'name': 'Second Level',
                        'children': [
                            {
                                'level': 5,
                                'id': 'third-level',
                                'name': 'Third Level',
                                'children': []
                            }
                        ]
                    }
                ]
            },
            extensions=[TocExtension(toc_depth='4-5', baselevel=3)]
        )

    def testMaxLevelwithBaseLevel(self):
        self.assertMarkdownRenders(
            self.dedent(
                '''
                # Some Header

                ## Next Level

                ### Too High
                '''
            ),
            self.dedent(
                '''
                <h2 id="some-header">Some Header</h2>
                <h3 id="next-level">Next Level</h3>
                <h4 id="too-high">Too High</h4>
                '''
            ),
            expected_attrs={
                'toc': (
                    '<div class="toc">\n'
                      '<ul>\n'                                                              # noqa
                        '<li class="toc2"><a href="#some-header">Some Header</a>'           # noqa
                          '<ul>\n'                                                          # noqa
                            '<li class="toc3"><a href="#next-level">Next Level</a></li>\n'  # noqa
                          '</ul>\n'                                                         # noqa
                        '</li>\n'                                                           # noqa
                      '</ul>\n'                                                             # noqa
                    '</div>\n'                                                              # noqa
                ),
                'toc_tokens': [
                    {
                        'level': 2,
                        'id': 'some-header',
                        'name': 'Some Header',
                        'children': [
                            {
                                'level': 3,
                                'id': 'next-level',
                                'name': 'Next Level',
                                'children': []
                            }
                        ]
                    }
                ]
            },
            extensions=[TocExtension(toc_depth=3, baselevel=2)]
        )

    def test_escaped_code(self):
        self.assertMarkdownRenders(
            self.dedent(
                '''
                [TOC]

                # `<test>`
                '''
            ),
            self.dedent(
                '''
                <div class="toc">
                <ul>
                <li class="toc1"><a href="#test">&lt;test&gt;</a></li>
                </ul>
                </div>
                <h1 id="test"><code>&lt;test&gt;</code></h1>
                '''
            ),
            extensions=['toc']
        )

    def test_escaped_char_in_id(self):
        self.assertMarkdownRenders(
            r'# escaped\_character',
            '<h1 id="escaped_character">escaped_character</h1>',
            extensions=['toc']
        )

    def testAnchorLinkWithCustomClass(self):
        self.assertMarkdownRenders(
            self.dedent(
                '''
                # Header 1

                ## Header *2*
                '''
            ),
            self.dedent(
                '''
                <h1 id="header-1"><a class="custom" href="#header-1">Header 1</a></h1>
                <h2 id="header-2"><a class="custom" href="#header-2">Header <em>2</em></a></h2>
                '''
            ),
            extensions=[TocExtension(anchorlink=True, anchorlink_class="custom")]
        )

    def testAnchorLinkWithCustomClasses(self):
        self.assertMarkdownRenders(
            self.dedent(
                '''
                # Header 1

                ## Header *2*
                '''
            ),
            self.dedent(
                '''
                <h1 id="header-1"><a class="custom1 custom2" href="#header-1">Header 1</a></h1>
                <h2 id="header-2"><a class="custom1 custom2" href="#header-2">Header <em>2</em></a></h2>
                '''
            ),
            extensions=[TocExtension(anchorlink=True, anchorlink_class="custom1 custom2")]
        )

    def testPermalinkWithEmptyText(self):
        self.assertMarkdownRenders(
            '# Header',
            '<h1 id="header">'                                                      # noqa
                'Header'                                                            # noqa
                '<a class="headerlink" href="#header" title="Permanent link"></a>'  # noqa
            '</h1>',                                                                # noqa
            extensions=[TocExtension(permalink="")]
        )

    def testPermalinkWithCustomClass(self):
        self.assertMarkdownRenders(
            '# Header',
            '<h1 id="header">'                                                        # noqa
                'Header'                                                              # noqa
                '<a class="custom" href="#header" title="Permanent link">&para;</a>'  # noqa
            '</h1>',                                                                  # noqa
            extensions=[TocExtension(permalink=True, permalink_class="custom")]
        )

    def testPermalinkWithCustomClasses(self):
        self.assertMarkdownRenders(
            '# Header',
            '<h1 id="header">'                                                                 # noqa
                'Header'                                                                       # noqa
                '<a class="custom1 custom2" href="#header" title="Permanent link">&para;</a>'  # noqa
            '</h1>',                                                                           # noqa
            extensions=[TocExtension(permalink=True, permalink_class="custom1 custom2")]
        )

    def testPermalinkWithCustomTitle(self):
        self.assertMarkdownRenders(
            '# Header',
            '<h1 id="header">'                                                    # noqa
                'Header'                                                          # noqa
                '<a class="headerlink" href="#header" title="custom">&para;</a>'  # noqa
            '</h1>',                                                              # noqa
            extensions=[TocExtension(permalink=True, permalink_title="custom")]
        )

    def testPermalinkWithEmptyTitle(self):
        self.assertMarkdownRenders(
            '# Header',
            '<h1 id="header">'                                                    # noqa
                'Header'                                                          # noqa
                '<a class="headerlink" href="#header">&para;</a>'                 # noqa
            '</h1>',                                                              # noqa
            extensions=[TocExtension(permalink=True, permalink_title="")]
        )

    def testPermalinkWithUnicodeInID(self):
        from markdown.extensions.toc import slugify_unicode
        self.assertMarkdownRenders(
            '# Unicode ヘッダー',
            '<h1 id="unicode-ヘッダー">'                                                            # noqa
                'Unicode ヘッダー'                                                                  # noqa
                '<a class="headerlink" href="#unicode-ヘッダー" title="Permanent link">&para;</a>'  # noqa
            '</h1>',                                                                               # noqa
            extensions=[TocExtension(permalink=True, slugify=slugify_unicode)]
        )

    def testPermalinkWithUnicodeTitle(self):
        from markdown.extensions.toc import slugify_unicode
        self.assertMarkdownRenders(
            '# Unicode ヘッダー',
            '<h1 id="unicode-ヘッダー">'                                                        # noqa
                'Unicode ヘッダー'                                                              # noqa
                '<a class="headerlink" href="#unicode-ヘッダー" title="パーマリンク">&para;</a>'  # noqa
            '</h1>',                                                                           # noqa
            extensions=[TocExtension(permalink=True, permalink_title="パーマリンク", slugify=slugify_unicode)]
        )

    def testPermalinkWithExtendedLatinInID(self):
        self.assertMarkdownRenders(
            '# Théâtre',
            '<h1 id="theatre">'                                                            # noqa
                'Théâtre'                                                                  # noqa
                '<a class="headerlink" href="#theatre" title="Permanent link">&para;</a>'  # noqa
            '</h1>',                                                                       # noqa
            extensions=[TocExtension(permalink=True)]
        )
