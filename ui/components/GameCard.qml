import QtQuick
import QtQuick.Controls

Rectangle {
    width: 260
    height: 120
    radius: 8
    color: "#2a2f36"

    property string title: "Game"
    property string price: "Free"

    Column {
        anchors.centerIn: parent
        spacing: 6

        Text {
            text: title
            color: "white"
            font.pixelSize: 16
        }

        Text {
            text: price
            color: "#9ca3af"
        }

        Button {
            text: "Open"
        }
    }
}