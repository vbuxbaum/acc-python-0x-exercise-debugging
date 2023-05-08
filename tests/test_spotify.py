from unittest.mock import patch
from src import spotify
import pytest

TEST_DATA_PATH = "tests/test_data/spotify.csv"


def mock_handler(*args):
    ...


def mock_reader(*args):
    ...


@patch("builtins.input")
@patch("src.spotify.handle_user_input")
def test_spotify_analyzer_main(mock_handler, mock_input, capsys):
    mock_input.side_effect = ["1", "", "Q"]
    with pytest.raises(SystemExit):
        spotify.main(TEST_DATA_PATH)

    mock_input.side_effect = ["2", "", "Q"]
    with pytest.raises(SystemExit):
        spotify.main(TEST_DATA_PATH)

    mock_input.side_effect = ["3", "", "Q"]
    with pytest.raises(SystemExit):
        spotify.main(TEST_DATA_PATH)

    captured = capsys.readouterr()

    assert captured.out.endswith("Encerrando! Até logo\n")


def test_spotify_second_option(capsys):
    with patch("builtins.input", side_effect=["2", "", "Q"]), pytest.raises(
        SystemExit
    ):
        spotify.main(TEST_DATA_PATH)

    captured = capsys.readouterr()

    assert "Top 10 músicas mais dançantes:" in captured.out
    assert captured.out.endswith("Encerrando! Até logo\n")


def test_spotify_third_option(capsys):
    with patch("builtins.input", side_effect=["3", "", "Q"]), pytest.raises(
        SystemExit
    ):
        spotify.main(TEST_DATA_PATH)

    captured = capsys.readouterr()

    assert "Top 10 músicas mais enérgicas:" in captured.out
    assert captured.out.endswith("Encerrando! Até logo\n")
