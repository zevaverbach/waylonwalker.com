---
date: 2022-01-14 23:43:42.001865
templateKey: til
title: python functools total ordering
tags:
  - python
status: draft

---


```
from enum import Enum, auto
from functools import total_ordering


@total_ordering
class LifeCycle(Enum):

    configure = auto()
    glob = auto()
    load = auto()
    pre_render = auto()
    render = auto()
    post_render = auto()
    save = auto()

    def __lt__(self, other):
        try:
            return self.value < other.value
        except AttributeError:
            return self.value < other

    def __eq__(self, other):
        try:
            return self.value == other.value
        except AttributeError:
            return self.value == other

```