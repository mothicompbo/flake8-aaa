import astroid

from flake8_aaa.act_block import ActBlock


def test_result_equals():
    node = astroid.parse('result = do_thing()').body[0]

    result = ActBlock.build(node)

    assert isinstance(result, ActBlock)
    assert result.node == node
    assert result.block_type == ActBlock.RESULT_EQUALS


def test_pytest_raises():
    node = astroid.parse('''with pytest.raises(Exception):
    do_thing()''').body[0]

    result = ActBlock.build(node)

    assert isinstance(result, ActBlock)
    assert result.node == node
    assert result.block_type == ActBlock.PYTEST_RAISES
