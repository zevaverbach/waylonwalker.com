---
canonical_url: https://waylonwalker.com/til/git-python-all-commits/
cover_image: https://images.waylonwalker.com/til/git-python-all-commits.png
description: I am getting ready to do some timeseries analysis on a git repo with
  python, my This returns a generator, if you are iterating over them this is likely
  what The
published: true
tags:
- python
- git
title: List all git commits with GitPython
---

I am getting ready to do some timeseries analysis on a git repo with python, my first step is to figure out a way to list all of the git commits so that I can analyze each one however I want.  The GitPython library made this almost trivial once I realized how.

``` python
from git import Repo

repo = Repo('.') commits = repo.iter_commits()
```

This returns a generator, if you are iterating over them this is likely what you want.

``` python
commits
# <generator object Commit._iter_from_process_or_stream at 0x7f3307584510>
```

The generator will return `git.Commit` objects with lots of information about each commit such as `hexsha`, `author`, `commited_datetime`, `gpgsig`, and
`message`.

``` python
next(commits)
# <git.Commit "d125317892d0fab10a36638a2d23356ba25c5621">
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
    
    <a class='prev' href='/til/git-rebase-root'>
    

        <svg width="50px" height="50px" viewbox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M13.5 8.25L9.75 12L13.5 15.75" stroke="var(--prevnext-color-angle)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"> </path>
        </svg>
        <div class='prevnext-text'>
            <p class='prevnext-subtitle'>prev</p>
            <p class='prevnext-title'>Git rebase to the beginning of time</p>
        </div>
    </a>
    
    <a class='next' href='/til/git-push-default-current'>
    
        <div class='prevnext-text'>
            <p class='prevnext-subtitle'>next</p>
            <p class='prevnext-title'>Configure Git to Always Push to the Current Branch</p>
        </div>
        <svg width="50px" height="50px" viewbox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M10.5 15.75L14.25 12L10.5 8.25" stroke="var(--prevnext-color-angle)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
        </svg>
    </a>
  </div>