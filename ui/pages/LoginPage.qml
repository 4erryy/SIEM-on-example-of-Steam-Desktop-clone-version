import QtQuick
import QtQuick.Controls

Rectangle {
    id: loginRoot
    anchors.fill: parent
    color: "#1b2838" // Фирменный темно-синий цвет Steam

    signal loginSuccess()

    Column {
        anchors.centerIn: parent
        spacing: 20
        width: 300

        Text {
            text: "STEAMLAB PRO"
            color: "#66c0f4"
            font.pointSize: 24
            font.bold: true
            anchors.horizontalCenter: parent.horizontalCenter
        }

        Label {
            text: "Sign in to your account"
            color: "#c7d5e0"
            font.pointSize: 12
            anchors.horizontalCenter: parent.horizontalCenter
        }

        TextField {
            id: usernameField
            width: parent.width
            placeholderText: "Account name"
            color: "white"
            background: Rectangle {
                color: "#2a475e"
                radius: 3
            }
        }

        TextField {
            id: passwordField
            width: parent.width
            placeholderText: "Password"
            echoMode: TextInput.Password
            color: "white"
            background: Rectangle {
                color: "#2a475e"
                radius: 3
            }
        }

        Text {
            id: errorText
            color: "#ff4d4d"
            width: parent.width
            wrapMode: Text.WordWrap
            horizontalAlignment: Text.AlignHCenter
            text: ""
        }

        Button {
            width: parent.width
            text: "Sign In"
            
            contentItem: Text {
                text: parent.text
                color: "white"
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                font.bold: true
            }

            background: Rectangle {
                color: parent.down ? "#a15513" : (parent.hovered ? "#d4752b" : "#b8601c") // Оранжевая кнопка
                radius: 3
            }

            onClicked: {
                errorText.text = ""
                if (usernameField.text === "" || passwordField.text === "") {
                    errorText.text = "Please fill in all fields"
                } else {
                    // Вызываем метод Python-обработчика
                    authHandler.login(usernameField.text, passwordField.text)
                }
            }
        }
    }

    // Слушаем ответы от Python бэкенда через глобальный объект authHandler
    Connections {
        target: authHandler

        onLoginSuccess: (token) => {
            console.log("Login successful! Token: " + token)
            loginRoot.loginSuccess() // Генерируем внутренний QML-сигнал для смены экрана
        }

        onLoginFailed: (errorMsg) => {
            errorText.text = errorMsg
        }
    }
}
