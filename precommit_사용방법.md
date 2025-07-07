# pre-commit 사용 방법 (Python 프로젝트 기준)

`pre-commit`은 커밋 전에 자동으로 코드 포매팅, 스타일 검사, 린팅 등을 실행해주는 도구입니다. 아래는 Python 프로젝트에서의 설정 및 사용 방법입니다.

---

## 1. pre-commit 설치

```bash
pip install pre-commit
```

설치 후 버전 확인 (선택):

```bash
pre-commit --version
```

---

## 2. 설정 파일 작성

프로젝트 루트에 `.pre-commit-config.yaml` 파일을 생성하고 다음과 같이 작성합니다:

```yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: trailing-whitespace   # 줄 끝 공백 제거
      - id: end-of-file-fixer     # 파일 끝 빈 줄 유지

  - repo: https://github.com/psf/black
    rev: 24.3.0
    hooks:
      - id: black                 # black 포매터 (코드 자동 정렬)

  - repo: https://github.com/pycqa/isort
    rev: 5.13.2
    hooks:
      - id: isort
        args: ["--profile", "black"]  # black 스타일에 맞게 import 정렬

  # 아래는 선택 사항입니다 (현재 비활성화 상태)
  # - repo: https://github.com/pycqa/flake8
  #   rev: 7.0.0
  #   hooks:
  #     - id: flake8
  #       args: [--max-line-length=92]
```

---

## 3. Git hook에 연결

다음 명령어를 실행하면 `.git/hooks/pre-commit` 스크립트가 자동으로 생성되어 Git 커밋 시 pre-commit이 실행됩니다:

```bash
pre-commit install
```

---

## 4. 커밋 전에 자동 실행 확인

이제 `git commit` 할 때마다 설정한 훅들이 자동으로 실행되어 코드 스타일을 검사하고 수정합니다.

---

## 5. 전체 코드에 수동 실행 (선택 사항)

기존 코드 전체에 한 번 적용하고 싶다면 아래 명령어로 실행할 수 있습니다:

```bash
pre-commit run --all-files
```

---

## 6. Git과 함께 사용 시 주의할 점

- 변경사항이 있는 파일은 자동으로 수정되거나 커밋이 중단될 수 있으니, `git status` 확인 후 재커밋 필요
- `black`, `isort` 등은 포맷팅 규칙을 강제하므로 팀 프로젝트 시 개발자 간의 설정 공유 필수

---

## 참고 명령어 요약

| 명령어 | 설명 |
|--------|------|
| `pre-commit install` | Git에 훅 설치 |
| `pre-commit run` | 변경된 파일에 훅 실행 |
| `pre-commit run --all-files` | 전체 파일에 훅 실행 |
| `pre-commit autoupdate` | 훅의 버전 업데이트 |

---

## 마무리

pre-commit은 개발자가 실수하기 쉬운 포매팅, 린트, 공백 문제 등을 자동화하여 코드 품질을 높이는 데 큰 도움이 됩니다. 팀 개발 시에도 통일된 코드 스타일을 유지하는 데 필수 도구입니다.
