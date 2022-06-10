---
cover: ''
date: 2020-10-17
datetime: 2020-10-17 00:00:00+00:00
description: "I was 20 commits into a hackoberfest PR when I suddenly realized they
  they all had my work email on them instead of my personal email \U0001F631."
edit_link: https://github.com/edit/main/pages/blog/fix-git-commit-author.md
jinja: false
long_description: "I was 20 commits into a hackoberfest PR when I suddenly realized
  they they all had my work email on them instead of my personal email \U0001F631.
  \ This is the story of how I corrected my email address on 19 individual commits
  after already submitting for a PR"
now: 2022-06-10 02:38:55.574557
path: pages/blog/fix-git-commit-author.md
slug: fix-git-commit-author
status: published
super_description: "I was 20 commits into a hackoberfest PR when I suddenly realized
  they they all had my work email on them instead of my personal email \U0001F631.
  \ This is the story of how I corrected my email address on 19 individual commits
  after already submitting for a PR. Before anything else set the email correctly
  First thing is to find how many commits back this mistake goes.  I opened up the
  git log, and saw mine went back 19 commits.  I rolled back 20 just to be sure. Now
  I start the rebase 20 commits back from"
tags: []
templateKey: blog-post
title: Fix git commit author
today: 2022-06-10
year: 2020
---

I was 20 commits into a hackoberfest PR when I suddenly realized they they all had my work email on them instead of my personal email 😱.  This is the story of how I corrected my email address on 19 individual commits after already submitting for a PR.

