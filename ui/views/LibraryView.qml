import QtQuick
import QtQuick.Controls

Rectangle {
    color: "#14181d"

    Column {
        anchors.centerIn: parent
        spacing: 10

        Text {
            text: "LIBRARY VIEW"
            color: "white"
            font.pixelSize: 24
        }

        Text {
            text: "Your installed games"
            color: "#9ca3af"
        }
    }
}