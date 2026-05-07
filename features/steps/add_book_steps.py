from behave import given, when, then


@given("att jag öppnar vyn Lägg till bok")
def step_open_add_book_view(context):
    context.app_page.open()
    context.app_page.click_navigation("Lägg till bok")

@when('jag fyller i titel "{title}"')
def step_fill_title(context, title):
    # "<null>" används som platshållare i Examples-tabellen för att
    # representera ett tomt fält. Behaves parse-matcher hanterar inte
    # tomma strängar i Scenario Outlines tillförlitligt.
    if title != "<null>":
        context.app_page.fill_title(title)

@when('jag fyller i författare "{author}"')
def step_fill_author(context, author):
    if author != "<null>":
        context.app_page.fill_author(author)

@when("jag klickar på Lägg till ny bok")
def step_click_add_new_book(context):
    context.app_page.click_add_new_book()

@then('ska boken "{title}" visas i katalogen')
def step_book_visible_in_catalog(context, title):
    assert context.app_page.book_in_view_is_visible("Katalog", title)

@then("ska fälten vara tomma")
def step_form_fields_empty(context):
    assert context.app_page.form_fields_are_empty()

@then("ska knappen Lägg till ny bok vara inaktiv")
def step_add_button_disabled(context):
    assert context.app_page.add_submit_button_is_disabled()