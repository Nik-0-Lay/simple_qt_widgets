# Qt-Widgets application
Basic example of how to deploy Qt-Widgets application using conan and cmake

## Setup
+ conan 2.16.1
+ cmake 3.31.0
+ qt 6.7.3
+ MSVC
+ C++17

## Deployment
Step-by-step deployment process. cmake invokes "conan install" command itself at "configure" step, so there is
no need to do it manualy 
1. Perform configure and generate steps with cmake gui or command-line interface
2. Build project for configuration needed

## Commonly Encountered Problems(CEP)
Here are some problems one can encounter dealing with similar task:
1. Having something like "unresolved_external_symbol qt_version_tag" is a linkage issue and it WILL NOT be solved by
   specifying 'DQT_NO_VERSION_TAGGING' as in some search results for this error. Instead verify that you have .dll files
   necessary for your project build configuration i.e. with 'd' suffix for Debug as in "Qt6Cored.dll" and without suffix 
   for Release as in "Qt6Core.dll". Then verify that you link against all libraries required for your project and call 
   windeployqt with custom script or with qt_generate_deploy_app_script.

2. Specifying "/Zc:__cplusplus" and "-permissive-" options also WILL NOT help and the problem is still with the linkage.
   Once you deal with it like proposed in the solution for the CEP(1) you will no longer have errors related to this options.

3. cmake breaks compatibility with versions required for installing Qt Debug configuration package in newer releases.
   If this is the issue, try use the cmake version mentioned in 'Setup' section