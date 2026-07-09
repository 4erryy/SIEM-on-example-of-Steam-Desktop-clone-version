import QtQuick
import QtQuick.Controls

Rectangle {
    width: 180
    height: 40
    color: "#111827"
    radius: 6

    property string text: "Button"

    MouseArea {
        anchors.fill: parent
        onClicked: console.log(text + " clicked")
    }

    Text {
        anchors.centerIn: parent
        text: parent.text
        color: "white"
    }
}