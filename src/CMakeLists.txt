#  Let CMake handle Qt's MOC, UIC and RCC automatically
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTOUIC ON)
set(CMAKE_AUTORCC ON)

#  Find Qt package 
find_package(Qt6 COMPONENTS Core Gui Widgets REQUIRED)

# Qt forces the 'OLD' behavior of this policy by default, so we mannualy set it to NEW to get rid of warning
set(QT_FORCE_CMP0156_TO_NEW ON)

#  Set up Qt-specific features for the project
qt_standard_project_setup()

#  Set up Qt-specific executable target which is e.g. automatically links to Qt6::Core
qt_add_executable(simple_qt main.cpp)

#  Link Qt libraries
target_link_libraries(simple_qt PUBLIC Qt6::Gui)
target_link_libraries(simple_qt PUBLIC Qt6::Widgets)

#  Install .exe file into '${CMAKE_INSTALL_BINDIR}' for corresponding configuration
install(TARGETS simple_qt
  BUNDLE DESTINATION .
  RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
  NO_UNSUPPORTED_PLATFORM_ERROR
)

#  Generate the Qt deployment script for the target specified
qt_generate_deploy_app_script(
  TARGET simple_qt
  OUTPUT_SCRIPT deploy_script
)

#  Call the deployment script
install(SCRIPT ${deploy_script})

#  Specify include directories to use for the target
target_include_directories(simple_qt PRIVATE "${Qt6_INCLUDE_DIRS}")