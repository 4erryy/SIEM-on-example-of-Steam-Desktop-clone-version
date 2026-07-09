import QtQuick
import QtQuick.Controls

Rectangle {
    color: "#0f172a"

    Column {
        anchors.centerIn: parent
        spacing: 10

        Button { text: "Store" }
        Button { text: "Library" }
        Button { text: "Profile" }
        Button { text: "Chat" }
        Button { text: "Settings" }
    }
}