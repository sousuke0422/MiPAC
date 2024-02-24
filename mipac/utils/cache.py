from functools import lru_cache, wraps
from typing import Any

DEFAULT_CACHE: dict[str, list[str]] = {}
DEFAULT_CACHE_VALUE: dict[str, Any] = {}


def set_cache(group: str, key: str, value: Any) -> None:
    """キャッシュを設定します

    Parameters
    ----------
    group : str
        キャッシュのグループ名
    key : str
        一意のキー
    value : Any
        設定する値
    """
    if len(DEFAULT_CACHE.get(group, [])) > 50:
        del DEFAULT_CACHE[group][-1]
        del DEFAULT_CACHE_VALUE[key]

    if DEFAULT_CACHE.get(group) is None:
        DEFAULT_CACHE[group] = []
    DEFAULT_CACHE[group].append(key)
    DEFAULT_CACHE_VALUE[key] = value


def cache(group: str = "default", override: bool = False):
    """キャッシュを行います"""

    def decorator(func):
        @wraps(func)
        async def wrapper(self, *args, **kwargs):
            key = cache_key_builder(func, self, *args, **kwargs)
            hit_item = DEFAULT_CACHE_VALUE.get(key)
            if hit_item and override is False and kwargs.get("cache_override") is None:
                return hit_item
            res = await func(self, *args, **kwargs)
            set_cache(group, key, res)
            return res

        return wrapper

    return decorator


@lru_cache
def cache_key_builder(func, cls, *args, **kwargs):
    """キャッシュのキーを作成します"""
    ordered_kwargs = sorted(kwargs.items())
    key = (func.__module__ or "") + ".{0}" + f"{cls}" + str(args) + str(ordered_kwargs)
    return key
