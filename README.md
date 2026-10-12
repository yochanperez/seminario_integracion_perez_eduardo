# 🎓 Seminario de Integración

Repositorio académico para el desarrollo, integración y documentación de proyectos de software.

El repositorio centraliza los proyectos y subproyectos desarrollados durante el seminario, aplicando buenas prácticas de programación, organización del código y control de versiones.

---

## 🛠️ Tecnologías

| Tecnología | Uso |
|---|---|
| 🐍 Python | Desarrollo de aplicaciones |
| ⚡ FastAPI | Desarrollo de API REST |
| 📦 uv | Gestión de dependencias y entornos virtuales de Python |
| 🟢 Node.js | Desarrollo de servicios y aplicaciones |
| 🅰️ Angular | Desarrollo de interfaces web |
| 🔀 Git | Control de versiones |

---

## 📁 Estructura del repositorio

seminario-integracion/ ├── backend/ # APIs y servicios backend │ ├── api-principal/ │ └── api-secundaria/ │ ├── frontend/ # Aplicaciones web │ ├── angular-admin/ │ └── angular-cliente/ │ ├── servicios/ # Servicios independientes │ └── servicio-node/ │ ├── documentacion/ # Documentación del proyecto ├── recursos/ # Recursos complementarios │ ├── .gitignore └── README.md


> La estructura es referencial y puede adaptarse según las necesidades de cada proyecto.

---

## 🚀 Configuración del entorno

### Requisitos

- [Git](https://git-scm.com/)
- [Python](https://www.python.org/)
- [uv](https://docs.astral.sh/uv/)
- [Node.js](https://nodejs.org/)
- [Angular](https://angular.dev/), cuando corresponda.

### Clonar el repositorio

git clone <URLDELREPOSITORIO> cd seminario-integracion


### Python y FastAPI

Accede al directorio del proyecto Python:

cd backend/api-principal


Instala las dependencias:

uv sync


Si todavía no has configurado FastAPI en el proyecto:

uv add fastapi "uvicorn[standard]"


Ejecuta la aplicación:

uv run uvicorn app.main:app --reload


Documentación interactiva de la API:

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

> El comando de ejecución supone que el archivo principal se encuentra en `app/main.py`.

### Node.js

Accede al directorio del servicio:

cd servicios/servicio-node


Instala las dependencias:

npm install


Ejecuta el script de desarrollo definido en `package.json`:

npm run dev


### Angular

Accede al directorio de la aplicación:

cd frontend/angular-admin


Instala las dependencias:

npm install


Inicia el servidor de desarrollo:

npx ng serve


La aplicación estará disponible normalmente en http://localhost:4200/.

---

## 🌿 Control de versiones

Se recomienda utilizar ramas para organizar el desarrollo y facilitar la integración de cambios.

Rama	Propósito
main	Versión estable del proyecto
develop	Integración de funcionalidades
feature/*	Desarrollo de nuevas funcionalidades
fix/*	Corrección de errores