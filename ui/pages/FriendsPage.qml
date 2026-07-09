import QtQuick
import QtQuick.Controls

Rectangle {
    color: "#0f1720"

    Column {
        anchors.fill: parent
        anchors.margins: 20
        spacing: 10

        Text {
            text: "FRIENDS"
            color: "white"
            font.pixelSize: 24
        }

        ListView {
            anchors.fill: parent
            model: ["Alice", "Bob", "Charlie", "David"]

            delegate: Rectangle {
                width: parent.width
                height: 50
                color: "#1f2937"

                Text {
                    anchors.centerIn: parent
                    text: modelData + " • online"
                    color: "lightgreen"
                }
            }
        }
    }
}