import QtQuick
import QtQuick.Controls
import "pages"

ApplicationWindow {
    id: window
    visible: true
    width: 1200
    height: 700
    title: "SteamLab Pro"

    // Свойство для отслеживания состояния авторизации
    property bool isAuthorized: false

    StackView {
        id: stack
        anchors.fill: parent
        // Стартуем с экрана логина
        initialItem: loginPage
    }

    // Объявляем компоненты страниц
    Component { 
        id: loginPage
        LoginPage {
            onLoginSuccess: {
                window.isAuthorized = true
                stack.replace(library) // Заменяем экран входа на библиотеку
            }
        }
    }
    
    Component { id: library; LibraryPage {} }
    Component { id: store; StorePage {} }
    Component { id: friends; FriendsPage {} }
    Component { id: settings; SettingsPage {} }

    // Footer отображается только ПОСЛЕ успешного входа
    footer: Row {
        spacing: 10
        anchors.horizontalCenter: parent.horizontalCenter
        visible: window.isAuthorized // Магия привязки свойства

        Button { text: "Library"; onClicked: stack.replace(library) }
        Button { text: "Store"; onClicked: stack.replace(store) }
        Button { text: "Friends"; onClicked: stack.replace(friends) }
        Button { text: "Settings"; onClicked: stack.replace(settings) }
    }
}
