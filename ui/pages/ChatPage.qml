import QtQuick
import QtQuick.Controls

Rectangle {
    color: "#0e1116"

    Row {
        anchors.fill: parent

        ListView {
            width: 200
            model: ["Alice", "Bob", "Charlie"]

            delegate: Rectangle {
                width: parent.width
                height: 50
                color: "#1f2937"

                Text {
                    anchors.centerIn: parent
                    text: modelData
                    color: "white"
                }
            }
        }

        Column {
            anchors.fill: parent
            spacing: 10

            Text {
                text: "Chat Window"
                color: "white"
                font.pixelSize: 18
            }

            Rectangle {
                width: parent.width
                height: 300
                color: "#111827"
            }

            TextField {
                placeholderText: "Type message..."
            }

            Button {
                text: "Send"
            }
        }
    }
}