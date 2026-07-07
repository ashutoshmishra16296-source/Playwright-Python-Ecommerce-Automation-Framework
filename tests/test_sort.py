from pages.sort_page import SortPage


def test_sort_name_az(logged_in_page):

    sort = SortPage(logged_in_page)

    sort.sort_by("az")

    products = sort.get_product_names()

    assert products == sorted(products)