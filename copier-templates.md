---
cover: ''
date: 2022-01-05
datetime: 2022-01-05 00:00:00+00:00
description: '%%include til/copier %%include til/copier-template-variables %%include
  til/copier-answers'
edit_link: https://github.com/edit/main/pages/blog/copier-templates.md
jinja: false
long_description: '%%include til/copier %%include til/copier-template-variables %%include
  til/copier-answers'
now: 2022-06-10 02:38:55.573901
path: pages/blog/copier-templates.md
slug: copier-templates
status: draft
super_description: '%%include til/copier %%include til/copier-template-variables %%include
  til/copier-answers'
tags:
- python
- linux
- cli
templateKey: blog-post
title: Copier Templates
today: 2022-06-10
year: 2022
---

I was completely stuck for awhile.  copier was not replacing my template
variables.  I found out that adding all these `_endops` fixed it.  Now
It will support all of these types of variable wrappers

``` yaml
# copier.yml
_templates_suffix: .jinja
_envops:
  block_end_string: "%}"
  block_start_string: "{%"
  comment_end_string: "#}"
  comment_start_string: "{#"
  keep_trailing_newline: true
  variable_end_string: "}}"
  variable_start_string: "{{"
```

> !RTFM: Later I read the docs and realized that copier defaults to using `[[`
> and `]]` for its templates unlike other tools like cookiecutter.
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
    
    <a class='prev' href='/til/dedupe-your-shell-paths'>
    

        <svg width="50px" height="50px" viewbox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M13.5 8.25L9.75 12L13.5 15.75" stroke="var(--prevnext-color-angle)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"> </path>
        </svg>
        <div class='prevnext-text'>
            <p class='prevnext-subtitle'>prev</p>
            <p class='prevnext-title'>Dedupe your shell paths</p>
        </div>
    </a>
    
    <a class='next' href='/til/copier-template-variables'>
    
        <div class='prevnext-text'>
            <p class='prevnext-subtitle'>next</p>
            <p class='prevnext-title'>copier template variables</p>
        </div>
        <svg width="50px" height="50px" viewbox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M10.5 15.75L14.25 12L10.5 8.25" stroke="var(--prevnext-color-angle)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
        </svg>
    </a>
  </div>

I've been looking for a templating tool for awhile that works well with
single files.  My go to templating tool `cookiecutter` does not work for
single files, it needs to put files into a directory underneath of it.

## template variables

By default copier uses double square brackets for its variables.
variables in files, directory_names, or file_names will be substituted
for their value once you render them.

``` python
# hello-py/hello.py.tmpl
print('hello-[[name]]')
```

> note! by default copier will not inject variables into your
> [[template-strings]] unless you use a .tmpl suffix.

Before running copier we need to tell copier what variables to ask for,
we do this with a copier.yml file.

``` yaml
# copier.yml
name:
  default: my_name
  type: str
  help: What is your name
```

## installing copier

I prefer to install cli tools that I need globally with pipx, this
always gives me access to the tool without worrying about dependency
conflicts, bloating my system site-packages, or managing a separate
virtual environment for it myself.

``` bash
pipx install copier
```
## running copier

When running `copier copy` we pass in the directory of the template, and
the directory that we want to render the template into.

``` bash
copier copy hello-py .
```

> note! the directory '.' is often referred to in cli programs to
> represent the current working directory that we are calling the
> command from.

## results

The resulting files will have your variables injected into them if you have
setup your template and copier.yml up correctly.

``` python
print('hello-you')
```
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
    
    <a class='prev' href='/til/copier_endops'>
    

        <svg width="50px" height="50px" viewbox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M13.5 8.25L9.75 12L13.5 15.75" stroke="var(--prevnext-color-angle)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"> </path>
        </svg>
        <div class='prevnext-text'>
            <p class='prevnext-subtitle'>prev</p>
            <p class='prevnext-title'>Changing copier template strings (_endops)</p>
        </div>
    </a>
    
    <a class='next' href='/til/copier-tasks'>
    
        <div class='prevnext-text'>
            <p class='prevnext-subtitle'>next</p>
            <p class='prevnext-title'>Copier Tasks | Python templating post run task</p>
        </div>
        <svg width="50px" height="50px" viewbox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M10.5 15.75L14.25 12L10.5 8.25" stroke="var(--prevnext-color-angle)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
        </svg>
    </a>
  </div>

