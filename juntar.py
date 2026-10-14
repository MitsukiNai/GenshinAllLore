#!/usr/bin/env python3

from pathlib import Path
from datetime import datetime

OUTPUT_FILE = "repositorio_completo.md"


def escribir_arbol_y_contenido(directorio, salida, nivel=0):
    indent = "│   " * nivel

    try:
        elementos = sorted(
            directorio.iterdir(),
            key=lambda p: (p.is_file(), p.name.lower())
        )
    except PermissionError:
        salida.write(f"{indent}❌ Sin permisos: {directorio}\n")
        return

    for elemento in elementos:
        if elemento.name == OUTPUT_FILE:
            continue

        if elemento.is_dir():
            salida.write(f"{indent}📂 ENTRANDO EN: {elemento.name}\n\n")

            escribir_arbol_y_contenido(elemento, salida, nivel + 1)

            salida.write(f"{indent}📂 SALIENDO DE: {elemento.name}\n\n")

        elif elemento.is_file() and elemento.suffix.lower() == ".md":
            salida.write(f"{indent}📄 ARCHIVO: {elemento.name}\n\n")

            ruta_relativa = elemento.relative_to(Path.cwd())

            salida.write("\n")
            salida.write("=" * 100 + "\n")
            salida.write(f"ARCHIVO: {ruta_relativa}\n")
            salida.write("=" * 100 + "\n\n")

            try:
                contenido = elemento.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                contenido = elemento.read_text(
                    encoding="utf-8",
                    errors="replace"
                )

            salida.write(contenido)
            salida.write("\n\n")


def main():
    raiz = Path.cwd()

    with open(OUTPUT_FILE, "w", encoding="utf-8") as salida:
        salida.write("# Exportación completa del repositorio\n\n")
        salida.write(
            f"Generado: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        )

        salida.write("# ESTRUCTURA DEL ÁRBOL\n\n")
        escribir_arbol_y_contenido(raiz, salida)

    print(f"Archivo generado: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()