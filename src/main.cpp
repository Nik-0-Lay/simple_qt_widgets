#include <QString>
#include <QGuiApplication>

int main(int argc, char* argv[])
{
	QString hello = { "Hello World!" };
	QGuiApplication app(argc, argv);
	qDebug() << hello;
	return app.exec();
}