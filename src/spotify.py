import csv
from typing import Dict, List
from rich import print

DATA_PATH = "data/spotify.csv"


def get_menu_presentation(data_path) -> str:
    return f"""
{'=' * 80}
Análise informações do Spotify baseado no arquivo '{data_path}'.

As opções são:
1 - Mostrar as top 10 músicas mais instrumentais no Spotify
2 - Mostrar as top 10 músicas mais dançantes no Spotify
3 - Mostrar as top 10 músicas mais enérgicas no Spotify
Q - Sair da execuçãoc

>>> Digite uma opção: """


def read_csv(path: str) -> List[Dict[str, str]]:
    """read csv file and return list of dictionaries"""
    with open(path, "r") as file:
        return list(csv.DictReader(file))


def get_most_instrumental_songs(
    data: List[Dict[str, str]]
) -> List[Dict[str, str]]:
    return sorted(
        data, key=lambda x: float(x["Instrumentalness"]), reverse=True
    )[:10]


def get_most_danceable_songs(
    data: List[Dict[str, str]]
) -> List[Dict[str, str]]:
    return sorted(data, key=lambda x: float(x["Danceability"]), reverse=True)[
        :10
    ]


def get_most_energetic_songs(
    data: List[Dict[str, str]]
) -> List[Dict[str, str]]:
    return sorted(data, key=lambda x: float(x["Energy"]), reverse=True)[:10]


def end_script() -> None:
    print("Encerrando! Até logo")
    exit()


OPTIONS = {
    "1": ("instrumentais", get_most_instrumental_songs),
    "2": ("dançantes", get_most_danceable_songs),
    "3": ("enérgicas", get_most_energetic_songs),
    "Q": end_script,
}


def process_music_analysis(data, option) -> None:
    print(f"{'. ' * 40}")
    print(f"Top 10 músicas mais {OPTIONS[option][0]}:")
    for index, song in enumerate(OPTIONS[option][1](data), start=1):
        print(f"{index:>2} - '{song['Track']}' de {song['Artist']}")


def handle_user_input(data, option) -> None:
    if option.upper() not in OPTIONS:
        print(f"!!! Opção {repr(option)} inválida!")
    elif option.isdigit():
        # elif isinstance(option, int):
        process_music_analysis(data, option.upper())
    elif option.isalpha():
        OPTIONS[option.upper()]()


def main(file_path) -> None:
    data = read_csv(file_path)
    while True:
        option = input(get_menu_presentation(file_path))
        handle_user_input(data, option)
        input("\n>>> Pressione ENTER para voltar ao menu...")


if __name__ == "__main__":
    main(DATA_PATH)
