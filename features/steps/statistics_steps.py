from behave import then


@then("ska det totala antalet böcker visas")
def step_total_books_visible(context):
    assert context.app_page.stats_total_is_visible()

@then("ska antalet favoritmarkerade böcker visas")
def step_favorite_books_visible(context):
    assert context.app_page.stats_favorites_is_visible()

@then('ska totalt antal böcker vara "{count:d}"')
def step_total_books_count(context, count):
    actual = context.app_page.stats_total_books()
    assert actual == count, f"Förväntade totalt {count} böcker, fick {actual}"

@then('ska antal favoriter vara "{count:d}"')
def step_favorite_books_count(context, count):
    actual = context.app_page.stats_favorite_books()
    assert actual == count, f"Förväntade {count} favoriter, fick {actual}"