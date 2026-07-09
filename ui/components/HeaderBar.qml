import QtQuick
import QtQuick.Controls

Rectangle {
    width: parent.width
    height: 50
    color: "#0f172a"

    Row {
        anchors.verticalCenter: parent.verticalCenter
        spacing: 20
        anchors.left: parent.left
        anchors.leftMargin: 10

        Text {
            text: "SteamLab"
            color: "white"
            font.pixelSize: 18
        }

        Text {
            text: "Store"
            color: "#9ca3af"
        }

        Text {
            text: "Library"
            color: "#9ca3af"
        }

        Text {
            text: "Profile"
            color: "#9ca3af"
        }
    }
}