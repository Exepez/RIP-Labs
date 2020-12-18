from strategy import *

# -*- coding: utf-8 -*-

from radish import given, when, then

@given('"I have the path "{path}"')
def have_path(step, path):
    step.context.path = path

@when('I am making a request')
def do_request(step):
    context.strategy = ConcreteStrategyB()
    step.context.result = context.do_some_business_logic(step.context.path)

@then('I expect the result to be "{result}"')
def expect_result(step, result):
    assert step.context.result == result