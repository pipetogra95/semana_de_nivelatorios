# ✅ Soluciones – Práctica de Comandos de Linux Bash

## 🧩 Nivel 1 – Fundamentos (Archivos, directorios y ayuda)

1) Crear carpeta y entrar
```bash
mkdir -p practica_bash && cd practica_bash
```

2) Crear subcarpetas
```bash
mkdir -p scripts logs data
```

3) Crear archivo vacío
```bash
touch readme.txt
```

4) Escribir texto en el archivo
```bash
echo "Bienvenido a la práctica de bash" > readme.txt
```

5) Mostrar contenido con dos comandos
```bash
cat readme.txt
less readme.txt
```

6) Copiar y renombrar a logs/log_inicio.txt
```bash
cp readme.txt logs/log_inicio.txt
```

7) Mover log_inicio.txt a data
```bash
mv logs/log_inicio.txt data/
```

8) Borrar el readme original
```bash
rm -f readme.txt
```

9) Leer el manual de ls
```bash
man ls
```

10) Listar data con detalles y por fecha
```bash
ls -lt data
```

---

## ⚙️ Nivel 2 – Filtros y manipulación de texto

11) Crear usuarios.txt con nombres (uno por línea)
```bash
printf "Ana\nJuan\nLucía\nMario\nAna\nSofía\n" > usuarios.txt
```

12) Primeras 3 líneas
```bash
head -3 usuarios.txt
```

13) Últimas 2 líneas
```bash
tail -2 usuarios.txt
```

14) Ordenar alfabéticamente
```bash
sort usuarios.txt > usuarios_ordenados.txt
```

15) Contar líneas
```bash
wc -l < usuarios.txt
```

16) Buscar una palabra (ej. “Juan”)
```bash
grep "Juan" usuarios.txt
```

17) Mostrar solo dominios de emails.txt
```bash
printf "ana@gmail.com\njuan@yahoo.com\nana@gmail.com\n" > emails.txt
cut -d'@' -f2 emails.txt
```

18) Quitar duplicados de una lista ordenada
```bash
sort usuarios.txt | uniq > usuarios_sin_duplicados.txt
```

19) Contar nombres que contienen “a”
```bash
grep -c "a" usuarios.txt
```

20) Redirigir salida de ls -l a listado.txt y verificar
```bash
ls -l > listado.txt
cat listado.txt
```

---

## 🧮 Nivel 3 – Permisos, variables y scripts

21) Script saludo.sh (nombre + fecha)
```bash
cat > saludo.sh <<'EOF'
#!/bin/bash
echo "Hola $(whoami), hoy es $(date)"
EOF
```

22) Dar permiso y ejecutar
```bash
chmod +x saludo.sh
./saludo.sh
```

23) Variable RUTA con ruta actual
```bash
RUTA="$(pwd)"; echo "$RUTA"
```

24) Crear test.txt y dejar solo lectura para el dueño
```bash
touch test.txt
chmod 400 test.txt
ls -l test.txt
```

25) Cambiar propietario (requiere sudo y usuario válido)
```bash
sudo chown ubuntu:ubuntu test.txt
```

26) Espacio en disco disponible
```bash
df -h
```

27) Tamaño total del directorio actual
```bash
du -sh .
```

28) Procesos activos (paginando)
```bash
ps aux | less
```

29) Iniciar en segundo plano y detenerlo
```bash
sleep 1000 &
jobs -l
kill %1
```

30) Script backup.sh con carpeta fechada
```bash
cat > backup.sh <<'EOF'
#!/bin/bash
set -euo pipefail
SRC_DIR="data"
DEST_DIR="backup_$(date +%F)"
mkdir -p "$DEST_DIR"
cp -a "$SRC_DIR"/. "$DEST_DIR"/
echo "Backup completado en: $DEST_DIR"
EOF

chmod +x backup.sh
./backup.sh
```

---

**Autor:** Rami  
**Propósito:** Práctica guiada de comandos esenciales de Linux Bash.
