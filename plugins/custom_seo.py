"""Custom HEADER tags for waylonwalker.com"""
import json
from pathlib import Path
from typing import TYPE_CHECKING, List

from bs4 import BeautifulSoup

from markata import Markata, __version__
from markata.hookspec import hook_impl

if TYPE_CHECKING:
    import frontmatter
    from bs4.element import Tag


def _create_seo(
    markata: Markata, soup: BeautifulSoup, article: "frontmatter.Post"
) -> List:
    if article.metadata["description"] == "" or None:
        article.metadata["description"] = " ".join(
            [p.text for p in soup.find(id="post-body").find_all("p")]
        ).strip()[:120]

    seo = [
        {
            "name": "og:image",
            "property": "og:image",
            "content": f'{markata.config["images_url"]}/{article.metadata["slug"]}-og_250x140.png',
        },
    ]
    return seo


def _add_seo_tags(seo: List, article: "frontmatter.Post", soup: BeautifulSoup) -> None:
    for meta in seo:
        soup.head.append(_create_seo_tag(meta, soup))


def _create_seo_tag(meta: dict, soup: BeautifulSoup) -> "Tag":
    tag = soup.new_tag("meta")
    for k in meta:
        tag.attrs[k] = meta[k]
    return tag


@hook_impl
def post_render(markata: Markata) -> None:
    with markata.cache as cache:
        for article in markata.iter_articles("add seo tags from seo.py"):
            key = markata.make_hash(
                __name__,
                "post_render",
                article.metadata["slug"],
                article.metadata["images_url"],
            )
            html_from_cache = cache.get(key)

            if html_from_cache is None:
                soup = BeautifulSoup(article.html, features="lxml")
                seo = _create_seo(markata, soup, article)
                _add_seo_tags(seo, article, soup)
                html = soup.prettify()
                cache.add(key, html, expire=15 * 24 * 60)
            else:
                html = html_from_cache
            article.html = html
