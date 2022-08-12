import PySimpleGUI as sg

sg.theme("DarkBrown4")
search_bar = [
    [
        sg.Text("Paste link here: "),
        sg.Input(size=(50, 1), key="-URL-"),
        sg.Button("Search", size=10, key="-SRC-"),
    ],
    [
        sg.Text("Destiny  Folder: "),
        sg.Input(size=(50, 1), disabled=True, key="-FOLDER-"),
        sg.FolderBrowse("Browse", size=10, key="-BROWSE-"),
    ],
]
playlist = [[sg.Multiline(size=(35, 18), disabled=True, key="-PLAYLIST-")]]
dl_panel = [
    [sg.Button("Download playlist", size=230)],
    [
        sg.Column(
            [
                [sg.Image(size=(120, 120), background_color="white", key="-IMG-")],
                [
                    sg.Column(
                        [
                            [sg.Text("Artist:", key="-ARTIST-")],
                            [sg.Text("Music:", key="-MUSIC-")],
                        ],
                        size=(260, 50),
                    )
                ],
            ],
            size=(260, 210),
        ),
    ],
    [sg.Text("DOWNLOANDING...", key="-STATUS-")],
    [
        sg.ProgressBar(
            max_value=100,
            orientation="h",
            size=(20, 10),
            border_width=4,
            key="-PROGRESS_BAR-",
            bar_color=("White", "Red"),
        )
    ],
]
layout = [
    [
        [sg.Column(search_bar)],
        sg.Column([[sg.Column(playlist), sg.Column(dl_panel)]]),
    ]
]

title = "Youtube Downloader"
size = (600, 400)
window = sg.Window(title=title, size=size, layout=layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == "Quit":
        break

window.close()
