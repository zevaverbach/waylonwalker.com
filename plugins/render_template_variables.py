import datetime

from markata.hookspec import hook_impl, register_attr


@hook_impl
@register_attr("articles")
def pre_render(markata) -> None:
    for article in markata.iter_articles("rendering markdown"):
        try:
            article["year"] = article["date"].year
        except KeyError:
            article["year"] = datetime.datetime.today().year
