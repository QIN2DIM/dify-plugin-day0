# dify-plugin-day0

```bash
mkdir -p difypkg
./dify-plugin-windows-amd64.exe plugin package day0/ -o difypkg/day0-0.0.1.difypkg
```

```bash
uv pip compile pyproject.toml -o day0/requirements.txt
```