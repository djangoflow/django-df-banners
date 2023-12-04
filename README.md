# Django DF Banners

Banner model with images, videos and tags

## Installation:

- Install the package

```
pip install django-df-banners
```

- Include default `INSTALLED_APPS` from `df_banners.defaults` to your `settings.py`

```python
from df_banners.defaults import DF_BANNERS_INSTALLED_APPS

INSTALLED_APPS = [
    ...
    *DF_BANNERS_INSTALLED_APPS,
    ...
]

```


### Video support

To enable video support you need to install `django-df-banners[video]` package and include `df_banners.video` to your `INSTALLED_APPS`:

```python
from df_banners.defaults import DF_BANNERS_VIDEO_INSTALLED_APPS

INSTALLED_APPS = [
    ...
    *DF_BANNERS_VIDEO_INSTALLED_APPS,
    ...
]
```

## Development

Installing dev requirements:

```
pip install -e .[test]
```

Installing pre-commit hook:

```
pre-commit install
```

Running tests:

```
pytest
```
