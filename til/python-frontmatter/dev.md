---
canonical_url: https://waylonwalker.com/til/python-frontmatter/
cover_image: https://images.waylonwalker.com/til/python-frontmatter.png
description: I use a package It Frontmatter is a handy way to add metadata to your
  plain text files.  It Here is the exact frontmatter for this post you are reading
  on my si
published: true
tags:
- python
title: How I load Markdown in Python
---

I use a package [eyeseast/python-frontmatter](https://github.com/eyeseast/python-frontmatter) to load files with frontmatter in them.  Its a handy package that allows you to load files with structured frontmatter (yaml, json, or toml).

## Install

It's on pypi, so you can install it into your virtual environment with pip.

```bash
python -m pip install python-frontmatter
```

## 🙋 What's Frontmatter

Frontmatter is a handy way to add metadata to your plain text files.  It's quite common to have yaml frontmatter in markdown.  All of my blog posts have yaml frontmatter to give the post metadata such as post date, tags, title, and template.  dev.to is a popular developer blogging platform that also builds all of its posts with markdown and yaml frontmatter.

## Let's see an example

Here is the exact frontmatter for this post you are reading on my site.

```markdown
---
date: 2022-03-24 03:18:48.631729 templateKey: til title: How I load Markdown in Python tags:
  - linux
  - python

---

This is where the markdown content for the post goes.
```

## So it's yaml

yaml is the most commmon, but [python-frontmatter](https://pypi.org/project/python-frontmatter/) also supports [Handlers](https://python-frontmatter.readthedocs.io/en/latest/handlers.html?highlight=toml#module-frontmatter.default_handlers) for toml and json.

If you want a good set of examples of yaml [learnxinyminutes](https://learnxinyminutes.com/docs/yaml/) has a fantastic set of examples in one page.

## How to load yaml frontmatter in python

Here is how I would load this post into python using [python-frontmatter](https://pypi.org/project/python-frontmatter/).

```python
import frontmatter inspect(frontmatter.load("pages/til/python-frontmatter.md"))
```

We can use [rich](https://github.com/Textualize/rich) to inspect the Post object to see what all it contains.

```python
❯ inspect(frontmatter.load("pages/til/python-frontmatter.md"))
╭────────────────────────────────────────────────────────── <class 'frontmatter.Post'> ───────────────────────────────────────────────────────────╮
│ A post contains content and metadata from Front Matter. This is what gets                                                                       │
│ returned by :py:func:`load <frontmatter.load>` and :py:func:`loads <frontmatter.loads>`.                                                        │
│ Passing this to :py:func:`dump <frontmatter.dump>` or :py:func:`dumps <frontmatter.dumps>`                                                      │
│ will turn it back into text.                                                                                                                    │
│                                                                                                                                                 │
│ ╭─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮ │
│ │ <frontmatter.Post object at 0x7f03c4c23ca0>                                                                                                 │ │
│ ╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯ │
│                                                                                                                                                 │
│  content = "I use a package\n[eyeseast/python-frontmatter](https://github.com/eyeseast/python-frontmatter)\nto load files with frontmatter in   │
│            them.  Its a handy package that allows you to\nload files with structured frontmatter (yaml, json, or toml).\n\n## Install\n\nIt's   │
│            on pypi, so you can install it into your virtual environment with pip.\n\n```bash\npython -m pip install                             │
│            python-frontmatter\n```\n\n## 🙋 What's Frontmatter\n\nFrontmatter is a handy way to add metadata to your plain text files.          │
│            It's\nquite common to have yaml frontmatter in markdown.  All of my blog posts have\nyaml frontmatter to give the post metadata such │
│            as post date, tags, title, and\ntemplate.  dev.to is a popular developer blogging platform that also builds all\nof its posts with   │
│            markdown and yaml frontmatter.\n\n## Let's see an example\n\nHere is the exact frontmatter for this post you are reading on my       │
│            site.\n\n```markdown\n---\ndate: 2022-03-24 03:18:48.631729\ntemplateKey: til\ntitle: How I load Markdown in Python\ntags:\n  -      │
│            linux\n  - python\n\n---\n\nThis is where the markdown content for the post goes.\n```\n\n## So it's yaml\n\nyaml is the most        │
│            commmon, but\n[eyeseast/python-frontmatter](https://github.com/eyeseast/python-frontmatter)\nalso                                    │
│            supports\n[Handlers](https://python-frontmatter.readthedocs.io/en/latest/handlers.html?highlight=toml#module-frontmatter.default_ha… │
│            toml and json.\n\nIf you want a good set of examples of yaml\n[learnxinyminutes](https://learnxinyminutes.com/docs/yaml/) has a      │
│            fantastic set\nof examples in one page.\n\n## How to load yaml frontmatter in python"                                                │
│  handler = <frontmatter.default_handlers.YAMLHandler object at 0x7f03bffbd910>                                                                  │
│ metadata = {                                                                                                                                    │
│                'date': datetime.datetime(2022, 3, 24, 3, 18, 48, 631729),                                                                       │
│                'templateKey': 'til',                                                                                                            │
│                'title': 'How I load Markdown in Python',                                                                                        │
│                'tags': ['linux', 'python', 'python']                                                                                            │
│            }                                                                                                                                    │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

## Getting Metadata

You can get items from the posts metadata just as you would from a dict.

```python
post = frontmatter.load("pages/til/python-frontmatter.md") post['date']
# datetime.datetime(2022, 3, 24, 3, 18, 48, 631729)

post.get('date')
# datetime.datetime(2022, 3, 24, 3, 18, 48, 631729)
```


  <div class="onelinelink-wrapper">
      <a class="onelinelink" href="https://waylonwalker.com/til/python-dict-get/">
          <img style="float: right;" align='right' src="https://images.waylonwalker.com/til/python-dict-get-og_250x140.png" alt="article cover for 
 python dict get
"/>
          <p><strong>
 python dict get
</strong></p>
      </a>
  </div>


> I have recently become fond of the `.get` method to give it an easy default value.

## Content is content

The content of the document is stored under `.content`

```python
post.content
```

## Links

* [python dict get](https://waylonwalker.com/til/python-dict-get/)
* [eyeseast/python-frontmatter](https://github.com/eyeseast/python-frontmatter)
* [python-frontmatter](https://pypi.org/project/python-frontmatter/)
* [python-frontmatter Handlers](https://python-frontmatter.readthedocs.io/en/latest/handlers.html?highlight=toml#module-frontmatter.default_handlers)
* [learnxinyminutes](https://learnxinyminutes.com/docs/yaml/)
* [python-frontmatter](https://pypi.org/project/python-frontmatter/)
* [rich](https://github.com/Textualize/rich)
<div class='prevnext'>

    <style type='text/css'>

    :root {
      --prevnext-color-text: #eefbfe;
      --prevnext-color-angle: #ff66c4;
      --prevnext-subtitle-brightness: 3;
    }
    [data-theme="light"] {
      --prevnext-color-text: #1f2022;
      --prevnext-color-angle: #ffeb00;
      --prevnext-subtitle-brightness: 3;
    }
    [data-theme="dark"] {
      --prevnext-color-text: #eefbfe;
      --prevnext-color-angle: #ff66c4;
      --prevnext-subtitle-brightness: 3;
    }
    .prevnext {
      display: flex;
      flex-direction: row;
      justify-content: space-around;
      align-items: flex-start;
    }
    .prevnext a {
      display: flex;
      align-items: center;
      width: 100%;
      text-decoration: none;
    }
    a.next {
      justify-content: flex-end;
    }
    .prevnext a:hover {
      background: #00000006;
    }
    .prevnext-subtitle {
      color: var(--prevnext-color-text);
      filter: brightness(var(--prevnext-subtitle-brightness));
      font-size: .8rem;
    }
    .prevnext-title {
      color: var(--prevnext-color-text);
      font-size: 1rem;
    }
    .prevnext-text {
      max-width: 30vw;
    }
    </style>
    
    <a class='prev' href='/til/python-git'>
    

        <svg width="50px" height="50px" viewbox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M13.5 8.25L9.75 12L13.5 15.75" stroke="var(--prevnext-color-angle)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"> </path>
        </svg>
        <div class='prevnext-text'>
            <p class='prevnext-subtitle'>prev</p>
            <p class='prevnext-title'>Using Git from Python</p>
        </div>
    </a>
    
    <a class='next' href='/til/python-enum'>
    
        <div class='prevnext-text'>
            <p class='prevnext-subtitle'>next</p>
            <p class='prevnext-title'>Python Enum</p>
        </div>
        <svg width="50px" height="50px" viewbox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M10.5 15.75L14.25 12L10.5 8.25" stroke="var(--prevnext-color-angle)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
        </svg>
    </a>
  </div>