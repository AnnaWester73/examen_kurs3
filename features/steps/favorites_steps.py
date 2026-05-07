from behave import given, when, then


@given('att jag navigerar till vyn "{view_name}"')
def step_navigate_to_view(context, view_name):
    context.app_page.open()
    context.app_page.go_to(view_name)

@when('jag markerar boken "{title}" som favorit')
@when('jag avmarkerar boken "{title}" som favorit')
def step_toggle_favorite(context, title):
    context.app_page.toggle_favorite(title)

@then('ska boken "{title}" vara markerad som favorit')
def step_book_should_be_favorite(context, title):
    assert context.app_page.is_marked_as_favorite(title)

@then('ska boken "{title}" visas i "{view_name}"')
def step_book_visible_in_view(context, title, view_name):
    assert context.app_page.book_in_view_is_visible(view_name, title)

@then('ska boken "{title}" inte visas i "{view_name}"')
def step_book_not_visible_in_view(context, title, view_name):
    assert context.app_page.book_in_view_count(view_name, title) == 0

@then("ska inga favoritböcker visas")
def step_no_favorites_visible(context):
    assert context.app_page.favorites_list_is_empty()