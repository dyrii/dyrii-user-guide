import sys, os
from sphinx.highlighting import lexers
from pygments.lexers.web import PhpLexer


lexers['php'] = PhpLexer(startinline=True, linenos=1)
lexers['php-annotations'] = PhpLexer(startinline=True, linenos=1)
primary_domain = 'php'

extensions = []
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = u'Dyrii User Manual'
copyright = u'2018, Dyrii LLC.'
version = '6'
html_title = "Dyrii User Manual"
html_short_title = "Dyrii"

exclude_patterns = ['_build']
html_static_path = ['_images']

##### Guzzle sphinx theme

#import guzzle_sphinx_theme
#html_translator_class = 'guzzle_sphinx_theme.HTMLTranslator'
#html_theme_path = guzzle_sphinx_theme.html_theme_path()
#html_theme = 'guzzle_sphinx_theme'

# Custom sidebar templates, maps document names to template names.
html_sidebars = {
    '**': ['logo-text.html', 'globaltoc.html', 'searchbox.html']
}

# Register the theme as an extension to generate a sitemap.xml
#extensions.append("guzzle_sphinx_theme")

# Guzzle theme options (see theme.conf for more information)
html_theme_options = {

    # Set the path to a special layout to include for the homepage
    # "index_template": "homepage.html",

    # Allow a separate homepage from the master_doc
    # homepage = index

    # Set the name of the project to appear in the nav menu
    # "project_nav_name": "Guzzle",

    # Set your Disqus short name to enable comments
    # "disqus_comments_shortname": "my_disqus_comments_short_name",

    # Set you GA account ID to enable tracking
    # "google_analytics_account": "my_ga_account",

    # Path to a touch icon
    # "touch_icon": "",

    # Specify a base_url used to generate sitemap.xml links. If not
    # specified, then no sitemap will be built.
    "base_url": "https://dyrii.com"

    # Allow the "Table of Contents" page to be defined separately from "master_doc"
    # tocpage = Contents

    # Allow the project link to be overriden to a custom URL.
    # projectlink = http://myproject.url
   
}



# -- Options for Epub output ---------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = u'Dyrii User Manual'
epub_author = u'dyrii.com'
epub_publisher = u'Dyrii LLC'
epub_copyright = copyright

# The language of the text. It defaults to the language option
# or en if the language is not set.
#epub_language = ''

# The scheme of the identifier. Typical schemes are ISBN or URL.
#epub_scheme = ''

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#epub_identifier = ''

# A unique identification for the text.
#epub_uid = ''

# A tuple containing the cover image and cover page html template filenames.
#epub_cover = ()

# HTML files that should be inserted before the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_pre_files = []

# HTML files shat should be inserted after the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_post_files = []

# A list of files that should not be packed into the epub file.
#epub_exclude_files = []

# The depth of the table of contents in toc.ncx.
#epub_tocdepth = 3

# Allow duplicate toc entries.
#epub_tocdup = True

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', 'Dyrii User Manual', u'Dyrii User Manual',
   u'dyrii.com', 'Dyrii LLC', 'One line description of project.',
   'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'Dyrii User Manual', u'Dyrii User Manual',
     [u'dyrii.com'], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
