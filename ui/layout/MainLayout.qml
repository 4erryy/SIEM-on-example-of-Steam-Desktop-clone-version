import QtQuick
import QtQuick.Controls

Rectangle {
    anchors.fill: parent
    color: "#0b0f14"

    property alias content: contentArea

    Column {
        anchors.fill: parent

        TopBar {
            width: parent.width
        }

        Row {
            anchors.fill: parent

            Sidebar {
                width: 200
                height: parent.height
            }

            Rectangle {
                id: contentArea
                width: parent.width - 200
                height: parent.height
                color: "#111827"
            }
        }
    }
}