The copier answers file is a key component to making your templates
re-runnable.  Let's look at the example for my setup.py.

``` bash
❯ tree ~/.copier-templates/setup.py
/home/walkers/.copier-templates/setup.py
├── [[ _copier_conf.answers_file ]].tmpl
├── copier.yml
├── setup.cfg
└── setup.py.tmpl

0 directories, 4 files
```

Inside of my `[[ _copier_conf.answers_file ]].tmpl` file is this, a
message not to muck around with it, and the ansers in yaml form.  The
first line is just a helper for the blog post.

``` yaml
# ~/.copier-templates/setup.py/\[\[\ _copier_conf.answers_file\ \]\].tmpl
# Changes here will be overwritten by Copier; NEVER EDIT MANUALLY
[[_copier_answers|to_nice_yaml]]
```

Inside my copier.yml I have setup my _answers_file to point to a special
file.  This is because this is not a whole projet template, but one just
for a single file.

``` yaml
# copier.yml
# ...
_answers_file: .setup-py-copier-answers.yml
```

> Once I change the _answers_file I was incredibly stuck

## Run it

I'm making a library of personal copier templates in my
`~/.copier-templates` directory and I am going to run it from there.

``` bash
copier copy ~/.copier-templates/setup.py
```
## Results

After rendering the template we have the following content in our
`.setup.setup-py-copier-answers.yml` file.  This will allow us to update
quick if we ever change our template.

``` yaml
# .setup-py-copier-answers.yml
# Changes here will be overwritten by Copier; NEVER EDIT MANUALLY
_src_path: /home/walkers/.copier-templates/setup.py
author_github: waylonwalker
author_name: Waylon Walker
description: awesomeness
framework: null
keywords: null
package_name: my-package
```

## Update it

This is where I was most stuck, primarily becuase `-a <answers_file>`
must come exactly after the base command `copier`.  This felt a bit odd
to and not where I expected it so it.

``` bash
copier -a .setup-py-copier-answers.yml update
```

## Stop asking all these damn questions

So the defaults are now changed to our previous results, but it keeps
asking for them.  To stop asking we can simply add a `-f` flag.

``` bash
copier -fa .setup-py-copier-answers.yml update
```
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
    
    <a class='prev' href='/til/copier-tasks'>
    

        <svg width="50px" height="50px" viewbox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M13.5 8.25L9.75 12L13.5 15.75" stroke="var(--prevnext-color-angle)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"> </path>
        </svg>
        <div class='prevnext-text'>
            <p class='prevnext-subtitle'>prev</p>
            <p class='prevnext-title'>Copier Tasks | Python templating post run task</p>
        </div>
    </a>
    
    <a class='next' href='/til/convert-markdown-pdf-linux'>
    
        <div class='prevnext-text'>
            <p class='prevnext-subtitle'>next</p>
            <p class='prevnext-title'>Converting markdown to pdf with pandoc on linux</p>
        </div>
        <svg width="50px" height="50px" viewbox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M10.5 15.75L14.25 12L10.5 8.25" stroke="var(--prevnext-color-angle)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
        </svg>
    </a>
  </div>
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
    
    <a class='prev' href='/quick-progress-bars-in-python-using-tqdm'>
    

        <svg width="50px" height="50px" viewbox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M13.5 8.25L9.75 12L13.5 15.75" stroke="var(--prevnext-color-angle)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"> </path>
        </svg>
        <div class='prevnext-text'>
            <p class='prevnext-subtitle'>prev</p>
            <p class='prevnext-title'>Quick Progress Bars in python using TQDM</p>
        </div>
    </a>
    
    <a class='next' href='/eight-years-cat'>
    
        <div class='prevnext-text'>
            <p class='prevnext-subtitle'>next</p>
            <p class='prevnext-title'>My first eight years as a working professional.</p>
        </div>
        <svg width="50px" height="50px" viewbox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M10.5 15.75L14.25 12L10.5 8.25" stroke="var(--prevnext-color-angle)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
        </svg>
    </a>
  </div>