'preamble': r'''
        %%%%%%%%%%%%%%%%%%%% Meher %%%%%%%%%%%%%%%%%%
        %%%add number to subsubsection 2=subsection, 3=subsubsection
        %%% below subsubsection is not good idea.
        \setcounter{secnumdepth}{3}
        %
        %%%% Table of content upto 2=subsection, 3=subsubsection
        \setcounter{tocdepth}{2}

        \usepackage{amsmath,amsfonts,amssymb,amsthm}
        \usepackage{graphicx}

        %%% reduce spaces for Table of contents, figures and tables
        %%% it is used "\addtocontents{toc}{\vskip -1.2cm}" etc. in the document
        \usepackage[notlot,nottoc,notlof]{}

        \usepackage{color}
        \usepackage{transparent}
        \usepackage{eso-pic}
        \usepackage{lipsum}

        \usepackage{footnotebackref} %%link at the footnote to go to the place of footnote in the text

        %% spacing between line
        \usepackage{setspace}
        %%%%\onehalfspacing
        %%%%\doublespacing
        \singlespacing


        %%%%%%%%%%% datetime
        \usepackage{datetime}

        \newdateformat{MonthYearFormat}{%
            \monthname[\THEMONTH], \THEYEAR}


        %% RO, LE will not work for 'oneside' layout.
        %% Change oneside to twoside in document class
        \usepackage{fancyhdr}
        \pagestyle{fancy}
        \fancyhf{}

        %%% Alternating Header for oneside
        \fancyhead[L]{\ifthenelse{\isodd{\value{page}}}{ \small \nouppercase{\leftmark} }{}}
        \fancyhead[R]{\ifthenelse{\isodd{\value{page}}}{}{ \small \nouppercase{\rightmark} }}

        %%% Alternating Header for two side
        %\fancyhead[RO]{\small \nouppercase{\rightmark}}
        %\fancyhead[LE]{\small \nouppercase{\leftmark}}

        %% for oneside: change footer at right side. If you want to use Left and right then use same as header defined above.
        \fancyfoot[R]{\ifthenelse{\isodd{\value{page}}}{{\tiny Meher Krishna Patel} }{\href{http://pythondsp.readthedocs.io/en/latest/pythondsp/toc.html}{\tiny PythonDSP}}}

        %%% Alternating Footer for two side
        %\fancyfoot[RO, RE]{\scriptsize Meher Krishna Patel (mekrip@gmail.com)}

        %%% page number
        \fancyfoot[CO, CE]{\thepage}

        \renewcommand{\headrulewidth}{0.5pt}
        \renewcommand{\footrulewidth}{0.5pt}

        \RequirePackage{tocbibind} %%% comment this to remove page number for following
        \addto\captionsenglish{\renewcommand{\contentsname}{Table of contents}}
        \addto\captionsenglish{\renewcommand{\listfigurename}{List of figures}}
        \addto\captionsenglish{\renewcommand{\listtablename}{List of tables}}
        \addto\captionsenglish{\renewcommand{\listtablename}{List of tables}} %%% Heading for TOC


        %%reduce spacing for itemize
        \usepackage{enumitem}
        \setlist{nosep}

        %%%%%%%%%%% Quote Styles at the top of chapter
        \usepackage{epigraph}
        \setlength{\epigraphwidth}{0.8\columnwidth}
        \newcommand{\chapterquote}[2]{\epigraphhead[60]{\epigraph{\textit{#1}}{\textbf {\textit{--#2}}}}}
        %%%%%%%%%%% Quote for all places except Chapter
        \newcommand{\sectionquote}[2]{{\quote{\textit{``#1''}}{\textbf {\textit{--#2}}}}}
    ''',


    'maketitle': r'''
        \pagenumbering{Roman} %%% to avoid page 1 conflict with actual page 1

        \begin{titlepage}
            \centering

            \vspace*{40mm} %%% * is used to give space from top
            \textbf{\Huge {Dyrii User Manual}}

            \vspace{0mm}
            \begin{figure}[!h]
                \centering
                \includegraphics[scale=0.3]{Dyrii_logo_theme_color.png}
            \end{figure}

            \vspace{0mm}
            \Large \textbf{{Published by Dyrii LLC.}}

            \small Created on : March, 2018

            \vspace*{0mm}
            \small  Last updated : June, 2018


            %% \vfill adds at the bottom
            \vfill
            \small \textit{More information available at }{\href{http://dyrii.com}{Dyrii.com}}
        \end{titlepage}

        \clearpage
        \pagenumbering{roman}
        \tableofcontents
        % \listoffigures
        % \listoftables
        \clearpage
        \pagenumbering{arabic}

        ''',
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
    'sphinxsetup': \
        'hmargin={0.7in,0.7in}, vmargin={1in,1in}, \
        verbatimwithframe=true, \
        TitleColor={rgb}{0,0,0}, \
        HeaderFamily=\\rmfamily\\bfseries, \
        InnerLinkColor={rgb}{0,0,1}, \
        OuterLinkColor={rgb}{0,0,1}',

        'tableofcontents':' ',
}


# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  ('index', 'dyrii.tex', u'Dyrii User Manual',
   u'Published by dyrii.com', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None
latex_logo = '_images/Dyrii_logo_theme_color.png'

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True
