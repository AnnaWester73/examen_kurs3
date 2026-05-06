from behave import given, when, then


@given("att jag öppnar Läslistan")
def step_open_application(context):
    context.app_page.open()

@when('jag klickar på "{view_name}"')
def step_click_navigation(context, view_name):
    context.app_page.click_navigation(view_name)

@then("ska navigeringsmenyn visas")
def step_verify_startpage(context):
    assert context.app_page.navigation_is_visible()

@then('ska vyn "{view_name}" visas')
def step_view_visible(context, view_name):
    assert context.app_page.view_is_visible(view_name)