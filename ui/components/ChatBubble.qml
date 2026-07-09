import QtQuick
import QtQuick.Controls

Rectangle {
    width: 200
    height: 40
    radius: 8
    color: "#2563eb"

    property string message: "Hello"

    Text {
        anchors.centerIn: parent
        text: message
        color: "white"
        wrapMode: Text.WordWrap
    }
}