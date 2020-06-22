import typing

from flake8_aaa.exceptions import AAAError
from flake8_aaa.line_markers import LineMarkers
from flake8_aaa.types import LineType


def test_ok():
    line_markers = LineMarkers(6 * [''], 7)
    line_markers.types[0] = LineType.func_def
    line_markers.types[1] = LineType.arrange
    line_markers.types[2] = LineType.blank_line
    line_markers.types[3] = LineType.act
    line_markers.types[4] = LineType.blank_line
    line_markers.types[5] = LineType._assert

    result = line_markers.check_comment_in_act()

    assert isinstance(result, typing.Generator)
    assert list(result) == []


# --- FAILURES ---


def test_comment_before():
    line_markers = LineMarkers(7 * [''], 11)
    line_markers.types[0] = LineType.func_def
    line_markers.types[1] = LineType.arrange
    line_markers.types[2] = LineType.blank_line
    line_markers.types[3] = LineType.comment
    line_markers.lines[3] = '    # Do action'
    line_markers.types[4] = LineType.act
    line_markers.types[5] = LineType.blank_line
    line_markers.types[6] = LineType._assert

    result = line_markers.check_comment_in_act()

    assert isinstance(result, typing.Generator)
    assert list(result) == [
        AAAError(
            line_number=14,
            offset=4,
            text='AAA06 comment in Act block',
        ),
    ]
