from behave import given, when, then
from todo_list import ToDoList

@given('the to-do list is empty')
def step_impl(context):
    context.todo_list = ToDoList()

@when('the user adds a task "{description}"')
def step_impl(context, description):
    context.todo_list.add_task(description)

@then('the to-do list should contain "{description}"')
def step_impl(context, description):
    assert (description, "Pending") in context.todo_list.list_tasks()

@given('the to-do list contains tasks:')
def step_impl(context):
    context.todo_list = ToDoList()
    for row in context.table:
        context.todo_list.add_task(row['Task'])

@when('the user lists all tasks')
def step_impl(context):
    context.output = context.todo_list.list_tasks()

@then('the output should contain:')
def step_impl(context):
    expected_output = context.text.strip().split("\n")[1:]
    expected_output = [(line[2:].strip(), "Pending") for line in expected_output]
    assert expected_output == context.output

@when('the user marks task "{description}" as completed')
def step_impl(context, description):
    context.todo_list.mark_as_completed(description)

@then('the to-do list should show task "{description}" as completed')
def step_impl(context, description):
    assert (description, "Completed") in context.todo_list.list_tasks()

@when('the user clears the to-do list')
def step_impl(context):
    context.todo_list.clear()

@then('the to-do list should be empty')
def step_impl(context):
    assert context.todo_list.list_tasks() == []