1. [Change the email for this repo](#change-the-email-for-this-repo)
1. [Prepare for rebasing](#prepare-for-rebasing)
1. [start the rebase](#start-the-rebase)
1. [🛠 Fix First wrong Commit](#fix-first-wrong-commit)
1. [Fix all commits](#fix-all-commits)
1. [Done](#done)
1. [ReCap](#recap)

    
## Change the email for this repo

_stop the bleeding_

Before anything else set the email correctly!

``` bash
cd kedro
git config user.name "Waylon Walker"
git config user.email quadmx08@gmail.com
```

## Prepare for rebasing

First thing is to find how many commits back this mistake goes.  I opened up the git log, and saw mine went back 19 commits.  I rolled back 20 just to be sure.

``` bash
$ git log
...
commit a355926b9d7ec4c05659adaa254beefbdb036332
Author: WaylonWalker <email@work.com>
Date:   Sat Oct 17 10:28:59 2020 -0500

    give name of function inside incorrect parameters error
  
commit 1756f5d121bd06c459560b2e982e0d7b6879e9ca
Author: Kiyohito Kunii (Kiyo) <8097799+921kiyo@users.noreply.github.com>
Date:   Fri Oct 2 15:33:09 2020 +0100

    Fix docs reference for registering `pipelines`
```

## start the rebase

Now I start the rebase 20 commits back from HEAD.  THis will pop you into a text file with a list of commits, for this change simply replace all `pick` with `edit`.

``` bash
git rebase -i HEAD~20
```

## Note for the first commit

If you want to rebase back to the start of the repo use the `--root` flag.

``` bash
git rebase -i --root
```

Run git log to see where we ended up.

``` bash
$ git log
commit 1756f5d121bd06c459560b2e982e0d7b6879e9ca
Author: Kiyohito Kunii (Kiyo) <8097799+921kiyo@users.noreply.github.com>
Date:   Fri Oct 2 15:33:09 2020 +0100

    Fix docs reference for registering `pipelines`
```

As expected we ended up on Kiyo's commit. So we can simply move forward without any edits.

``` bash
$ git rebase --continue
Stopped at e162ca7...  correct function name in tests
You can amend the commit now, with

  git commit --amend

Once you are satisfied with your changes, run

  git rebase --continue
```

## 🛠 Fix First wrong Commit

Checking the log again I an now on my first commit with a mistake.

``` bash
$ git log
commit 95c209a740d6d0340e19a8fc36298cbf874f8bf7 (HEAD)
Author: WaylonWalker <email@work.com>
Date:   Sat Oct 3 11:59:44 2020 -0500

    correct function name in tests

commit cde2e8baa3c1c4a9f1da4135258381466b1da40a
Author: Waylon Walker <quadmx08@gmail.com>
Date:   Sat Oct 17 10:30:07 2020 -0500

    update tests

commit a355926b9d7ec4c05659adaa254beefbdb036332
Author: Waylon Walker <quadmx08@gmail.com>
Date:   Sat Oct 17 10:28:59 2020 -0500

    give name of function inside incorrect parameters error

commit 1756f5d121bd06c459560b2e982e0d7b6879e9ca
Author: Kiyohito Kunii (Kiyo) <8097799+921kiyo@users.noreply.github.com>
Date:   Fri Oct 2 15:33:09 2020 +0100

    Fix docs reference for registering `pipelines`
```

Running the following command will reset the author on the current commit.

``` bash
git commit --amend --reset-author
```

Double check with a quick `git log` that the author was fixed.

``` bash
commit ccaaa56059ee4554731fa83297ca9e8e387a7592 (HEAD)
Author: Waylon Walker <quadmx08@gmail.com>
Date:   Sat Oct 17 10:35:40 2020 -0500

    correct function name in tests

commit cde2e8baa3c1c4a9f1da4135258381466b1da40a
Author: Waylon Walker <quadmx08@gmail.com>
Date:   Sat Oct 17 10:30:07 2020 -0500

    update tests

commit a355926b9d7ec4c05659adaa254beefbdb036332
Author: Waylon Walker <quadmx08@gmail.com>
Date:   Sat Oct 17 10:28:59 2020 -0500

    give name of function inside incorrect parameters error

commit 1756f5d121bd06c459560b2e982e0d7b6879e9ca
Author: Kiyohito Kunii (Kiyo) <8097799+921kiyo@users.noreply.github.com>
Date:   Fri Oct 2 15:33:09 2020 +0100

    Fix docs reference for registering `pipelines`
```

## Fix all commits

Now to do this for 18 other commits.  I found that chaining the three commands into a bash one-liner was quite helpful.  I turned off pre-commit hooks with `--no-verify`.  I also turned off the `log` pager by adding `--no-pager`.

``` bash
git rebase --continue && \
git commit --amend --reset-author --no-edit --no-verify && \
git --no-pager log -n 3
```

## Done

This was quick and easy for 19 commits.  I have tried to loop through changes like this in the past, and it does get a bit hairy.  I find its easier to just setup a one-liner and crank through them one by one.

## A note on changing history...

Since this was done in a rebase it has changed the history of the repo.  This is ok to do only when you are the only person or are in close communication with everyone using the repo.  One thing I have ran into is that if you do this after you submit a PR, but before its completed it duplicates your commits in a merge.  For this particular change I simply closed the first PR and opened a second.  If someone has a better suggestion, I would be glad to know a better way.

## ReCap

``` bash
cd kedro
git config user.name "Waylon Walker"
git config user.email quadmx08@gmail.com
git log
git rebase -i HEAD~20
git log
git rebase --continue
git log
git rebase --continue && git commit --amend --reset-author --no-edit --no-verify && git --no-pager log -n 3
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
    
    <a class='prev' href='/fix-styled-components-in-gatsby'>
    

        <svg width="50px" height="50px" viewbox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M13.5 8.25L9.75 12L13.5 15.75" stroke="var(--prevnext-color-angle)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"> </path>
        </svg>
        <div class='prevnext-text'>
            <p class='prevnext-subtitle'>prev</p>
            <p class='prevnext-title'>I finally fixed my Styled-Components in gatsby.js</p>
        </div>
    </a>
    
    <a class='next' href='/find-replace'>
    
        <div class='prevnext-text'>
            <p class='prevnext-subtitle'>next</p>
            <p class='prevnext-title'>Find and Replace in the Terminal.</p>
        </div>
        <svg width="50px" height="50px" viewbox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M10.5 15.75L14.25 12L10.5 8.25" stroke="var(--prevnext-color-angle)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
        </svg>
    </a>
  </div>