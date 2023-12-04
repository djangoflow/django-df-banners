import pytest
from rest_framework.test import APIClient

from df_banners.models import Banner

pytestmark = pytest.mark.django_db


@pytest.mark.parametrize(
    "titles",
    [
        ["Banner1", "Banner2"],
        ["Banner3", "Banner4", "Banner5"],
    ],
)
def test_list_banners(titles: list[str], client: APIClient) -> None:
    for title in titles:
        Banner.objects.create(title=title)

    response = client.get("/api/v1/banners/banners/")

    assert response.status_code == 200
    assert response.json()["count"] == len(titles)
    assert {banner["title"] for banner in response.json()["results"]} == set(titles)


@pytest.mark.parametrize(
    "banners, filter_tags, expected_titles",
    [
        [
            {
                "banner1": ["tag1", "tag2"],
                "banner2": ["tag1", "tag3"],
                "banner3": ["tag2", "tag3"],
            },
            ["tag1"],
            ["banner1", "banner2"],
        ],
        [
            {
                "banner1": ["tag1", "tag2"],
                "banner2": ["tag1"],
                "banner3": ["tag2"],
            },
            ["tag1", "tag2"],
            ["banner1"],
        ],
    ],
)
def test_list_banners_filter_tags(
    banners: dict[str, list[str]],
    filter_tags: list[str],
    expected_titles: list[str],
    client: APIClient,
) -> None:
    for title, tags in banners.items():
        banner = Banner.objects.create(title=title)
        banner.tags.set(tags)

    response = client.get("/api/v1/banners/banners/", {"tags": ",".join(filter_tags)})

    assert response.status_code == 200
    assert response.json()["count"] == len(expected_titles)
    assert {banner["title"] for banner in response.json()["results"]} == set(
        expected_titles
    )
