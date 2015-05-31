all:
	@echo "Comandos disponibles:"
	@echo ""
	@echo "   ejecutar      Inicia la aplicacion con honcho."
	@echo "   compilar      Inicia y compila la aplicacion ember."
	@echo ""

compilar:
	cd client; npm install; bower install; ember build

ejecutar:
	honcho start
